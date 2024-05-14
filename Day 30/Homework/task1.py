"""შექმენით ფუნქცია, რომელსაც გადაეცემა სტრინგი და დააბრუნეთ ეს სტრინგდი შებრუნებულ + დიდი ასოებით (reversed / upper).

test_case = ("VaNo MoTiashvili") ---> "ILIVHSAITOM ONAV"""

def capitalaize_backwards(string):
    return string[::-1].upper()
    
    
print(capitalaize_backwards("VaNo MoTiashvili"))