import tkinter as tk
import random
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Canvas 6")
platno = tk.Canvas(root, width=400, height=900)
platno.pack()
platno.focus_set()

panenka_img = ImageTk.PhotoImage(Image.open("panenka.png").resize((150,150)))
platno.create_image(200, 75, image=panenka_img)


start_x = 175
start_y = 750
hrac_velikost = 50

hrac_img = ImageTk.PhotoImage(Image.open("hrac.jpg").resize((50,50)))
hrac = platno.create_image(start_x, start_y, image=hrac_img, anchor="nw")

cil_y = 155
platno.create_line(0, cil_y, 400, cil_y, fill="red", dash=(4, 4))

semafor = platno.create_oval(275, 50, 325, 100, fill="green")
semafor_je_zelena = True

hra_bezi = True

def zmena_svetla():
    global semafor_je_zelena
    if hra_bezi:
        semafor_je_zelena = not semafor_je_zelena
        barva = "green" if semafor_je_zelena else "red"
        platno.itemconfig(semafor, fill=barva)
        root.after(random.randint(1000, 5000), zmena_svetla)

def pohyb_hrace(event):
    if hra_bezi and semafor_je_zelena:
        platno.move(hrac, 0, -20)
        kontrola_vyhry()
    else:
        konec_hry("gameover")

def kontrola_vyhry():
    x1, y1 = platno.coords(hrac)
    if y1 <= cil_y:
        konec_hry("vitez")

def konec_hry(stav):
    global hra_bezi
    hra_bezi = False
    if (stav == "vitez"):
        platno.create_text(200, 400, text="VYHRAL JSI", font=("Arial", 28), fill="green")
    elif (stav == "gameover"):
        platno.create_text(200, 400, text="GAME OVER", font=("Arial", 28), fill="red")

platno.bind("<Up>", pohyb_hrace)
platno.bind("w", pohyb_hrace)

zmena_svetla()

root.mainloop()