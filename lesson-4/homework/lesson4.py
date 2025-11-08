### 1. Sort a Dictionary by Value
## Write a Python script to sort (ascending and descending) a dictionary by value.
my_dict = {"apple": 50, "banana": 20, "cherry": 30, "date": 40}
ascending_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Qiymatlar bo‘yicha o‘sish tartibi:", ascending_dict)
descending_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Qiymatlar bo‘yicha kamayish tartibi:", descending_dict)

### 2. Add a Key to a Dictionary
## Write a Python script to add a key to a dictionary.

## Sample Dictionary:**
sample = {0: 10, 1: 20}
sample[2]=30
print(sample)

### 3. Concatenate Multiple Dictionaries
## rite a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
merged_dict = {**dic1, **dic2, **dic3}
print("Birlashgan dic: ", merged_dict)

### 4. Generate a Dictionary with Squares
## Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form `(x, x*x)`.
n = 5
squares_dict = {x: x*x for x in range(1, n+1)}
print("Kvadratlar dictionary:", squares_dict)

### 5. Dictionary of Squares (1 to 15)
## Write a Python script to print a dictionary where the keys are numbers between 1 and 15 
## (both included) and the values are the square of the keys.
squares_dict = {x: x**2 for x in range(1, 16)}
print("1 dan 15 gacha sonlar kvadrati dictionary:", squares_dict)

### 1. Create a Set
## Write a Python program to create a set.
my_set = {1, 2, 3, 4, 5}
print("Yaratilgan set:", my_set)

### 2. Iterate Over a Set
###Write a Python program to iterate over sets.
my_set = {"apple", "banana", "cherry"}
for item in my_set:
    print(item)

### 3. Add Member(s) to a Set
### Write a Python program to add member(s) to a set.
my_set = {1, 2, 3}

# Bitta element qo‘shish
my_set.add(4)

# Bir nechta element qo‘shish
my_set.update([5, 6, 7])

# Natijani chop etish
print("Yangilangan set:", my_set)

### 4. Remove Item(s) from a Set
## Write a Python program to remove item(s) from a given set.
my_set = {1, 2, 3, 4, 5}

# Bitta elementni o‘chirish
my_set.remove(3)  # Agar element bo‘lmasa, xato beradi

# Boshqa elementni xavfsiz o‘chirish
my_set.discard(10)  # Element bo‘lmasa ham xato bermaydi

# Bir nechta elementni o‘chirish
my_set.difference_update({1, 2})

print("Yangilangan set:", my_set)

### 5. Remove an Item if Present in the Set
### Write a Python program to remove an item from a set if it is present in the set.
my_set = {1, 2, 3, 4, 5}
# O‘chiriladigan element
item_to_remove = 3
# Element mavjud bo‘lsa o‘chirish
if item_to_remove in my_set:
    my_set.remove(item_to_remove)
print("Yangilangan set:", my_set)
