import sys
from random import randint
from map_file import map_list
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QLabel, QGridLayout, QMainWindow, QVBoxLayout, QPushButton

schet = 0
stavka = 0
lemming_i = None
lemming_j = None
map = map_list[randint(0, 2)]


class MainMenu(QMainWindow, QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.resize(2040, 1000)
        self.setMinimumSize(QtCore.QSize(2040, 1000))
        self.setMaximumSize(QtCore.QSize(2040, 1000))

        #  Окно Главного меню
        self.setGeometry(150, 150, 1040, 880)
        self.setWindowTitle('Главное меню')
        self.setStyleSheet("background-color: black; ")

        #  Текст в Окне "Главное меню"
        self.gl_text = QLabel(self)
        self.gl_text.setText("Главное меню")
        self.gl_text.setGeometry(870, 10, 280, 55)
        self.gl_text.setStyleSheet("color: green")

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.gl_text.setFont(font)
        self.gl_text.setObjectName("gl_text")

        self.button1 = QPushButton("Старт", self)
        self.button1.setGeometry(800, 150, 450, 60)
        self.button1.setStyleSheet("background-color: green; ")
        self.button1.clicked.connect(self.open_train_window)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")

        self.button2 = QPushButton("Правила", self)
        self.button2.setGeometry(800, 250, 450, 60)
        self.button2.setStyleSheet("background-color: green; ")
        self.button2.clicked.connect(self.open_rules)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button2.setFont(font)
        self.button2.setObjectName("button2")

        self.button3 = QPushButton("Выход", self)
        self.button3.setGeometry(800, 350, 450, 60)
        self.button3.setStyleSheet("background-color: green; ")
        self.button3.clicked.connect(self.exit_programm)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button3.setFont(font)
        self.button3.setObjectName("button3")

    def open_train_window(self):
        self.close()
        self.train = MainWindow()
        self.train.show()

    def open_rules(self):
        self.rules = TextWindow()
        self.rules.show()

    def exit_programm(self):
        QApplication.quit()


class TextWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(1000, 920)
        self.setMinimumSize(QtCore.QSize(1000, 920))
        self.setMaximumSize(QtCore.QSize(1000, 920))
        self.text_edit = QTextEdit()

        self.text_edit.setReadOnly(True)
        self.setCentralWidget(self.text_edit)

        # Устанавливаем заголовок окна
        self.setWindowTitle('Правила игры')

        # Добавляем текст в текстовый редактор
        self.text_edit.setPlainText(
            'Правила игры: 1.Дойти до финиша он обозначен синим квадратом                                  '
            '2.Постарайся не наткнутся на желтого монстра иначе игра будет оконьчена.                       '
            '3.Управление производится клафишами "Up,Down,Right,Left"                                            '
            '              4.Не пугайтесь Лемминг может и сам передвигаться по карте                             '
            '                      (Что бы закрыть это окно нажмите Esc) ')
        self.setStyleSheet("background-color: black")
        self.text_edit.setStyleSheet("color: green")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


class winpage(QWidget):
    def __init__(self):
        super().__init__()
        global schet
        schet = 0

        self.setGeometry(150, 150, 2040, 1000)
        if schet == 1:
            self.setWindowTitle('Вы выиграли')
            self.setStyleSheet("background-color: black; ")

            self.gl_text = QLabel(self)
            self.gl_text.setText("Вы выиграли!")
            self.gl_text.setGeometry(870, 10, 280, 55)
            font = QtGui.QFont()
            font.setPointSize(30)
            font.setBold(True)
            font.setWeight(75)
            self.gl_text.setFont(font)
            self.gl_text.setObjectName("gl_text")
        else:
            self.setWindowTitle('Вы проиграли')
            self.setStyleSheet("background-color: black; ")

            self.gl_text = QLabel(self)
            self.gl_text.setText("Вы проиграли!")
            self.gl_text.setGeometry(870, 10, 280, 55)
            font = QtGui.QFont()
            font.setPointSize(100)
            font.setBold(True)
            font.setWeight(75)
            self.gl_text.setFont(font)
            self.gl_text.setObjectName("gl_text")

        self.button11 = QPushButton("Играть заново", self)
        self.button11.setGeometry(800, 150, 450, 60)
        self.button11.setStyleSheet("background-color: green; ")
        self.button11.clicked.connect(self.open_train_window)
        self.button11.clicked.connect(self.closer)

        self.button13 = QPushButton("В главное меню", self)
        self.button13.setGeometry(800, 250, 450, 60)
        self.button13.setStyleSheet("background-color: green; ")
        self.button13.clicked.connect(self.open_main)
        self.button13.clicked.connect(self.closer)

    def open_train_window(self):
        self.game = MainWindow()
        self.game.show()

    def open_main(self):
        self.game = MainMenu()
        self.game.show()

    def closer(self):
        self.close()


class Lemming(QLabel):
    def __init__(self):
        super().__init__()

        self.setStyleSheet('min-width: 24px; min-height: 24px; background: red')
        self.resize(24, 24)


class Monster(QLabel):
    def __init__(self):
        super().__init__()

        self.setStyleSheet('min-width: 24px; min-height: 24px; background: yellow')
        self.resize(24, 24)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = None
        self.lemming = None
        self.monster = None
        self.setWindowTitle("The Lemmings")
        self.setGeometry(150, 150, 2040, 1000)
        self.setStyleSheet('background: black')
        self.setLayout(self.print_map())

    def print_map(self):
        self.layout = QGridLayout()
        for row in range(len(map)):
            for col in range(len(list(map[row]))):
                cell = map[row][col]

                if cell == '#':
                    label = QLabel()
                    label.resize(24, 24)
                    label.setStyleSheet('min-width: 24px; min-height: 24px; background: green')
                    self.layout.addWidget(label, row, col)
                if cell == 'S':
                    self.lemming = Lemming()
                    self.layout.addWidget(self.lemming, row, col)
                    self.timer_l = QTimer(self)
                    self.timer_l.timeout.connect(self.random_l)
                    self.timer_l.start(1000)
                if cell == 'M':
                    self.monster = Monster()
                    self.layout.addWidget(self.monster, row, col)
                    self.timer_m = QTimer(self)
                    self.timer_m.timeout.connect(self.random_m)
                    self.timer_m.start(1000)
                if cell == 'F':
                    label = QLabel()
                    label.resize(24, 24)
                    label.setStyleSheet('min-width: 24px; min-height: 24px; background: blue')
                    self.layout.addWidget(label, row, col)
        return self.layout

    def you_winner(self):
        global schet
        location_index = self.layout.indexOf(self.lemming)
        location = self.layout.getItemPosition(location_index)
        i = location[0]
        j = location[1]
        for row in range(len(map)):
            for col in range(len(list(map[row]))):
                cell = map[row][col]
                if row == i and col == j:
                    if cell == 'F':
                        print('Win')
                        print(stavka)
                        schet = 1
                        self.winpage()
                        self.close()

    def you_dead(self):
        global schet
        location_index = self.layout.indexOf(self.Monster)
        location = self.layout.getItemPosition(location_index)
        i = location[0]
        j = location[1]
        for row in range(len(map)):
            for col in range(len(list(map[row]))):
                cell = map[row][col]
                if row == i and col == j:
                    if cell == 'M':
                        print('Dead')
                        schet = 0
                        print(stavka)
                        self.winpage()
                        self.close()

    def winpage(self):
        print('yes')
        self.game = winpage()
        self.game.show()

    def lemming_moving(self, direction):
        location_index = self.layout.indexOf(self.lemming)
        location = self.layout.getItemPosition(location_index)
        i = location[0]
        j = location[1]
        global lemming_i, lemming_j
        lemming_i = i
        lemming_j = j

        if direction == 3:
            moving_left = j - 1
            for row in range(len(map)):
                for col in range(len(list(map[row]))):
                    cell = map[row][col]
                    if row == i and col == moving_left:
                        if cell == '#':
                            moving_left += 1
                        self.layout.addWidget(self.lemming, i, moving_left)
                        if cell == 'F':
                            self.you_winner()
                        print(f'леминга координаты: {i}, {moving_left}')
        if direction == 1:
            moving_right = j + 1
            for row in range(len(map)):
                for col in range(len(list(map[row]))):
                    cell = map[row][col]
                    if row == i and col == moving_right:
                        if cell == '#':
                            moving_right -= 1
                        self.layout.addWidget(self.lemming, i, moving_right)
                        if cell == 'F':
                            self.you_winner()
                        print(f'леминга координаты: {i}, {moving_right}')
        if direction == 0:
            moving_up = i - 1
            for row in range(len(map)):
                for col in range(len(list(map[row]))):
                    cell = map[row][col]
                    if row == moving_up and col == j:
                        if cell == '#':
                            moving_up += 1
                        self.layout.addWidget(self.lemming, moving_up, j)
                        if cell == 'F':
                            self.you_winner()
                        print(f'леминга координаты: {moving_up}, {j}')
        if direction == 2:
            moving_down = i + 1
            for row in range(len(map)):
                for col in range(len(list(map[row]))):
                    cell = map[row][col]
                    if row == moving_down and col == j:
                        if cell == '#':
                            moving_down -= 1
                        self.layout.addWidget(self.lemming, moving_down, j)
                        if cell == 'F':
                            self.you_winner()
                        print(f'леминга координаты: {moving_down}, {j}')

    def monster_moving(self, direction, l_i, l_j):
        location_index = self.layout.indexOf(self.monster)
        location = self.layout.getItemPosition(location_index)
        i = location[0]
        j = location[1]

        if i == l_i and j == l_j:
            self.you_dead()

        if direction == 3:
            moving_left = j - 1
            for row in range(len(map)):
                for col in range(len(list(map[row]))):
                    cell = map[row][col]
                    if row == i and col == moving_left:
                        if cell == '#':
                            moving_left += 1
                        self.layout.addWidget(self.monster, i, moving_left)
                        print(f'монстра координаты: {i}, {moving_left}')
        if direction == 1:
            moving_right = j + 1
            for row in range(len(map)):
                for col in range(len(list(map[row]))):
                    cell = map[row][col]
                    if row == i and col == moving_right:
                        if cell == '#':
                            moving_right -= 1
                        self.layout.addWidget(self.monster, i, moving_right)
                        print(f'монстра координаты: {i}, {moving_right}')
        if direction == 0:
            moving_up = i - 1
            for row in range(len(map)):
                for col in range(len(list(map[row]))):
                    cell = map[row][col]
                    if row == moving_up and col == j:
                        if cell == '#':
                            moving_up += 1
                        self.layout.addWidget(self.monster, moving_up, j)
                        print(f'монстра координаты: {moving_up}, {j}')
        if direction == 2:
            moving_down = i + 1
            for row in range(len(map)):
                for col in range(len(list(map[row]))):
                    cell = map[row][col]
                    if row == moving_down and col == j:
                        if cell == '#':
                            moving_down -= 1
                        self.layout.addWidget(self.monster, moving_down, j)
                        print(f'монстра координаты: {moving_down}, {j}')

    def collision(self, i, j, lemming_i, lemming_j):
        if i == lemming_i:
            self.winpage()
        else: self.you_dead()
        if j == lemming_j:
            self.winpage()
        else: self.you_dead()



    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Right:
            self.lemming_moving(1)
        if event.key() == Qt.Key_Left:
            self.lemming_moving(3)
        if event.key() == Qt.Key_Up:
            self.lemming_moving(0)
        if event.key() == Qt.Key_Down:
            self.lemming_moving(2)
        if event.key() == Qt.Key_Escape:
            self.close()

    def random_l(self):
        el = randint(0, 3)
        self.lemming_moving(int(el))
        self.timer_l.start(110)
        global stavka
        stavka += 1

    def random_m(self):
        el = randint(0, 3)
        self.monster_moving(int(el), lemming_i, lemming_j)
        self.timer_m.start(110)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec_())
