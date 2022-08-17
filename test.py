import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + 'video/0')
print(response.json())

response = requests.put(BASE + 'video/100',{"videoName":"How to create Python REST APIs","videoViews":1000,"videoLikes":459})
print(response.json())

response = requests.patch(BASE + 'video/0',{"videoName":"HelloWorld","videoViews":1,"videoLikes":8})
print(response.json())

response = requests.delete(BASE + 'video/0')
print(response)