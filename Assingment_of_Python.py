# 1) What are the types of Applications?

# ANS : Applications can be classified as:
# * Desktop Applications – Run on computers (MS Word, VLC)
# * Web Applications – Run in browsers (Gmail, Facebook)
# * Mobile Applications – Run on smartphones (WhatsApp)
# * Enterprise Applications – Used in organizations (ERP, CRM)
# * Embedded Applications – Used in machines/devices (Washing machines)

# 2) What is programming?
# ANS : Programming is the process of writing instructions (code) that a computer follows to perform a task or solve a problem.

# 3) What is Python?

# ANS : Python is a high-level, interpreted, and easy-to-learn programming language used for:
# * Web development
# * Data science
# * AI & ML
# * Automation
# * Software development

# 4) Write a Python program to check if a number is positive, negative or zero.

# Number = int(input("Enter Number Here: "))
# if Number == 0:
#     print("The number is Zero: ",Number)
# elif Number > 0:
#     print("The number is Positive: ",Number)
# else :
#     print("The number is Negative: ",Number)

# 5) Write a Python program to get the Factorial number of given numbers.

# Number = int(input("Enter Number Here: "))
# import math
# if num == 0 | num < 0:
#    print(f"This {num} is not Suitable For Factorial.")
# else: 
#    print("Factorial is:", math.factorial(num))

# AND #

# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1,num + 1):
#     if num == 0 | num < 0:
#         print(f"This {num} is not Suitable For Factorial.")
#     else:
#         factorial *= i
# print("Factorial of", num, "is", factorial)

# 6) Write a Python program to get the Fibonacci series of given range.
# n = int(input("Enter the number of terms: "))
# a, b = 0, 1
# print("Fibonacci series:")
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# 7) How memory is managed in Python?

# ANS : Python manages memory automatically using:
# * Heap memory
# * Garbage Collection
# * Reference Counting
# Programmers don’t need to allocate or free memory manually.

# 8) What is the purpose of continue statement in Python?

# ANS : continue skips the current iteration and moves to the next loop iteration.
# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

# 9) Write python program that swap two number with temp variable and without temp variable.
# temp = 0
# a = 5
# b = 10
# with temp variable
# temp = a
# a = b
# b = temp
# print("a = ",a)
# print("b = ",b)
# without temp variable
# a, b = b, a
# print("a =", a)
# print("b =", b)

# 10) Write a Python program to find whether a given number is even or odd, print out an appropriate message 
#     to the user.

# Number = int(input("Enter Number Here: "))
# if Number % 2 == 0:
#     print(f"The Number {Number} Is Even.")
# else:
#     print(f"The Number {Number} Is Odd.")

# 11) Write a Python program to test whether a passed letter is a vowel or not.

# Letter = input("Enter Letter Here: ")
# Vowels = ["a","A","e","E","i","I","o","O","u","U"]
# if Letter in Vowels:
#     print(f"The Passed Letter '{Letter}' Is Vowel.")
# else:
#     print(f"The Passed Letter '{Letter}' is Not Vowel.")

# 12) Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
# Number_1 = int(input("Enter Number 1: "))
# Number_2 = int(input("Enter Number 2: "))
# Number_3 = int(input("Enter Number 3: "))
# Sum = Number_1 + Number_2 + Number_3
# if Number_1 == Number_2 or Number_2 == Number_3 or Number_3 == Number_1:
#     print("The Two Value Are Equal so Sum: ",0)
# else:
#     print(Sum)

# 13) Write a Python program that will return true if the two given integer values are equal or their 
#     sum or difference is 5.

# Number1 = int(input("Enter Number1 Here: "))
# Number2 = int(input("Enter Number2 Here: "))
# if Number1 == Number2 or Number1 + Number2 == 5 or Number1 - Number2 == 5:
#     print("The Integer Value Is True.")
# else:
#     print("The Integer Value Is False.")

# 14) Write a python program to sum of the first n positive integers.

