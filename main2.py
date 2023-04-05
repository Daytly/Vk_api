import datetime

import vk_api


def main():
    login, password = '79130983726', 'nfrcf123'
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    # Используем метод wall.get
    response = vk.friends.get(fields="bdate, city")
    res = []
    if response['items']:
        for i in response['items']:
            try:
                res.append([i['first_name'], i['last_name'], f'Дата рождения: {i["bdate"]}'])
            except Exception as error:
                print(f'Ошибка вывода: {error}')
    res.sort(key=lambda x: x[1])
    for i in res:
        print(*i)


if __name__ == '__main__':
    main()