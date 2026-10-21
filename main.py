from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='Sarubima App', font_size='20sp'))
        
        btn_farmer = Button(text='Farmer Screen', size_hint=(1, 0.2))
        btn_farmer.bind(on_press=lambda x: setattr(self.manager, 'current', 'farmer'))
        layout.add_widget(btn_farmer)
        
        btn_consumer = Button(text='Consumer Screen', size_hint=(1, 0.2))
        btn_consumer.bind(on_press=lambda x: setattr(self.manager, 'current', 'consumer'))
        layout.add_widget(btn_consumer)
        
        self.add_widget(layout)

class FarmerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='Farmer Input Data'))
        btn_back = Button(text='Back', size_hint=(1, 0.2))
        btn_back.bind(on_press=lambda x: setattr(self.manager, 'current', 'home'))
        layout.add_widget(btn_back)
        self.add_widget(layout)

class ConsumerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='Consumer View Data'))
        btn_back = Button(text='Back', size_hint=(1, 0.2))
        btn_back.bind(on_press=lambda x: setattr(self.manager, 'current', 'home'))
        layout.add_widget(btn_back)
        self.add_widget(layout)

class SarubimaApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(FarmerScreen(name='farmer'))
        sm.add_widget(ConsumerScreen(name='consumer'))
        return sm

if __name__ == '__main__':
    SarubimaApp().run()
