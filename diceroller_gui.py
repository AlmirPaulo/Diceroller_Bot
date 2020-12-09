import PySimpleGUI as sg
from selenium.webdriver import Firefox, Chrome
import random

#Janela 1
def step1():
    sg.theme('DarkBrown3')
    layout1 = [
            [sg.Text('Choose your browser:')],
            [sg.Radio('Firefox', 'browser', key = 'firefox'), sg.Radio('Chrome', 'browser', key = 'chrome')],
            [sg.Button('Launch')]
              ]    
    return sg.Window('Diceroller Bot', layout1, finalize = True)
#Janela 2
def step2():
    sg.theme('DarkBrown3')
    layout2 = [
        [sg.Text('''Please pay attention at the following instructions: 
        \n 1. In a few seconds your browser will launch and acess web whatsapp page. Just wait. 
        \n 2. Login with the QR Code 
        \n 3. Go to the group you going to play your RPG session.
        \n 4. Make sure the page is fully loaded.
        \n 5. Now press the button bellow.
        ''')],
        [sg.Button('Start')]
    ]

    return sg.Window('Diceroller Bot', layout2, finalize = True)

#Janela 3
def step3():
    sg.theme('DarkBrown3')
    layout3 = [
        [sg.Text('Choose the dice: '), sg.Combo(['d2', 'd3', 'd4',
                                                  'd6','d8', 'd10',
                                                  'd12', 'd20','d100'], key = 'dices')],
        [sg.Text('How many dices? '), sg.Spin([i for i in range(1,31)], initial_value = 1, key = 'roll')],
        [sg.Button('Roll!'), sg.Button('Help?')]
    ]
    return sg.Window('Diceroller Bot',layout3, finalize = True)
#Loop
launch, trigg, rolls = step1(), None, None
while True:
    win, ev, val = sg.read_all_windows()
    if ev == sg.WINDOW_CLOSED:
        break
    if win == launch and ev == 'Launch':
        if val['firefox'] == True:
            trigg = step2()
            launch.hide()
            driver = Firefox()
            driver.get('https://web.whatsapp.com/')
        elif val['chrome'] == True:
            trigg = step2()
            launch.hide()
            driver = Chrome()
            driver.get('https://web.whatsapp.com/')
    if win == trigg and ev == 'Start':
        trigg.hide()
        rolls = step3()
    if win == rolls and ev == 'Help?':
        msg = driver.find_element_by_xpath(r'/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
        msg.send_keys('''Hi! \n
        I am the Diceroller Bot. I am a creation of Almir Paulo. You can check his works or make contact here: \n
        https://github.com/AlmirPaulo/
        If you need help, you can read my manual here: \n 
        https://github.com/AlmirPaulo/Diceroller_Bot/blob/main/DicerollerBotManual.md\n
        Any bug founded can be reported on this issues page:\n
        https://github.com/AlmirPaulo/Diceroller_Bot/issues \n
        Have a nice game!\n''')
    elif win == rolls and ev == 'Roll!':
        msg = driver.find_element_by_xpath(r'/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
        dice = val['dices']
        y = 0
        x = int(val['roll'])
        while y != x:
            if dice == 'd20':
                msg.send_keys('D20: ',str(random.randint(1,20)))
                driver.find_element_by_class_name('_2Ujuu').click()
            elif dice == 'd3':
                msg.send_keys('D3: ',str(random.randint(1,3)))
                driver.find_element_by_class_name('_2Ujuu').click()
            elif dice == 'd4':
                msg.send_keys('D4: ',str(random.randint(1,4)))
                driver.find_element_by_class_name('_2Ujuu').click()
            elif dice == 'd6':
                msg.send_keys('D6: ',str(random.randint(1,6)))
                driver.find_element_by_class_name('_2Ujuu').click()
            elif dice == 'd8':
                msg.send_keys('D8: ',str(random.randint(1,8)))
                driver.find_element_by_class_name('_2Ujuu').click()
            elif dice == 'd100':
                msg.send_keys('D100: ',str(random.randint(1,100)))
                driver.find_element_by_class_name('_2Ujuu').click()
            elif dice == 'd12':
                msg.send_keys('D12: ',str(random.randint(1,12)))
                driver.find_element_by_class_name('_2Ujuu').click()
            elif dice == 'd2':
                msg.send_keys('D2: ',str(random.randint(1,2)))
                driver.find_element_by_class_name('_2Ujuu').click()
            elif dice == 'd10':
                msg.send_keys('D10: ',str(random.randint(1,10)))
                driver.find_element_by_class_name('_2Ujuu').click()
            y = y +1


