"""დავალება: შექმენით ფუნქცია, რომელსაც გადაეცემა ორი რიცხვი: start, end. ფუნქციამ უნდა დაბეჭდოს მათ შორის არსებული რიცხვები range-ის გამოყენებით"""
def function(start,end):
    result_list = []
    for i in range(start,end):
        result_list.append(i)
    return result_list

print(function(5,14))
