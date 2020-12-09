from selenium.webdriver import Firefox
import re, random

driver = Firefox(executable_path = '/home/ap/code/projetos/Diceroller_Bot/geckodriver')
driver.get('https://web.whatsapp.com/')


trigg = input ('>')
if trigg == '1':
    while True:
        msg = driver.find_element_by_xpath(r'/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
        roll = input ('--')
        match = re.search(r'roll.[1-9]d*', roll)
        if match != None:
            if roll[6] != 'd':
                y = 0
                x = int(roll[5] + roll[6])
            else:
                y = 0
                x = int(roll[5])
            while y != x:
                if 'd20' in roll:
                    msg.send_keys('D20: ',str(random.randint(1,20)))
                    driver.find_element_by_class_name('_2Ujuu').click()
                elif 'd3' in roll:
                    msg.send_keys('D3: ',str(random.randint(1,3)))
                    driver.find_element_by_class_name('_2Ujuu').click()
                elif 'd4' in roll:
                    msg.send_keys('D4: ',str(random.randint(1,4)))
                    driver.find_element_by_class_name('_2Ujuu').click()
                elif 'd6' in roll:
                    msg.send_keys('D6: ',str(random.randint(1,6)))
                    driver.find_element_by_class_name('_2Ujuu').click()
                elif 'd8' in roll:
                    msg.send_keys('D8: ',str(random.randint(1,8)))
                    driver.find_element_by_class_name('_2Ujuu').click()
                elif 'd100' in roll:
                    msg.send_keys('D100: ',str(random.randint(1,100)))
                    driver.find_element_by_class_name('_2Ujuu').click()
                elif 'd12' in roll:
                    msg.send_keys('D12: ',str(random.randint(1,12)))
                    driver.find_element_by_class_name('_2Ujuu').click()
                elif 'd2' in roll:
                    msg.send_keys('D2: ',str(random.randint(1,2)))
                    driver.find_element_by_class_name('_2Ujuu').click()
                elif 'd10' in roll:
                    msg.send_keys('D10: ',str(random.randint(1,10)))
                    driver.find_element_by_class_name('_2Ujuu').click()
                y = y +1
           
