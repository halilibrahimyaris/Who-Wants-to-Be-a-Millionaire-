from tkinter import *
import pygame
import MyGraph
import MyTel
from tkinter import messagebox


pygame.init()
root = Tk()
root.title("Kim Milyoner Olmak İster?")
root.geometry('1352x652+0+0')
root.configure(background='black')

Genel = Frame(root, bg='black')
Genel.grid()

genel1 = Frame(root, bg='black', bd=20, width=900, height=600)
genel1.grid(row=0, column=0)

genel2 = Frame(root, bg='black', bd=20, width=452, height=600)
genel2.grid(row=0, column=1)

genel1a = Frame(genel1, bg='black', bd=20, width=900, height=200)
genel1a.grid(row=0, column=0)
Genel1b= Frame(genel1, bg='black', bd=20, width=900, height=200)
Genel1b.grid(row=1, column=0)
Genel1c = Frame(genel1, bg='gray', bd=20, width=900, height=200)
Genel1c.grid(row=2, column=0)


# ----------------------------------------------------------------------

def lost():
    yeniEkran = Tk()
    yeniEkran.title("Oyun Bitti")
    yeniEkran.geometry('400x400+0+0')


def change50():
    canvas = Canvas(genel1a, bg='black', width=200, height=80)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    resim = PhotoImage(file='50X.png')
    canvas.create_image(100, 40, image=resim)
    canvas.image = resim
    yarıyarıya()


def changeSeyirci():
    canvas = Canvas(genel1a, bg='black', width=200, height=80)
    canvas.grid(row=0, column=1)
    canvas.delete("all")
    resim = PhotoImage(file='seyirci2.png')
    canvas.create_image(100, 40, image=resim)
    canvas.image = resim
    MyGraph.drawMyGraph()



def changeTel():
    canvas = Canvas(genel1a, bg='black', width=200, height=80)
    canvas.grid(row=0, column=2)
    canvas.delete("all")
    resim = PhotoImage(file='telefon2.png')
    canvas.create_image(100, 40, image=resim)
    canvas.image = resim




def ChangeMoneyTree1():
    tree = ['Picture1']
    for i in tree:
       canvas = Canvas(genel2, bg='black', width=430, height=600)
       canvas.grid(row=0, column=0)
       canvas.delete('all')
       resim = PhotoImage(file=i.title()+'.png')
       canvas.create_image(215, 300, image=resim)
       canvas.image = resim

def ChangeMoneyTree2():
    tree = ['Picture2']
    for i in tree:
       canvas = Canvas(genel2, bg='black', width=430, height=600)
       canvas.grid(row=0, column=0)
       canvas.delete('all')
       resim = PhotoImage(file=i.title()+'.png')
       canvas.create_image(215, 300, image=resim)
       canvas.image = resim


def ChangeMoneyTree3():
    tree = ['Picture3']
    for i in tree:
        canvas = Canvas(genel2, bg='black', width=430, height=600)
        canvas.grid(row=0, column=0)
        canvas.delete('all')
        resim = PhotoImage(file=i.title() + '.png')
        canvas.create_image(215, 300, image=resim)
        canvas.image = resim

def ChangeMoneyTree4():
    tree = ['Picture4']
    for i in tree:
       canvas = Canvas(genel2, bg='black', width=430, height=600)
       canvas.grid(row=0, column=0)
       canvas.delete('all')
       resim = PhotoImage(file=i.title()+'.png')
       canvas.create_image(215, 300, image=resim)
       canvas.image = resim
def ChangeMoneyTree5():
    tree = ['Picture5']
    for i in tree:
       canvas = Canvas(genel2, bg='black', width=430, height=600)
       canvas.grid(row=0, column=0)
       canvas.delete('all')
       resim = PhotoImage(file=i.title()+'.png')
       canvas.create_image(215, 300, image=resim)
       canvas.image = resim
