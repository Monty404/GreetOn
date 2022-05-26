from kivy import config
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty as OP
import random,importlib
from os import path

Window.size = (300,700)#width, height

f_ls = [
    'Greetings_volume_App.cfg',
    'Greetings_phrase_App.cfg',
    'GenderApp.cfg',
    'Default.cfg'
    ]

gen_greet = [
    'Hello and Welcome Back',
    'Dont kill yourself, youre too seggxy, ah ha ha',
    'Ready to have some fun times?',
    'What can I call you?? Also my name is GreetOn',
    'Did You know you can change what I say to almost anything?',
    'Oh its you, again?',
    'Back so soon?',
    'Dont you think youve been on too long today?',
    'I love seeing the sunshine, its truly beautiful',
    'I hope your day is going well'
    ]

generator = random.choice(gen_greet)

if path.exists(f_ls[0]) == False or path.exists(f_ls[1]) == False or path.exists(f_ls[2]) == False or path.exists(f_ls[3]) == False:
    volume = open(file=f_ls[0],mode='w')
    volume.write('100.0')
    volume.close()
    phrase = open(file=f_ls[1],mode='w')
    phrase.close()
    f_Gender = open(file=f_ls[2],mode='w')
    f_Gender.write('Male')
    f_Gender.close()
    default = open(file=f_ls[3],mode='w')
    default.close()

vol = str(open(file=f_ls[0],mode='r').read())
phrase = open(file=f_ls[1],mode='r').read()

if phrase == "":
    default = open(file=f_ls[3],mode='w')
    default.write(str(generator))
    default.close()

import VoiceTXTMD

class ScreenMan(Widget):
    phrase = OP(None)   

    def gender(self):#Changes the voice type
        Gender = open(file=f_ls[2],mode='r')
        re_Gen = Gender.read()
        if re_Gen == "Female":
            f_Gender = open(file=f_ls[2],mode='w')
            f_Gender.write('Male')
            f_Gender.close()

        elif re_Gen == "Male":
            f_Gender = open(file=f_ls[2],mode='w')
            f_Gender.write('Female')
            f_Gender.close()
        

    #loads any known text
    def load(self):
        #opens the name and phrase file to be read only
        phrase_bt = open(file='Greetings_phrase_App.cfg',mode='r').read()

        print('Loaded as: '+phrase_bt)

        #Loads the last known file
        self.phrase.text = phrase_bt

    #test the voice in the application
    def voiceTest(self):
        #reloads the voice file
        importlib.reload(VoiceTXTMD)
        print('this is a voice test!')
  
    #saves the known text
    def save(self):
        #makes the variable global
        global phrase_bt

        phrase_bt =  self.phrase.text

        wt_phrase = open(file=f_ls[1],mode='w')
        wt_phrase.write(str(phrase_bt))
        print("Phrase: "+str(phrase_bt))
        wt_phrase.close()

        #sets text back to null phase
        phrase_bt = ''



class GreetOn(MDApp):
    def build(self):
        return Builder.load_file('MDStyle100.kv')

GreetOn().run()