# Num = int(input("Enter n Here: "))
# Sum = 0
# for n in range(1,Num + 1):
#     Sum += n
# print(f"sum of first {n} positive integers are {Sum}.")

# 15) Write a Python program to calculate the length of a string.

# Text = input("Enter Text Here: ")
# Length = len(Text)
# print("The Length Of This Text Is: ",Length)

# 16) Write a Python program to count the number of characters (character frequency) in a string.

# text = input("Enter Any Text Here: ")
# freq = {}
# for char in text:
#     freq[char] = freq.get(char, 0) + 1
# for char, count in freq.items():
#     print(f"'{char}': {count}")

# AND #

# from collections import Counter
# String = input("Enter Any Text Here: ")
# print(Counter(String))

# 17) What are negative indexes and why are they used?

# ANS : Negative indexing starts from the end of a sequence.
# list = [10, 20, 30]
# print(list[-1])
# Used to access elements from the end easily.

# 18) Write a Python program to count occurrences of a substring in a string.

# String = input("Enter string: ")
# Sub_String = input("Enter substring: ")

# print(String.count(Sub_String))

# 19) Write a Python program to count the occurrences of each word in a given sentence.

# sentence = input("Enter Any Text Which Has Same No. Of Words More Than 1: ")
# words = sentence.split()
# word_count = {}
# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1
# for word, count in word_count.items():
#     print(f"{word}: {count}")

# AND #

# sentence = input("Enter a sentence: ")
# word_count = Counter(sentence.split())
# print(word_count)

# 20) Write a Python program to get a single string from two given strings,separated by a space and swap 
#     the first two characters of each string.

# str1 = input("Enter the first string: ")
# str2 = input("Enter the second string: ")
# new1 = str1[:2] + str2[2:]
# new2 = str2[:2] + str1[2:]
# result = new1 + "  " + new2
# print("Result: ",result)

# 21) Write a Python program to add 'in' at the end of a given string (length should be at least 3). 
#     If the given string already ends with 'ing' then add 'ly' instead
#     if the string length of the given string is less than 3, leave it unchanged.

# string = input("Enter any string here: ")
# if len(string) < 3:
#     print(f'String {string} Has Length Less Than 3.')
# elif string.endswith("ing"):
#     print(string + "ly")
# else:
#     print(string + "ing")

# 22) Write a Python function to reverses a string if its length is a multiple of 4.

# String = input("Enter String Here: ")
# def reverse_if_multiple_of_4(String):
#     if len(String) % 4 == 0:
#         return String[::-1]
#     else:
#         String
# Ans = reverse_if_multiple_of_4(String)
# print("Ans: ",Ans)

# 23) Write a Python program to get a string made of the first 2 and last 2 chars from a given string.
#     If the string length is less than 2,return instead of the empty string.

# Message = input("Enter Any Sting Word Here: ")
# new_s = "  "
# if len(Message) < 2:
#     print("This Contains Less Than 2 Words.")
# elif len(Message) > 2:
#     new_s.append(Message[:2] and Message[-2:])
# print(new_s)

# 24) Write a Python function to insert a string in the middle of a string.

# String = input("Enter Any Sentence Here: ")
# Middle = input("Enter A word Which You Have To Put In Middle: ")
# def Insert_in_middle(String,Middle):
#     mid_index = len(String) // 2
#     return String[:mid_index] + Middle + String[mid_index:]
# print("Result:",Insert_in_middle(String,Middle))

# 25) What is List? How will you reverse a list?

# ANS : A list is an ordered, mutable collection. Ways to reverse:
# * list.reverse()
#        or
# * list[::-1]

# 26) How will you remove last object from a list?

# ANS : Using pop():
# * list.pop()

# 27) list1 = [2, 33, 222, 14, 25], what is list1[-1]?

# ANS :  25

# 28) Difference between append() and extend()

#       append()	              extend()
# * Adds one element	 Adds multiple elements
# * list.append(5)	 list.extend([5,6])

# 29) Write a Python function to get the largest & smallest number and sum of all from a list.