def ChangeMoneyTree6():
    tree = ['Picture6']
    for i in tree:
       canvas = Canvas(genel2, bg='black', width=430, height=600)
       canvas.grid(row=0, column=0)
       canvas.delete('all')
       resim = PhotoImage(file=i.title()+'.png')
       canvas.create_image(215, 300, image=resim)
       canvas.image = resim
def ChangeMoneyTree7():
    tree = ['Picture7']
    for i in tree:
       canvas = Canvas(genel2, bg='black', width=430, height=600)
       canvas.grid(row=0, column=0)
       canvas.delete('all')
       resim = PhotoImage(file=i.title()+'.png')
       canvas.create_image(215, 300, image=resim)
       canvas.image = resim
def ChangeMoneyTree8():
    tree = ['Picture8']
    for i in tree:
       canvas = Canvas(genel2, bg='black', width=430, height=600)
       canvas.grid(row=0, column=0)
       canvas.delete('all')
       resim = PhotoImage(file=i.title()+'.png')
       canvas.create_image(215, 300, image=resim)
       canvas.image = resim
def ChangeMoneyTree9():
    tree = ['Picture9']
    for i in tree:
       canvas = Canvas(genel2, bg='black', width=430, height=600)
       canvas.grid(row=0, column=0)
       canvas.delete('all')
       resim = PhotoImage(file=i.title()+'.png')
       canvas.create_image(215, 300, image=resim)
       canvas.image = resim
def ChangeMoneyTree10():
    tree = ['Picture10']
    for i in tree:
       canvas = Canvas(genel2, bg='black', width=430, height=600)
       canvas.grid(row=0, column=0)
       canvas.delete('all')
       resim = PhotoImage(file=i.title()+'.png')
       canvas.create_image(215, 300, image=resim)
       canvas.image = resim
def ChangeMoneyTree11():
    tree = ['Picture11']
    for i in tree:
       canvas = Canvas(genel2, bg='black', width=430, height=600)
       canvas.grid(row=0, column=0)
       canvas.delete('all')
       resim = PhotoImage(file=i.title()+'.png')
       canvas.create_image(215, 300, image=resim)
       canvas.image = resim
def ChangeMoneyTree12():
    tree = ['Picture12']
    for i in tree:
       canvas = Canvas(genel2, bg='black', width=430, height=600)
       canvas.grid(row=0, column=0)
       canvas.delete('all')
       resim = PhotoImage(file=i.title()+'.png')
       canvas.create_image(215, 300, image=resim)
       canvas.image = resim


def yarıyarıya():
    txtSoru1 = Label(Genel1c, font=('arial', 14, 'bold'), bg='gray', fg='white', bd=5, width=17, height=2,
                     justify=CENTER, textvariable="")
    txtSoru1.grid(row=1, column=1, pady=4)
    txtSoru3 = Label(Genel1c, font=('arial', 14, 'bold'), bg='gray', fg='white', bd=1, width=17, height=2,
                     justify=CENTER, textvariable="")
    txtSoru3.grid(row=2, column=1, pady=4)


def cekil():
    if messagebox.askokcancel("Quit", "Son kararınız mı?"):
        root.destroy()
        MyGraph.cekil()

def yanlis():
    i=1
    if i == 1:
        root.destroy()
        MyGraph.yanlis()


    # ---------------------------------------------------------------------------------


Logo= PhotoImage(file='milyoner.png')
LogoCentre = Label(Genel1b, image=Logo, bg='black', width=300, height=200)
LogoCentre.grid()

Resim_50 = PhotoImage(file='50.png')
yeni50 = Button(genel1a, image=Resim_50, bg='black', width=200, height=80, command=change50)
yeni50.grid(row=0, column=0)

Resim_seyirci = PhotoImage(file='seyirci.png')
yeni50 = Button(genel1a, image=Resim_seyirci, bg='black', width=200, height=80, command=changeSeyirci)
yeni50.grid(row=0, column=1)

