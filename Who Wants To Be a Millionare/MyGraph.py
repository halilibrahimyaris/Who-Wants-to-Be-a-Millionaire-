import matplotlib, numpy
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk

def drawMyGraph():
    root = Tk.Tk()
    root.title('Seyirci Jokeri')
    f = Figure(figsize=(5,4), dpi=100)
    ax = f.add_subplot(111)

    data = (10, 25, 30, 35,100)

    ind =['A','B','C','D','Total']
    width = .5

    rects1 = ax.bar(ind, data, width)

    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
    Tk.mainloop()
def cekil():
    root = Tk.Tk()
    image1 = Tk.PhotoImage(file="basta.png")
    w = image1.width()
    h = image1.height()
    root.geometry("%dx%d+0+0" % (w, h))

    panel1 = Tk.Label(root, image=image1)
    panel1.pack(side='top', fill='both', expand='yes')

    panel1.image = image1
    Tk.mainloop()
def yanlis():
    root = Tk.Tk()
    image1 = Tk.PhotoImage(file="Adsiz.png")
    w = image1.width()
    h = image1.height()
    root.geometry("%dx%d+0+0" % (w, h))

    panel1 = Tk.Label(root, image=image1)
    panel1.pack(side='top', fill='both', expand='yes')

    panel1.image = image1
    Tk.mainloop()
