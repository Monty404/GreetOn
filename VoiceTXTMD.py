import pyttsx3 as pv

f_phrase =  open(file='Greetings_phrase_App.cfg',mode='r').read()
f_volume =  float(open(file='Greetings_volume_App.cfg', mode='r').readline())
f_gender = open(file='GenderApp.cfg').readline()
default = open(file='Default.cfg',mode='r').readline()
files = [f_phrase,f_volume,f_gender,default]

engine = pv.init()

voices = engine.getProperty('voices')

volume = engine.setProperty('volume', (files[1]/100))#controls the volume

if files[2] == 'Female':
    engine.setProperty('voice', voices[1].id)
else:
    engine.setProperty('voice', voices[0].id)

if files[0] == "":
    engine.say(files[3])
else:
    engine.say(files[0])


engine.runAndWait()#runs the voice