Resim_telefon = PhotoImage(file='telefon.png')
yeni50 = Button(genel1a, image=Resim_telefon, bg='black', width=200, height=80, command=changeTel)
yeni50.grid(row=0, column=2)

Resim_cekil = PhotoImage(file='çekil.png')
yeni50 = Button(genel1a, image=Resim_cekil, bg='black', width=200, height=80, command=cekil)
yeni50.grid(row=0, column=3)


Moneytree = PhotoImage(file='Picture01.png')
montree = Label(genel2, image=Moneytree, bg='black', width=430, height=600)
montree.grid(row=0, column=0)
# -------------------------------------------------------------
Soru = StringVar()

Cevap1 = StringVar()
Cevap2 = StringVar()
Cevap3 = StringVar()
Cevap4 = StringVar()
Soru.set("Türkiyenin Başkenti Neresidir?")
Cevap1.set("Sivas")
Cevap2.set("İstanbul")
Cevap3.set("Bursa")
Cevap4.set("Ankara")
ChangeMoneyTree1()
def Soru1():
        Soru.set("Izafiyet Teorisi kime aittir?")
        Cevap1.set("A.Einstein")
        Cevap2.set("Newton")
        Cevap3.set("Maxwell")
        Cevap4.set("Marie Curie")
        ChangeMoneyTree2()

def Soru2():
    Soru.set("Türkiye Cumhuriyetinin kuruluş tarihi kaçtır?")
    Cevap1.set("1071")
    Cevap2.set("1923")
    Cevap3.set("1881")
    Cevap4.set("1920")
    ChangeMoneyTree3()
def Soru3():
    Soru.set("Mustafa Kemal Atatürk’ün Nüfusa Kayıtlı Olduğu İl Hangisidir?")
    Cevap1.set("Sivas")
    Cevap2.set("Bursa")
    Cevap3.set("Gaziantep")
    Cevap4.set("Ankara")
    ChangeMoneyTree4()
def Soru4():
    Soru.set("Hangisi ile 333 topanırsa sonuç 1000 eder?")
    Cevap1.set("666")
    Cevap2.set("777")
    Cevap3.set("667")#
    Cevap4.set("787")
    ChangeMoneyTree5()
def Soru5():
    Soru.set("Aşağıdakilerden Hangisi Dünya Sağlık Örgütünün Kısaltılmış İsmidir? ")
    Cevap1.set("WHO")#
    Cevap2.set("BM")
    Cevap3.set("UNESCO")
    Cevap4.set("UNİCEF")
    ChangeMoneyTree6()

def Soru6():
    Soru.set("Bir Gün Kaç Saniyedir? ")
    Cevap1.set("12345")
    Cevap2.set("86520")
    Cevap3.set("84200")
    Cevap4.set("86400")#
    ChangeMoneyTree7()
def Soru7():
    Soru.set(" Avrupa Birliği'nin başkenti neresidir?")
    Cevap1.set("Berlin")
    Cevap2.set("Londra")
    Cevap3.set("Brüksel")#
    Cevap4.set("Oslo")
    ChangeMoneyTree8()
def Soru8():
    Soru.set("Aşağıdakilerden  hangisi bir yazılım dili değildir?")
    Cevap1.set("R")
    Cevap2.set("Java")
    Cevap3.set("Python")
    Cevap4.set("V")#
    ChangeMoneyTree9()
def Soru9():
    Soru.set("Malazgirt savaşı kaç yılında yapılmıştır?")
    Cevap1.set("1071")#
    Cevap2.set("1299")
    Cevap3.set("1041")
    Cevap4.set("1453")
    ChangeMoneyTree10()
def Soru10():
    Soru.set("Her yüz yılda 7 cm yere yaklaşan Pisa Kulesi hangi yöne doğru eğilmektedir?")
    Cevap1.set("Batı")
    Cevap2.set("Doğu")#
    Cevap3.set("Kuzey")
    Cevap4.set("Güney")
    ChangeMoneyTree11()
