from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.title('my game:)')

click = True


def do_move(button):
    global click
    if button['text'] == ' ' and click is True:
        button['text'] = 'X'
        check_win()
        click = False
    elif button['text'] == ' ' and click is False:
        button['text'] = '0'
        check_win()
        click = True


def check_win():
    if button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or \
            button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or \
            button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or \
            button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or \
            button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or \
            button1['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or \
            button3['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or \
            button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X':
        mess = 'X-winner!!!'
        final_result(mess)

    elif button1['text'] == '0' and button2['text'] == '0' and button3['text'] == '0' or \
            button4['text'] == '0' and button5['text'] == '0' and button6['text'] == '0' or \
            button7['text'] == '0' and button8['text'] == '0' and button9['text'] == '0' or \
            button1['text'] == '0' and button4['text'] == '0' and button7['text'] == '0' or \
            button2['text'] == '0' and button5['text'] == '0' and button8['text'] == '0' or \
            button1['text'] == '0' and button6['text'] == '0' and button9['text'] == '0' or \
            button3['text'] == '0' and button5['text'] == '0' and button9['text'] == '0' or \
            button3['text'] == '0' and button5['text'] == '0' and button7['text'] == '0':
        mess = '0-winner'
        final_result(mess)
    else:
        check_draw()


def final_result(message):
    message_for_user = messagebox.askyesno('Game over!!!', f'{message}')
    if message_for_user:
        button1['text'] = ' '
        button2['text'] = ' '
        button3['text'] = ' '
        button4['text'] = ' '
        button5['text'] = ' '
        button6['text'] = ' '
        button7['text'] = ' '
        button8['text'] = ' '
        button9['text'] = ' '
    else:
        tk.destroy()


def check_draw():
    if button1['text'] != ' ' and button2['text'] != ' ' and button3['text'] != ' ' and button4['text'] != ' ' \
            and button5['text'] != ' ' and button6['text'] != ' ' and button7['text'] != ' ' and button8['text'] != ' ':
        mess = 'This is Draw!!!'


buttons = StringVar()

button1 = Button(tk, text=' ', font='Times 26 bold', width=8, height=6, command=lambda: do_move(button1))
button1.grid(row=0, column=0)
button2 = Button(tk, text=' ', font='Times 26 bold', width=8, height=6, command=lambda: do_move(button2))
button2.grid(row=0, column=1)
button3 = Button(tk, text=' ', font='Times 26 bold', width=8, height=6, command=lambda: do_move(button3))
button3.grid(row=0, column=2)
button4 = Button(tk, text=' ', font='Times 26 bold', width=8, height=6, command=lambda: do_move(button4))
button4.grid(row=1, column=0)
button5 = Button(tk, text=' ', font='Times 26 bold', width=8, height=6, command=lambda: do_move(button5))
button5.grid(row=1, column=1)
button6 = Button(tk, text=' ', font='Times 26 bold', width=8, height=6, command=lambda: do_move(button6))
button6.grid(row=1, column=2)
button7 = Button(tk, text=' ', font='Times 26 bold', width=8, height=6, command=lambda: do_move(button7))
button7.grid(row=2, column=0)
button8 = Button(tk, text=' ', font='Times 26 bold', width=8, height=6, command=lambda: do_move(button8))
button8.grid(row=2, column=1)
button9 = Button(tk, text=' ', font='Times 26 bold', width=8, height=6, command=lambda: do_move(button9))
button9.grid(row=2, column=2)

tk.mainloop()
