#Importe Libs
import pywhatkit
import time
import os
import sys
import datetime
import PySimpleGUI as sg

sg.theme("DarkGreen1")

if os.path.exists('pywhatkit_dbs.txt'):
	os.remove('pywhatkit_dbs.txt')

firstlayout = [
	[sg.Text("Nachrichten Sender")],
	[sg.Text("Die Vorwahl:"), sg.InputText()],
	[sg.Text("Die Nummer:"), sg.InputText()],
	[sg.Text("Die Nachricht:"), sg.InputText()],
	[sg.Text("Die Ankunftsstunde:"), sg.Spin(values=["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"])], #, key="-Std-")
	[sg.Text("Die Ankunftsminute:"), sg.Spin(values=["00", "05", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55"])], #, key="-Min-")
	[sg.Button("Senden")],
	[sg.Text(key="-Anwser-")]
]

layout = [
	[sg.Text("Nachrichten Sender")],
	[sg.Text("Die Nummer:"), sg.InputText()],
	[sg.Text("Die Nachricht:"), sg.InputText()],
	[sg.Text("Die Ankunftsstunde:"), sg.Spin(values=["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"])],
	[sg.Text("Die Ankunftsminute:"), sg.Spin(values=["00", "05", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55"])],
	[sg.Button("Senden")],
	[sg.Text(key="-Anwser-")]
]

if os.path.exists('Prefix.txt'):
	window = sg.Window("Nachrichten Sender", icon="Icon.ico", element_justification='c').Layout(layout)
	while True:
		event, values = window.read()

		if event == sg.WIN_CLOSED:
			if os.path.exists('pywhatkit_dbs.txt'):
				os.remove('pywhatkit_dbs.txt')
			break
		elif event == "Senden":
			window.minimize()
			Nummer = values[0]
			Nachricht = values[1]
			Hr = values[2]
			Min = values[3]
			with open("Prefix.txt", "r") as o:
				Vor = o.read()
				o.close()
			h = datetime.datetime.now().strftime("%H")
			m = datetime.datetime.now().strftime("%M")
			Time = ((int(Hr) * 3600) + (int(Min) * 60) - ((int(h) * 3600) + (int(m) * 60)))
			sg.popup(f"Die Nachricht wird in {Time} Sekunden gesendet")
			pywhatkit.sendwhatmsg(Vor + Nummer, Nachricht, int(Hr), int(Min))
			sg.popup("Done!")
			break
else:
	window = sg.Window("Nachrichten Sender", icon="Icon.ico", element_justification='c').Layout(firstlayout)
	while True:
		event, values = window.read()

		if event == sg.WIN_CLOSED:
			if os.path.exists('pywhatkit_dbs.txt'):
				os.remove('pywhatkit_dbs.txt')
			break
		elif event == "Senden":
			window.minimize()
			Vor = values[0]
			Nummer = values[1]
			Nachricht = values[2]
			Hr = values[3]
			Min = values[4]
			with open("Prefix.txt", "w") as w:
				w.write(Vor + "\n")
				w.close()
			h = datetime.datetime.now().strftime("%H")
			m = datetime.datetime.now().strftime("%M")
			Time = ((int(Hr) * 3600) + (int(Min) * 60) - ((int(h) * 3600) + (int(m) * 60)))
			sg.popup(f"Die Nachricht wird in {Time} Sekunden gesendet")
			pywhatkit.sendwhatmsg(Vor + Nummer, Nachricht, int(Hr), int(Min))
			sg.popup("Done!")
			break

if os.path.exists('pywhatkit_dbs.txt'):
	os.remove('pywhatkit_dbs.txt')
window.close()
