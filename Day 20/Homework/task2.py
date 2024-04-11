"""მომხმარებელს შემოატანინეთ ხუთი რიცხვი და შეიტანეთ ისინი სიაში. შემდეგ თქვენ უნდა იმუშაოთ ამ სიაზე: 
თუ რომელიმე ელემენტი სიაში ორჯერ მეორდება, დაამატეთ ის ახალ სიაში. საბოლოოდ გექნებათ ორი ვარიანტი: ცარიელი ახალი სია / 
ახალი სია სადაც იქნება მინიმუმ ერთი ელემენტი. თუ სია ცარიელი იქნება, დაბეჭდეთ რომ სია ცარიელია. სხვა შემთხვევაში დაბეჭდეთ ახალი სია.
test case: [1, 1, 2, 2, 3] -> [1, 2]
test case: [1, 2, 3, 4, 5] -> "List is empty"""

number_list = []
new_list = []
for i in range(5):
    num =int(input("Enter a number: "))
    number_list.append(num)
for num in number_list:
    if num in new_list:
        pass
    else:
        new_list.append(num)

if len(new_list) == 0:
    print("Your list is empty")
else:
    print(new_list)