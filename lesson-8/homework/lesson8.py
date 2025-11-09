## 1. Write a Python program to handle a `ZeroDivisionError` exception when dividing a number by zero.
try:
    a = int(input("Birinchi sonni kiriting: "))
    b = int(input("Ikkinchi sonni kiriting: "))
    result = a / b
    print("Natija:", result)
except ZeroDivisionError:
    print("Xato: Siz 0 ga bo‘lishga urindingiz!")  # 0 ga bo‘lish xatosi
except ValueError:
    print("Xato: Iltimos, faqat son kiriting!") 

## 2. Write a Python program that prompts the user to input an integer and raises a `ValueError` exception if the input is not a valid integer.
try:
    num = input("Iltimos, bir butun son kiriting: ")
    if not num.isdigit() and not (num.startswith('-') and num[1:].isdigit()):
            raise ValueError("Bu butun son emas!")
    num = int(num)
    print("Siz kiritgan son:", num)
except ValueError as xato:
    print("Xato:", xato)

## 3. Write a Python program that opens a file and handles 
## a `FileNotFoundError` exception if the file does not exist.
filename = input("Fayl nomini kiriting: ")

try:
        with open(filename, "r") as file:
        content = file.read()
        print("Fayl mazmuni:")
        print(content)

except FileNotFoundError:
        print(f"Xato: '{filename}' nomli fayl topilmadi!")

## 4. Write a Python program that prompts the user to input two numbers and 
# raises a `TypeError` exception if the inputs are not numerical.
try:
    a = input("Birinchi sonni kiriting: ")
    b = input("Ikkinchi sonni kiriting: ")

    # Foydalanuvchi kiritgan qiymatlar sonmi?
    if not (a.replace('.', '', 1).isdigit() or (a.startswith('-') and a[1:].replace('.', '', 1).isdigit())):
        raise TypeError("Birinchi kiritilgan qiymat raqam emas!")
    if not (b.replace('.', '', 1).isdigit() or (b.startswith('-') and b[1:].replace('.', '', 1).isdigit())):
        raise TypeError("Ikkinchi kiritilgan qiymat raqam emas!")

    # Haqiqiy sonlarga o‘tkazish
    a = float(a)
    b = float(b)

    print(f"Natija: {a} + {b} = {a + b}")

except TypeError as te:
    print("Xato:", te)


## 5. Write a Python program that opens a file and handles a `PermissionError` 
# exception if there is a permission issue.
filename = input("Fayl nomini kiriting: ")

try:
    # Faylga yozish uchun ochish
    with open(filename, "w") as file:
        file.write("Bu faylga yozilayotgan test matni.\n")
        print("Faylga muvaffaqiyatli yozildi!")

except PermissionError:
    # Agar foydalanuvchida faylga yozish yoki ochish uchun ruxsat bo‘lmasa
    print(f"Xato: '{filename}' fayliga kirish uchun ruxsat yo‘q!")

## 6. Write a Python program that executes an operation on a list and handles an 
# `IndexError` exception if the index is out of range.
my_list = [10, 20, 30, 40, 50]

try:
    index = int(input("Qaysi indeksdagi elementni ko‘rmoqchisiz (0-4): "))
    print("Tanlangan element:", my_list[index])

except IndexError:
    print("Xato: Siz tanlagan indeks ro‘yxat chegarasidan tashqarida!")
except ValueError:
    print("Xato: Iltimos, faqat butun son kiriting!")


## 7. Write a Python program that prompts the user to input a number and handles a
#  `KeyboardInterrupt` exception if the user cancels the input.
try:
    num = int(input("Iltimos, bir son kiriting: "))
    print("Siz kiritgan son:", num)

except KeyboardInterrupt:
    print("\nXato: Foydalanuvchi kiritishni bekor qildi (Ctrl + C bosildi).")
except ValueError:
    print("Xato: Iltimos, faqat butun son kiriting!")


