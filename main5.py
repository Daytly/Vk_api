import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import datetime

TOKEN = 'vk1.a.skeoPCk_tj7uaPrgXMB_43Z0z144qxV6HD2aPkhDSW8vsNCKU7CnPWJH3z2JagPfJ2t9LcQEeAPSXcSvTyof5n6Og6Kf1nHPg8oujPMAsbEVC6-c-Vm-mGbDspdLX6fOkAaLJhZCo6gu1_ZRkr3469VJ398uVbmkAG5WiDfqeexoGTARNhn1SeLri7hXrxZwzFqxakqgBluEak_G1Nshng'
_dict = {0: 'Понедельник',
         1: 'Вторник',
         2: 'Среда',
         3: 'Четверг',
         4: 'Пятница',
         5: 'Суббота',
         6: 'Воскресенье'}


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
            msg = set(event.obj.message['text'].split())
            vk = vk_session.get_api()
            words = set(list(["время", "число", "дата", "день"]))
            offset = datetime.timezone(datetime.timedelta(hours=3))
            dt = datetime.datetime.now(offset)
            dWeek = _dict[datetime.datetime.now(offset).weekday()]
            if words & msg:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"{dt} {dWeek}",
                                 random_id=random.randint(0, 2 ** 64))
            else:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Спроси у меня дату и время",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
