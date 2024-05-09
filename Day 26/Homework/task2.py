"""შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვი. თქვენი დავალებაა, რომ დააბრუნოთ ლუწია თუ კენტი ის."""

def even_or_odd(num):
    if num % 2 == 1:
        return "You number is odd"
    else:
        return "You number is even"

print(even_or_odd(2))
print(even_or_odd(3))
    