"""
GUI for regression model
"""
import tkinter
from tkinter import *
from tkinter import filedialog
import home_controller

# creating the application main window.
home = Tk()

# home dimensions  & position...
home.title("Regression")
window_width = 500
window_height = 500
# home.geometry("400x400")
home.resizable(True, True)

# get the screen dimension
screen_width = home.winfo_screenwidth()
screen_height = home.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
home.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# always on top...
home.attributes('-topmost', 1)

# configure grid...
home.columnconfigure(0, weight=1)
home.columnconfigure(1, weight=2)

width_col_left = 35

# -----------
# RIGA 0...
# -----------

# button load...
load_button = tkinter.Button(
    home,
    text="Load",
    width=5,
    command=lambda: call_for_load_file()
)
load_button.grid(column=0, row=0, padx=5, pady=5, ipadx=10, ipady=5)

# file path control...
file_data = tkinter.StringVar()
file_path = tkinter.Entry(
    home,
    textvariable=file_data,
    width=width_col_left
)
file_path.grid(column=1, row=0, padx=5, pady=5)

browser_files = tkinter.Button(
    home,
    text='Search',
    width=5,
    command=lambda: dialog_file_choice()
)
browser_files.grid(column=2, row=0, padx=5, pady=5, ipadx=10, ipady=5)

# ----------
# RIGA 1...
# ----------

# radio button for Regression type...
regression_type_label = tkinter.Label(text='Type:')
regression_type_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)
regression_type_selected = tkinter.StringVar()
type_radio_button_1 = tkinter.Radiobutton(home, text='Linear', value='L', variable=regression_type_selected)
type_radio_button_2 = tkinter.Radiobutton(home, text='Polynomial 2', value='P2',
                                          variable=regression_type_selected)
type_radio_button_3 = tkinter.Radiobutton(home, text='polynomial 3', value='P3',
                                          variable=regression_type_selected)
type_radio_button_1.grid(column=0, row=2, sticky=tkinter.W, padx=5, pady=5)
type_radio_button_2.grid(column=0, row=3, sticky=tkinter.W, padx=5, pady=5)
type_radio_button_3.grid(column=0, row=4, sticky=tkinter.W, padx=5, pady=5)

# R2 Coefficient of determination...
r2_label = tkinter.Label(text='R2 Coeff. of determination:')
r2_label.grid(column=1, row=1, padx=5, pady=5)
r2_text = tkinter.Text(home,
                       height=1,
                       width=35
                       )
r2_text.insert('1.0', 'to calculate...')
r2_text.grid(column=1, row=2, padx=5, pady=5)

# Intercept...
intercept_label = tkinter.Label(text='Intercept:')
intercept_label.grid(column=1, row=3, padx=5, pady=5)
intercept_text = tkinter.Text(home,
                              height=1,
                              width=35
                              )
intercept_text.insert('1.0', 'to calculate...')
intercept_text.grid(column=1, row=4, padx=5, pady=5)

# Coefficient...
coefficient_label = tkinter.Label(text='Coefficient:')
coefficient_label.grid(column=1, row=5, padx=5, pady=5)
coefficient_text = tkinter.Text(home,
                                height=1,
                                width=35
                                )
coefficient_text.insert('1.0', 'to calculate...')
coefficient_text.grid(column=1, row=6, padx=5, pady=5)

# Predict input...
predict_input_label = tkinter.Label(text='Predict input:')
predict_input_label.grid(column=1, row=7, padx=5, pady=5)
predict_input_text = tkinter.Text(home,
                                  height=1,
                                  width=35
                                  )
predict_input_text.insert('1.0', 'to calculate...')
predict_input_text.grid(column=1, row=8, padx=5, pady=5)

# Predict output...
predict_output_label = tkinter.Label(text='Predict output:')
predict_output_label.grid(column=1, row=9, padx=5, pady=5)
predict_output_text = tkinter.Text(home,
                                   height=1,
                                   width=35
                                   )
predict_output_text.insert('1.0', 'to calculate...')
predict_output_text.grid(column=1, row=10, padx=5, pady=5)

# Calc button...
calc_button = tkinter.Button(
    home,
    text="Calc",
    width=5,
    command=lambda: home_controller.calc_linear_regression()
)
calc_button.grid(column=0, row=5, padx=5, pady=5, ipadx=10, ipady=5)

# Graph button...
graph_button = tkinter.Button(
    home,
    text="Graph",
    width=5,
    command=lambda: home_controller.graph_regression()
)
graph_button.grid(column=0, row=6, padx=5, pady=5, ipadx=10, ipady=5)

# message field...
msg = tkinter.Text(home,
                   height=1,
                   width=40
                   )
msg.insert('1.0', 'messaggio...')
msg.grid(column=1, row=11, sticky=tkinter.S, padx=5, pady=5)

# Exit button...
exit_button = tkinter.Button(
    home,
    text="Exit",
    width=5,
    command=lambda: exit_click()
)
exit_button.grid(column=0, row=12, padx=5, pady=5, ipadx=10, ipady=5)


# Exit click...
def exit_click():
    quit(0)


# Load file data...
def call_for_load_file():
    msg.delete('1.0', END)
    msg.insert('1.0', home_controller.load_click(file_data.get()))


# select file...
def dialog_file_choice():
    # hide home panel...
    home.attributes('-alpha', 0)
    # Choice file data...
    file_select = tkinter.filedialog.askopenfilename(
        initialdir='/Users/giorgio/Library/Mobile Documents/com~apple~CloudDocs/WORKSPACES/Superenalotto/',
        title='scegliere il file dei dati',
        filetypes=[('Execl files', '*.xlsx'), ('CSV files', '*.csv')]
    )
    file_path.insert(1, file_select)
    home.attributes('-alpha', 1.0)


# Entering the event main loop
home.mainloop()
