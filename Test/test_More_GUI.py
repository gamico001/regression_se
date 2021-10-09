# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as tk

home_gui = tk.Tk()
graph_gui = tk.Tk()


def home_button1_action():
    print('primo estratto!')
    home_gui.deiconify()
    graph_gui.deiconify()


def home_button2_action():
    print('secondo estratto!')


def graph_button1_action():
    graph_gui.deiconify()
    home_gui.deiconify()


# controls...
home_button1 = tk.Button(home_gui, text='primo estratto', command=home_button1_action).pack()
home_button2 = tk.Button(home_gui, text='secondo estratto', command=home_button2_action).pack()
home_button3 = tk.Button(home_gui, text='Exit', command=quit).pack()
graph_button1 = tk.Button(graph_gui, text='Exit', command=graph_button1_action).pack()

home_gui.title('Home')
home_gui.geometry('300x200+10+10')

graph_gui.title('Graph')
graph_gui.geometry('300x200+10+10')
graph_gui.deiconify()

home_gui.mainloop()