def Soru11():
    Soru.set("3+5")
    Cevap1.set("5")
    Cevap2.set("15")
    Cevap3.set("8")
    Cevap4.set("6")
    ChangeMoneyTree12()



def soruSor():
    lblSoru = Label(Genel1c, font=('arial', 14, 'bold'), bg='gray', fg='white', bd=5, width=44, justify=CENTER,
                    textvariable=Soru)
    lblSoru.grid(row=0, column=0, columnspan=4, pady=4)

    lblSoruA = Label(Genel1c, font=('arial', 14, 'bold'), text='A:', bg='black', fg='white', bd=5, width=0,
                     justify=CENTER)
    lblSoruA.grid(row=1, column=0, pady=4, sticky=W)

    txtSoru1 = Button(Genel1c, font=('arial', 14, 'bold'), bg='gray', fg='white', bd=5, width=17, height=2,
                      justify=CENTER,
                      textvariable=Cevap1,command=Soru2)
    txtSoru1.grid(row=1, column=1, pady=4)

    lblSoruB = Label(Genel1c, font=('arial', 14, 'bold'), text='B:', bg='black', fg='white', bd=5, width=0,
                     justify=LEFT)
    lblSoruB.grid(row=1, column=2, pady=4, sticky=W)

    txtSoru2 = Button(Genel1c, font=('arial', 14, 'bold'), bg='gray', fg='white', bd=1, width=17, height=2,
                      justify=CENTER,
                      textvariable=Cevap2,command=lambda:[Soru3()])
    txtSoru2.grid(row=1, column=3, pady=4)

    lblSoruC = Label(Genel1c, font=('arial', 14, 'bold'), text='C:', bg='black', fg='white', bd=5, width=0,
                     justify=LEFT)
    lblSoruC.grid(row=2, column=0, pady=4, sticky=W)

    txtSoru3 = Button(Genel1c, font=('arial', 14, 'bold'), bg='gray', fg='white', bd=1, width=17, height=2,
                      justify=CENTER,textvariable=Cevap3,command=lambda:[Soru4, soruSor2()])
    txtSoru3.grid(row=2, column=1, pady=4)

    lblSoruD = Label(Genel1c, font=('arial', 14, 'bold'), text='D:', bg='black', fg='white', bd=5, width=0,
                     justify=LEFT)
    lblSoruD.grid(row=2, column=2, pady=4, sticky=W)

    txtSoru4 = Button(Genel1c, font=('arial', 14, 'bold'), bg='gray', fg='white', bd=1, width=17, height=2,
                      justify=CENTER,
                      textvariable=Cevap4,command=Soru1)
    txtSoru4.grid(row=2, column=3, pady=4)


