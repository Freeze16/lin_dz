def main():
    with open('1.txt', 'r') as file:
        text = [word for line in file.readlines() for word in line.split(' ')]

    return text


if __name__ == '__main__':
    print(main())
