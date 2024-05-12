"""დავალება: შექმენით თქვენი ხელით range-ის ფუნქციონალი"""

def range(start,stop,step=1):
    result_list = []
    while start != stop:
        result_list.append(start)
        start += step
    return result_list

print(range(1,25,2))
