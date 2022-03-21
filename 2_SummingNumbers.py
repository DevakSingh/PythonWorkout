def mysum(*numbers):
    total = 0
    for number in numbers: 
        total = number + total 
    print(total)
    return

mysum(10, 20, 30, 5)