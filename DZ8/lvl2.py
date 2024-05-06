import os
import csv
from dotenv import load_dotenv

import requests

load_dotenv()


class Friends:
    TOKEN = 'access_token=' + os.environ.get('ACCESS_TOKEN')
    VERSION = '&v=5.92&'
    BASE_LINK = 'https://api.vk.com/method/'

    METHODS = {
        'friends_get': 'friends.get?user_id={}',
        'user_get': 'users.get?user_ids={}'
    }

    def __init__(self, base_user_id: str | int):
        self.base_user_id = str(base_user_id)
        self.friends = Friends.BASE_LINK + Friends.METHODS['friends_get'] + Friends.VERSION + Friends.TOKEN
        self.user = Friends.BASE_LINK + Friends.METHODS['user_get'] + Friends.VERSION + Friends.TOKEN

    def get_friends(self, user_id: str = None) -> list[str] | str:
        user_id = user_id if user_id else self.base_user_id
        link = self.friends.format(user_id)
        response = requests.get(link).json()
        print(0)
        try:
            return list(map(str, response['response']['items']))
        except KeyError:
            return f'Ошибка пользователя {user_id}'

    def get_users(self, user_ids: list[str]) -> dict[str, str] | str:
        link = self.user.format(','.join(user_ids))
        try:
            response: dict = requests.get(link).json()
            temp = {str(response['response'][i]['id']): response['response'][i]['first_name'] + ' ' +
                                                        response['response'][i]['last_name'] for i in
                    range(len(response['response']))}
            print(temp)
            return temp
        except:
            return 'fail'


def main():
    f = Friends(375670989)
    first_friends = f.get_friends()
    temp1 = f.get_users(first_friends)
    second_friends = {friend: f.get_friends(friend) for friend in first_friends}
    temp2 = {my_friend: f.get_users(second_friends[my_friend]) for my_friend in second_friends}

    # with open('names1', 'r') as file:
    #     first_friends: dict[str, str] = eval(file.read())
    # with open('names2', 'r') as file:
    #     seconds_friends: dict[dict[str, str] | str] = eval(file.read())
    first_friends = temp1
    seconds_friends = temp2

    table = [['id', 'label']]
    temp = []
    for i in first_friends:
        if i != 'f':
            table.append([i, first_friends[i]])
            temp.append(i)

    for i in seconds_friends:
        if i == "450030546":
            break
        if seconds_friends[i] != 'fail':
            for j in seconds_friends[i]:
                if seconds_friends[i][j] != 'DELETED ' and j not in temp:
                    table.append([j, seconds_friends[i][j]])
                    temp.append(j)

    with open('misc/nodes.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(table)

    table = [['source', 'target']]
    for i in seconds_friends:
        if seconds_friends[i] != 'fail':
            for j in seconds_friends[i]:
                if seconds_friends[i][j] != 'DELETED ':
                    table.append([i, j])

    with open('misc/edges.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(table)


if __name__ == '__main__':
    # with open('my_friends.txt', 'r') as file:
    #     file = file.readlines()
    #
    # a = [i.split('/')[-1][2:-1] for i in file]
    main()
    # print(main())
