import math
from tkinter import *
def lol():
	xx1 = Label(window)
	xx1.grid(column=0, row=5)
	xx2 = Label(window)
	xx2.grid(column=0, row=6)
	xx1.configure(text="-----------------------")
	xx2.configure(text="-----------------------")
	ai = format(a.get())
	ai = int(ai)
	bi = format(b.get())
	bi = int(bi)
	ci = format(c.get())
	ci = int(ci)
	di = bi*bi-4*ai*ci
	print(di)
	if(di >= 0):
		oi = -1*bi
		x1 = (oi+math.sqrt(di))/2*ai
		x2 = (oi-math.sqrt(di))/2*ai
		xxx1 = "Первый корень: {}".format(x1)
		xxx2 = "Первый корень: {}".format(x2)
		xx1.configure(text=xxx1)
		xx2.configure(text=xxx2)
	else:
		windowerr = Tk()
		error = Label(windowerr, text="Нет корней!")
		error.grid(column=0, row=0)
window = Tk()
window.title("Ебаный килькилятор V2.1 for KWANTER-INC")
window.geometry('350x150')
lbl = Label(window, text="Коэффицент A:")
lbl.grid(column=0, row=0)
a = Entry(window, width=10)
a.grid(column=1, row=0)
lbl2 = Label(window, text="Коэффицент B:")
lbl2.grid(column=0, row=1)
b = Entry(window, width=10)
b.grid(column=1, row=1)
lbl3 = Label(window, text="Коэффицент C:")
lbl3.grid(column=0, row=2)
c = Entry(window, width=10)
c.grid(column=1, row=2)
btn = Button(window, text="Вычислть", command=lol)
btn.grid(column=3, row=6)
window.mainloop()
