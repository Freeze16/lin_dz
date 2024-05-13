import re
import json

parts_of_speech = {
    'A': 'Прилагательное',
    'ADV': 'Наречие',
    'CONJ': 'Союз',
    'INTJ': 'Междометие',
    'NUM': 'Числительное',
    'PART': 'Частица',
    'PR': 'Предлог',
    'S': 'Существительное',
    'V': 'Глагол'
}

cases = {
    'им': 'Именительный',
    'род': 'Родительный',
    'дат': 'Дательный',
    'вин': 'Винительный',
    'твор': 'Творительный',
    'пр': 'Предложный',
}

numbers = {
    'ед': 'Единственное число',
    'мн': 'Множественное число'
}

genders = {
    'муж': 'Мужской род',
    'жен': 'Женский род',
    'сред': 'Средний род'
}


def counter_parts_of_speech(part: str, words: list[str]) -> int:
    template = '=' + part + ',' if part in ('S', 'V') else '=' + part + '='
    count = 0
    for word in words:
        if re.search(template, word):
            count += 1

    return count


def counter_case(case: str, words: list[str]) -> int:
    template = '=' + case + ','
    temp, count = '=S,', 0
    for word in words:
        if re.search(temp, word):
            if re.search(template, word.split('|')[-1]):
                count += 1

    return count


def counter_numbers_or_genders(value: str, words: list[str]) -> int:
    template = ',' + value + '[,}]'
    temp, count = '=S,', 0
    for word in words:
        if re.search(temp, word):
            if re.search(template, word.split('|')[-1]):
                count += 1

    return count


def main(name: str):
    base_json = {}
    with open(name, 'r') as file:
        data = [word.strip('\n') for word in file.readlines()]

    print(data)

    parts = {}
    for p in parts_of_speech:
        parts[parts_of_speech[p]] = counter_parts_of_speech(p, data)

    case = {}
    for c in cases:
        case[cases[c]] = counter_case(c, data)

    number = {}
    for n in numbers:
        number[numbers[n]] = counter_numbers_or_genders(n, data)

    gender = {}
    for g in genders:
        gender[genders[g]] = counter_numbers_or_genders(g, data)

    base_json['parts_of_speech'] = parts
    base_json['cases'] = case
    base_json['numbers'] = number
    base_json['genders'] = gender

    with open('data.json', 'w') as file:
        json.dump(base_json, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main('output.txt')
