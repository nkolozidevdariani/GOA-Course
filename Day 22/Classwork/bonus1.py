""""დავალება: შექმენით range-ის ალგორითმი სადაც გექნებათ step -1ის ტოლი, ანუ იქნება კლებადობით."""

def range(start,stop,step=1):
    step = -step
    result_list = []
    while start != stop:
        result_list.append(start)
        start += step
    return result_list

print(range(1,25,2))
