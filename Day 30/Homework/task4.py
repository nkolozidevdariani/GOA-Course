"""შექმენით ფუნქცია რომელსაც გადაეცემა სია შემდგარი ყველანაირი სტრინგისგან (დიდი ასოებით / პატარა ასოებით : "vano" , "LUKA") , 
გადაურეთ ამ სიას და თუ ეს კონკრეტული ელემენტი არის შემდგარი დიდი ასოებისგან, 
დაამატეთ სიაში ისე როგორც lower, ხოლო თუ შედგება პატარა ასოებისგან დაამატეთ სიაში ისე როგორც upper / !HINT : გადახედეთ ფუნქციებს, isupper() და islower()!

test_case = (["vano" , "DAVIT" , "LUKA" , "nika"]) ---> result_list = ["VANO" , "davit" , "luka" , "NIKA"]"""

def lower_or_upper(list):
    res_list=[]
    for string in list:
        if string.isupper():
            res_list.append(string.lower())
        else:
            res_list.append(string.upper())
    return res_list

print(lower_or_upper(["vano" , "DAVIT" , "LUKA" , "nika"]))