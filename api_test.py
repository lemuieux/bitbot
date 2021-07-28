import requests, json

params = {'key':'value'}

headers = {'Content-type' : 'application/json; charset=utf-8'}
cookies = {'session_id' : 'cookies...'}

res = requests.get("https://wwww.tistory.com", headers=headers, cookies=cookies, params=params)
res2 = requests.post("https://wwww.tistory.com", headers=headers, cookies=cookies, data=json.dumps(params))

print(res.url)
print(res)
print(res2.url)
print(res2)