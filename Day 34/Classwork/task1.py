"""1) შექმენით ფუნქცია რომესლაც გადაეცემა რიცხვების სია, თვენ კი უნდა დააბრუნოთ ლუწების რაოდენობა ფუნქციიდან."""

def even_nums(number_list):
    even_list=[]
    list = []
    for num in range(len(number_list)):
        if number_list[num] % 2 == 0:
            even_list.append(number_list[num])
        else:
            list.append(number_list[num])
            return num

print(even_nums[2,3,45,5,6,6])