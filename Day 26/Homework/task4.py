"""შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. თქვენი დავალებაა,
რომ დააბრუნოთ ამ სიის განახლებული ვერსია, სადაც ყველა სახელი დიდი ასოთი დაიწყება."""

def name_capitalize(name_list):
    result_list=[]
    for name in name_list:
        result_list.append(name.capitalize())
    return result_list

print(name_capitalize(["saba", "luka", "NiKa", "DEMETRE"]))
print(name_capitalize(["nika", "chad", "gigachad"]))