# list1 = [16,14,15,18,17,19]
# Largest = max(list1)
# Smallest = min(list1)
# Total = sum(list1)
# print("Largest: ",Largest)
# print("Smallest: ",Smallest)
# print("Total: ",Total)

# 30) How will you compare two lists?

# ANS : list1 == list2

# 31) Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same 
#     from a given list of strings. 

# string_list = ["abc", "xyz", "aba", "1221", "aa", "b", "cac"]
# count = 0
# for s in string_list:
#     if len(s) >= 2 and s[0] == s[-1]:
#         count += 1
# print("Number of strings meeting the criteria are:", count)

# 32) Write a Python program to remove duplicates from a list. 

# LIST2 = ["Kirtan","Krishna","Monil","Kirtan","David","Krishna","Smeet","Neel","David"]
# New_List2 = []
# for char in LIST2:
#     if char not in New_List2:
#         New_List2.append(char)
# print(New_List2)

# 33) Write a Python program to check a list is empty or not. 

# list1 = []
# if not list1:
#     print("Yes, This List Is Empty.")
# else:
#     print("No,This List is List Is Not Empty.")

# 34) Write a Python function that takes two lists and returns true if they have at least one common member.

# def common_numbers(list1,list2):
#     for item in list1:
#         if item in list2:
#             return True
#     return False
# list1 = input("Enter the elements of the first list, separated by spaces: ").split()
# list2 = input("Enter the elements of the second list, separated by spaces: ").split()
# if common_numbers(list1, list2):
#     print("The lists contains one common element.")
# else:
#     print("The lists do Not Contains any common elements.")

# 35) Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.

# Numbers = range(1,31,1)
# Squared = []
# for i in Numbers:
#     i **= 2
#     Squared.append(i)
# Filtered_List = Squared[:5] + Squared[-5:]
# print(Filtered_List)

# 36)  Write a Python function that takes a list and returns a new list with unique elements of the first list.

# List1 = input("Enter Some Elements Here: ").split()
# def Unique_List(List1):
#     return list(set(List1))
# New_List = Unique_List(List1)
# print(New_List)

# 37) Write a Python program to convert a list of characters into a string.

# List1 = ['#','D','A','H','I','_','P','A','N','N','E','R','_','@','6','4','8']
# String1 = ''.join(List1)
# print("This Is A List String: ",String1)

# 38) Write a Python program to select an item randomly from a list.

# import random as rn
# Items = ["USA","MORROCO","SPAIN","RUSSIA","THAILAND","AUSTRAILA","CHINA"]
# Select_Item = rn.choice(Items)
# print("The Random Item Selected From The Items List Is: ",Select_Item)

# 39) Write a Python program to find the second smallest number in a list.

# Numbers = list(map(int,input("Enter Numbers Here Using Space:  ").split()))
# Ascending = sorted(set(Numbers))
# if len(Numbers) < 2:
#     print("There is no second smallest number.")
# else:
#     Smallest_2nd = Ascending[1]
#     print(Smallest_2nd,"Is the 2nd smallest number in the list")

# 40) Write a Python program to get unique values from a list.

# Values = [51,54,62,67,38,49,62,54,38,57]
# Unique_Values = []
# for v in Values:
#     if v not in Unique_Values:
#         Unique_Values.append(v)
# print("Here Are All Unique Values: ",Unique_Values)

# 41) Write a Python program to check whether a list contains a sub list.

# Two_Lists = [[67,74,86],[97,94,89],[34,45,47],[84,82,79]]
# Sub_Lists = [34,45,47]
# if Sub_Lists in Two_Lists:
#     print("This List Contains Sub-List.")
# else:
#     print("This List Does'nt Contains Sub-List.")

# 42) Write a Python program to split a list into different variables.

# List1 = ["Darshil","David","Denish","Darshan","Daku","Divy"]
# Split = len(List1) // 2
# D = List1[:Split]
# K = List1[Split:]
# print("D= ",D)
# print("K= ",K)

# 43) What is tuple? Difference between list and tuple?

