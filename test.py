# togri = 0
#
# # 1-savol
# print("1-savol: Qaysi biri Python’ga to‘g‘ri o‘zgaruvchi nomi?")
# print("a) 1ism")
# print("b) ism3")
# print("c) 1-ism")
# javob = input("Javobingiz: ").lower()
# if javob == "b":
#     togri += 1
#
# # 2-savol
# print("2-savol: Python'da ro'yxat qanday belgilanadi?")
# print("a) {}")
# print("b) []")
# print("c) ()")
# javob = input("Javobingiz: ").lower()
# if javob == "b":
#     togri += 1
#
# # 3-savol
# print("3-savol: Qaysi biri shart operatori?")
# print("a) if")
# print("b) for")
# print("c) var")
# javob = input("Javobingiz: ").lower()
# if javob == "a":
#     togri += 1
#
# # 4-savol
# print("4-savol: Matn qanday turda bo‘ladi?")
# print("a) int")
# print("b) str")
# print("c) float")
# javob = input("Javobingiz: ").lower()
# if javob == "b":
#     togri += 1
#
# # 5-savol
# print("5-savol: Foydalanuvchidan qiymat olish uchun qaysi funksiya?")
# print("a) input()")
# print("b) print()")
# print("c) read()")
# javob = input("Javobingiz: ").lower()
# if javob == "a":
#     togri += 1
#
# # 6-savol
# print("6-savol: Aylanish operatori qaysi?")
# print("a) if")
# print("b) while")
# print("c) elif")
# javob = input("Javobingiz: ").lower()
# if javob == "b":
#     togri += 1
#
# # 7-savol
# print("7-savol: Ro'yxatga element qo'shish uchun?")
# print("a) append()")
# print("b) add()")
# print("c) insert()")
# javob = input("Javobingiz: ").lower()
# if javob == "a":
#     togri += 1
#
# # 8-savol
# print("8-savol: 5 == 5 ifodasi nima qaytaradi?")
# print("a) True")
# print("b) False")
# print("c) Error")
# javob = input("Javobingiz: ").lower()
# if javob == "a":
#     togri += 1
#
# # 9-savol
# print("9-savol: Butun son turi qanday?")
# print("a) float")
# print("b) int")
# print("c) str")
# javob = input("Javobingiz: ").lower()
# if javob == "b":
#     togri += 1
#
# # 10-savol
# print("10-savol: 'and' bu nima?")
# print("a) mantiqiy operator")
# print("b) matn")
# print("c) list funksiyasi")
# javob = input("Javobingiz: ").lower()
# if javob == "a":
#     togri += 1
#
# # 11-savol
# print("11-savol: print() funksiyasi nima qiladi?")
# print("a) chop etadi")
# print("b) o‘chirish")
# print("c) kiritish")
# javob = input("Javobingiz: ").lower()
# if javob == "a":
#     togri += 1
#
# # 12-savol
# print("12-savol: float nima?")
# print("a) matn")
# print("b) butun son")
# print("c) onlik son")
# javob = input("Javobingiz: ").lower()
# if javob == "c":
#     togri += 1
#
# # 13-savol
# print("13-savol: '==' nimani bildiradi?")
# print("a) tayinlash")
# print("b) tenglik")
# print("c) ayirish")
# javob = input("Javobingiz: ").lower()
# if javob == "b":
#     togri += 1
#
# # 14-savol
# print("14-savol: input() funksiyasi?")
# print("a) chiqadi")
# print("b) kiritadi")
# print("c) o‘chiradi")
# javob = input("Javobingiz: ").lower()
# if javob == "b":
#     togri += 1
#
# # 15-savol
# print("15-savol: for nima?")
# print("a) tsikl")
# print("b) if")
# print("c) o‘zgaruvchi")
# javob = input("Javobingiz: ").lower()
# if javob == "a":
#     togri += 1
#
# # 16-savol
# print("16-savol: str() nima qiladi?")
# print("a) raqamga aylantiradi")
# print("b) matnga aylantiradi")
# print("c) o‘chirish")
# javob = input("Javobingiz: ").lower()
# if javob == "b":
#     togri += 1
#
# # 17-savol
# print("17-savol: elif nimaga xizmat qiladi?")
# print("a) shart operatori")
# print("b) ro'yxat")
# print("c) funksiya")
# javob = input("Javobingiz: ").lower()
# if javob == "a":
#     togri += 1
#
# # 18-savol
# print("18-savol: Ro'yxatdan o‘chirish?")
# print("a) delete()")
# print("b) remove()")
# print("c) delit()")
# javob = input("Javobingiz: ").lower()
# if javob == "b":
#     togri += 1
#
# # 19-savol
# print("19-savol: True va False qanday tur?")
# print("a) int", "b) str", "c) bool")
# javob = input("Javobingiz: ").lower()
# if javob == "c":
#     togri += 1
#
# # 20-savol
# print("20-savol: Python fayl ochish funksiyasi?")
# print("a) open()", "b) file()", "c) read()")
# javob = input("Javobingiz: ").lower()
# if javob == "a":
#     togri += 1
#
# #songi qism
# print("Siz", togri, "ta savolga to‘g‘ri javob berdingiz.")




while True:
    togri = 0
    import random
    javob = input("1) O'zbekiston qaysi qit'ada joylashgan? ").strip().lower()
    if javob == "osiyo":
        togri += 1

    javob = input("2) Python dasturlash tilini kim yaratgan? ").strip().lower()
    if javob == "guido van rossum":
        togri += 1

    javob = input("3) Yer Quyosh atrofida nechta kunda aylanishni tugatadi? ").strip().lower()
    if javob == "365":
        togri += 1

    javob = input("4) HTML so‘zining to‘liq ochilishi nima? ").strip().lower()
    if javob == "hypertext markup language":
        togri += 1

    javob = input("5) Kompyuterning yuragi deb nimani atashadi? ").strip().lower()
    if javob == "processor":
        togri += 1

    javob = input("6) Quyosh sistemasidagi eng katta sayyora qaysi? ").strip().lower()
    if javob == "yupiter":
        togri += 1

    javob = input("7) 3 × 9 nechchi bo‘ladi? ").strip().lower()
    if javob == "27":
        togri += 1

    javob = input("8) Toshkent nechanchi yilda poytaxt bo‘lgan? ").strip().lower()
    if javob == "1930":
        togri += 1

    javob = input("9) Inson tanasidagi eng katta aʼzo nima? ").strip().lower()
    if javob == "teri":
        togri += 1

    javob = input("10) Dunyoning eng uzun daryosi qaysi? ").strip().lower()
    if javob == "nil":
        togri += 1

    print("\nTo‘g‘ri javoblar soni:", togri, "/ 10")

    if togri >= 8:
        print("Siz imtihondan o‘tdingiz.")
        break
    else:
        print("Siz imtihondan o‘tolmadingiz. Qaytadan urinib ko‘ring.")