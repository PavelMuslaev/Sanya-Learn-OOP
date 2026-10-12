file1 = open("example.txt", "w")
file1.write("Hello World!\n")
file1.write("Hello World!\n")
file1.write("Hello World!\n")
file1.close() # Запись происходит разом из буфера при закрытии файла.

file2 = open("example.txt", "r")
data = file2.read()
print(data)
file2.close()


# for i in range(1000): 
#     f = open(f'file_{i}.txt', 'w') 
#     f.write('some data') 
      # закрытия нет! 


f = open("example.txt", "r")
data = f.read() 
# тут могут возникнуть ошибки, например, деление на ноль или 
# обращение по несуществующему индексу 
# x = 10 / 0   # исключение! 
f.close()    
# этот код уже не выполнится

f = open('example.txt', 'r') 
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
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write("Буба!")

with open('project/data.txt ', 'r', encoding="utf-8") as f:
    data = f.read()

print(data)








