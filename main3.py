import os

import vk_api

TOKEN = 'vk1.a.skeoPCk_tj7uaPrgXMB_43Z0z144qxV6HD2aPkhDSW8vsNCKU7CnPWJH3z2JagPfJ2t9LcQEeAPSXcSvTyof5n6Og6Kf1nHPg8oujPMAsbEVC6-c-Vm-mGbDspdLX6fOkAaLJhZCo6gu1_ZRkr3469VJ398uVbmkAG5WiDfqeexoGTARNhn1SeLri7hXrxZwzFqxakqgBluEak_G1Nshng'


def main():
    login, password = '89130983726', 'nfrcf123'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    """ В VkUpload реализованы методы загрузки файлов в ВК
    """

    upload = vk_api.VkUpload(vk_session)
    for file in os.listdir('static/img'):
        photo = upload.photo(  # Подставьте свои данные
            f'static/img/{file}',
            album_id=292366937,
            group_id=219630349
        )

        vk_photo_url = 'https://vk.com/photo{}_{}'.format(
            photo[0]['owner_id'], photo[0]['id']
        )
        print(photo, '\nLink: ', vk_photo_url)


if __name__ == '__main__':
    main()
