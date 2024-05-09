"""შექმენით ფუნქცია, რომელიც დააბრუნებს მარტივია თუ არა რიცხვი (მარტივია რიცხვი, თუ მას მარტო ორი გამყოფი აქვს)."""

def is_prime(num):
    if num <= 1:
        return "Not Prime"
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return "Not Prime"
        

    return "Prime"

print(is_prime(7))
print(is_prime(4))
print(is_prime(16))