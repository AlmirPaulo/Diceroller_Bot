from selenium.webdriver import Firefox
import re, random

driver = Firefox(executable_path = 'path/to/geckodriver')
driver.get('https://web.whatsapp.com/')

group = 'GroupName'
find_group = driver.find_elements_by_css_selector('span[title]')
for i in find_group:
    if i.text == group:
        i.click()
#A fazer: Se escrever roll... rola enviar msg com o roll.

while True:
    roll = 
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
