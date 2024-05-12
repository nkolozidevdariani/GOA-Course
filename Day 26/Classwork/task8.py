"""დავალება8: შექმენით ფუნქცია, რომელსაც გადაეცემა სახელი. თქვენი დავალებაა, რომ ახალ სთრინგში დაამატოთ 
ლუწ ინდექსიანი ასოები სახელიდან. ეს შედეგი დააბრუნებინეთ ფუნქციას, ასევე დაბეჭდეთ ფუნქციის გარეთ"""

def even_char(name):
    new_str = ""
    for i in range(len(name)):
        if i % 2 == 0:
            new_str += name[i]
    return new_str

print(even_char("goal_oriented_academy"))