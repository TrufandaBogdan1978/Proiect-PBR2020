from threading import Thread
from tkinter import *
import tkinter.messagebox
import random
from time import sleep
from pyswip import Prolog

prolog = Prolog()
prolog.consult("test.pl")
list(prolog.query("init."))

tk = Tk()
tk.title("PBR: Tic Tac Toe")
tk.iconbitmap("index.ico")
tk.geometry("1014x500+450+152")
tk.resizable(0, 0)

debug = True
game, game1 = 1, 1
bclick = True
flag = 0
win = False
moves_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]


def learn():
    # def local_learn():
    global moves_list, win, game1
    with open("../Prolog/games.csv", "r") as fd:
        for x in fd.readlines():
            reset()
            win = False
            x = x.strip("\n")
            move = x.split(", ")
            query = "learn({}).".format(move)
            list(prolog.query(query))
            txtOutput.insert(END, str(game1) + "." + " ")
            for y in range(len(move)):
                mov = move[y][0]
                play = move[y][1].upper()
                txtOutput.insert(END, str(mov) + str(play) + " ")
                if not win:
                    button_click(button_list[moves_list.index(mov)], play)
            txtOutput.insert(END, "\n")
            txtOutput.see(END)
            game1 += 1
            sleep(0.01)
    val = list(prolog.query("display(A)."))
    print("Val:\t", val[0]["A"])

    # c = Thread(target=local_learn)
    # c.start()


def generate():
    global win
    reset()
    lista = []
    index = random.randint(2, 4)
    for _ in range(index):
        poz = random.choice(button_list)
        if poz not in lista:
            lista.append(poz)
            button_click(poz)


def verify():
    listax = []
    lista0 = []
    for index, button in enumerate(button_list):
        if button["text"] == "X":
            listax.append("{}{}".format(moves_list[index], "x"))
        if button["text"] == "0":
            lista0.append("{}{}".format(moves_list[index], "0"))
    print(listax)
    print(lista0)

    lista_mare = []
    for x in range(min(len(listax), len(lista0))):
        lista_mare.append(listax[x])
        lista_mare.append(lista0[x])

    if len(listax) > len(lista0):
        lista_mare.append(listax[-1])
    elif len(listax) < len(lista0):
        lista_mare.append(lista0[-1])

    print(lista_mare)
    query = "verify({},V).".format(lista_mare)
    print(list(prolog.query(query)))


def button_click(buttons, player=None):
    global bclick, flag
    if buttons["text"] == " " and bclick:
        if player is None:
            player = "X"
        buttons["text"] = player
        bclick = False
        tk.title("PBR: Tic Tac Toe          Now Playing: 0")
        win_check()
        flag += 1

    elif buttons["text"] == " " and not bclick:
        if player is None:
            player = "0"
        buttons["text"] = player
        bclick = True
        tk.title("PBR: Tic Tac Toe          Now Playing: X")
        win_check()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")


def reset():
    global flag, win, bclick
    button1["text"] = button2["text"] = button3["text"] = button4["text"] = button5["text"] = button6["text"] = \
        button7["text"] = button8["text"] = button9["text"] = " "
    flag = 0
    win = True
    bclick = True


def fullreset():
    global game, game1
    reset()
    game, game1 = 1, 1
    txtOutput.delete('0.0', END)
    txtOutput1.delete('0.0', END)


def win_check():
    global game
    if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
            button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
            button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
            button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
            button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
            button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
            button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
        # tkinter.messagebox.showinfo("Tic-Tac-Toe", "X Won!")
        txtOutput1.insert(END, str(game) + "." + " " + "X Won!" + "\n")
        txtOutput1.see(END)
        game += 1
        reset()
        return True

    elif flag == 8:
        # tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
        txtOutput1.insert(END, str(game) + "." + " " + "Tie!\n")
        txtOutput1.see(END)
        game += 1
        reset()
        return True

    elif (button1["text"] == "0" and button2["text"] == "0" and button3["text"] == "0" or
          button4["text"] == "0" and button5["text"] == "0" and button6["text"] == "0" or
          button7["text"] == "0" and button8["text"] == "0" and button9["text"] == "0" or
          button1["text"] == "0" and button5["text"] == "0" and button9["text"] == "0" or
          button3["text"] == "0" and button5["text"] == "0" and button7["text"] == "0" or
          button1["text"] == "0" and button4["text"] == "0" and button7["text"] == "0" or
          button2["text"] == "0" and button5["text"] == "0" and button8["text"] == "0" or
          button3["text"] == "0" and button6["text"] == "0" and button9["text"] == "0"):
        # tkinter.messagebox.showinfo("Tic-Tac-Toe", "0 Won!")
        txtOutput1.insert(END, str(game) + "." + " " + "0 Won!" + "\n")
        txtOutput1.see(END)
        game += 1
        reset()
        return True
    return False