# ANS : A tuple is an ordered, immutable collection.
#     List	          Tuple
#   Mutable	        Immutable
#   Uses []	        Uses ()
#   Slower	        Faster

# 44) Write a Python program to create a tuple with different data types.

# Tuple1 = ("Aditya",34,6.1,"Male",True,"82W")
# print(Tuple1)

# 45) Write a Python program to unzip a list of tuples into individual lists.

# data = [(1, 'a', True), (2, 'b', False), (3, 'c', True)]
# list1, list2, list3 = zip(*data)
# list1 = list(list1)
# list2 = list(list2)
# list3 = list(list3)
# print("List 1:", list1)
# print("List 2:", list2)
# print("List 3:", list3)

# 46) Write a Python program to convert a list of tuples into a dictionary. 

# List_of_Tuples = [("Swayam",17,"E-Commerce","Stage1"),("Mangesh",19,"Milkman","Stage3"),("Bharat",18,"Diamond","Stage2")]
# Dictionary_of_Tuples = dict()
# for Name,Age,Work,Stage in List_of_Tuples:
#     Dictionary_of_Tuples[Name] = {"Age":Age,"Work":Work,"Stage":Stage}
# print(Dictionary_of_Tuples)

# 47) How will you create a dictionary using tuples?

# ANS : tuples = (('a',1), ('b',2))
# dict1 = dict(tuples)

# 48) Write a Python script to sort (ascending and descending) a dictionary by value.

# Dictionary = {"Hema":78,"Sonal":73,"Aarti":91,"Palak":89}
# Dictionary_Ascending = dict(sorted(Dictionary.items(),key=lambda item: item[1]))
# Dictionary_Descending = dict(sorted(Dictionary.items(),key=lambda item: item[1],reverse=True))
# print("Dictionary In Ascending Order: ",Dictionary_Ascending)
# print("Dictionary In Descending Order: ",Dictionary_Descending)

# 49) Write a Python script to concatenate following dictionaries to create a new one.

# Dict1 = {"Smeet":2323,"Kirtan":7767,"Darshil":648,"Dhanik":2308}
# Dict2 = {"Neel":9988,"Krishna":1122,"Monil":4524}
# Dict3 = {"Divy":1909,"Rudresh":1006,"Sahil":1488}
# New_Dict = Dict1 | Dict2 | Dict3
# print("New Dictionary After Concatenation: ",New_Dict)

# 50) Write a Python script to check if a given key already exists in a dictionary.  

# Dictionary = {"Harrier":14,"Victoris":32,"Creta":19,"Virtus":27,"Slavia":7}
# Keys = input("Enter Key Here o Check In Dictionary: ")
# if Keys in Dictionary:
#     print("Yes, Key",Keys,"Exists In Dictionary With Value:",Dictionary[Keys])
# else:
#     print("No, Key",Keys,"Does Not Exists In Dictionary.")

# 51) Traverse through dictionary.

# ANS : for key, value in d.items():
#         print(key, value)

# 52) Check presence of a key.

# ANS : 'a' in d

# 53) Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

# Dict = {}
# for i in range(1, 16):
#     Dict[i] = i+0
# print(Dict)

# 54) Write a Python program to check multiple keys exists in a dictionary.

# Dictionary = {"Harrier":14,"Victoris":32,"Creta":19,"Virtus":27,"Slavia":7,"Thar":6,"Nexon":45,"Elevate":11,"Fortuner":17,"Hector":19}
# Keys = input("Enter Multiple Keys Here Separated By Comma To Check In Dictionary: ").split(",")
# for key in Keys:
#     if key in Dictionary:
#         print("Yes, Key",key,"Exists In Dictionary With Value:",Dictionary[key])
#     else:
#         print("No, Key",key,"Does Not Exists In Dictionary.")

# 55) Write a Python script to merge two Python dictionaries.

# Dict1 = {"Harrier":14,"Victoris":32,"Creta":19}
# Dict2 = {"Virtus":27,"Slavia":7,"Thar":6}
# Merged_Dict = Dict1 | Dict2
# print("Merged Dictionary: ",Merged_Dict)

