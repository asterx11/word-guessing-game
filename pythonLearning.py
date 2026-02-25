message='bazen çok yoruluyorum'
message=message.capitalize()
print(message)
list=['ali', 'ahsen', 10, 3.2]
list.append('ahmet') #en sona ekler
print(list)
list.insert(0, "sena")
print(list)
list.remove(10)
print(list)
list.pop() #index vermediğimizde sondaki elemanı siler
print(list)
index = list.index("ahsen")
print(index)
res="can" in list
print(res)
res=list.index("ali")
print(res)
list.reverse()
print(list)
#list.sort() str ise alfabetik sıraya dizer sayı ise küçükten büyüğe sıralanır
str="chevy ımpala"
str=str.split("v")
print(str)
num=list.count("ali")
print(num)
list.clear()
print(list)
tuple=("coward", "merdane", "coraline", "coraline")
print(tuple)
tuple=tuple.count("coraline")
print(tuple)


