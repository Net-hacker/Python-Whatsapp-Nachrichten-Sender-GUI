#Importierte Libs
import pywhatkit
import keyboard
import time
import os
import sys
from tkinter import *

#Variablen
Nummer: str
Nachricht: str
hr: int
mint: int
Vor: str


if os.path.exists('pywhatkit_dbs.txt'):
	os.remove('pywhatkit_dbs.txt')

def FirstUse():
	global Vor
	if os.path.exists('Prefix.txt'):
		with open('Prefix.txt', 'r') as o:
			Vor = o.read()
			o.close()
	else:
		Vor = input("Deine Vorwahl: ")
		with open('Prefix.txt', 'w') as w:
			w.write(Vor)
	os.system('cls')
	window.mainloop()


def LockNum():
	global Nummer
	Nummer = numPad.get()

def LockText():
	global Nachricht
	Nachricht = str(textPad.get())

def LockHr():
	global hr
	hr = int(hrPad.get())

def LockMin():
	global mint
	mint = int(minPad.get())

def Sender():
	global Nummer
	global Nachricht
	global hr
	global mint
	window.destroy()
	pywhatkit.sendwhatmsg(Vor + Nummer, Nachricht, hr, mint)
	sys.exit()

	if os.path.exists('pywhatkit_dbs.txt'):
		os.remove('pywhatkit_dbs.txt')

window = Tk()
window.geometry("720x400")
window.title('Nachrichten Sender')
window.configure(background='#141010')

numText = Label(window, text="Die Nummer:", bg='#141010', fg='#FFFFFF').pack(pady=10, padx=20, anchor='w')
textText = Label(window, text="Die Nachricht:", bg='#141010', fg='#FFFFFF').pack(pady=5, padx=20, anchor='w')
hrText = Label(window, text="Die Stunde wo es ankommt:", bg='#141010', fg='#FFFFFF').pack(pady=20, padx=20, anchor='w')
minText = Label(window, text="Die Minute wo es ankommt:", bg='#141010', fg='#FFFFFF').pack(pady=0, padx=20, anchor='w')


numPad = Entry(window)
textPad = Entry(window)
hrPad = Spinbox(window, from_=0, to_=23)
minPad = Spinbox(window, from_=0, to=59)


numPad.place(x=250, y=10)
textPad.place(x=250, y=50)
hrPad.place(x=250, y=90)
minPad.place(x=250, y=130)

b1 = Button(window, text='Lock', command=LockNum, width=10, bg='#777777')
b1.place(x=400, y=10)

b2 = Button(window, text='Lock', command=LockText, width=10, bg='#777777')
b2.place(x=400, y=50)

b3 = Button(window, text='Lock', command=LockHr, width=10, bg='#777777')
b3.place(x=400, y=90)

b4 = Button(window, text='Lock', command=LockMin, width=10, bg='#777777')
b4.place(x=400, y=130)

b5 = Button(window, text='Senden', command=Sender, width=10, bg='#777777')
b5.place(x=250, y=200)

print("Script Made by Juri-Zockt")
FirstUse()
