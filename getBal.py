import requests

headers = {
    'Content-Type': 'application/json; charset=utf-8',
}

json_data = {
    'body': '余额不足，及时处理',
    'title': '余额处理通知',
    'badge': 1,
    'category': 'myNotificationCategory',
    'sound': 'minuet.caf',
    'icon': 'https://day.app/assets/images/avatar.jpg',
    'group': 'test',
}

response = requests.post('https://api.day.app/GbuozPNR64v7kQLotmtnCR', headers=headers, json=json_data)
