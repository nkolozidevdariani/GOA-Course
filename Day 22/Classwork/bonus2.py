"""დავალება2: შექმენით ალგორითმი, სადაც შეაბრუნებთ სიას slicing-ის გამოყენებით, აქაც დაგჭირდებათ უარყოფითი მნიშვნელობის სტეპი - დაწერეთ თქვენი ალგორითმი"""

def slicing(collection,start,stop,step=1):
    step = -step
    if stop is None:
        stop = len(collection)
    return collection[start:stop:step]


print(slicing([2,4,7,4,1],1,3))