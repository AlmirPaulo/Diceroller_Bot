import re, random

while True:
    roll = input('')
    match = re.search(r'roll.[1-9]d*', roll)
    if match != None:
        x = int(roll[5])
        y = 0
        while y != x:
            if 'd20'in roll:
                print(random.randint(1,20))
            elif 'd3' in roll:
                print(random.randint(1,3))
            elif 'd4' in roll:
                print(random.randint(1,4)) 
            elif 'd6' in roll:
                print(random.randint(1,6))
            elif 'd8' in roll:
                print(random.randint(1,8))
            elif 'd100' in roll:
                print(random.randint(1,100))
            elif 'd12' in roll:
                print(random.randint(1,12))
            elif 'd2' in roll:
                print(random.randint(1,2))
            elif 'd10' in roll:
                print(random.randint(1,10))
            y = y +1
