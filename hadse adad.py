import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Test(App):
    def build(self):
        self.icon = "myicon.png"
        self.title = "hadse adad"
        listt1 = ['1','2','3','4','5','6','7']
        self.listt1 = listt1
        listt2 = ['8','9','10','11','12','13','14']
        self.listt2 = listt2
        listt3 = ['15','16','17','18','19','20','21']
        self.listt3 = listt3

        shomarande = 1
        self.shomarande = shomarande

        boxx = BoxLayout(orientation='vertical')
        box = BoxLayout(orientation='horizontal')

        btn = Button(text="[b]1[/b]",size_hint=(0.2,0.3 ),background_color=(0,0.8,1,1),color=(1,1,1,1),markup=True)
        btn.bind(on_press=self.li1)
        btn2 = Button(text="[b]2[/b]",size_hint=(0.2,0.3 ),background_color=(0,0.8,1,1),color=(1,1,1,1),markup=True)
        btn2.bind(on_press=self.li2)
        btn3 = Button(text="[b]3[/b]",size_hint=(0.2,0.3 ),background_color=(0,0.8,1,1),color=(1,1,1,1),markup=True)
        btn3.bind(on_press=self.li3)
        prin = ""
        for i in range(7):
            prin += (f"  {listt1[i]}                   {listt2[i]}                   {listt3[i]}\n")
        self.prin = prin

        ch2 = Label(text=f"{self.prin}",font_size="22sp",markup=True)
        self.prin = ""
        self.ch2 = ch2

        cha = Label(text="[color=00c1ff]First select a number and\nsay which one is on the list\nI recognize the number after 3 questions[/color]",font_size="19sp",markup=True)
        self.cha = cha

        ch = Label(text="",font_size="19sp",size_hint=(0.1,0.1 ))
        self.ch = ch
        emp1 = Label(text="",font_size="19sp",size_hint=(0.1,0.1 ))
        emp2 = Label(text="",font_size="19sp",size_hint=(0.1,0.1 ))
        
        ch3 = Label(text="[color=00a0d8]@python_sec - @neema_af[/color]",font_size="19sp",size_hint=(0.1,0.1 ),pos_hint={'x':.25 , 'y':.6 },markup=True)
        self.ch3 = ch3

        empty = Label(text="",font_size="19sp",size_hint=(0.007,0.007 ))
        empty2 = Label(text="",font_size="19sp",size_hint=(0.007,0.007 ))

        h = 0
        self.h = h
        
        box.add_widget(emp1)
        box.add_widget(btn)
        box.add_widget(empty)
        box.add_widget(btn2)
        box.add_widget(empty2)
        box.add_widget(btn3)
        box.add_widget(emp2)

        boxx.add_widget(ch3)
        boxx.add_widget(cha)
        boxx.add_widget(ch2)
        boxx.add_widget(box)
        boxx.add_widget(ch)
        return boxx

    def li1(self,event):
        listt4 = self.listt2 + self.listt1 + self.listt3
        self.listt3 = []
        self.listt2 = []
        self.listt1 = []
        for i in range(0,21,3):
            #print(listt4)
            self.prin += (f"  {listt4[i]}                   {listt4[i+1]}                   {listt4[i+2]}\n")
            
            self.listt1.append(listt4[i])
            self.listt2.append(listt4[i+1])
            self.listt3.append(listt4[i+2])
        if self.shomarande%3 == 0:
            self.ch2.text=self.prin
            self.ch2.text = self.ch2.text+f"\n[color=00a8e3]your number is : {listt4[10]}[/color]"
        else :
            self.ch2.text=self.prin
        
        self.prin = ""
        self.shomarande += 1

    def li2(self,event):
        listt4 = self.listt1 + self.listt2 + self.listt3
        self.listt3 = []
        self.listt2 = []
        self.listt1 = []
        for i in range(0,21,3):
            #print(listt4)
            self.prin += (f"  {listt4[i]}                   {listt4[i+1]}                   {listt4[i+2]}\n")
            
            self.listt1.append(listt4[i])
            self.listt2.append(listt4[i+1])
            self.listt3.append(listt4[i+2])
        if self.shomarande%3 == 0:
            self.ch2.text=self.prin
            self.ch2.text = self.ch2.text+f"\n[color=00a8e3]your number is : {listt4[10]}[/color]"
        else :
            self.ch2.text=self.prin
        
        self.prin = ""
        self.shomarande += 1

    def li3(self,event):
        listt4 = self.listt2 + self.listt3 + self.listt1
        self.listt3 = []
        self.listt2 = []
        self.listt1 = []
        for i in range(0,21,3):
            #print(listt4)
            self.prin += (f"  {listt4[i]}                   {listt4[i+1]}                   {listt4[i+2]}\n")
            
            self.listt1.append(listt4[i])
            self.listt2.append(listt4[i+1])
            self.listt3.append(listt4[i+2])
        if self.shomarande%3 == 0:
            self.ch2.text=self.prin
            self.ch2.text = self.ch2.text+f"\n[color=00a8e3]your number is : {listt4[10]}[/color]"
        else :
            self.ch2.text=self.prin
        
        self.prin = ""
        self.shomarande += 1

if __name__=="__main__":
    Test().run()