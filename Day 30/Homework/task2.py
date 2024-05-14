"""შექმენით ფუნქცია რომელსაც გადაეცემა სია შემდგარი სტრინგებისგან ---> (["vano" , "nika" , "bubazi" , "zauri"....)], დამატებით შექმენით ორი სია odd = [] და even = [], 
გადაუარეთ ორიგინალ სიას for ციკლით და გაიგეთ რომელი ელემენტი შედგება კენტი ასოებისგან და რომელი ლუწი, 
საბოლოოდ ჩაამატეთ შესაბამისი სტრინგები შესაბამის სიებში (odd / even) დიდ ასოებათ (upper) და ბოლოს დაბეჭდეთ.

test_case = (["vano" , "davit" , "zuka" , "yiyliyo"]) ---> odd = ["davit" , "yiyliyo"] / even = ["vano" , "zuka"]
 
"""

def even_odd(list):
    even=[]
    odd=[]
    for i in range(len(list)):
        if i % 2 == 1:
            even.append(list[i].upper())
        else:
            odd.append(list[i].upper())
    return [even,odd]

print(even_odd(["vano" , "davit" , "zuka" , "yiyliyo"]))