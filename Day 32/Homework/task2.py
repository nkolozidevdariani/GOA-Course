"""შექმენით ფუნქცია სახელად manual_index, რომელსაც გადაეცემა 2 მნიშვნელობა, პარამეტრებად სახელები დაარქვიათ numbers_list 
and search_value, ფუნქციამ უნდა დააბრუნოს საძიებელი მნიშვნელობის ინდექსი სიიდან (ყველა ხაზი ახსენით კომენტარებით და შექმენით ნახატი)"""

def manul_index(numbers_list, search_value):
    for i in range(len(numbers_list)):
        if numbers_list[i] == search_value:
            return i
    return None

print(manul_index([145,238,991,832],991))