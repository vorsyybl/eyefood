import food
import sqlite3 as sql
import fns
import tkinter as tk
import datetime as dt

#   Root tk window.
root_main = tk.Tk()
root_main.geometry('420x800')
root_main.title('Food Tracker')

#   Data/storage.
features = ('Create?', 'Update?', 'View?', 'Quit?')
nutrients = [nutrient for nutrient in food.all_nuts]
menu = [meal for meal in food.foods]
menu = sorted(menu)
new_items = []
db = 'main.db'

#   Skeleton configuration.
# root_main.rowconfigure(0)

#   Main branch.
options_frame = tk.LabelFrame(root_main, text='What would you like to do?')
options_frame.grid(row=0, column=0)
choice = tk.StringVar()
choice.set('Create?')

#   Features.
create_button = tk.Radiobutton(options_frame, text=features[0], value=features[0], variable=choice)
create_button.grid(row=0, column=0)
update_button = tk.Radiobutton(options_frame, text=features[1], value=features[1], variable=choice)
update_button.grid(row=1, column=0)
view_button = tk.Radiobutton(options_frame, text=features[2], value=features[2], variable=choice)
view_button.grid(row=2, column=0)
quit_btn = tk.Radiobutton(options_frame, text=features[3], value=features[3], variable=choice)
quit_btn.grid(row=3, column=0)

#   Feature branch.
choice_set_button = tk.Button(root_main, text='Continue...', command=lambda: fns.feature_branch(choice.get(), root_main, menu, new_items, db))
choice_set_button.grid(row=0, column=1)

root_main.mainloop()



