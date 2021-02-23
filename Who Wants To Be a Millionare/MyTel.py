
from tkinter import *
import MyGraph
from PIL import ImageTk, Image
import pygame
import os

os.getcwd()
pygame.init()
def telefonRehberi():
    root = Tk()
    root.title("Rehberiniz")
    root.geometry('900x800')
    root.configure(background='black')

    resimler = Frame(root, bg='black', bd=40, width=452, height=600)
    resimler.grid(row=0, column=0)
    kisi1= Frame(resimler, bg='black', bd=40, width=400, height=150)
    kisi1.grid(row=0, column=0)
    kisi2 = Frame(resimler, bg='black', bd=40, width=400, height=150)
    kisi2.grid(row=1, column=0)
    kisi3 = Frame(resimler, bg='black', bd=40, width=400, height=150)
    kisi3.grid(row=2, column=0)

    butonlar = Frame(root, bg='black', bd=20, width=452, height=600)
    butonlar.grid(row=0, column=1)
    buton1= Frame(butonlar, bg='black', bd=40, width=400, height=150)
    buton1.grid(row=0, column=0)
    buton2 = Frame(butonlar, bg='black', bd=40, width=400, height=150)
    buton2.grid(row=1, column=0)
    buton3 = Frame(butonlar, bg='black', bd=40, width=400, height=150)
    buton3.grid(row=2, column=0)
    #--------------------------------------------------------------------------------
    Resim_ilber = PhotoImage(file='ilbe.png')
    yeniilber = Label(kisi1, image=Resim_ilber, bg='black', width=400, height=150)
    yeniilber.grid(row=0, column=0)
    Resim_celal= PhotoImage(file='celalSengor.png')
    yenicelal = Label(kisi2, image=Resim_celal, bg='black', width=400, height=150)
    yenicelal.grid(row=0, column=0)
    Resim_murat = PhotoImage(file='muratbardakci.png')
    yenimurat = Label(kisi3, image=Resim_murat, bg='black', width=400, height=150)
    yenimurat.grid(row=0, column=0)

    #----------------------------------------------------------------------------------
    Resim_telefon1 = PhotoImage(file='telefon.png')
    yeni50 = Button(buton1, image=Resim_telefon1, bg='black', width=200, height=150)
    yeni50.grid(row=0, column=0)
    Resim_telefon2 = PhotoImage(file='telefon.png')
    yeni50 = Button(buton2, image=Resim_telefon2, bg='black', width=200, height=150)
    yeni50.grid(row=0, column=0)
    Resim_telefon3 = PhotoImage(file='telefon.png')
    yeni50 = Button(buton3, image=Resim_telefon3, bg='black', width=200, height=150)
    yeni50.grid(row=0, column=0)

    root.mainloop()
#telefonRehberi()
def mainPage():


    root = Tk()

    canvas = Canvas(root, width=1200, height=720)

    image = ImageTk.PhotoImage(Image.open("baslangic.png"))

    canvas.create_image(0, 0, anchor=NW, image=image)

    button1 = Button(root, text="   Oyuna başla" ,font=('arial', 25, 'bold'),bg='gray', fg='white', anchor=W)
    button1.configure(width=12,height=5, activebackground="#33B5E5", relief=FLAT)
    button1_window = canvas.create_window(500, 400, anchor=NW, window=button1)
    canvas.pack()

    root.mainloop()
