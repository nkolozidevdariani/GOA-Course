"""დავალება3: შექმენით ფუნქცია, რომელსაც გადაეცემა start, end. ამ ორ რიცხვს შორის არსებული, ყველა დაამატეთ ახალ სიაში. საბოლოოდ დაბეჭდეთ სიის საშუალო არითმეტიკული"""
def calculate_arithmetic(start, end):
    numbers = []

    for i in range(start, end):
        numbers.append(i)
    
    result = sum(numbers) / len(numbers)

    print(result)

calculate_arithmetic(5, 11)

