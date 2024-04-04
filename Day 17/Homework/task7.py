"""7) შექმენით სტრინგი და for ციკლის გამოყენებით შეართეთ მხოლოდ ის სიმბოლოები რომლებიც არიან ლუწ ინდექსებზე"""

news = "georgia is in european union"
string = ""

for i in range(len(news)):
    if i % 2 == 0:
        string += news[i]
print(string)
