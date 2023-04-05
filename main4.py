import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random

TOKEN = 'vk1.a.skeoPCk_tj7uaPrgXMB_43Z0z144qxV6HD2aPkhDSW8vsNCKU7CnPWJH3z2JagPfJ2t9LcQEeAPSXcSvTyof5n6Og6Kf1nHPg8oujPMAsbEVC6-c-Vm-mGbDspdLX6fOkAaLJhZCo6gu1_ZRkr3469VJ398uVbmkAG5WiDfqeexoGTARNhn1SeLri7hXrxZwzFqxakqgBluEak_G1Nshng'


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, 219630349)

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            vk = vk_session.get_api()
            user_get = vk.users.get(user_ids=(event.obj.message['from_id']))
            user_get = user_get[0]
            first_name = user_get['first_name']
            city = None
            if 'city' in user_get.keys():
                city = user_get['city']
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"Привет, {first_name}!",
                             random_id=random.randint(0, 2 ** 64))
            if city:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Как поживает {city}?",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()