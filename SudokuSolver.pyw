import numpy as np
from tkinter import *

def funcSolve():
    global grid, plid
    grid = np.zeros(81).reshape(9,9)

    for m in range(9):
        for n in range(9):
            if gVar["gvar{0}{1}".format(m, n)].get() == "":
                grid[m][n] = 0
            else:
                grid[m][n] = gVar["gvar{0}{1}".format(m, n)].get()

    plid = grid

    def possible(row, column, number):
        global grid
        # Is the number appearing in the given row?
        for i in range(0, 9):
            if grid[row][i] == number:
                return False

        # Is the number appearing in the given column?
        for i in range(0, 9):
            if grid[i][column] == number:
                return False

        # Is the number appearing in the given square?
        x0 = (column // 3) * 3
        y0 = (row // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if grid[y0 + i][x0 + j] == number:
                    return False

        return True


    def solve():
        global grid, plid
        for row in range(0, 9):
            for column in range(0, 9):
                if grid[row][column] == 0:
                    for number in range(1, 10):
                        if possible(row, column, number):
                            grid[row][column] = number
                            solve()
                            grid[row][column] = 0

                    return

        for s in range(9):
            for d in range(9):
                if gVar["gvar{0}{1}".format(s, d)].get() == "":
                    board["e{0}{1}".format(s, d)].config(fg="black")
                    gVar["gvar{0}{1}".format(s, d)].set(f"{grid[s][d]}"[0])
                if plid[s][d] == 0:
                    board["e{0}{1}".format(s, d)].configure(fg="black")


    solve()

    cas.configure(text="The Sudoku is Solved!")



def funcClear():
    cas.configure(text="")
    for i in range(9):
        for j in range(9):
            gVar["gvar{0}{1}".format(i, j)].set("")



board = {}
gVar = {}

if __name__ == "__main__":
    root = Tk()
    root.geometry("335x439")
    root.title("Sudoku Solver")

    f1 = Frame(root, bg="white")
    f1.pack(side=TOP, fill=X)

    fint = Frame(f1, bg="white")
    fint.pack(side=TOP, fill=X)

    Label(fint, text="Welcome To Sudoku Solver", bg="white", font="Arial 15 bold").pack(side=TOP, anchor="center",
                                                                                        pady=5)

    cas = Label(fint, text="", bg="white", font="Arial 9 bold", fg="green")
    cas.pack(side=TOP, anchor="center")

    fGrids = Frame(f1, bg="white")
    fGrids.pack(side=TOP, fill=X, pady=10, padx=10)

    for i in range(9):
        for j in range(9):
            backcol = "#D0ffff"

            if i // 3 == 1 and j // 3 == 1:
                backcol = "#D0ffff"
            elif i // 3 == 1 or j // 3 == 1:
                backcol = "#ffffd0"
            else:
                backcol = "#D0ffff"

            gVar["gvar{0}{1}".format(i, j)] = StringVar()
            board["e{0}{1}".format(i, j)] = Entry(fGrids, textvariable=gVar["gvar{0}{1}".format(i, j)], width=3,
                                                  justify=CENTER, bg=backcol, fg="red", font="Arial 13 bold")
            board["e{0}{1}".format(i, j)].grid(row=i, column=j, padx=2, pady=2, ipady=3)


    fButton = Frame(f1, bg="white")
    fButton.pack(side=TOP, fill=X, padx=50, pady=10)

    keySolve = Button(fButton, text="SOLVE", command=funcSolve, bg="green", fg="white", font="Arial 10 bold")
    keySolve.pack(side=LEFT, anchor="nw", ipadx=5, ipady=2)

    keyClear = Button(fButton, text="CLEAR", command=funcClear, bg="green", fg="white", font="Arial 10 bold")
    keyClear.pack(side=RIGHT, anchor="ne", ipadx=5, ipady=2)

    f3 = Frame(f1, bg="white", height=10)
    f3.pack(side=TOP, fill=X)






    root.mainloop()