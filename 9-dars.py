# i = 0

from random import randint
# while i <= 5:
#     print(i)
#     i += 1

# name = ''
# name = input('>> ')
# while True:
#     while name == 'Tom':

# name = ""
# while name != 'Tom':
#     name = input('Name: ')
#
# print('Salom Tom')


# while True:
#     num1 = randint(1, 10)
#     num2 = randint(1, 10)
# 
#     a = num1 + num2
#       print(f'{num1}+{num2}')
#     res = int(input('Javov: '))
#     if a == res:
#         print('Sizning javobingiz togri')
#         break
#     else:
#         print('Notogri')

# a = 'Assalomu aleykum wdsfsdfsdfsdfsdf'
# i = 0
# while i < len(a):
#     if a[i] == " ":
#         break
#     print(a[i]) #
#     i += 1

# a = 'salom hammaga'
# for i in a:
#     print(i)


# a = 'salom hammaga'
# for i in a:
#     if i == 'h':
#         break
#     print(i)

# name = 'Tom'
# age = 23
# text = f'Salom mening ismim {name} yoshim {age} da'
# text = 'Salom mening ismim {} yoshim {} da'.format(name, age)
# print(text)


# a = input('a: ')
# for i in a:
#     print(f'<{i}>')

# fruits = ['apple', 'banana', 'cherry', 'mango', 'kivi']
# for i in fruits:
#     print(i)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in nums:
#     print(i)

# range
"""
range(start, stop, step)
range(stop)
range(1, 11, 1)
range()
"""

# a = list(range(5)) # stop start=0
# print(a)

# a = list(range(1, 5)) # start stop step=1
# print(a)

# a = list(range(1, 5, 2)) # start stop step
# print(a)

# a = list(range(1, 11, 1))
# for i in a:
#     print(i)

# # for i in range(1, 11, 1):
# #     print(5, '*', i, '=', 5*i)
# k = int(input('k: ')) # 15
# n = int(input('n: ')) # 4
# for i in range(0, n):
#     print(k)
# """
# 15
# 15
# 15
# 15
# """

# a = ["olma","uzum",'kiwi']
# a.append("banan")
# a.remove("kiwi")
# print(a)

# for i in range(1,11):
#     print(i, '*' ,'2', '=' ,i * 2)





# for i in range(65,91):
#     print(chr(i))







import  random


# while True:
#     a = input(">>")
#     b = {
#       1:'qaychi',
#       2:'qogoz',
#       3:'tosh'
#         }
#     d = 0
#     c = randint(1,3)
#     print(b.get(c))
#     if a == "qogoz":
#         if c == 1:
#             print('siz yutqazdingiz')
#         elif c == 3:
#             print("siz yutingiz")
#             d+=1
#         elif c ==2:
#             print("durang")
#     if a == "tosh":
#         if c == 1:
#             print("siz yutingiz")
#             d+=1
#         elif c == 2:
#             print("siz yutqazdingiz")
#         elif c == 3:
#             print("durang")
#     if a == 'qaychi':
#         if c == 1:
#             print('durang')
#         elif c == 2:
#             print('siz yutingiz')
#             d+=1
#         elif c == 3:
#             print('siz yutqazdingiz')