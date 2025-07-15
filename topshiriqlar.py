#  1-masala
#  L = int(input("L metrni liritimg: "))
#  metrlar = L // 100
#
#  print("L metr javobi:", metrlar)
#  2-masala
# M = int(input("Og'irlikni kiriting (grammda): "))
# ogirlik = M // 1000
# print("Kilogrammda og'irlik:", ogirlik)
#
# 4-misol
# A = float(input("A kesmaning uzunligini kiriting: "))
# B = float(input("B kesmaning uzunligini kiriting: "))
# if B <= 0:
#     print("B musbat son bo'lishi kerak.")
# else:
#     joylashish_soni = int(A // B)
#     print(f"B kesmani A kesmaga {joylashish_soni} marta joylashtirish mumkin.")
#
# 5-misol
# A = float(input("A kesma uzunligini kiriting: "))
# B = float(input("B kesma uzunligini kiriting: "))
# if B > 0:
#     joylashish_soni = int(A // B)
#     print(f"B kesmani A kesmaga {joylashish_soni} marta joylashtirish mumkin.")
# else:
#     print("B musbat son bo'lishi kerak.")
#
#  6-masala
#  5 shni ishlay olmadim 4 niham qiyin ekan
# son = int(input("Sonni kiriting: "))
# onlik = son // 10
# birlik = son % 10
# print("Onliklar:", onlik)
# print("Birliklar:", birlik)
#
#
#  7- masala
#  son =  input("sonni kiriting:")
#  a = son // 10
#  b = son % 10
#  print("sonlar yigindisi" )
#
#   8-masala
#  son = int(input("sonni kiritin"))
#  a_son = son // 10
#  b_son = son % 10
#  c_son = b_son + a_son
#  print("javob",c_son)
#
#  9-misol
#  son = int(input("Uch xonali son kiriting: "))
#  birlik = son % 10
#  onlik = (son // 10) % 10
#  print("Birliklar xonasidagi raqam:", birlik)
#  print("O'nliklar xonasidagi raqam:", onlik)
#
#  10-misol
#  son = int(input("Uch xonali son kiriting: "))
#  birlik = son % 10
#  onlik = (son // 10) % 10
#  yuzlik = son // 100
#  yigindi = yuzlik + onlik + birlik
#  print("javob:", yigindi)
#
#  11-misol
#
#  son = int(input("Uch xonali son kiriting: "))
#  yuzlik = son // 100
#  onlik = (son // 10) % 10
#  birlik = son % 10
#  yangi_son = onlik * 10 + birlik
#  yangi_son = yangi_son * 10 + yuzlik
#  print("javob:", yangi_son)
#
#  12-misol
#  son = int(input("Uch xonali son kiriting: "))
#  yuzlik = son // 100
#  onlik = (son // 10) % 1
#  birlik = son % 10
#  yangi_son = birlik * 100 + yuzlik * 10 + onlik
#  print("javob:", yangi_son)
#
#  # 13-misol
#  son = int(input("Uch xonali son kiriting: "))
#  yuzlik = son // 100
#  onlik = (son // 10) % 10
#  birlik = son % 1
#  yangi_son = onlik * 100 + yuzlik * 10 + birlik
#  print("Yangi hosil bo'lgan son:", yangi_son)
#
# # 14-misol
# son = int(input("Uch xonali son kiriting: "))
# yuzlik = son // 100
# onlik = (son // 10) % 10
# birlik = son % 10
# yangi_son = onlik * 100 + yuzlik * 10 + birlik
# print("Yangi hosil bo'lgan son:", yangi_son)
#
# 15-misol
# son = int(input("Uch xonali son kiriting: "))
# birlik = son % 10
# onlik = (son // 10) % 10
# yuzlik = son // 100
# print("Yangi son:",)
#
# 16-misol
# son = int(input("Uch xonali son kiriting: "))
# yuzlik = son // 100
# onlik = (son // 10) % 10
# birlik = son % 10
# yangi_son = yuzlik * 100 + birlik * 10 + onlik
# print("Yangi son:", yangi_son)

#17-misol
# son = int(input("999 dan katta sonni kiriting: "))
# if son > 999:
#     yuzlik = (son // 100) % 10
#     print("Yuzliklar xonasidagi raqam:", yuzlik)
# else:
#     print("Son 999 dan katta bo'lishi kerak.")

# '''1 chi misol--begin-1'''
# a = float(input("honani yuzasini kiriting: "))
# yuza = a ** 2
# print("honani  yuzisi:", yuza )
#
#
# a = float(input("a ni kiriting: "))
# b = float(input("b ni kiriting: "))
# yuzasi = a * b
# perimetri = 2 * (a + b)
# print("Yuzasi:", yuzasi)
# print("Perimetri:", perimetri)
#
#
# '''begin_4'''
# import math
# d = float(input("Uyning diametrini kiriting: "))
# L = math.pi * d
# print("Uyni uzunligi uzunligi:", L)
#
#
# # begin_5
# a = float(input("Uyning yon tomonini kiriting: "))
# P = 12 * a
# print(uyning perimetri (barcha girralar yig'indisi):", P)
#
#
# # begin_6
# a = float(input("a tomonini kiriting: "))
# b = float(input("b tomonini kiriting: "))
# c = float(input("c tomonini kiriting: "))
# V = a * b * c
# S = 2 * (a*b + b*c + a*c)
# print("Parallelepipedning hajmi:", V)
# print("Parallelepipedning to‘la sirti:", S)
#
#
# # begin_7
# import math
# R = float(input("Doiraning radiusini kiriting: "))
# L = 2 * math.pi * R
# S = math.pi * R**2
# print("Doiraning uzunligi (perimetri):", L)
# print("Doiraning yuzasi:", S)
#
#
# # begin_8
# a = float(input(" son kiriting (a): "))
# b = float(input(" son kiriting (b): "))
# A = (a + b) / 2
# print("O‘rta arifmetik:", A)

# begin-9
# import math
# a = -4
# b = -9
# geo = math.sqrt(a * b)
# print("Geometrik o‘rtacha:", geo)
# begin-10
# son = int(input("Uch xonali son kiriting: "))

#begin-10
# if 100 <= son <= 999:
#     birlik = son % 10
#     onlik = (son // 10) % 10
#     print("javob:", birlik)
#     print("javob:", onlik)

# begin-11
# son = int(input("Uch xonali sonni kiriting: "))
# birlik = son % 10
# onlik = (son // 10) % 10
# yuzlik = son // 100
# yigindi = birlik + onlik + yuzlik
# print("Raqamlar yig'indisi:", yigindi)

# begin-12
# son = int(input("Uch xonali sonni kiriting: "))
# birlik = son % 10
# onlik = (son // 10) % 10
# yuzlik = son // 100
# yangi_son = birlik * 100 + onlik * 10 + yuzlik
# print("barcha yigindi:", yangi_son)
# Foydalanuvchidan uch xonali sonni olish

# begin-13
# son = int(input("soni kiriting: "))
# yuzlik = son // 100
# a = son % 100
# b = a * 10 + yuzlik
# print("javob", b)

# begin-14
# son = int(input("Uch xonali sonni kiriting: "))
# birlik = son % 10
# qolgan = son // 10

# begin-15
# son = int(input("sonni kirirting: "))
# birlik = son % 10
# onlik = (son // 10) % 10
# yuzlik = son // 100
# yangi_son = onlik * 100 + yuzlik * 10 + birlik
# print("javob:", yangi_son)
