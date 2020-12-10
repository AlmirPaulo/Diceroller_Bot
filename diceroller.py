from selenium.webdriver import Firefox, Chrome
import re, random


print('Welcome to the Diceroller Bot! \n If you are having problems running this bot you can find some information here:\n https://github.com/AlmirPaulo/Diceroller_Bot')
browser = input ('What is your browser? \n (1) Firefox \n (2) Chrome \n--')
if browser == '1':
    driver = Firefox()
elif browser == '2':
    driver = Chrome()

driver.get('https://web.whatsapp.com/')


trigg = input ('When you ready say "go" ')
if trigg == 'go':
    while True:
        msg = driver.find_element_by_xpath(r'/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
        roll = input ('>')
        match = re.search(r'roll.[1-9]d*', roll)
        if roll == 'help':
            print('''Hi! \n
        I am the Diceroller Bot. I am a creation of Almir Paulo. You can check his works or make contact here: \n
        https://github.com/AlmirPaulo/
        If you need help, you can read my manual here: \n 
        https://github.com/AlmirPaulo/Diceroller_Bot/blob/main/DicerollerBotManual.md\n
        Any bug founded can be reported on this issues page:\n
        https://github.com/AlmirPaulo/Diceroller_Bot/issues \n
        Have a nice game!\n''')
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
        else:
            print('Something is wrong. If you need some help, type: help')       
           
