# """
# doct(dictiondy)
# """
#
# # d = {"name":"azizbek", "age": 23,"phobne":"93923019320"}
# # ismi = d.get("name ")
#
#
#
#
# # a = {
# #     'city':'berlin',
# #     'country':'Geraniy',
# #     'population':'3645000'
# # }
# #
# # print(a.get('population'))
#
#
#
#
# lugat ={
#     'mushuk':'cat',
#     'kitob':'book',
#     'avtomabil':'car',
#     'avtobus':'bus',
#     'bosh':'head',
#     'ari':'bee',
#     'asal ari':"honey bee",
#     'qizil':'red',
#     'qora':'black',
#     'hujum':'atack',
#     'ichida':'in',
#     'chimoli':'ant',
#     'tulki':'fox'
#
#
# }
# while True:
#     a = input('>>')
#     print(lugat.get(a))
# a =  {
#     0:'nol',
#     1:'bir',
#     2:'ikki',
#     3:'uch',
#     4:'to`rt',
#     5:'besh',
#     6:'olti',
#     7:'yetti',
#     8:'sakkiz',
#     9:'toqqiz'
# }
# while True:
#      b = int(input('son kiriting:'))
#      print(a.get(b))
#      if b == 0:
#       break



# a = {
#     1:'bir',
#     2:'ikki',
#     3:'uch',
#     4:'to`rt',
#     5:'besh',
#     6:'olti',
#     7:'yetti',
#     8:'sakkiz',
#     9:'toqqiz'
# }
# b = {
#      10:'on',
#      20:"yigirma",
#      30:"ottiz",
#      40:'qirq',
#      50:"elik",
#      60:'oltmish',
#      70:'yettmish',
#      80:"sakson",
#      90:"toqsan"
# }
# while True:
#      c = int(input("sonni kiriting:")) # 25
#      n1 = c // 10 * 10
#      n2 = c % 10
#      print(b.get(n1), a.get(n2))
#      if c == 0:
#           break


a = {
    0:'',
    1:'bir',
    2:'ikki',
    3:'uch',
    4:'to`rt',
    5:'besh',
    6:'olti',
    7:'yetti',
    8:'sakkiz',
    9:'toqqiz'
}
b = {
     10:'on',
     20:"yigirma",
     30:"ottiz",
     40:'qirq',
     50:"elik",
     60:'oltmish',
     70:'yettmish',
     80:"sakson",
     90:"toqsan"
}
c = {
     100:'biryuz',
     200:'ikkiyuz',
     300:'uchyuz',
     400:'tortyuz',
     500:'beshyuz',
     600:'oltiyuz',
     700:'yettiyuz',
     800:'sakkiz yuz',
     900:'toqqiz yuz'
}
while True:
      n = int(input("sonni kiriting:")) # 145
      n4 = n // 10 * 10# onlilar uchun
      n1 = n // 100 * 100# 1
      n2 = n % 100 //10 * 10# 4
      n3 = n % 10 #5
      n5 = n % 10
      if n in b:
          print(b.get(n))
      elif n in c:
          print(c.get(n1))
      elif n in a:
          print(a.get(n))
      elif n < 10:
          print(a.get(n3))
      elif 10 <= n <= 99:
          print(b.get(n2), a.get(n3))
      elif 100 < n <= 999:
          print(c.get(n1), b.get(n2), a.get(n5))