import requests

url = 'https://notify-api.line.me/api/notify'
token = 'qvpqRQ42fzkIxXzZfS8xHmVHungKm9xdlPWqoVQbCpZ'
headers = {'Authorization':'Bearer '+token}
 
message = input('กรุณาใส่ชื่อเพื่อเช็คชื่อ: ')
requests.post(url=url, headers=headers, data={'message':message})

