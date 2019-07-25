import requests

resp = requests.get('http://127.0.0.1:5000/users')
if resp.status_code != 200:
    # Soemthing went wrong
    # raise ApiError('GET / tasks/ {}'.format(resp.status_code))
    print("Something went wrong")
print(resp.json())
users = resp.json()
for user in users:
    print("Name is :", user['name'])
    print("Age is :", user['age'])
    print("Occupation is :", user['occupation'])

newsong = {"name": "xd", "age": 22, "occupation": "student"}
post_resp = requests.post('http://127.0.0.1:5000/users', json=newsong)
if post_resp.status_code != 201:
    print("Something is wrong")
else:
    print(resp.status_code)
