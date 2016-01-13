#This is a simple program to randomly assign students to a seat

import sys
import random
from PyQt4.QtGui import *
from PyQt4.QtCore import *



#make the things here
app = QApplication(sys.argv)
wind = QMainWindow()

#customize the window here
wind.resize(960,720)
wind.setWindowTitle("SeatSwitcher v1.0")
background = QPalette()
background.setBrush(QPalette.Background,QBrush(QPixmap("SkyBurst.jpg")))
wind.setPalette(background)
wind.setWindowIcon(QIcon('SeatSwitcherIcon.png'))

#variables for functions go here
classList = []
tempList = []

#functions go here
def randomize():
    global classList
    global tempList

    if classList == []:
        QMessageBox.critical(wind, "Warning", "No class list loaded!")
    else:
        while classList != []:
            movingElement = classList[random.randint(0, len(classList)-1)]
            tempList.append(movingElement)
            classList.remove(movingElement)
        textbox01.setText(tempList[0])
        textbox02.setText(tempList[1])
        textbox03.setText(tempList[2])
        textbox04.setText(tempList[3])
        textbox05.setText(tempList[4])
        textbox06.setText(tempList[5])
        textbox07.setText(tempList[6])
        textbox08.setText(tempList[7])
        textbox09.setText(tempList[8])
        textbox10.setText(tempList[9])
        textbox11.setText(tempList[10])
        textbox12.setText(tempList[11])
        textbox13.setText(tempList[12])
        textbox14.setText(tempList[13])
        textbox15.setText(tempList[14])
        textbox16.setText(tempList[15])
        classList = tempList
        tempList = []

def open_file():
    global classList

    #openedFile = QFileDialog.getOpenFileName(wind, "Open File", "C:\") #this is the windows code
    openedFile = QFileDialog.getOpenFileName(wind, "Open File", "/") #this is the linux(mac?) code ###add '*.txt' filter
    classList = open(openedFile).readlines()

    textbox01.setText(classList[0])
    textbox02.setText(classList[1])
    textbox03.setText(classList[2])
    textbox04.setText(classList[3])
    textbox05.setText(classList[4])
    textbox06.setText(classList[5])
    textbox07.setText(classList[6])
    textbox08.setText(classList[7])
    textbox09.setText(classList[8])
    textbox10.setText(classList[9])
    textbox11.setText(classList[10])
    textbox12.setText(classList[11])
    textbox13.setText(classList[12])
    textbox14.setText(classList[13])
    textbox15.setText(classList[14])
    textbox16.setText(classList[15])

def save_file():
    global classList
    saveContent = ''.join(classList)

    saveFileName = QFileDialog.getSaveFileName(wind, "Save File", "/") #add '*.txt' filter
    saveFile = open(saveFileName, 'w')
    saveFile.write(saveContent)
    QMessageBox.information(wind, "Message", "Your file has been saved.")

def exit_app():
    areYouSure = QMessageBox.question(wind, 'Exit', "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    if areYouSure == QMessageBox.Yes:
        sys.exit()

#Make the randomize button here
btn = QPushButton('Randomize', wind)
btn.clicked.connect(randomize)
btn.resize(btn.sizeHint())
btn.move(50, 589)


#menu bar and options go here
openFileAction = QAction("Open File", wind)
openFileAction.triggered.connect(open_file)
saveFileAction = QAction("Save As...", wind)
saveFileAction.triggered.connect(save_file)
exitAppAction = QAction("Exit", wind)
exitAppAction.triggered.connect(exit_app)

mainMenu = wind.menuBar()
mainMenu.setNativeMenuBar(False)
fileMenu = mainMenu.addMenu("&File")
fileMenu.addAction(openFileAction)
fileMenu.addAction(saveFileAction)
fileMenu.addAction(exitAppAction)

#textboxes go here*16
textbox01 = QLineEdit(wind)
textbox01.move(280,130)
textbox01.resize(150,30)

textbox02 = QLineEdit(wind)
textbox02.move(280,184) #textbox01 y+54
textbox02.resize(150,30)

textbox03 = QLineEdit(wind)
textbox03.move(280,239) #textbox02 y+55
textbox03.resize(150,30)

textbox04 = QLineEdit(wind)
textbox04.move(280,291) #textbox03 y+52
textbox04.resize(150,30)

textbox05 = QLineEdit(wind)
textbox05.move(646,130) #textbox01 x+366
textbox05.resize(150,30)

textbox06 = QLineEdit(wind)
textbox06.move(646,184)
textbox06.resize(150,30)

textbox07 = QLineEdit(wind)
textbox07.move(646,239)
textbox07.resize(150,30)

textbox08 = QLineEdit(wind)
textbox08.move(646,291)
textbox08.resize(150,30)

textbox09 = QLineEdit(wind)
textbox09.move(280,428)
textbox09.resize(150,30)

textbox10 = QLineEdit(wind)
textbox10.move(299,482) #textbox01 x+19
textbox10.resize(150,30)

textbox11 = QLineEdit(wind)
textbox11.move(299,537)
textbox11.resize(150,30)

textbox12 = QLineEdit(wind)
textbox12.move(299,589)
textbox12.resize(150,30)

textbox13 = QLineEdit(wind)
textbox13.move(665,428) #textbox05 x+19,
textbox13.resize(150,30)

textbox14 = QLineEdit(wind)
textbox14.move(665,482)
textbox14.resize(150,30)

textbox15 = QLineEdit(wind)
textbox15.move(665,537)
textbox15.resize(150,30)

textbox16 = QLineEdit(wind)
textbox16.move(665,589)
textbox16.resize(150,30)

#show your work
wind.show()



sys.exit(app.exec_())
