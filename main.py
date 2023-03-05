#Импорты из библиотеки
from kivy.app import App
from kivy.uix.button import Button


#Основной класс приложения
class Main(App):
    def build(self):
        return Button(text = "Houston naz?",
            font_size = 30,
            on_press = self.btn_press,
            background_color = [.32, .85, .94, 1,])

    def btn_press(self, instance):
        instance.text = 'YES!'


if __name__ == "__main__":
    Main().run()

