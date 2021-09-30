from kivy.core.window import Window
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.chip import MDChip


class MainApp(MDApp):
    title = StringProperty('')
    list = ObjectProperty()
    cip = ObjectProperty()
    text = StringProperty('')
    message = StringProperty('')

    def back_button(self):
        sm = self.root
        sm.current = "one"

    def on_start(self):
        self.temporary_screen()
        #self.message_chip()

    # MENU BUTTON ##

    def drop_down(self):
        menu = [
            "Restart WhatsApp",
            "Message Scheduler",
            "Group Brodcast",
            "New Group",
            "New Broadcast",
            "Linked Devices",
            "Starred Message",
            "Settings"]

        self.menu = MDDropdownMenu(
            items=menu,
            width_mult=4,
            on_release=self.menu_callback

        )

    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

    def menu_callback(self, menu):
        self.menu.dismiss()
        print(menu.text)

    # SCREENS ##

    def screen(self, instance):
        sm = self.root
        self.title = instance.text
        sm.current = 'two'

    def temporary_screen(self):
        add = self.root.ids.container
        for i in range(10):
            self.list = TwoLineListItem(text=f'name {i}', secondary_text='oi joe uko wap', on_release=self.screen)
            self.list.id = i
            add.add_widget(self.list)

   #def message_chip(self):
   #    chip = self.root.ids.chip
   #    self.cip = MDChip(text='')

    #def the_title(self):






    def build(self):
        self.size_x, self.size_y = Window.size
        Window.size = (360, 640)
        self.title = "chat"


MainApp().run()