# 56) Write a Python program to map two lists into a dictionary.

# List1 = ["Smeet","Kirtan","Monil","Dhanik"]
# List2 = ["Jariwala","Shah","Patel","Verma"]
# List3 = [69,74,71,79]
# Map_Dict = zip(List1,List2,List3)
# Result_Dict = {k:{"Surname":v,"Marks":m} for k,v,m in Map_Dict}
# print("Mapped Dictionary: ",Result_Dict)

# 57) Write a Python program to find the highest 3 values in a dictionary.

# Dict1 = {'John': 42, 'David': 35, 'Bravo': 48, 'Nicolas': 29, 'Peter': 36, 'Marshall':45}
# High_3 = dict(sorted(Dict1.items(),key=lambda item:item[1],reverse=True)[:3])
# print("Here Are The Highest Three Value Of Dictionary: ",High_3)

# 58) Write a Python program to combine values in python list of dictionaries. 
#     Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, o {'item': 'item1', 'amount': 750}] 
#     Expected Output: 
#     Counter ({'item1': 1150, 'item2': 300})

# Data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Result = {}
# for d in Data:
#     item = d['item']
#     amount = d['amount']
#     if item in Result:
#         Result[item] += amount
#     else:
#         Result[item] = amount
# print(Result)

# 59) Write a Python program to create a dictionary from a string.
#     Note: Track the count of the letters from the string.

# Text = input("Enter Any Text Here By Seperating Space: ")
# Dict_of_Text = {}
# for word in Text:
#     if word in Dict_of_Text:
#         Dict_of_Text[word] += 1
#     else:
#         Dict_of_Text[word] = 1
# print(Dict_of_Text)

# 60) Sample string:'w3resource'.
#     Expected output:
#     {'3': 1,'s': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

# text = 'w3resource'
# letter_count = {}
# for char in text:
#     if char in letter_count:
#         letter_count[char] += 1
#     else:
#         letter_count[char] = 1
# print(letter_count)

# 61) Write a Python function to calculate the factorial of a number (a non-negative integer).

# Number = int(input("Enter Any Number Here: "))
# Factorial = 1
# if Number <= 0:
#     print("The Number Should Be Greater Than 1")
# else:
#     for i in range(1,Number + 1):
#         Factorial *= i
# print("The Factorial Of Number",Number,"Is",Factorial)

# 62) Write a Python function to check whether a number is in a given range.

# def check_range(num, low, high):
#     if num >= low and num <= high:
#         print("Okay, The Number is in the range")
#     else:
#         print("Sorry, The Number is not in the range")
# Number = input("Enter num, low, high (comma separated): ").split(",")
# num = int(Number[0])
# low = int(Number[1])
# high = int(Number[2])
# check_range(num, low, high)

# 63) Write a Python function to check whether a number is perfect or not.

# def check_perfect(num):
#     sum = 0
#     for i in range(1, num):
#         if num % i == 0:
#             sum = sum + i
#     if sum == num:
#         print("Perfect Number")
#     else:
#         print("Not a Perfect Number")
# Number = input("Enter Number Here: ")
# num = int(Number)
# check_perfect(num)

# 64) Write a Python function that checks whether a passed string is palindrome or not.

# def check_palindrome(s):
#     if s == s[::-1]:
#         print("This String Is Palindrome")
#     else:
#         print("This String Is Not Palindrome")
# s = input("Enter Any String Here: ")
# check_palindrome(s)

# 65) How many basic types of functions in Python?

# ANS :
# * Built-in functions
# * User-defined functions
# * Anonymous (Lambda) functions

# 66) Pick random item from list/tuple.

# ANS : import random
#       random.choice(list)

# 67) Pick random item from a range.

# ANS : random.choice(range(1,10))

# 68) Get a random number.

# ANS : random.randint(1,100)

# 69) Set starting value for random numbers.

# ANS : random.seed(10)

