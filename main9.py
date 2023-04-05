import requests
import vk_api
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexLyceum_secret_key'

TOKEN = 'vk1.a.d3GFOnvUx-ZSXklcKCuCj0_INZBvv4k0-62y2k9sYa2Umx1uE6lk0wQAVdAsUscX7vOi2hHxfozLv5X9HFDwQpRm-cBZ2AHNaKsLQUDFRXYe6p8VyfFNJFm8f_uY2U58Gs1paxgF8sJ_9ms3k0xwA0XZu_ZFeVyVqJHQZF3OQq5IgH8wZEIEVxFKmB3nyEU4XOwkIjR_b9Ko9lqBi1cwwg'


def get_offset(group_id):
    """Выявляем параметр offset для групп, 1 смещение * 1000 id"""
    params = {'access_token': TOKEN, 'group_id': group_id, 'v': 5.131}
    r = requests.get('https://api.vk.com/method/groups.getMembers', params=params)
    count = r.json()
    print(count)
    print(f'Количество подписчиков: {count}')
    if count > 1000:
        return count // 1000
    else:
        count = 1
        return count


def main():
    app.run()


@app.route("/vk_stat/<int:group_id>")
def index(group_id):
    login, password = '89130983726', 'nfrcf123'
    vk_session = vk_api.VkApi(login, password, token=TOKEN)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    # res = vk_session.method('stats.get', values={'fields': 'reach', 'group_id': group_id})
    get_offset(292366937)
    return render_template("index.html")


@app.route("/", methods=['POST'])
def index1():
    return '1e221c05'


get_offset(292366937)
main()
