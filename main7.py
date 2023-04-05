import datetime
import random

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

TOKEN = 'vk1.a.skeoPCk_tj7uaPrgXMB_43Z0z144qxV6HD2aPkhDSW8vsNCKU7CnPWJH3z2JagPfJ2t9LcQEeAPSXcSvTyof5n6Og6Kf1nHPg8oujPMAsbEVC6-c-Vm-mGbDspdLX6fOkAaLJhZCo6gu1_ZRkr3469VJ398uVbmkAG5WiDfqeexoGTARNhn1SeLri7hXrxZwzFqxakqgBluEak_G1Nshng'
_dict = {0: 'Понедельник',
         1: 'Вторник',
         2: 'Среда',
         3: 'Четверг',
         4: 'Пятница',
         5: 'Суббота',
         6: 'Воскресенье'}


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
            msg = event.obj.message['text'].split('-')
            vk = vk_sessionBot.get_api()
            if len(msg) == 3:
                if len(msg[0]) == 4 and len(msg[1]) == 2 and len(msg[2]) == 2:
                    today = datetime.datetime(int(msg[0]), int(msg[1]), int(msg[2]))
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=_dict[today.weekday()],
                                     random_id=random.randint(0, 2 ** 64))
                else:
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f"Введите дату! В формате YYYY-MM-DD",
                                     random_id=random.randint(0, 2 ** 64))
            else:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Введите дату! В формате YYYY-MM-DD",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
