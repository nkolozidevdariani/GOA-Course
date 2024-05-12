"""დავალება2: შექმენით ფუნქცია, რომელსაც გადაეცემა start, end. ამ შემთხვევაში გამოთვალეთ მათ შორის არსებული რიცხვების ჯამი"""
def sum_range(start, end):
    sum = 0

    for i in range(start, end):
        sum += i
    return sum

print(sum_range(5, 11))