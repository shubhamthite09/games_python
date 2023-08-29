print("welcome to tip calculoter ")
bill_ammount = int(input("what is bill ammount? "))
tip_ammount = int(input("how many percentage of tip you want to give 5 10 or 15? "))
spilt = int(input("how many people are you at dinning? "))
tip = bill_ammount * tip_ammount /100
final_ammount = bill_ammount + tip
shere = round(final_ammount/spilt,2)
print(f"one person shere will be: {shere}")