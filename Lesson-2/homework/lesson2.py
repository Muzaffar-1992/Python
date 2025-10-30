# Homework Exercises

## 1. Age Calculator
# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

from datetime import date
bugun=date.today()
hozirgi_yil=bugun.year
ism="Muzaffar"
tugilgan_sana=date(1992,3,29)
yosh=hozirgi_yil-tugilgan_sana.year
if (bugun.month, bugun.day) < (tugilgan_sana.month, tugilgan_sana.day):
    yosh -= 1
print(f"Salom, {ism}! Siz {yosh} dasiz.")


## 2. Extract Car Names
#Extract car names from the following text: ```python

txt = 'LMaasleitbtui'
Car_name=txt[::2]
print(Car_name)


## 3. Extract Car Names Extract car names from the following text: ```python
txt = 'MsaatmiazD'

car_name=txt[::2]
print(car_name)

## 4. Extract Residence Area Extract the residence area from the following text: ```python
#1 variant
txt = "I'am John. I am from London"
resident_area=txt[21::]
print(resident_area)
#2 variant
txt = "I'am John. I am from London"
resident_area=txt[-6::]
print(resident_area)
#3 variant
txt = "I'am John. I am from London"




## 5. Reverse String Write a Python program that takes a user input string and prints it in reverse order.
txt="Write a Python program that takes a user input string and prints it in reverse order"
print(txt[::-1])

## 6. Count Vowels txt="Write a Python program that takes a user input string and prints it in reverse order"
unlilar=["a", "u","i", "o", "e"]
soni=sum(txt.count(harf) for harf in unlilar)
print("Jami unli harflar", soni)

## 7. Find Maximum Value Write a Python program that takes a list of numbers as input and prints the maximum value.
txt=("1 2 3 4 5 6 7 8 9").split()
txt = [int(x) for x in txt]
print(max(txt))

## 8. Check Palindrome Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
name="Aziza"
print(name[::-1])

## 9. Extract Email Domain Write a Python program that extracts and prints the domain from an email address provided by the user.
email =("muzaffar@gmail.com: ")

if '@' in email:
    domain = email.split('@')[1]
    print(f"Domen: {domain}")
else:
    print("xato!")

## 10. Generate Random Password Write a Python program to generate a random password containing letters, digits, and special characters.
import secrets
import string

def xavfsiz_parol(uzunlik):
    belgilar = string.ascii_letters + string.digits + string.punctuation
    parol = ''.join(secrets.choice(belgilar) for _ in range(uzunlik))
    return parol

print(xavfsiz_parol(16))
