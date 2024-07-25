from tkinter import *
from tkinter.messagebox import *

#
# TODO : make the code beautiful (the code is functional but not pretty)
# TODO : error handling


def ice_calulator(nb_ice: int, ice_mining_speed_list: list[list[tuple]]) -> float:
    ice_mining_speed: float = 0
    for speed in harvest_calculation(ice_mining_speed_list):
        ice_mining_speed += speed

    time_for_ice: float = (nb_ice / ice_mining_speed)
    return time_for_ice/3600


def harvest_calculation(ice_harvester_list: list[list[float | tuple]]) -> list[float]:
    ice_mining_speed_list: list[float] = []
    for harvester in ice_harvester_list:
        ice_per_cycle: int = harvester[0][0]
        sec_per_cycle: int = harvester[0][1]

        ice_per_sec: float = (ice_per_cycle/sec_per_cycle)
        residue_multiplier: int = harvester[1][0]

        residue_chance: int = harvester[1][1]

        residue_per_cycle: float = (residue_multiplier*ice_per_cycle)*residue_chance

        residue_per_sec: float = (residue_per_cycle/sec_per_cycle)

        harvest_speed: float = (ice_per_sec+residue_per_sec)

        ice_mining_speed_list.append(harvest_speed)

    return ice_mining_speed_list


def calculate(nb_ice: int, ice_harvester_list: list[list[tuple]]) -> None:
    showinfo(title="Ice remaing", message=f"we need ~ {ice_calulator(nb_ice, ice_harvester_list):.1f}h to mine the rest of the belt")
    print(nb_ice)


def get_ship_stats() -> None:

    ice_harvester_list = []
    for ship in all_entries:
        # [[(2, 32), (1, 0.34)],[(4, 43), (1, 0.34)]]

        ship_stat: list = ship.winfo_children()
        ship_name: str = ship_stat[0].cget("text")
        print(ship_name)
        ship_nb_lazer = int(Window.globalgetvar(ship_stat[2].cget("textvariable")))
        ship_time_per_cycle = int(Window.globalgetvar(ship_stat[4].cget("textvariable")))
        ship_residue_multiplier = int(Window.globalgetvar(ship_stat[6].cget("textvariable")))
        ship_residue_chance = float(Window.globalgetvar(ship_stat[8].cget("textvariable")))
        print(ship_nb_lazer)
        print(ship_time_per_cycle)
        ship_lazer_tuple: tuple = (ship_nb_lazer, ship_time_per_cycle)
        print(ship_residue_multiplier)
        print(ship_residue_chance)
        ship_residue_tuple: tuple = (ship_residue_multiplier, ship_residue_chance)
        ice_harvester_list.append([ship_lazer_tuple, ship_residue_tuple])
    print(ice_harvester_list)
    nb_ice = int(entree.get())
    print(nb_ice)
    calculate(nb_ice, ice_harvester_list)


def addBox():
    global ship_number
    print(f"SHIP {ship_number} ADDED")
    frame = Frame()
    frame.pack()

    Label(frame, text=f'Ship N°{ship_number}').grid(row=0, column=1)

    Label(frame, text='number of lazers').grid(row=1, column=0)
    nb_lazer = IntVar()
    ent1 = Entry(frame, textvariable=nb_lazer)
    ent1.grid(row=2, column=0)

    Label(frame, text='time per cycle').grid(row=1, column=2)
    time_cycle = IntVar()
    ent2 = Entry(frame, textvariable=time_cycle)
    ent2.grid(row=2, column=2)

    residue_multiplier = IntVar()
    Label(frame, text=' residue multiplier').grid(row=3, column=0)
    ent3 = Entry(frame, textvariable=residue_multiplier)
    ent3.grid(row=4, column=0)

    residue_chance = IntVar()
    Label(frame, text=' residue multiplier').grid(row=3, column=2)
    ent4 = Entry(frame, textvariable=residue_chance)
    ent4.grid(row=4, column=2)

    all_entries.append(frame)
    ship_number += 1


def removeBox():
    global ship_number
    ship_number -= 1
    print(f"SHIP {ship_number} REMOVED")

    all_entries[-1].pack_forget()
    all_entries.pop()


if __name__ == '__main__':
    Window = Tk()
    Window.title("Ice Calulator")
    Window.iconbitmap("./assets/DG.ico")
    Window.geometry("500x500")

    menubar = Menu()
    # menubar.add_command(label="Calculate", command=lambda: calculate(value.get()))
    menubar.add_command(label="Calculate", command=get_ship_stats)
    menubar.add_command(label="Quit", command=Window.quit)

    Window.config(menu=menubar)
    all_entries = []

    text_label: str = "number of Ice to mine ?"
    label = Label(text=text_label)
    label.pack()

    value = IntVar()

    entree = Entry(textvariable=value, width=30)
    entree.pack()

    buttons_frame = Frame()
    buttons_frame.pack()
    ship_number: int = 1
    text_label2: str = "add a ship |"

    label2 = Label(buttons_frame, text=text_label2)
    label2.grid(row=0, column=0)

    bouton_add = Button(buttons_frame, text="+", command=addBox)
    bouton_add.grid(row=1, column=0)

    text_label3: str = "| remove a ship"
    label3 = Label(buttons_frame, text=text_label3)
    label3.grid(row=0, column=1)

    bouton_add = Button(buttons_frame, text="-", command=removeBox)
    bouton_add.grid(row=1, column=1)

    Window.mainloop()

    # list_exemple = [[(ice_per_cycle, sec_per_cycle),(residue_mulitplier, residue_chance)], [an_other_ice_harvester]]
    # ice_harvester_list: list[list[tuple[int] | tuple[int, float]]] = [[(2, 32), (1, 0.34)],
    #                                                                  [(4, 43), (1, 0.34)]]
    # nb_ice: int = 450
    # print(f"we need ~ {ice_calulator(nb_ice, ice_harvester_list):.1f}h to mine the rest of the belt")
