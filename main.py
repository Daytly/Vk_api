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
    response = vk.wall.get(count=5, offset=1)
    if response['items']:
        for i in response['items']:
            if 'is_deleted' not in i['copy_history'][0].keys():
                print(f"text: {i['copy_history'][0]['attachments'][0]['photo']['text']}")
                print(datetime.datetime.utcfromtimestamp(
                    i['copy_history'][0]['attachments'][0]['photo']['date']).strftime('date: %Y-%m-%d, time: %H:%M:%S')
                      )
                print('-' * 10)
            else:
                print('Запись была удалена')


if __name__ == '__main__':
    main()