# 70) Randomize list items in place.

# ANS : random.shuffle(list)

# 71) File function & keywords.

# ANS : File function: open()
# Modes:
# * r – read
# * w – write
# * a – append
# * x – create

# 72) Write a Python program to read an entire text file.

# file = open("data.txt", "r")
# content = file.read()
# print(content)
# file.close()

# 73) Write a Python program to append text to a file and display the text.

# file = open("data.txt", "a")
# file.write("\nThis text is appended to the file.")
# file.close()
# file = open("data.txt", "r")
# content = file.read()
# print(content)
# file.close()

# 74) Write a Python program to read first n lines of a file.

# n = int(input("Enter number of lines to read: "))
# file = open("data.txt", "r")
# for i in range(n):
#     line = file.readline()
#     print(line, end="")
# file.close()

# 75) Write a Python program to read last n lines of a file.

# n = int(input("Enter number of last lines to read: "))
# file = open("data.txt", "r")
# lines = file.readlines()
# last_lines = lines[-n:]
# for line in last_lines:
#     print(line, end="")
# file.close()

# 76) Write a Python program to read a file line by line and store it into a list.

# file = open("data.txt", "r")
# lines_list = []
# for line in file:
#     lines_list.append(line.strip())
# file.close()
# print(lines_list)

# 77) Write a Python program to read a file line by line store it into a variable.

# file = open("data.txt", "r")
# data = ""
# for line in file:
#     data = data + line
# file.close()
# print(data)

# 78) Write a python program to find the longest words.

# with open("data.txt", "r") as f:
#     words = f.read().split()
# longest = max(words, key=len)
# print("Longest word:", longest)

# AND #

# text = input("Enter a sentence: ")
# words = text.split()
# longest_word = max(words, key=len)
# print("Longest word is:", longest_word)

# 79) Write a Python program to count the number of lines in a text file.

# file = open("data.txt", "r")
# lines = file.readlines()
# print("Number of lines:", len(lines))
# file.close()

# 80) Write a Python program to count the frequency of words in a file.

# file = open("data.txt", "r")
# text = file.read()
# file.close()
# words = text.split()
# freq = {}
# for word in words:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1
# print(freq)

# 81) Write a Python program to write a list to a file.

# my_list = ["Python", "Java", "C++", "HTML"]
# file = open("data.txt", "w")
# for item in my_list:
#     file.write(item + "\n")
# file.close()

# 82) Write a Python program to copy the contents of a file to another file.

# file1 = open("source.txt", "r")
# content = file1.read()
# file1.close()
# file2 = open("copy.txt", "w")
# file2.write(content)
# file2.close()
# print("File copied successfully!")

# 83) Exception handling & Error.

# ANS : Error: Problem that stops execution
# Exception handling: Managing errors using try-except

# 84) How many except blocks?

# ANS : Multiple except blocks allowed.
# Built-in exceptions:
# * ValueError
# * TypeError
# * ZeroDivisionError
# * IndexError

# 85) When else executes?

# ANS : When no exception occurs.

# 86) Can one except handle multiple exceptions?

# ANS : Yes
# except (ValueError, TypeError):

# 87) When is finally executed?

# ANS : Always, whether exception occurs or not.

# 88) What happens when "1" == 1?

# ANS : False (string ≠ integer)

# 89) How Do You Handle Exceptions with Try/Except/Finally in Python? Explain with coding snippets. 

# Exception handling in Python is done using try, except, and finally blocks. 
# The try block contains risky code, except handles errors, and finally executes cleanup code whether an exception occurs or not.

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     result = a / b
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Please enter valid numbers")
# finally:
#     print("Program Ended")

# 90) Write a python program that user to enter only odd numbers, else will raise an exception.

# try:
#     num = int(input("Enter an odd number: "))
#     if num % 2 == 0:
#         raise ValueError("Even number entered! Only odd numbers are allowed.")
#     print("You entered a valid odd number:", num)
# except ValueError as e:
#     print("Error:", e)