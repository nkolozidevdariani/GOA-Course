"""შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვების სია. შემდეგ გამოიყენეთ ციკლი, რათა განიხილოთ
ამ სიის ყველა რიცხვი - თუ რიცხვი ლუწია, ახალ სიაში დაამატეთ მისი განაყოფი ორზე,
ხოლო თუ კენტია, მაშინ რიცხვის ნამრავლი ორზე. საბოლოოდ დააბრუნეთ განახლებული სია"""

def func(num_list):
    new_list=[]
    for num in num_list:
        if num % 2 == 0:
            new_list.append(num/2)
        else:
            new_list.append(num*2)
    return new_list

print(func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(func([11,12,13,14,15,16,17,18,19,20]))