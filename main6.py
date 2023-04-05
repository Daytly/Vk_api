import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import wikipedia

TOKEN = 'vk1.a.skeoPCk_tj7uaPrgXMB_43Z0z144qxV6HD2aPkhDSW8vsNCKU7CnPWJH3z2JagPfJ2t9LcQEeAPSXcSvTyof5n6Og6Kf1nHPg8oujPMAsbEVC6-c-Vm-mGbDspdLX6fOkAaLJhZCo6gu1_ZRkr3469VJ398uVbmkAG5WiDfqeexoGTARNhn1SeLri7hXrxZwzFqxakqgBluEak_G1Nshng'
_dict = {0: 'Понедельник',
         1: 'Вторник',
         2: 'Среда',
         3: 'Четверг',
         4: 'Пятница',
         5: 'Суббота',
         6: 'Воскресенье'}


def main():
    user_ids = []
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, 219630349)

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            msg = event.obj.message['text']
            user_id = event.obj.message['from_id']
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', user_id)
            print('Текст:', msg)
            vk = vk_session.get_api()
            if user_id not in user_ids:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Привет, что ты хочешь узнать?",
                                 random_id=random.randint(0, 2 ** 64))
                user_ids.append(user_id)
            else:
                wikipedia.set_lang('ru')
                ny = wikipedia.page(msg)
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"{ny.title}\n{ny.content[:2000]}...",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
