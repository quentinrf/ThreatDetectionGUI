import os
os.environ["KIVY_HOME"] = '/Users/quentinrf/Documents/2ndYear/APSC200/GUI'

import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from functools import partial
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.video import Video
#Configuration Files
from kivy.config import Config
Config.read('test.txt')
Config.set('kivy', 'exit_on_escape', '1')
Window.size = (1000,65)
Config.set('graphics', 'position', 'custom')
Config.write()
#Make Dem Screens!!
Builder.load_string("""
<LoginScreen>:
    BoxLayout:
        TextInput:
            id: login
        TextInput:
            id: passw
            password: True
        Button:
            text: "Login"
            on_press: root.verify_credentials()

<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Main Office'
            on_press:
                root.resize()
                root.manager.transition.direction = 'left'
                app.root.current = "office"
        Button:
            text: 'Gymnasium'
            on_press:
                root.resize()
                root.manager.transition.direction = 'left'
                app.root.current = "gym"
        Button:
            text: 'Library'
            on_press:
                root.resize()
                root.manager.transition.direction = 'left'
                app.root.current = "lib"
        Button:
            text: 'Math Department'
            on_press:
                root.resize()
                root.manager.transition.direction = 'left'
                app.root.current = "math"
        Button:
            text: 'Physics Department'
            on_press:
                root.resize()
                root.manager.transition.direction = 'left'
                app.root.current = "physics"
        Button:
            text: 'Auditorium'
            on_press:
                root.resize()
                root.manager.transition.direction = 'left'
                app.root.current = "aud"

<MainOffice>:
    BoxLayout:
        Button:
            text: 'Refresh'
        Button:
            text: 'Back to Menu'
            on_press:
                root.undo()
                root.manager.transition.direction = 'right'
                app.root.current = "menu"

<Gymnasium>:
    BoxLayout:
        Button:
            text: 'Refresh'
        Button:
            text: 'Back to Menu'
            on_press:
                root.undo()
                root.manager.transition.direction = 'right'
                app.root.current = "menu"
<Library>:
    BoxLayout:
        Button:
            text: 'Refresh'
        Button:
            text: 'Back to Menu'
            on_press:
                root.undo()
                root.manager.transition.direction = 'right'
                app.root.current = "menu"

<MathDepartment>:
    BoxLayout:
        Button:
            text: 'Refresh'
        Button:
            text: 'Back to Menu'
            on_press:
                root.undo()
                root.manager.transition.direction = 'right'
                app.root.current = "menu"
<PhysicsDepartment>:
    BoxLayout:
        Button:
            text: 'Refresh'
        Button:
            text: 'Back to Menu'
            on_press:
                root.undo()
                root.manager.transition.direction = 'right'
                app.root.current = "menu"
<Auditorium>:
    BoxLayout:
        Button:
            text: 'Refresh'
        Button:
            text: 'Back to Menu'
            on_press:
                root.undo()
                root.manager.transition.direction = 'right'
                app.root.current = "menu"
""")


#Declaring Screens
class LoginScreen(Screen):
    def verify_credentials(self):
        if self.ids["login"].text == "quentinrf" and self.ids["passw"].text == "dick":
            self.manager.current = "menu"

class MenuScreen(Screen):
    def resize(self):
        Window.size = (900, 600)
class MainOffice(Screen):
    def undo(self):
        Window.size = (1000, 65)
    def vid(self):
        video = Video(source='party.mov', play=True)
class Gymnasium(Screen):
    def undo(self):
        Window.size = (1000, 65)
class Library(Screen):
    def undo(self):
        Window.size = (1000, 65)
class MathDepartment(Screen):
    def undo(self):
        Window.size = (1000, 65)
class PhysicsDepartment(Screen):
    def undo(self):
        Window.size = (1000, 65)
class Auditorium(Screen):
    def undo(self):
        Window.size = (1000, 65)


##AnchorLayout:
##        Video:
##            source: 'party.mov'
##            play: True

#Setup ScreenManager
sm = ScreenManager()
sm.add_widget(LoginScreen(name = 'login'))
sm.add_widget(MenuScreen(name = 'menu'))
sm.add_widget(MainOffice(name = 'office'))
sm.add_widget(Gymnasium(name = 'gym'))
sm.add_widget(Library(name = 'lib'))
sm.add_widget(MathDepartment(name = 'math'))
sm.add_widget(PhysicsDepartment(name = 'physics'))
sm.add_widget(Auditorium(name = 'aud'))
#Run dat app BITCH
class Threatdetection(App):
    def build(self):
        self.icon = "fire.png"
        return sm
if __name__ == '__main__':
    Threatdetection().run()
