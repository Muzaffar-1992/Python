# 1. Create and Access List Elements
## Create a list containing five different fruits and print the third fruit.

Mevalar = ["olma", "banan", "shaftoli", "anjir", "gilos"]
print(f"Uchinchi meva: {Mevalar[2]}")

## 2. Concatenate Two Lists
## Create two lists of numbers and concatenate them into a single list.

Mevalar = ["olma", "shaftoli", "gilos"]
Mevalar2 = ["banan", "anjir"]
Jami_mevalar = Mevalar+Mevalar2
print(Jami_mevalar)

Sonlar = [1, 2 , 3, 4]
sonlar2 = [2, 3, 4]
yigindi = Sonlar + sonlar2
print("Jami sonlar: ", yigindi)

## 3. Extract Elements from a List
## Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
Raqamlar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
birinchi = Raqamlar[0]
orta = Raqamlar[len(Raqamlar)//2]
oxirgi = Raqamlar[-1]
yangi = [birinchi, orta, oxirgi]
print("Soralgan royxat: ", yangi)

## 4. Convert List to Tuple
## Create a list of your five favorite movies and convert it into a tuple.
Sevimli_kino = ['Kino nomi1', 'kino nomi2', 'kino nomi3']
tuple_uzgardi = tuple(Sevimli_kino)
print("Tuplega o`zgargan: ", tuple_uzgardi)

## 5. Check Element in a List
## Given a list of cities, check if "Paris" is in the list and print the result.
Shaxarlar = ["Toshkent", "London", "New York", "Paris", "Tokyo"]
if "Paris" in Shaxarlar:
    print("xa, Paris bor")
else:
    print("bunday shaxar royxatda yuq")

## 6. Duplicate a List Without Using Loops
## Create a list of numbers and duplicate it without using loops.
Shaxarlar = ["Toshkent", "London", "New York", "Paris", "Tokyo"]
duplicate = Shaxarlar*2
print("Duplicat qilingan royxat: ", duplicate)

## 7. Swap First and Last Elements of a List
## Given a list of numbers, swap the first and last elements.
Shaxarlar = ["Toshkent", "London", "New York", "Paris", "Tokyo"]
Shaxarlar[0], Shaxarlar[-1] = Shaxarlar[-1], Shaxarlar[0]
print("yangi royxat: ", Shaxarlar)

## 8. Slice a Tuple
## Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
Sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Slice_raqam = Sonlar[3:8]
print("Ajratilgan raqam: ", Slice_raqam)

## 9. Count Occurrences in a List
## Create a list of colors and count how many times "blue" appears in the list.
ranglar = ["oq", "sariq", "blue", "ko`k", "blue"]
takrorini_sanash = ranglar.count("blue")
print("Takrorlar soni:", takrorini_sanash,"marta")

## 10. Find the Index of an Element in a Tuple
## Given a tuple of animals, find the index of "lion".
Hayvonlar = ['sher', 'yo`lbars', 'lion', 'quyon']
hayvonlar_index = Hayvonlar.index("lion")
print(hayvonlar_index)

## 11. Merge Two Tuples
## Create two tuples of numbers and merge them into a single tuple.
tuple1 = (1, 2)
tuple2 = (3, 4)
merged_tuple = tuple1 + tuple2
print("Birlashtirilgan tuple:", merged_tuple)

## 12. Find the Length of a List and Tuple
## Given a list and a tuple, find and print their lengths.
my_list = [10, 20, 30, 40, 50]
my_tuple = (1, 2, 3, 4, 5, 6)
list_length = len(my_list)
tuple_length = len(my_tuple)
print("Ro‘yxat uzunligi:", list_length)
print("Tuple uzunligi:", tuple_length)

## 13. Convert Tuple to List
##Create a tuple of five numbers and convert it into a list.
numbers_tuple = (10, 20, 30, 40, 50)
numbers_list = list(numbers_tuple)
print("List ko‘rinishida:", numbers_list)

## 14. Find Maximum and Minimum in a Tuple
## Given a tuple of numbers, find and print the maximum and minimum values.
Sonlar = (10, 20, 5, 30, 15)
maximum = max(Sonlar)
minimum = min(Sonlar)
print("Tuple ichidagi eng katta qiymat:", maximum)
print("Tuple ichidagi eng kichik qiymat:", minimum)

## 15. Reverse a Tuple
## Create a tuple of words and print it in reverse order.
ranglar = ["oq", "sariq", "blue", "ko`k", "blue"]
teskari_tuple = ranglar[::-1]
print(teskari_tuple)
