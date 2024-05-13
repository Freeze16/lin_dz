import csv

import asyncio
import aiohttp
from aiohttp.client_exceptions import ClientOSError

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

BASE_LINK = 'https://moe-online.ru'
PAGE_LINK = 'https://moe-online.ru/news?page={}'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Cookie': 'io=mlU5_5ACv9f8A5ejcg1F; __ddg1_=lMe2REn9U7YQYVrmdCOh; XSRF-TOKEN=eyJpdiI6Ii9jVStnU2xMVGFYWWpibFVQbmFtZWc9PSIsInZhbHVlIjoiQ2FDOVZObkJlWm1GZlpyR3N5cjBKR1U3VjNQMzNSWUNJeDU3NjBtK0tLcmxLcDljM1JUKzUrNjlFdmFXQjFzVERQYU5uMElFem1GMm9CNlg5NTVVbEhXc2RoQnprS2xORFRRY0FmUGUwVDY5bVVRWnVlendZZERoOGpYSnZ4aDkiLCJtYWMiOiI3N2M0NmUxNGNhNWM2YzhiN2M1NWE4OWY1ZmMxODM4MDA5MjdiZWQ1MGRiYmVkMTRhNTZhOGY0YTBjMjlhYjEyIiwidGFnIjoiIn0%3D; moeonline=eyJpdiI6Im1ZcnlzWXh3WXZuM2t6QU1yU3E4a0E9PSIsInZhbHVlIjoiSU9wMVRzM1FFdngwYjdobDhIREhkQjExWkh6…LMEdLWVVjdENEcjEySGxNNVZtY2hlcyIsIm1hYyI6IjQyYzZlYjIwMWVhMDY0ZjQ2NTU3Yzg5ODUxZTcxMDYxZDc1ZjlkMjhiNTE1ZGFlMTQwMjhlNTIzYTNjMGUxMDYiLCJ0YWciOiIifQ%3D%3D; _ga_3DPVB4PEBG=GS1.1.1715281439.2.1.1715281867.17.0.0; _ga=GA1.2.1499027246.1715277836; _ym_uid=1715277836114042339; _ym_d=1715277836; tmr_lvid=94e2308dee90b53034df9065458ea00f; tmr_lvidTS=1694992699846; _gid=GA1.2.1178718296.1715277836; domain_sid=UQ08GAHu_qRES9Ag2RKjS%3A1715277836101; _ym_isad=2; tmr_detect=0%7C1715281870565; _ym_visorc=w; chash=LzT61Um8M8',
    'User-Agent': UserAgent().random
}


def create_csv_table():
    table = [['Заголовок', 'Текст', 'Автор', 'Дата', 'Время']]

    for title in base_data:
        if base_data[title][1]:
            table.append([
                title,
                base_data[title][0],
                base_data[title][1],
                base_data[title][2].split(' ')[0],
                base_data[title][2].split(' ')[1],
            ])

    with open('data.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(table)


def get_title(soup: BeautifulSoup) -> str:
    return soup.find('h1').text.replace('\xa0', ' ')


def get_content(soup: BeautifulSoup) -> str | None:
    div = soup.find('div', class_='font_os')
    try:
        tags = div.find_all('p')
    except AttributeError:
        return

    content = ''
    for text in tags:
        if text.find('span'):
            text = text.find('span')
        content += text.text + ' '

    return content.replace('\xa0', ' ')


def get_author(soup: BeautifulSoup) -> str | None:
    div = soup.find('div', class_='author-block')

    try:
        return div.find_all('p')[1].text
    except AttributeError:
        return
    except IndexError:
        return


def get_data(soup: BeautifulSoup) -> list[str]:
    prob_nums = soup.find_all('a', class_='plitka_text')

    return [a.get('href') for a in prob_nums if 'http' not in a.get('href')]


def get_time(soup: BeautifulSoup) -> str | None:
    try:
        div = soup.find('div', class_='material-head-box-1')
        return div.find('time').text
    except AttributeError:
        return


def reformat(name: str) -> str | None:
    if name:
        first_name, last_name = name.split(' ')
        last_name = last_name[0] + last_name[1:].lower()

        return first_name + ' ' + last_name


async def get_page(link: str, recursion: bool = True):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link, headers=headers) as response:
                html = await response.text()
                soup = BeautifulSoup(html, 'lxml')

        if recursion:
            articles = get_data(soup)
            tasks = [asyncio.create_task(get_page(BASE_LINK + src, False)) for src in articles]
            await asyncio.gather(*tasks)

        else:
            title = get_title(soup)
            content = get_content(soup)
            author = get_author(soup)
            time = get_time(soup)

            base_data[title] = content, reformat(author), time
    except ClientOSError:
        await asyncio.sleep(1)
        await get_page(link, False)
        print(link)


async def main():
    tasks = []
    for i in range(1, 85):
        task = asyncio.create_task(get_page(PAGE_LINK.format(i)), name=f'task#{i}')
        tasks.append(task)

    await asyncio.gather(*tasks)

    create_csv_table()


if __name__ == '__main__':
    base_data = {}
    asyncio.run(main())
