#!/usr/bin/python3

#Импортируем модули
from datetime import date, datetime
from time import time
import requests
import datetime
import json

#Записываем в переменную текущую дату
currentDate = str(datetime.datetime.now())

url = 'http://t72.ru'

#Получаем код ответа и записываем его в пременную
responseCode = requests.get(url).status_code

#Создаем словарь и записываем в него дату и код ответа
dict = {
    "checkTime": currentDate,
    "responseCode": responseCode
}
#В зависимости от кода ответа создаем файл
if responseCode == 200:

    with open("g.result.json", "a") as f:
        json.dump(dict, f)

else:
    responseCode !=200
    with open("b.result.json", "a") as f:
        json.dump(dict, f)