"""შექმენით პროგრამა სადაც გექნებათ სახელების სია. შემდეგ მომხმარებელს შემოატანინეთ რიცხვი და სიიდან მაგ ინდექსზე მყოფი ელემენტი გამოიტანეთ."""

Enter = int(input("Enter any number from zero to six: "))

name_list = ["daviti","mamuka","elene","gia","giorgi","luka"]

if Enter == 0:
    print(name_list[0])
elif Enter == 1:
    print(name_list[1])
elif Enter == 2:
    print(name_list[2])
elif Enter == 3:
    print(name_list[3])
elif Enter == 4:
    print(name_list[4])
elif Enter == 5:
    print(name_list[5])
else:
    print("Hey I say only from zero to six!")
