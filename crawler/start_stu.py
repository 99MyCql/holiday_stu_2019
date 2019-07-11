import requests

res = requests.get('https://www.baidu.com')

print('res type = ', type(res))

print('status_code = ', res.status_code)

res.encoding = 'utf-8'

print('text = ', res.text)

data = {
    'name': 'dounine',
    'age': 9
}

res_get = requests.get('http://httpbin.org/get', params=data)

res_post = requests.post('http://httpbin.org/post', data=data)