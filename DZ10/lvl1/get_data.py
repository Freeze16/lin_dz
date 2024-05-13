from pandas import read_csv
from pandas.core.frame import DataFrame


def get_title_and_content(file: str) -> DataFrame:
    data = read_csv(file, header=None, usecols=[0, 1])
    data.columns = ['title', 'content']

    return data


def formating(res: DataFrame) -> str:
    text = ''
    for i in list(res.values)[1:]:
        text += i[0] + i[1] + '\n'

    return text


def main(file):
    result = get_title_and_content(file)
    txt = formating(result)

    with open('parsed_data.txt', 'w') as f:
        f.write(txt)


if __name__ == '__main__':
    main('data.csv')