def soruSor2():
    lblSoru = Label(Genel1c, font=('arial', 14, 'bold'), bg='gray', fg='white', bd=5, width=44, justify=CENTER,
                    textvariable=Soru)
    lblSoru.grid(row=0, column=0, columnspan=4, pady=4)

    lblSoruA = Label(Genel1c, font=('arial', 14, 'bold'), text='A:', bg='black', fg='white', bd=5, width=0,
                     justify=CENTER)
    lblSoruA.grid(row=1, column=0, pady=4, sticky=W)

    txtSoru5 = Button(Genel1c, font=('arial', 14, 'bold'), bg='gray', fg='white', bd=5, width=17, height=2,
                      justify=CENTER,
                      textvariable=Cevap1,command=Soru6)
    txtSoru5.grid(row=1, column=1, pady=4)

    lblSoruB = Label(Genel1c, font=('arial', 14, 'bold'), text='B:', bg='black', fg='white', bd=5, width=0,
                     justify=LEFT)
    lblSoruB.grid(row=1, column=2, pady=4, sticky=W)

    txtSoru6 = Button(Genel1c, font=('arial', 14, 'bold'), bg='gray', fg='white', bd=1, width=17, height=2,
                      justify=CENTER,
                      textvariable=Cevap2,command=Soru4())
    txtSoru6.grid(row=1, column=3, pady=4)

    lblSoruC = Label(Genel1c, font=('arial', 14, 'bold'), text='C:', bg='black', fg='white', bd=5, width=0,
                     justify=LEFT)
    lblSoruC.grid(row=2, column=0, pady=4, sticky=W)

    txtSoru7 = Button(Genel1c, font=('arial', 14, 'bold'), bg='gray', fg='white', bd=1, width=17, height=2,
                      justify=CENTER,textvariable=Cevap3,command=Soru5)
    txtSoru7.grid(row=2, column=1, pady=4)

    lblSoruD = Label(Genel1c, font=('arial', 14, 'bold'), text='D:', bg='black', fg='white', bd=5, width=0,
                     justify=LEFT)
    lblSoruD.grid(row=2, column=2, pady=4, sticky=W)

    txtSoru8 = Button(Genel1c, font=('arial', 14, 'bold'), bg='gray', fg='white', bd=1, width=17, height=2,
                      justify=CENTER,
                      textvariable=Cevap4,command=lambda:[Soru7(), soruSor3()])
    txtSoru8.grid(row=2, column=3, pady=4)

def soruSor3():
    lblSoru = Label(Genel1c, font=('arial', 14, 'bold'), bg='gray', fg='white', bd=5, width=44, justify=CENTER,
                    textvariable=Soru)
    lblSoru.grid(row=0, column=0, columnspan=4, pady=4)

    lblSoruA = Label(Genel1c, font=('arial', 14, 'bold'), text='A:', bg='black', fg='white', bd=5, width=0,
                     justify=CENTER)
    lblSoruA.grid(row=1, column=0, pady=4, sticky=W)

    txtSoru9 = Button(Genel1c, font=('arial', 14, 'bold'), bg='gray', fg='white', bd=5, width=17, height=2,
                      justify=CENTER,
                      textvariable=Cevap1,command=Soru10)
    txtSoru9.grid(row=1, column=1, pady=4)

    lblSoruB = Label(Genel1c, font=('arial', 14, 'bold'), text='B:', bg='black', fg='white', bd=5, width=0,
                     justify=LEFT)
    lblSoruB.grid(row=1, column=2, pady=4, sticky=W)

    txtSoru10 = Button(Genel1c, font=('arial', 14, 'bold'), bg='gray', fg='white', bd=1, width=17, height=2,
                      justify=CENTER,
                      textvariable=Cevap2,command=lambda:[Soru11(),yanlis()])
    txtSoru10.grid(row=1, column=3, pady=4)

    lblSoruC = Label(Genel1c, font=('arial', 14, 'bold'), text='C:', bg='black', fg='white', bd=5, width=0,
                     justify=LEFT)
    lblSoruC.grid(row=2, column=0, pady=4, sticky=W)

    txtSoru11 = Button(Genel1c, font=('arial', 14, 'bold'), bg='gray', fg='white', bd=1, width=17, height=2,
                      justify=CENTER,textvariable=Cevap3,command=Soru8)
    txtSoru11.grid(row=2, column=1, pady=4)

    lblSoruD = Label(Genel1c, font=('arial', 14, 'bold'), text='D:', bg='black', fg='white', bd=5, width=0,
                     justify=LEFT)
    lblSoruD.grid(row=2, column=2, pady=4, sticky=W)

    txtSoru12 = Button(Genel1c, font=('arial', 14, 'bold'), bg='gray', fg='white', bd=1, width=17, height=2,
                      justify=CENTER,
                      textvariable=Cevap4,command=lambda:[Soru9()])
    txtSoru12.grid(row=2, column=3, pady=4)


# -------------------------------------------------------------

soruSor()
root.protocol("WM_DELETE_WINDOW", cekil())
root.mainloop()
