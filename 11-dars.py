# t = 'hgdhgrdajrgsd jtdjanhtdjathdj  hjafdagfjj ghdjhgjgajhgjhma'
# n = 0
# for i in t:
#     if i == "a":
#         n += 1
# print(n)
#
#
# t = 'hgdDgrdajAgsd jtdjaAhtdjDathdj  hjaDfdagfjj ghAdjhgjgajAhgjhma'
# n = ""
# for i in t:
#     if i == "a":
#         n+=i
# print(n)

# t = 'hgdDgrdajAgsd jtdjaAhtdjDathdj  hjaDfdagfjj ghAdjhgjgajAhgjhma'
# n = ""
# for i in t:
#     if  i.isupper():
#         n+=i
# print(n)

# t = 'hgdDgrdajAgsd jtdjaAhtdjDathdj  hjaDfdagfjj ghAdjhgjgajAhgjhma'
# n = ""
# m = ""
# for i in t:
#     if  i.islower():
#         n += i
#     if i.isupper():
#         m+=i
# print(n)
# print(m)


# nums = [45,45,30,45,20,44,20]
# k = 0
# for i in nums:
#     if i == 45:
#         k+=1
# print(k)

# nums = [45,45,45,45,45,45,4,54,24242,422,2,]
# k =[]
# for i in nums:
#     if i ==45:
#         k.append(i)
# print(k)


# number = input(">>")
# nums = [45,34,100,3,33,45,23,22,10,50,56,12]
# k = []
# n = []
# for i in nums:
#     if i % 5 == 0:
#         k.append(i)
#     if i % 3 == 0:
#         n.append(i)
# print(k)
# print(n)

# number = int(input(">>"))
# nums = [45,34,100,3,33,45,23,22,10,50,56,12]
# k = []
# for i in nums:
#     if number != i:
#         k.append(i)
# print(k)

# a = int(input(">>"))
# nums = [45,34,100,3,33,45,23,22,10,50,56,12]
# k = []
# for i in nums:
#     if a == 1:
#         if i % 2 == 0:
#             k.append(i)
#     if a == 2:
#         if i % 2 == 1:
#             k.append(i)
# print(k)




# s = [1,5,7,3,6,10,22,50,60,33,99,100,111,239,560,999,777,674,467]
# a = []
# b = []
# c = []
# for i in s:
#     if i < 10:
#         a.append(i)
#     if i >= 10 and i < 100:
#             b.append(i)
#     if i >= 100 and i < 1000:
#                 c. append(i)
#
# print(a)
# print(b)
# print(c)


# d = int(input(">>"))
# s = [1,5,7,3,6,10,22,50,60,33,99,100,111,239,560,999,777,674,467]
# a = []
# b = []
# c = []
# for i in s:
#     if d == 1:
#         if i % 2 == 0:
#             if i < 10:
#                 a.append(i)
#             if i >= 10 and i < 100:
#                 b.append(i)
#             if i >= 100 and i < 1000:
#                 c.append(i)
#     if d == 2:
#         if i % 2 == 1:
#             if i < 10:
#                 a.append(i)
#             if i >= 10 and i < 100:
#                 b.append(i)
#             if i >= 100 and i < 1000:
#                 c.append(i)
#     if d == 3:
#         if i < 10:
#             a.append(i)
#         if i >= 10 and i < 100:
#             b.append(i)
#         if i >= 100 and i < 1000:
#             c.append(i)
# print(a)
# print(b)
# print(c)


## forga oid misolar
# k = int(input("k sonini kiriting: "))
# n = int(input("necha marta chiqarilsin: "))
# nums = [k] * n
# for num in nums:
#     print(num)
#

# a = int(input("a ni kiriting: "))
# b = int(input("b ni kiriting: "))
# numbers = [a + j for j in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] if a + j <= b]
# for num in numbers:
#     print(num)
#

# a = int(input("a ni kiriting: "))
# b = int(input("b ni kiriting: "))
# numbers = [b - j for j in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] if b - j >= a]

# for num in numbers:
#     print(num)
#
# price = float(input("1 kg konfet narxi: "))
# nums = [1,2,3,4,5,6,7,8,9,10]
# for num in nums:
#     print(num, "kg konfet narxi:", price * num)
#
#
# price = float(input("1 kg konfet narxi: "))
# nums = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
# for num in nums:
#     print(num, "kg konfet narxi:", price * num)




