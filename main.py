from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window

# Функция обработчика значений
def script(instance, value):
    global txt

    lbl2.text = ""
    err = 0
    txt = value[::-1]
    txt = txt.lower()
    prt = ''
    for i in range(len(txt)):
        if txt[i] == 'l':
            tx = '7'
        elif txt[i] == 'b':
            tx = '9'
        elif txt[i] == 'h':
            tx = '4'
        elif txt[i] == 's':
            tx = '5'
        elif txt[i] == 'g':
            tx = '6'
        elif txt[i] == 'e':
            tx = '3'
        elif txt[i] == 'i':
            tx = '1'
        elif txt[i] == 'o':
            tx = '0'
        elif txt[i] == ' ':
            tx = ' '
        elif txt[i] == '\n':
            tx = '\n'
        else:
            err = 1
            tx = '?'
        prt += tx

    if err == 0:
        lbl.text = prt
    else:
        lbl.text = prt
        lbl2.text = "ОШИБКА! НАЙДЕНЫ НЕПОДДЕРЖИВАЕМЫЕ СИМВОЛЫ"

# Класс приложения
class Application(App):

    # Сборка интерфейса
    def build(self):
        global lbl
        global lbl2

        # Белый цвет фона
        Window.clearcolor = (.9, .9, .9, 1)

        # Сетка для размещения виджетов
        grid = GridLayout(cols=1)

        # Поле ввода
        input = TextInput(size_hint=(.04, .01), pos_hint={'center_x': .5, 'center_y': 1})
        input.bind(text=script)

        # Картинка
        img = Image(source="txt.png", size_hint=(0, .05))

        # Выход значения
        lbl = Label(size_hint=(0, .05), color=(0, 0, 0))

        # Выход ошибок
        lbl2 = Label(size_hint=(0, .05), color=(1, 0, 0))

        # Описание
        dsrpt = Label(size_hint=(0, .05), color=(0, 0, .6), halign="center", text="Это приложение сделает из слова (только латинские буквы)\nшифр для калькулятора! Более подробнее на официальном\nGitHub - https://github.com/WaysoonProgramms/HackYourCalculator\n \nВведите слово в строку вводаи вы увидете результат ниже")

        # Сборка всех виджетов в сетку
        grid.add_widget(img)
        grid.add_widget(dsrpt)
        grid.add_widget(lbl2)
        grid.add_widget(lbl)
        grid.add_widget(input)

        return grid

if __name__ == "__main__":
    Application().run()