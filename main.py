import os

from kivymd.uix.tab import MDTabsBase
from kivymd.app import MDApp 
from kivy.uix.screenmanager import ScreenManager,Screen 
from kivy.core.window import Window 
from kivy.lang import Builder 
from kivy.uix.popup import Popup 
from kivy_garden.mapview import MapView 
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import StringProperty
from kivy.core.text import LabelBase,DEFAULT_FONT
from kivy.resources import resource_add_path

resource_add_path("C:/Users/武田　哲士takedasatoshi/csp/TownDev/assets/font/")
LabelBase.register(
    DEFAULT_FONT,
    "NotoSansJP-VariableFont_wght.ttf"
)

global screen 

screen = ScreenManager()


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    content_text = StringProperty("")

class SplashScreen(Screen):
    pass

class MainScreen(Screen):
   pass

class MapScreen(Screen):
    mapview = MapView(zoom=11,lat=34.6919,lon=135.701)

class ShopScreen(Screen):
    pass


screen.add_widget(SplashScreen(name='splash'))
screen.add_widget(MainScreen(name='main'))
screen.add_widget(MapScreen(name='map'))
screen.add_widget(ShopScreen(name='shop'))


class MainApp(MDApp):
    def build(self):
        kv = Builder.load_file("UI.kv")
        screen = kv
        return screen

if __name__ == '__main__':
    MainApp().run()

