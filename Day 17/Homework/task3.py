"""3)შექმენით სია სადაც გექნებათ 1-10 ჩათვლი რიცხვები, for ციკლის გამოყენებით დაბეჭდეთ ამ რიცხვების ჯამი ცალკე და ნამრავლი ცალკე"""

number_list = [1,2,3,4,5,6,7,8,9,10]

sum = 0
product = 1
for i in number_list:
    sum = sum + i
    product = product * i
print(sum)
print(product)