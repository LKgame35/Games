import tkinter as tk
from time import strftime
import sqlite3

koef = 0

savienojums = sqlite3.connect("laiks.db")
kursors = savienojums.cursor()

class Pulkstenis:

    def __init__(self, stundas, minutes,sekundes):

        self.stundas=stundas
        self.minutes=minutes
        self.sekundes=sekundes

        kursors.execute('''CREATE TABLE IF NOT EXISTS laiks (
                    id INTEGER PRIMARY KEY,
                    stundas INT NOT NULL,
                    minutes INT NOT NULL,
                    sekundes INT NOT NULL)
                    ''')

    def ieslegts(self, stundas, minutes, sekundes):

        kursors.execute(f'''INSERT INTO visitors (stundas, minutes, sekundes)
            VALUES("{stundas}", "{minutes}", "{sekundes}",0)
            ''')




def stunda():
    koef=1
def minute():
    koef=1.08
def sekunde():
    koef=0.86

def time():
    tt = strftime('%H:%M:%S %p')
    a.config(text=tt)
    a.after(1000, time)

s=Pulkstenis(14,12,56)

def pievienot():

    sekundes = e_skaitlis1.get()
    minutes = e_skaitlis2.get()
    stundas = e_skaitlis3.get()

    nn= strftime(f'{stundas}H:{minutes}M:{sekundes}S %p')

def iestatit():
    sekundes = e_skaitlis1.get()
    minutes = e_skaitlis2.get()
    stundas = e_skaitlis3.get()




root = tk.Tk()

root.title("Laiks")
root.geometry("500x400")
root.resizable(0,0)

l_virsraksts = tk.Label(root, text='Stundas', font=(25), fg="red")
l_virsraksts.place(x=80, y=70)

l_virsraksts = tk.Label(root, text='Minūtes', font=(25), fg="red")
l_virsraksts.place(x=220, y=70)

l_virsraksts = tk.Label(root, text='Sekundes', font=(25), fg="red")
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


jaunais = tk.Label(root, text='Laiks: ', font=(25), fg="red")
jaunais.place(x=180, y=200)




    
a = tk.Label(root, font=('calibri', 25), fg="red")
a.place(x=140, y=300)




# l_virsraksts = tk.Label(root, text=f'Laiks{a}', font=(25), fg="red")
# l_virsraksts.place(x=220, y=300)

time()
root.mainloop()