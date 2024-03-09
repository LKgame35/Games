import threading
import time
import tkinter as tk
from time import strftime
import sqlite3

stundas = 0
minutes=0
sekundes=0
eror_teksts=""

root = tk.Tk()
root.title("Laiks")
root.geometry("500x400")
root.resizable(0,0)


savienojums = sqlite3.connect("laiks2.db")
kursors = savienojums.cursor()

class Pulkstenis:

    def __init__(self, stundas2, minutes2,sekundes2):

        self.stundas=stundas2
        self.minutes=minutes2
        self.sekundes=sekundes2

        kursors.execute('''CREATE TABLE IF NOT EXISTS laiks2 (
                    id INTEGER PRIMARY KEY,
                    stundas2 INT NOT NULL,
                    minutes2 INT NOT NULL,
                    sekundes2 INT NOT NULL)
                    ''')

    def iestatija(self, stundas2, minutes2, sekundes2):

        kursors.execute(f'''INSERT INTO laiks2 (stundas2, minutes2, sekundes2)
            VALUES("{stundas2}", "{minutes2}", "{sekundes2}")
            ''')

def plus_minute():
    global minutes
    global sekundes
    minutes+=1
    sekundes=0

def plus_stunda():
    global minutes
    global stundas
    stundas+=1
    minutes=0


def increment_variable():
    global stundas
    global sekundes
    global minutes

    while True:
        if sekundes==59:
            plus_minute()
        else:    
            sekundes += 1
        if minutes==59:
            plus_stunda()

        if stundas<10:st0="0"
        else:st0=""
        if minutes<10:mi0="0"
        else:mi0=""
        if sekundes<10:se0="0"
        else:se0=""
        
        a = tk.Label(root, text=f'{st0}{stundas}:{mi0}{minutes}:{se0}{sekundes}',font=('calibri', 25), fg="green")
        a.place(x=140, y=300)

        l_virsraksts = tk.Label(root, text=f'{eror_teksts}', font=(25), fg="red")
        l_virsraksts.place(x=220, y=250)

        time.sleep(1)



def iestatit():
    global stundas
    global sekundes
    global minutes
    global eror_teksts

    stundas_str = str(e_skaitlis1.get())
    minutes_str = str(e_skaitlis2.get())
    sekundes_str = str(e_skaitlis3.get())
    if stundas_str=="":stundas_str="0"
    if minutes_str=="":minutes_str="0"
    if sekundes_str=="":sekundes_str="0"


    stundas1 = int(stundas_str)
    minutes1 = int(minutes_str)
    sekundes1 = int(sekundes_str)-1

    if stundas1>23 or minutes1>59 or sekundes1>59:
        eror_teksts="Neiespējams laiks ievadīts"
    else:
        n=Pulkstenis(stundas1,minutes1,sekundes1)
        n.iestatija(stundas1,minutes1,sekundes1)
        stundas=stundas1
        minutes=minutes1
        sekundes=sekundes1


def pievienot():
    global stundas
    global sekundes
    global minutes
    global eror_teksts

    stundas_str = str(e_skaitlis1.get())
    minutes_str = str(e_skaitlis2.get())
    sekundes_str = str(e_skaitlis3.get())
    if stundas_str=="":stundas_str="0"
    if minutes_str=="":minutes_str="0"
    if sekundes_str=="":sekundes_str="0"

    stundas1 = int(stundas_str)
    minutes1 = int(minutes_str)
    sekundes1 = int(sekundes_str)

    if stundas+stundas1>23 or minutes1+minutes>59 or sekundes1+sekundes>59:
        eror_teksts="Neiespējams laiks ievadīts"
    else:
        stundas+=stundas1
        minutes+=minutes1
        sekundes+=sekundes1



increment_thread = threading.Thread(target=increment_variable)
increment_thread.start()




l_virsraksts = tk.Label(root, text='Stundas', font=(25), fg="black")
l_virsraksts.place(x=80, y=70)

l_virsraksts = tk.Label(root, text='Minūtes', font=(25), fg="black")
l_virsraksts.place(x=220, y=70)

l_virsraksts = tk.Label(root, text='Sekundes', font=(25), fg="black")
l_virsraksts.place(x=370, y=70)

b_poga = tk.Button(root, text="Pievienot", command=pievienot)
b_poga.place(x=150, y=150)

bb_poga = tk.Button(root, text="Iestatīt", command=iestatit)
bb_poga.place(x=250, y=150)



e_skaitlis1 = tk.Entry(root)
e_skaitlis1.place(x=50, y=100)
e_skaitlis2 = tk.Entry(root)
e_skaitlis2.place(x=200, y=100)
e_skaitlis3 = tk.Entry(root)
e_skaitlis3.place(x=350, y=100)

jaunais = tk.Label(root, text='Laiks: ', font=(25), fg="black")
jaunais.place(x=140, y=280)




root.mainloop()