## 8. Write a Python program that executes division and handles 
# an `ArithmeticError` exception if there is an arithmetic error.
try:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting: "))

    result = a / b
    print(f"Natija: {a} / {b} = {result}")

except ArithmeticError:
    print("Xato: Arifmetik xato yuz berdi (masalan, nolga bo‘lish mumkin emas)!")
except ValueError:
    print("Xato: Iltimos, faqat son kiriting!")

## 9. Write a Python program that opens a file and handles a `UnicodeDecodeError` 
# exception if there is an encoding issue.
filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print("Fayl mazmuni:")
        print(content)

except FileNotFoundError:
    print(f"Xato: '{filename}' nomli fayl topilmadi!")

except UnicodeDecodeError:
    print(f"Xato: '{filename}' faylini o‘qishda kodlash (encoding) muammosi yuz berdi!")
    print("Masalan, fayl boshqa kodlashda (latin1 yoki cp1251) yozilgan bo‘lishi mumkin.")


## 10. Write a Python program that executes a list operation and handles 
## an `AttributeError` exception if the attribute does not exist.
my_list = [1, 2, 3, 4, 5]

try:
       my_list.push(6)
    print("Yangilangan ro‘yxat:", my_list)

except AttributeError:



## 1. Write a Python program to read an entire text file.


## 3. Write a Python program to append text to a file and display the text.
filename = input("Fayl nomini kiriting: ")
text_to_append = input("Faylga qo‘shmoqchi bo‘lgan matningizni kiriting: ")

try:
    # Faylga matn qo‘shish (append mode 'a')
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text_to_append + "\n")  # yangi qator qo‘shish

    # Fayl mazmunini chiqarish
    print("\n📄 Fayl mazmuni:")
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())

except FileNotFoundError:
    print(f"Xato: '{filename}' nomli fayl topilmadi!")
except UnicodeDecodeError:
    print(f"Xato: '{filename}' faylini o‘qishda kodlash (encoding) muammosi yuz berdi.")


## 4. Write a Python program to read last n lines of a file.
filename = input("Fayl nomini kiriting: ")

try:
    n = int(input("Nechta oxirgi qatorni o‘qimoqchisiz? "))

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()  # fayldagi barcha qatorlarni ro'yxatga olish
        # Oxirgi n qatorni olish
        last_lines = lines[-n:]

        print(f"\n📄 Faylning oxirgi {n} qatori:")
        for line in last_lines:
            print(line.strip())

except FileNotFoundError:
    print(f"Xato: '{filename}' nomli fayl topilmadi!")
except ValueError:
    print("Xato: Iltimos, butun son kiriting!")
except UnicodeDecodeError:
    print(f"Xato: '{filename}' faylini o‘qishda kodlash (encoding) muammosi yuz berdi.")


## 5. Write a Python program to read a file line by line and store it into a list.
filename = input("Fayl nomini kiriting: ")

try:
    lines_list = []  # qatorlarni saqlash uchun bo‘sh ro‘yxat

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:  # faylni qatorma-qator o‘qish
            lines_list.append(line.strip())  # '\n' belgilarini olib tashlash

    print("\n📄 Fayl mazmuni ro‘yxat shaklida:")
    print(lines_list)

except FileNotFoundError:
    print(f"Xato: '{filename}' nomli fayl topilmadi!")
except UnicodeDecodeError:
    print(f"Xato: '{filename}' faylini o‘qishda kodlash (encoding) muammosi yuz berdi.")


## 6. Write a Python program to read a file line by line and store it into a variable.
filename = input("Fayl nomini kiriting: ")

try:
    file_content = ""  # fayl mazmunini saqlash uchun bo‘sh o‘zgaruvchi

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:  # faylni qatorma-qator o‘qish
            file_content += line  # har bir qatorni o‘zgaruvchiga qo‘shish

    print("\n📄 Fayl mazmuni bitta o‘zgaruvchida:")
    print(file_content)

