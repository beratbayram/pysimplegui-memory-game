import PySimpleGUI as gui
from random import randint
import threading as th
from time import sleep

def getDifficulty():
    layout = [
        [gui.Text("Speed:")],
        [gui.Radio("Easy","DiffRadio"),gui.Radio("Medium","DiffRadio",default=True),gui.Radio("Hard","DiffRadio"),gui.Radio("Extreme","DiffRadio")],
        [gui.Text("Initial Size:")],
        [gui.Slider(range=(1,100),default_value=5,orientation='h',size=(50,10))],
        [gui.OK()]
    ]

    window = gui.Window("Difficulty", layout, keep_on_top=True, font=(None, 15))
    event , values = window.read()
    window.close()

    if values[0]: return (2.00, values[4])
    if values[1]: return (1.00, values[4])
    if values[2]: return (0.50, values[4])
    if values[3]: return (0.25, values[4])

def showNumber():
    global pos, nums, window
    window[pos]('')
    pos = 'box'+ randNum()
    newNumber = randDigit()
    nums.append(newNumber)
    window[pos](newNumber)

def showTime(window,sec,limit):
    
    if limit == 0:
        return
    
    showNumber()
    window.finalize()
    sleep(sec)
    showTime(window,sec,limit-1)


def randNum():
    return str(randint(0, 99))

def randDigit():
    return str(randint(0, 9))

def disableControls(window):
    window["Quit"].Update(disabled=True)
    window["OK"].Update(disabled=True)
    window["input"].Update(disabled=True)

def enableControls(window):
    window["Quit"].Update(disabled=False)
    window["OK"].Update(disabled=False)
    window["input"].Update(disabled=False)


gui.ChangeLookAndFeel('Dark Amber')

layout = [[gui.Text('PYTHON MEMORY GAME')],
          [gui.Text(' ', key='box0', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box10', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box20', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box30', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box40', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box50', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box60', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box70', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box80', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box90', size=(5, 1), pad=(1, 10))],
          [gui.Text(' ', key='box1', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box11', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box21', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box31', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box41', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box51', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box61', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box71', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box81', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box91', size=(5, 1), pad=(1, 10))],
          [gui.Text(' ', key='box2', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box12', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box22', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box32', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box42', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box52', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box62', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box72', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box82', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box92', size=(5, 1), pad=(1, 10))],
          [gui.Text(' ', key='box3', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box13', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box23', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box33', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box43', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box53', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box63', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box73', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box83', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box93', size=(5, 1), pad=(1, 10))],
          [gui.Text(' ', key='box4', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box14', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box24', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box34', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box44', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box54', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box64', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box74', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box84', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box94', size=(5, 1), pad=(1, 10))],
          [gui.Text(' ', key='box5', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box15', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box25', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box35', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box45', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box55', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box65', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box75', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box85', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box95', size=(5, 1), pad=(1, 10))],
          [gui.Text(' ', key='box6', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box16', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box26', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box36', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box46', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box56', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box66', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box76', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box86', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box96', size=(5, 1), pad=(1, 10))],
          [gui.Text(' ', key='box7', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box17', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box27', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box37', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box47', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box57', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box67', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box77', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box87', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box97', size=(5, 1), pad=(1, 10))],
          [gui.Text(' ', key='box8', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box18', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box28', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box38', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box48', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box58', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box68', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box78', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box88', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box98', size=(5, 1), pad=(1, 10))],
          [gui.Text(' ', key='box9', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box19', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box29', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box39', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box49', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box59', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box69', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box79', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box89', size=(5, 1), pad=(1, 10)),gui.Text(' ', key='box99', size=(5, 1), pad=(1, 10))],
          [gui.Text('Press START to begin',pad=(1,10),key="info",size=(50,1))],
          [gui.In(size=(40,1),disabled=True,background_color='white',key="input",text_color='black'), gui.Submit('START',key="OK",size=(5,1)),gui.CloseButton('Quit',button_color=('white','red'),key="Quit",size=(5,1))]
          ]

window = gui.Window('Memory Game', layout, keep_on_top=True, font=(None, 15))


nums = []
pos = 'box0'

isStart = 1
isWaiting = 0

temp = getDifficulty()


if temp == None:
    sec = 1
    level = 5
else:
    sec , level = temp

print(level)
print(sec)

while True:
    
    event, values = window.read()
    print('Event:',event, values)
    if event in (None, 'Quit'):
        break
    
    if not isStart:
        if values["input"].split() == nums:
            gui.PopupAutoClose("CORRECT",title='',keep_on_top=True,background_color='Dark Green',text_color='White',auto_close_duration=1,button_type=5)
        else:
            gui.Popup("WRONG\n\nCorrect Answer:\n" +" ".join(nums),title='',keep_on_top=True,background_color='Dark Red',text_color='White',font=("Helvetica",15))
            break
        nums.clear()
        window["input"]('')
        isWaiting = 1
        window["info"]("Round "+ str(level - 4) +" >> Press START for next round")
        window["OK"].Update('START')
        window.finalize()
        level += 1
        isWaiting = 1
        isStart = 1

    if not isWaiting:
        window["info"]("Round "+ str(level - 4) +" >> Memorise Them!")
        window.finalize()
        disableControls(window)
        showTime(window,sec,level)
        enableControls(window)
        window[pos]('')
        window["info"]("Round "+ str(level - 4) +" >> Write Down Numbers")
        window["OK"].Update('OK')
        window.finalize()
        isStart = 0
    else:
        isWaiting = 0

    print('nums',nums)

window.close()
