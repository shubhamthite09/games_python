import random



# print("welcome to band name suggsation program")
# city_name = input("which city do you born?  ")
# pen_name = input("what is your pet name?  ")
# name = city_name + pen_name
# print(f"your bant name will be {name} like this.")
# print(f"or like this {city_name} {pen_name} .")
# for _ in range(4):
#     print("Hello world")
#
#
# New Program <-- bill spliter program  -->
# def normal(ammount, tip):
#     tip_ammount = tip/100*ammount
#     bill_after_tip = ammount + tip_ammount
#     print(f"You have to pay {bill_after_tip}$.")
#
# def split(ammount, tip, split_num):
#     tip_ammount = tip/100*ammount
#     bill_after_tip = (ammount + tip_ammount)/split_num
#     print(f"A one person share will be {bill_after_tip}$.")
# spliting = input("Do you want to split bill with other 'Yes' or 'No'  ")
# if spliting == "Yes":
#     bill = float(input("What is the bill? "))
#     tip = float(input("What persentage would you like to give? "))
#     split_input = float(input("How many of you are eaten? "))
#     split(bill,tip,split_input)
# else:
#     bill = float(input("What is the bill? "))
#     tip = float(input("What persentage would you like to give? "))
#     normal(bill,tip)
# <---length of name --->
# print(len(input("what is your name? ")))
# <--- addition of two digit number--->
# number = input("type two digit number? ")
# print(int(number[0]) + int(number[1]))

# <--- odd or even number --->
# number = int(input("enter a number that you want to check? "))
# modular = number % 2
# if modular == 0:
#     print(f"{number} is a even number.")
# else:
#     print(f"{number} is a odd number.")
# <---BMi calculator with suggection --->
# weight = float(input("what is your weight in kg "))
# hight = float(input("what is your hight in cm "))/100
# bmi = round(weight/hight ** 2)
# print(bmi)
# if bmi <= 19:
#     print("you are underweight.")
# elif bmi <= 26 and bmi > 19:
#     print("you are normalweight.")
# elif bmi <= 30 and bmi > 26:
#     print("you are overweight.")
# elif bmi <= 35 and bmi > 30:
#     print("you are obes.")
# else:
#     print("you are clinicaly obes.")
# <--- leap year --->
# year = int(input("enter year that you want to check? "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")
# else:
#     print("not leap year")
# <--- pizza bill calculator --->
# SMALL = 15
# MEDIUM = 20
# LARGE = 25
# PEPRONI_SMALL = 2
# PEPRONI_LARGE = 3
# EXTRA_CHEAS = 1
# size = input("what size pizza you want?(s,m,l) ")
# peproni = input("do you want peproni?(y,n) ")
# extra = input("do you want extra chees?(y,n) ")
# if size == "s":
#     if peproni == "y":
#        if extra == "y":
#            print(f"Your bill is {SMALL + PEPRONI_SMALL + EXTRA_CHEAS} $")
#        else:
#            print(f"Your bill is {SMALL + PEPRONI_SMALL} $")
#     else:
#         print(f"Your bill is {SMALL} $")
# elif size == "m":
#         if peproni == "y":
#             if extra == "y":
#                 print(f"Your bill is {MEDIUM + PEPRONI_LARGE + EXTRA_CHEAS} $")
#             else:
#                 print(f"Your bill is {MEDIUM + PEPRONI_LARGE} $")
#         else:
#             print(f"Your bill is {MEDIUM} $")
# else:
#         if peproni == "y":
#             if extra == "y":
#                 print(f"Your bill is {LARGE + PEPRONI_LARGE + EXTRA_CHEAS} $")
#             else:
#                 print(f"Your bill is {LARGE + PEPRONI_LARGE} $")
#         else:
#             print(f"Your bill is {LARGE} $")
# <---heads and tells ---->
# coin = random.randint(0, 1)
# if coin == 1:
#     print("It's Heads")
# else:
#     print("It's Teals")
# <---Split card bill coad --->
# bill_payers = input("input every one's name for peeking up for bill payer? ")
# .split is a inbuildfunction that split string into list
# bill_payer = bill_payers.split(", ")
# bill = len(bill_payers) - 1
# index = random.randint(0,bill)
# print(f"Today {bill_payer[index]} is going to paying bill.")
# <---list contamination--->
