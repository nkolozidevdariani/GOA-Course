"""შექმენით ფუნქცია რომელსაც გადაეცემა სია შემდგარი სტრინგებისგან, გადაუარეთ ამ სიას და შეამოწმეთ თუ მისი characterების რაოდენობა არის ლუწი, 
ჩაამატეთ ეს კონკრეტული სიის ელემენტი ახალ ცარიელ სიაში და გადააკეთეთ იგი upper ფუნქციით, 
თუ იქნება ამ სტრინგის ასოების რაოდენობა კენტი, ჩაამატეთ ეს ელემენტი ახალ სიაში რომელსაც პირველი character ექნება გადიდებული, დანარჩენი პატარა. საბოლოოდ გამოიტანეთ ეს სია.

test_case = (["goa_best" , "vano" , "nesvi" , "tskhVarAdzE"]) ---> result = ["GOA_BEST" , "VANO" , "Nesvi" , "Tskhvaradze"]"""

def function(list):
    res_list=[]
    for string in list:
        if len(string) % 2 == 0:
            res_list.append(string.upper())
        else:
            res_list.append(string.capitalize())
    return res_list

print(function(["goa_best" , "vano" , "nesvi" , "tskhVarAdzE"]))