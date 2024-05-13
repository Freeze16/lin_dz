import re


def main():
    with open('1.txt', 'r') as file:
        text = file.read()

    template = "[a-zA-Z0-9’]{1,}"
    tokens = re.findall(template, text)

    return tokens


if __name__ == '__main__':
    print(main())
