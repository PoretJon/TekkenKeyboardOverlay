from PyQt6 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt6.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox, QLabel
from PyQt6.QtCore import pyqtSlot
from pynput.keyboard import Key, Listener, KeyCode
import sys
from TekkenKbOverlay import Ui_MainWindow
import os



class TekkenKBOverlayWrapper(QtWidgets.QMainWindow):

    DEFAULT_BINDS_STR = '''UP:w
DOWN:s
LEFT:a
RIGHT:d
ONE:u
TWO:i
THREE:j
FOUR:k
HEAT:p
RAGE:;
    '''
    

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.default_binds = {
            KeyCode.from_char('w') : self.ui.imgBtnUp,
            KeyCode.from_char('s') : self.ui.imgBtnDown,
            KeyCode.from_char('a') : self.ui.imgBtnLeft,
            KeyCode.from_char('d') : self.ui.imgBtnRight,
            KeyCode.from_char('j') : self.ui.imgBtnThree,
            KeyCode.from_char('k') : self.ui.imgBtnFour,
            KeyCode.from_char('u') : self.ui.imgBtnOne,
            KeyCode.from_char('i') : self.ui.imgBtnTwo,
            KeyCode.from_char('p') : self.ui.imgBtnHeat,
            KeyCode.from_char(';') : self.ui.imgBtnRage
        }
        self.bindings = {
            'UP': self.ui.imgBtnUp,
            'DOWN': self.ui.imgBtnDown,
            'LEFT': self.ui.imgBtnLeft,
            'RIGHT': self.ui.imgBtnRight,
            'ONE': self.ui.imgBtnOne,
            'TWO': self.ui.imgBtnTwo,
            'THREE': self.ui.imgBtnThree,
            'FOUR': self.ui.imgBtnFour,
            'HEAT': self.ui.imgBtnHeat,
            'RAGE': self.ui.imgBtnRage
        }

        self.buttons = {}
        # set up the button bindings
        # TODO: have this read in data from a file
        with open('keybinds.cfg', 'a+') as file:
            # check if file is empty (making the file)
            new_file = os.path.getsize('keybinds.cfg') == 0
            if new_file:
                # write default binds to file
                file.write(self.DEFAULT_BINDS_STR)
            # reset cursor
            file.seek(0)
            # load keybinds
            for line in file:
                bind = line.strip().split(':')
                if len(bind) != 2 or bind[0] not in self.bindings:
                    # TODO: make error dialog
                    self.buttons = self.default_binds
                    break
                print(f'binding {bind[1]} to {bind[0]}')
                self.buttons[KeyCode.from_char(bind[1])] = self.bindings[bind[0]]
        # make everything "not pressed"
        for key in self.buttons:
            self.buttons[key].setVisible(False)
        self.ui.imgBaseOverlay.setVisible(True)

    # when a button is pressed, if its in our list of buttons, highlight the button
    def on_press(self, key):
        if key in self.buttons.keys():
            img = self.buttons[key]
            img.setVisible(True)
        return
    
    # if a button is released and in our set, make the button "unpressed" on the GUI
    def on_release(self, key):
        if key in self.buttons.keys():
            img = self.buttons[key]
            img.setVisible(False)
        return
    
    # make the thread and start
    # This feels janky, but its not.
    def startListening(self):
        listener = Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()
    

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = TekkenKBOverlayWrapper()
    window.show()
    window.startListening() # see comment above method definition
    sys.exit(app.exec())