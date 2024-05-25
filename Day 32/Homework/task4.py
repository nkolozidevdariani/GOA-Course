"""შექმენით ფუნქცია სახელად manual_pop რომელსაც გადაეცემა სია და წასაშლელი მნიშვნელობის index, ფუნქციამ უნდაა 
დააბრუნოს ახალი სია სადაც გადმოცემულ ინდექსზე მდგომი მნიშვნელობა წაშლილი იქნება (ახსენით კომენტარები და გააკეთეთ ნახატი)"""


def manual_pop(list,index):
    rest_list = []
    for i in range(len(list)):
        if i != index:
            rest_list.append(list[i])
    return rest_list

print(manual_pop([22,33,44,55,66],2))

