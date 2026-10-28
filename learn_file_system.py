"""
    Сериализация — это процесс преобразования структуры данных 
    (например, объекта в памяти программы) в последовательность байтов, 
    текста или другой формы, удобной для хранения в файле, 
    передачи по сети или записи в очередь. 
    
    Обратная операция — десериализация (или структуризация) — 
    восстанавливает из этой последовательности исходный объект или структуру.
"""


file1 = open("data/txt/example.txt", "w")
file1.write("Hello World!\n")
file1.write("Hello World!\n")
file1.write("Hello World!\n")
file1.close() # Запись происходит разом из буфера при закрытии файла.

file2 = open("data/txt/example.txt", "r")
data = file2.read()
print(data)
file2.close()


# for i in range(1000): 
#     f = open(f'file_{i}.txt', 'w') 
#     f.write('some data') 
      # закрытия нет! 


f = open("data/txt/example.txt", "r")
data = f.read() 
# тут могут возникнуть ошибки, например, деление на ноль или 
# обращение по несуществующему индексу 
# x = 10 / 0   # исключение! 
f.close()    
# этот код уже не выполнится

f = open('data/txt/example.txt', 'r') 
try: 
    data = f.read() 
    # опасный код 
    # x = 10 / 0 
finally: 
    # закроется при любом исходеs
    f.close()   
print("\n\n")


# МАГИЯ WITH: ДВЕРЬ ЗАКРЫВАЕТСЯ САМА 
# КОНТЕКСТНЫЙ МЕНЕДЖЕР with
with open('data/txt/data.txt', 'w', encoding='utf-8') as f:
    f.write("Буба!")

with open('data/txt//data.txt', 'r', encoding="utf-8") as f:
    data = f.read()

print(data)
print()


# TODO: ВОТ ОТ СЮДА


# TODO: ДО СЮДА

import csv

with open("data/csv/info_user.csv", encoding='UTF-8') as f: 
    reader = csv.reader(f)
    for line in reader:
        print(line)
print()

with open("data/csv/info_user.csv", encoding='UTF-8') as f: 
    reader = csv.DictReader(f)
    for line in reader:
        print(line)
print()

new_users = [ 
    ['name', 'age', 'city'],           # заголовок 
    ['Пётр', '35', 'Казань'], 
    ['Мария', '27', 'Екатеринбург'] 
]


with open("data/csv/new_info_users.csv", 'w', encoding='UTF-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(new_users)# запись все строки сразу 
    # или writer.writerow(new_users[0]) для одной строки


 
users = [ 
    {'name': 'Алексей', 'age': 32, 'city': 'Сочи'}, 
    {'name': 'Елена', 'age': 29, 'city': 'Калининград'} 
] 

with open("data/csv/new_info_users2.csv", 'w', encoding='UTF-8', newline='') as f: 
    fieldnames = users[0].keys()    # порядок колонок 
    writer = csv.DictWriter(f, fieldnames=fieldnames) 
 
    writer.writeheader()        # записать строку с заголовками 
    writer.writerows(users)     # записать все строки 


import csv 

with open('data/csv/access.log.csv', 'r', encoding='utf-8') as infile, \
    open('data/csv/unsuccess.csv', 'w', encoding='utf-8', newline='') as outfile: 
    reader = csv.DictReader(infile) 
    fieldnames = reader.fieldnames   # берём те же заголовки 

    writer = csv.DictWriter(outfile, fieldnames=fieldnames) 
    writer.writeheader() 
 
    for row in reader: 
        if row['status'] != '200': 
            writer.writerow(row)
print()


""" 
JSON - Java Script Object Notation.

Типы данных, которые понимает JSON: 
• Строки (обязательно в двойных кавычках) 
• Числа (целые и вещественные) 
• Булевы значения (true/false в JSON, а в Python они 
станут True/False) 
• null (в Python превращается в None) 
• Объекты и массивы (те самые вложенные коробки)  
"""

import json

with open("data/json/first_example.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data)

 
first_user = data['users'][0] 
print(first_user['name'])               # Петр 
print(first_user['orders'][0]['item'])  # ноутбук 
print()


person = { 
    'name': 'Анна', 
    'age': 30, 
    'hobbies': ['чтение', 'путешествия'], 
    'is_car': True 
} 

with open("data/json/first_example2.json", "w", encoding="utf-8") as file:
    json.dump(person, file, ensure_ascii=False, indent=4)
print()



import json 
from datetime import datetime 

data = {'date': datetime.now()} 
print(data)

with open("data/json/first_example3.json", "w", encoding="utf-8") as file:
    json.dump(
        data, 
        file, 
        ensure_ascii=False, 
        indent=4, 
        default=str
)
print()


with open("data/json/books.json", "r", encoding='utf-8') as file:
    catalog = json.load(file)
    print(catalog)

for book in catalog['catalog']['books']:
    print(book['author']['name'])


 
all_tags = set() 
for book in catalog['catalog']['books']: 
    for tag in book['tags']: 
        all_tags.add(tag) 
print(all_tags)
print()
print()






# # Представим, что это ответ от API 
json_string = '{"name": "Иван", "age": 32, "city": "Москва", "is_car": true}' 
info_user = json.loads(json_string)
print(info_user)



person = { 
    'name': 'Анна', 
    'age': 30, 
    'hobbies': ['чтение', 'путешествия'], 
    'has_car': True 
} 

json_string = json.dumps(person) 
print(json_string) 

# {"name": "\u0410\u043d\u043d\u0430", "age": 30, "hobbies": 
# ["\u0447\u0442\u0435\u043d\u0438\u0435", "\u043f\u0443\u0442\u0435\u0448\u0435\u0441\u0442\u0432\u0438\u044f"], 
# "has_car": true} 




from pathlib import Path


PATH_FILE = "data/json/books.json"

SOURCE_FILE = Path("data")
JSON_DIR = SOURCE_FILE / "json"
BOOKS_FILE = JSON_DIR / "books.json"
FOOD_FILE = JSON_DIR / "food.json"





