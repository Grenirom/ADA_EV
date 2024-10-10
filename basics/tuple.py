"==============================Tuple================================"
# Кортеж это - неизменяемый, индексируемый, упорядочный, итерируемый тип данных, предназначенных для хранения людых данных в определенном порядке(по сути, не отличается от списков, просто он не изменяемый , поэтому занимает меньше места)

# литералы tuple это НЕ СКОБКИ, а запятые
tuple1 = (1, 2, 3, 3, 3, 3)
print(tuple1)
print(type(tuple1))# <class 'tuple'>
tuple2 = (4)
print(type(tuple2))# <class 'int'>
tuple3 = (4, )
print(type(tuple3))# <class 'tuple'>
tuple4 = 1, 2, 3
print(tuple4)# (1, 2, 3)
print(type(tuple4))# <class 'tuple'>

tuple6 = (1, 2, 3, 4, 5, ['hello', 1])
tuple6[-1].append('world')
print(tuple6)

"=========================Метода tuple=========================="
print(dir(tuple1))

#count() - это метода, который считает количество принятого элемента в кортеже
tuple1 = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 325, 3, 6)
print(tuple1.count(1))# 11


# index() - возвращает индекс первого вхождения принятого элемента
tuple2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(tuple2.index(5678))# ValueError: tuple.index(x): x not in tuple
print(tuple2.index(6))# 5
