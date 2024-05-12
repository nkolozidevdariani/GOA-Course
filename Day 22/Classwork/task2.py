"""დავალება2: შექმენიტ თქვენი ხელით slicing-ის ფუნქციონალი"""

def slicing(collection,start,stop,step=1):
    if stop is None:
        stop = len(collection)
    return collection[start:stop:step]


print(slicing([2,4,7,4,1],1,3))