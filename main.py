from kivymd.app import MDApp
from kivy.core.window import Window

from kivy import utils
from kivymd.toast import toast
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar

if utils.platform != 'android':
    Window.size = (360, 640)


class MainApp(MDApp):


    def menu_icon(self, ext):
        menu = [
            "vimbweta vya uwanjani",
            "vimbweta vya stationary",
            "vimbweta vya girls hostel",
            "vimbweta vya boys hostel",
        ]

        self.menu = MDDropdownMenu(
            caller=ext,
            items=menu,
            width_mult=4,
            callback=self.menu_callback
        )

        self.menu.bind(
            on_release=self.menu_callback
        )

    def menu_callback(self, menu):
        self.menu_text = menu.text
        self.menu.dismiss()

    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

        toast("wait still in progress")

    def build(self):
        self.size_x, self.size_y = Window.size
        self.title = "CHANZI"


MainApp().run()
