import csv


def filter_text(txt: list[list[str]]) -> list[str]:
    new_txt = []
    for line in txt:
        for word in line:
            temp = ''
            for char in word:
                if char in alphabet:
                    temp += char.lower()
            if temp:
                new_txt.append(temp)

    return new_txt


def calculate_frequency(txt: list[str]) -> dict[str, float]:
    no_repeats = set(txt)
    frequency = {word: txt.count(word) for word in no_repeats}

    return frequency


def create_csv_table(txt: list[str], fr: dict[str, float], name: str = 'statistic'):
    table = [['Номер', 'Слово', 'Встречаемость']]
    skip, count = [], 1

    for word in txt:
        if word not in skip:
            skip.append(word)
            table.append([str(count), word, fr[word]])
            count += 1

    with open(f'{name}.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(table)


def main():
    with open('1.txt', 'r') as file:
        text1 = [line.split(' ') for line in file.readlines()]

    with open('2.txt', 'r', encoding='windows-1251') as file:
        text2 = [line.split(' ') for line in file.readlines()]

    text1 = filter_text(text1)
    text2 = filter_text(text2)

    frequency1 = calculate_frequency(text1)
    frequency2 = calculate_frequency(text2)

    create_csv_table(text1, frequency1, 'statistic1')
    create_csv_table(text2, frequency2, 'statistic2')


if __name__ == '__main__':
    alphabet = 'йцукенгшщзхъфывапролджэячсмитьбю-' + 'йцукенгшщзхъфывапролджэячсмитьбю'.upper()
    main()
