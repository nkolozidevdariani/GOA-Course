"""შექმენით ფუნქცია სახელად manual_max and manual_min პირველს ფუნქციასაც და მეორესაც გადაეცემა რიცხვების სია, 
პირველმა ფუნქციამ უნდა იპოვოს რიცხვების სიიდან მაქსიმუმი მნიშვნელობა და მეორემ მინიმუმი (ახსენით კომენტარებით ყველა ხაზი და შეადგინეთ ნახატი)"""

def manual_max(number_list):
    max = number_list[0]
    for num in number_list:
        if max < num:
            max = num
    return max

print(manual_max([23,25,77,76,14]))

def manual_min(number_list):
    min = number_list[0]
    for num in number_list:
        if min > num:
            min = num
    return min

print(manual_min([23,25,77,76,14]))