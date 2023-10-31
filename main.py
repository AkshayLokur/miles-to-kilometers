from tkinter import Tk, Entry, Button, Label, Grid

tk = Tk()
tk.title("Miles to Kms converter")
tk.minsize(width=300, height=300)
tk.config(padx=50, pady=50)

miles_entry = Entry()
miles_entry.grid(row=0, column=1)
miles_entry.focus()

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

iq_eq_to_lbl = Label(text="is equal to")
iq_eq_to_lbl.grid(row=1, column=0)

answer_lbl = Label(text="0")
answer_lbl.grid(row=1, column=1)

km_lbl = Label(text="Kms")
km_lbl.grid(row=1, column=2)


def convert_miles_to_kms():
    miles = miles_entry.get()
    kms = float(miles) * 1.609344
    answer_lbl.config(text=kms)


calc_btn = Button(text="Calculate", command=convert_miles_to_kms)
calc_btn.grid(row=2, column=1)

tk.mainloop()
