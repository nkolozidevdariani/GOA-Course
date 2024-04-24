"""2. for ციკლით შექმენით 10-იდან 20-ის ჩათვლით არსებული მთელი 
რიცხვების სია. შემდეგ გამოიყენეთ slicing, სადაც სტეპი იქნება 2-ის ტოლი."""

numbers_list = []
for num in range(10,20+1):
    numbers_list.append(num)



print(numbers_list[0::2])