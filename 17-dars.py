"""
funksiya 4 turga bolib olamiz:
1-oddiy funksiya:
    def hi():
        print('salom')

    hi()
2-qiymat qaytaruvchi funksiya
    def hi():
        return 'salom'

    t = hi()
    print(t)
3-oddiy parametrli funksiya
4-qiymat qaytaruvchi parametrli funksiya

def fuksiya yaratish kalit sozi
def ... shu yerda funksiya nomi yoziladi va bu nom orqali funksiya chaqiriladi
        va funksiya ichidagi dastur ishga tushadi
"""

# 1 tur
# def hi():
#     print('salom')
#
# hi()

# 1 - tur
# def nums():
#     for i in range(1, 11):
#         print(i)
#
#
# nums()
# nums()

# 2 chi tur
# def nums():
#     n = []
#     for i in range(1, 11):
#         n.append(i)
#     return n
#
#
# print(nums())
# print(nums())


# 3 - tur
# def hi(name):
#     print(f'Assalomu aleykum {name}')
#
# hi('Behruz')
# hi('Tom')
# hi('Ali')
# hi('Feruz')

# 4-tur
# def hi(name):
#     return f"Assalomu aleykum {name}"
#
# print(hi('Behruz'))
# print(hi('Ali'))
# print(hi('ali'))




# def nums():
#     n = []
#     for i in range(1, 11):
#         n.append(i)
#     return n
#
#
# print(nums())
# print(nums())




#
# t1 = ["l", "a", "l", "o", "m"]
# t2 = ["*", "*", "*", "*", "*",]
# t = 0
# while True:
#     print(t2)
#     a = input('>> ')[0].lower() # l
#     if a in t1:
#         n = t1.index(a)# l ni index raqami
#         for i in range(len(t1)):
#             if t1[i] == a:
#                 t2[i] = a
#         g = t1.index(a)
#         t2[n]=t1[n]
#     elif t2 != a:
#         t+=1
#         print('bu notogri harf')
#     if t2 == t1:
#        break
# print('siz notogri kiritgan harf:', t)


# from random import randint
# t1 = [['s', 'a', 'l', 'o', 'm'], ['h', 'a', 'y', 'r'],['u','c','h'],['a','b','e','t']]
# t2 = [["*", "*", "*", "*", "*"], ['*', '*', '*', '*'],['*','*','*'],['*','*','*','*']]
# i2 = randint(0, 3)
# while True:
#     print(t2[i2])
#     a = input('>> ')[0].lower()
#     if a in t1[i2]:
#         for i in range(len(t1[i2])):
#             if t1[i2][i] == a:
#                 t2[i2][i] = a
#     if t1[i2] == t2[i2]:
#         break
# print('siz barcha sozni togri topdingiz')