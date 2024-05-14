"""შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგი, ამ სტრინგზე გამოიყენეთ find() ფუნქცია და თუ find ფუნქცია დააბრუნებს ლუწ ინდექს მაშინ ეს 
სტრინგი დააბრუნეთ დიდი ასოებით (upper) ხოლო თუ დააბრუნებს კენტ ინდექსს, მაშინ დააბრუნეთ ეს სტრინგი რომლის პირველი ასოც იქნება დიდი (capitalize)

test_case = ("vano motiashvili") ---> name.find("n") = "VANO MOTIASHVILI" // name.find("m") = Vano motiashvili."""

def even_index(string):
    res_str=""
    for char in string:
        if string.find(char) % 2 == 0:
            res_str += char.upper()
        else:
            res_str += char.capitalize()
    return res_str
            
print(even_index("vano motiashvili"))