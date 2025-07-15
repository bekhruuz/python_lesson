"""
taqqoslash operatori (realations)
< > <= >= == !=
"""

# print(89 > 0) # True
# print(89 < 0) # False
# print(89 <= 89) # True
# print(89 <= 90) # True
# print(89 >= 90) # False
# print(89 == 90) # False
# print(89 != 90) # True

"""
bool(boolean) - True va False (1 va 0)
"""

# a = bool("salom") #
# b = bool("") # False
# c = bool(0)  # False
# d = bool(-0.000000001) # True
# print(d)
# a = int(input("a: ")) # 17
# n1 = a // 10 # 1
# n2 = a % 10 # 7
# print(n2, n1) # 7 1  mumkin emas


# a = int(input("a: ")) # 123 -> 321
# n1 = a // 100 # 1
# n2 = a % 100 // 10  # 2
# n3 = a % 10 # 3
# natija = n3 * 100 + n2 * 10 + n1 # 321
# print(natija)


#
# '''organib kelish and or not va if'''
# '''uyga fazifa'''
# if shartli operatori
# a = int("son kiriting")
# if a%2==0:
#  print(a,"juft son")
# else:
#     print(a,"toq son")

#2- usuli

# a = int(input("son kiriting:"))
# if (-1) **a>0:
#  print(a,"juft son")
# else:
#     print(a,"toq son")

'''or-->yoki haqida'''
# yosh = int(input("yoshingizni kiriting:"))
# if  yosh <=6 or yosh >= 60:
#     print("sizga teatr uchu bepul chipta")
# else:
#     print("sizga chipta yoq ")

'''and-->va haqida'''
# login =input("login:")
# parol =input("parol:")
# if login =="admin" and parol=="1234":
#     print("sizga ruxsat")
# else:
#     print("notogri parol , qaytadan urinib koring")

''''not-->inkor haqida'''
son =int(input("son:"))
if not(son>0):
    print("bu son musbat")
else:
    print("bu son manfiy")
