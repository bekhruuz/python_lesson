# import datetime
#
# date = datetime.date(2025,7,5)
# today = datetime.date.today()
#
# time = datetime.time(4,20)
# now = datetime.datetime.now()
#
#
# print(now, today)


from datetime import datetime
import time


# now = datetime.now()
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)


# while True:
#     now = datetime.now()
#     print(f"{now.hour}:{now.minute}:{now.second}")
#     time.sleep(1)


# print('salom hammaga')
# time.sleep(1)
while True:
 a = input("soatni kriting")
 now = datetime.now()
 print(now.hour ,":", now.minute)
 if now == a:
    print("ayni vaqtida")
 else:
    print('hozir unday vaqt emas')