button1 = Button(tk, text=" ", font="Times 20 bold", bg="white", fg="black", height=4, width=8,
                 command=lambda: button_click(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=" ", font="Times 20 bold", bg="white", fg="black", height=4, width=8,
                 command=lambda: button_click(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=" ", font="Times 20 bold", bg="white", fg="black", height=4, width=8,
                 command=lambda: button_click(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=" ", font="Times 20 bold", bg="white", fg="black", height=4, width=8,
                 command=lambda: button_click(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=" ", font="Times 20 bold", bg="white", fg="black", height=4, width=8,
                 command=lambda: button_click(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=" ", font="Times 20 bold", bg="white", fg="black", height=4, width=8,
                 command=lambda: button_click(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=" ", font="Times 20 bold", bg="white", fg="black", height=4, width=8,
                 command=lambda: button_click(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=" ", font="Times 20 bold", bg="white", fg="black", height=4, width=8,
                 command=lambda: button_click(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=" ", font="Times 20 bold", bg="white", fg="black", height=4, width=8,
                 command=lambda: button_click(button9))
button9.grid(row=5, column=2)

button_list = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

buttonlearn = Button(tk, text="Learn", font="Times 12 bold", bg="red4", fg="white", height=2, width=10,
                     command=learn).place(x=23, y=445)

buttongenerate = Button(tk, text="Generate", font="Times 12 bold", bg="red4", fg="white", height=2, width=10,
                        command=generate).place(x=159, y=445)

buttongo = Button(tk, text="Verify", font="Times 12 bold", bg="red4", fg="white", height=2, width=10,
                  command=verify).place(x=290, y=445)

buttonreset = Button(tk, text="Reset", font="Times 12 bold", bg="red4", fg="white", height=2, width=10,
                     command=fullreset).place(x=845, y=333)

if debug:
    Label(tk, text="a", font="Times 10", bg="white").place(x=0, y=0)
    Label(tk, text="b", font="Times 10", bg="white").place(x=140, y=0)
    Label(tk, text="c", font="Times 10", bg="white").place(x=280, y=0)
    Label(tk, text="d", font="Times 10", bg="white").place(x=0, y=150)
    Label(tk, text="e", font="Times 10", bg="white").place(x=140, y=150)
    Label(tk, text="f", font="Times 10", bg="white").place(x=280, y=150)
    Label(tk, text="g", font="Times 10", bg="white").place(x=0, y=300)
    Label(tk, text="h", font="Times 10", bg="white").place(x=140, y=300)
    Label(tk, text="i", font="Times 10", bg="white").place(x=280, y=300)

Label(tk, text="Games", font="Times 15 bold", justify=RIGHT).place(x=450, y=30)
Label(tk, text="Wins", font="Times 15 bold").place(x=450, y=250)
txtFrame = Frame(tk, borderwidth=1, relief="sunken")
txtOutput = Text(txtFrame, wrap=NONE, height=10, width=58, borderwidth=0)
vscroll = Scrollbar(txtFrame, orient=VERTICAL, command=txtOutput.yview)
txtOutput["yscroll"] = vscroll.set

vscroll.pack(side="right", fill="y")
txtOutput.pack(side="left", fill="both", expand=True)

txtFrame.place(x=450, y=60)

txtFrame1 = Frame(tk, borderwidth=1, relief="sunken")
txtOutput1 = Text(txtFrame1, wrap=NONE, height=10, width=40, borderwidth=0)
vscroll1 = Scrollbar(txtFrame1, orient=VERTICAL, command=txtOutput1.yview)
txtOutput1["yscroll"] = vscroll1.set

vscroll1.pack(side="right", fill="y")
txtOutput1.pack(side="left", fill="both", expand=True)

txtFrame1.place(x=450, y=280)

tk.mainloop()
