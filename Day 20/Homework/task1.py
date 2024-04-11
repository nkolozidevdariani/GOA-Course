"""1. მომხმარებელს შემოატანინეთ სიტყვა და შეამოწმეთ არის თუ არა ის პალინდრომი. პალინდრომი არის სიტყვა, 
რომელიც შებრუნებულიც ზუსტად იგივე გამოდის - radar, level, rotor. ამ დავალებისთვის გამოიყენეთ ციკლი და indexing."""


word = input("Enter any word: ")

if word == word[::-1]:
    print("Your word is palindrone")
else:
    print("Your word isn't plaidrone")