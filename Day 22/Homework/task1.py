"""1. მომხმარებელს შემოატანინეთ ნებისმიერი სიტყვა. თუ მისი სიგრძე აღემატება სამს, დაბეჭდეთ 
მისი პირველი სამი ასო. ხოლო თუ ნაკლებია ან ტოლი სამის, დაბეჭდეთ სიტყვის პირველი ასო."""


user_word = input("Please enter a any world: ")

if len(user_word) > 3:
    print(user_word[0] + user_word[1] + user_word[2])
else:
    print(user_word[0])