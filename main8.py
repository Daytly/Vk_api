import datetime
import random
import sys
from PIL import Image
from io import BytesIO
import requests
import vk_api
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

TOKEN = 'vk1.a.skeoPCk_tj7uaPrgXMB_43Z0z144qxV6HD2aPkhDSW8vsNCKU7CnPWJH3z2JagPfJ2t9LcQEeAPSXcSvTyof5n6Og6Kf1nHPg8oujPMAsbEVC6-c-Vm-mGbDspdLX6fOkAaLJhZCo6gu1_ZRkr3469VJ398uVbmkAG5WiDfqeexoGTARNhn1SeLri7hXrxZwzFqxakqgBluEak_G1Nshng'
_usersID = []
_dict = {'Карта': 'sat', 'Схема': 'map', 'Карта+Схема': 'sat,skl'}


def upload_photo(upload, photo):
    response = upload.photo_messages(photo)[0]

    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']

    return owner_id, photo_id, access_key


def main():
    vk_sessionBot = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_sessionBot, 219630349)
    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            msg = event.obj.message['text']
            vk = vk_sessionBot.get_api()
            if event.obj.message['from_id'] not in _usersID:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message='Привет, введи местность, которую хочешь посмотреть',
                                 random_id=random.randint(0, 2 ** 64))
            elif 'Карта' not in msg and 'Схема' not in msg and 'Карта+Схема' not in msg:
                keyBoard = VkKeyboard(one_time=True)
                keyBoard.add_button(f'Карта {msg}', VkKeyboardColor.PRIMARY)
                keyBoard.add_button(f'Схема {msg}', VkKeyboardColor.PRIMARY)
                keyBoard.add_button(f'Карта+Схема {msg}', VkKeyboardColor.PRIMARY)
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message='ghbdtn',
                                 random_id=random.randint(0, 2 ** 64),
                                 keyboard=keyBoard.get_keyboard())
            else:
                geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
                geocoder_params = {
                    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                    "geocode": msg,
                    "format": "json"}

                response = requests.get(geocoder_api_server, params=geocoder_params)

                if not response:
                    print('error')
                # Преобразуем ответ в json-объект
                json_response = response.json()
                # Получаем первый топоним из ответа геокодера.
                toponym = json_response["response"]["GeoObjectCollection"][
                    "featureMember"][0]["GeoObject"]
                x, y = map(float, toponym['boundedBy']['Envelope']['lowerCorner'].split())
                x1, y1 = map(float, toponym['boundedBy']['Envelope']['upperCorner'].split())
                # Координаты центра топонима:
                toponym_coodrinates = toponym["Point"]["pos"]
                # Долгота и широта:
                toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

                delta = "0.005"

                # Собираем параметры для запроса к StaticMapsAPI:
                map_params = {
                    "ll": ",".join([toponym_longitude, toponym_lattitude]),
                    "spn": f'{abs(x - x1) * 0.5},{abs(y - y1) * 0.5}',
                    'pt': f'{toponym_longitude},{toponym_lattitude},flag',
                    "l": _dict[msg.split()[0]]
                }

                map_api_server = "http://static-maps.yandex.ru/1.x/"
                # ... и выполняем запрос
                response = requests.get(map_api_server, params=map_params)
                upload = VkUpload(vk)
                Image.open(BytesIO(
                    response.content)).save('image.png')
                owner_id, photo_id, access_key = upload_photo(upload, 'image.png')
                attachment = f'photo{owner_id}_{photo_id}_{access_key}'
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message='Что ещё показать?',
                                 random_id=random.randint(0, 2 ** 64),
                                 attachment=attachment)
            _usersID.append(event.obj.message['from_id'])


if __name__ == '__main__':
    main()