except FileNotFoundError:
    print(f"Xato: '{filename}' nomli fayl topilmadi!")
except UnicodeDecodeError:
    print(f"Xato: '{filename}' faylini o‘qishda kodlash (encoding) muammosi yuz berdi.")


## 7. Write a Python program to read a file line by line and store it into an array.
filename = input("Fayl nomini kiriting: ")

try:
    lines_array = []  # qatorlarni saqlash uchun bo‘sh array (list)

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:  # faylni qatorma-qator o‘qish
            lines_array.append(line.strip())  # '\n' belgilarini olib tashlash

    print("\n📄 Fayl mazmuni array (list) shaklida:")
    print(lines_array)

except FileNotFoundError:
    print(f"Xato: '{filename}' nomli fayl topilmadi!")
except UnicodeDecodeError:
    print(f"Xato: '{filename}' faylini o‘qishda kodlash (encoding) muammosi yuz berdi.")
Python’da array ko‘pincha list sifatida ishlatiladi.

## for line in file: → faylni qatorma-qator o‘qiydi.
## line.strip() → qator oxiridagi bo‘sh joy va \n belgilarini olib tashlaydi.
## lines_array.append() → har bir qatorni array (list) ga qo‘shadi.

## 8. Write a Python program to find the longest words.
text = input("Matn kiriting: ")
# So‘zlarni bo‘sh joylar bo‘yicha ajratish
words = text.split()
# Eng uzun so‘z uzunligini topish
max_length = max(len(word) for word in words)
# Eng uzun so‘zlarni olish
longest_words = [word for word in words if len(word) == max_length]

print(f"\nEng uzun so‘z(lar) ({max_length} belgidan iborat): {longest_words}")

## text.split() → matndagi barcha so‘zlarni ro‘yxatga ajratadi.
## max(len(word) for word in words) → eng uzun so‘z uzunligini topadi.
## [word for word in words if len(word) == max_length] → barcha eng uzun so‘zlarni ro‘yxatga soladi.

## 9. Write a Python program to count the number of lines in a text file.
filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        line_count = sum(1 for line in file)  # har bir qator uchun 1 qo‘shish

    print(f"\nFaylda jami {line_count} qator mavjud.")

except FileNotFoundError:
    print(f"Xato: '{filename}' nomli fayl topilmadi!")
except UnicodeDecodeError:
    print(f"Xato: '{filename}' faylini o‘qishda kodlash (encoding) muammosi yuz berdi.")

## sum(1 for line in file) → fayldagi har bir qatorda 1 qo‘shadi va jami qatorlar sonini hisoblaydi.
## with open(...) as file: → faylni xavfsiz ochish va avtomatik yopishni ta’minlaydi.
## FileNotFoundError va UnicodeDecodeError → faylni topa olmaslik yoki kodlash muammolari uchun


## 10. Write a Python program to count the frequency of words in a file.
from collections import Counter
import string

filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    # So‘zlarni ajratish va punktuatsiyani olib tashlash
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).lower().split()

    # So‘zlar chastotasini hisoblash
    word_count = Counter(words)

    print("\n📊 Fayldagi so‘zlar chastotasi:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

except FileNotFoundError:
    print(f"Xato: '{filename}' nomli fayl topilmadi!")
except UnicodeDecodeError:
    print(f"Xato: '{filename}' faylini o‘qishda kodlash (encoding) muammosi yuz berdi.")

## str.maketrans('', '', string.punctuation) → barcha punktuatsiya belgilarini olib tashlaydi.
## text.translate(translator).lower().split() → matnni kichik harflarga o‘tkazadi va so‘zlarga ajratadi.
## Counter(words) → har bir so‘zning nechta marta kelganini hisoblaydi.
## word_count.items() → so‘z va uning chastotasini chiqaradi.

## 11. Write a Python program to get the file size of a plain file.
import os

filename = input("Fayl nomini kiriting: ")

try:
    # Fayl hajmini baytlarda olish
    size_in_bytes = os.path.getsize(filename)

    print(f"\nFayl hajmi: {size_in_bytes} bayt")

except FileNotFoundError:
    print(f"Xato: '{filename}' nomli fayl topilmadi!")
except OSError as e:
    print(f"Xato: Fayl hajmini olishda muammo yuz berdi. ({e})")

## os.path.getsize(filename) → fayl hajmini baytlarda qaytaradi.
## FileNotFoundError → fayl mavjud bo‘lmasa xatolikni bildiradi.
## OSError → boshqa tizim bilan bog‘liq muammolarni ushlaydi (masalan, faylga ruxsat yo‘q).

## 12. Write a Python program to write a list to a file.
my_list = ["Olma", "Banan", "Anor", "Apelsin", "Gilos"]

# Fayl nomi
filename = "fruits.txt"
try:
    with open(filename, "w", encoding="utf-8") as file:
        for item in my_list:
            file.write(item + "\n")  # har bir elementni yangi qatorga yozish

    print(f"Ro'yxat '{filename}' fayliga yozildi muvaffaqiyatli!")

except OSError as e:
    print(f"Xato: Faylga yozishda muammo yuz berdi. ({e})")

## with open(filename, "w") → faylni yozish uchun ochadi (w mavjud faylni ustiga yozadi).
## for item in my_list: → ro‘yxat elementlarini birma-bir faylga yozadi.
## item + "\n" → har bir elementni yangi qatordan boshlash uchun.


## 13. Write a Python program to copy the contents of a file to another file.
source_file = input("Manba fayl nomini kiriting: ")
destination_file = input("Nusxa fayl nomini kiriting: ")

try:
    # Manba faylni o'qish
    with open(source_file, "r", encoding="utf-8") as src:
        content = src.read()

    # Mazmunni yangi faylga yozish
    with open(destination_file, "w", encoding="utf-8") as dest:
        dest.write(content)

    print(f"Fayl muvaffaqiyatli nusxalandi: '{destination_file}'")

except FileNotFoundError:
    print(f"Xato: '{source_file}' fayl topilmadi!")
except OSError as e:
    print(f"Xato: Fayl bilan ishlashda muammo yuz berdi. ({e})")

# with open(source_file, "r") → manba faylni o‘qish uchun ochadi.
# with open(destination_file, "w") → nusxa faylni yozish uchun ochadi.
# src.read() → fayldagi barcha matnni o‘qiydi.
# dest.write(content) → o‘qilgan matnni yangi faylga yozadi.
# FileNotFoundError → manba fayl mavjud bo‘lmasa xatolikni bildiradi.
# OSError → faylga ruxsat yoki boshqa tizim xatoliklari uchun.

## 14. Write a Python program to combine each line from the
# first file with the corresponding line in the second file.
file1 = input("Birinchi fayl nomini kiriting: ")
file2 = input("Ikkinchi fayl nomini kiriting: ")
output_file = input("Natija fayl nomini kiriting: ")

try:
    # Ikkala faylni o'qish
    with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # Qatorlarni birlashtirish (qisqaroq fayl uzunligiga moslash)
    combined_lines = [l1.strip() + " " + l2.strip() for l1, l2 in zip(lines1, lines2)]

    # Natijani faylga yozish
    with open(output_file, "w", encoding="utf-8") as out:
        for line in combined_lines:
            out.write(line + "\n")

    print(f"Fayllar muvaffaqiyatli birlashtirildi: '{output_file}'")

except FileNotFoundError as e:
    print(f"Xato: Fayl topilmadi! ({e.filename})")
except OSError as e:
    print(f"Xato: Fayl bilan ishlashda muammo yuz berdi. ({e})")

# readlines() → fayldagi barcha qatolarni ro‘yxatga o‘qiydi.
# zip(lines1, lines2) → ikki fayldagi qatolarni birma-bir juftlaydi.
# strip() → qatordagi bo‘shliq va yangi qatordan tozalash uchun.
# l1.strip() + " " + l2.strip() → qatolarni bitta qatorda bo‘sh joy bilan birlashtiradi.
# Natija output_file ga yoziladi.

# 15. Write a Python program to read a random line from a file.
import random

filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()  # fayldagi barcha qatolarni ro'yxatga olish

    if lines:
        random_line = random.choice(lines).strip()  # tasodifiy qatorni tanlash va bo'shliqni olib tashlash
        print("Tasodifiy qator:", random_line)
    else:
        print("Fayl bo'sh!")

except FileNotFoundError:
    print(f"Xato: '{filename}' fayl topilmadi!")
except OSError as e:
    print(f"Xato: Fayl bilan ishlashda muammo yuz berdi. ({e})")

# readlines() → fayldagi barcha qatolarni ro‘yxatga oladi.
# random.choice(lines) → ro‘yxatdan tasodifiy element tanlaydi.
# .strip() → qatordagi ortiqcha bo‘sh joy va yangi qatordan tozalaydi.
# FileNotFoundError → fayl mavjud bo‘lmasa xatolikni bildiradi.

## 16. Write a Python program to assess if a file is closed or not.
filename = input("Fayl nomini kiriting: ")

try:
    # Faylni ochish
    file = open(filename, "r", encoding="utf-8")
    print("Fayl hozir ochiqmi?", not file.closed)  # True → ochiq, False → yopiq

    # Faylni yopish
    file.close()
    print("Fayl yopilgandan keyin:", file.closed)  # True → yopilgan

except FileNotFoundError:
    print(f"Xato: '{filename}' fayl topilmadi!")
except OSError as e:
    print(f"Xato: Fayl bilan ishlashda muammo yuz berdi. ({e})")

# file.closed → faylning yopilgan yoki ochiq ekanligini tekshiradi.
# True → fayl yopilgan
# False → fayl ochiq
# file.close() → faylni yopadi.
# FileNotFoundError → fayl mavjud bo‘lmasa xatolikni bildiradi.

## 17. Write a Python program to remove newline characters from a file
filename = input("Fayl nomini kiriting: ")
output_file = input("Natija fayl nomini kiriting: ")

try:
    # Fayldan o'qish
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    # Yangi qator belgilarini olib tashlash
    content_without_newlines = content.replace("\n", "")

    # Natijani faylga yozish
    with open(output_file, "w", encoding="utf-8") as out:
        out.write(content_without_newlines)

    print(f"Fayldagi barcha yangi qator belgilar olib tashlandi va saqlandi: '{output_file}'")

except FileNotFoundError:
    print(f"Xato: '{filename}' fayl topilmadi!")
except OSError as e:
    print(f"Xato: Fayl bilan ishlashda muammo yuz berdi. ({e})")

# file.read() → fayldagi barcha matnni o‘qiydi.
# content.replace("\n", "") → barcha yangi qator belgilarini olib tashlaydi.
# Natija output_file ga yoziladi.
# FileNotFoundError → fayl mavjud bo‘lmasa xatolikni bildiradi.

## 18. Write a Python program that takes a text file as input and returns the number of words in a given text file.
#   - **Note:** Some words can be separated by a comma with no space.
import re

filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    # So'zlarni ajratish: bo'shliq, vergul va boshqa tinish belgilariga qarab
    words = re.split(r'[,\s]+', content.strip())  # vergul yoki bo'shliq bo'yicha ajratish

    # Bo'sh elementlarni olib tashlash (agar bo'sh string bo'lsa)
    words = [word for word in words if word]

    print(f"Faylda jami so'zlar soni: {len(words)}")

except FileNotFoundError:
    print(f"Xato: '{filename}' fayl topilmadi!")
except OSError as e:
    print(f"Xato: Fayl bilan ishlashda muammo yuz berdi. ({e})")

# re.split(r'[,\s]+', content.strip()) →
# Fayldagi matnni bo‘shliq (\s) yoki vergul bo‘yicha ajratadi, shuningdek ketma-ket bo‘sh joylar va vergullar bilan ishlaydi.
# words = [word for word in words if word] → bo‘sh stringlarni chiqarib tashlaydi.
# len(words) → jami so‘zlar sonini beradi.

## 19. Write a Python program to extract characters from various text files and put them into a list.
filenames = input("Fayl nomlarini vergul bilan ajrating: ").split(",")

all_chars = []

for fname in filenames:
    fname = fname.strip()  # ortiqcha bo'sh joylarni olib tashlash
    try:
        with open(fname, "r", encoding="utf-8") as file:
            content = file.read()
            all_chars.extend(list(content))  # har bir belgini ro'yxatga qo'shish
    except FileNotFoundError:
        print(f"Xato: '{fname}' fayl topilmadi!")
    except OSError as e:
        print(f"Xato: Fayl bilan ishlashda muammo yuz berdi. ({e})")

print("Barcha belgilar ro'yxati:")
print(all_chars)
print(f"Jami belgilar soni: {len(all_chars)}")

# filenames = input(...).split(",") → foydalanuvchi kiritgan fayl nomlarini vergul orqali ajratadi.
# list(content) → har bir fayldagi barcha belgilarni ro‘yxatga qo‘shadi.
# all_chars.extend(...) → barcha fayllardan olingan belgilarni bitta umumiy ro‘yxatga qo‘shadi.
# FileNotFoundError va OSError → fayl mavjud bo‘lmasa yoki ochishda muammo bo‘lsa xatolikni bildiradi.


## 20. Write a Python program to generate 26 text files named `A.txt`, `B.txt`, and so on up to `Z.txt`.
import string

# A dan Z gacha harflar ro'yxati
letters = string.ascii_uppercase  # ['A', 'B', ..., 'Z']

for letter in letters:
    filename = f"{letter}.txt"
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Bu fayl {letter}.txt deb nomlangan.\n")
        print(f"Fayl yaratildi: {filename}")
    except OSError as e:
        print(f"Xato: '{filename}' faylni yaratib bo'lmadi ({e})")

# string.ascii_uppercase → A dan Z gacha barcha katta harflarni beradi.
# with open(filename, "w") → har bir faylni yozish rejimida yaratadi.
# Faylga oddiy matn yoziladi: "Bu fayl X.txt deb nomlangan."
# OSError → fayl yaratishda muammo bo‘lsa xatolikni bildiradi.

## 21. Write a Python program to create a file where all letters of the English alphabet are 
# listed with a specified number of letters on each line.

import string

# Foydalanuvchidan fayl nomi va har bir qatordagi harflar sonini so'rash
filename = input("Yaratiladigan fayl nomini kiriting: ")
letters_per_line = int(input("Har bir qatorda nechta harf bo'lishini xohlaysiz? "))

alphabet = string.ascii_uppercase  # A dan Z gacha harflar

try:
    with open(filename, "w", encoding="utf-8") as file:
        for i in range(0, len(alphabet), letters_per_line):
            # Har bir qatorda n ta harf yoziladi
            line = alphabet[i:i + letters_per_line]
            file.write(line + "\n")
    print(f"Fayl yaratildi: {filename}")

except OSError as e:
    print(f"Xato: Fayl yaratishda muammo yuz berdi. ({e})")

# string.ascii_uppercase → A dan Z gacha barcha katta harflarni beradi.
# range(0, len(alphabet), letters_per_line) → har bir qadamda kerakli miqdordagi harflarni oladi.
# file.write(line + "\n") → har bir qatorda letters_per_line harf va yangi qator belgisini yozadi.
