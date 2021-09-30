from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.chip import MDChip

class MainApp(MDApp):
    text = StringProperty('')



    def add_chip(self):
        card = self.root.ids.one
        self.mycard = MDCard(Label(), pos_hint={"center_x": .5, "center_y": .9})
        card.add_widget(self.mycard)







    def build(self):
        self.title = 'all my test'


MainApp().run()
