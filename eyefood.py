import food
import sqlite3 as sql
import fns
import tkinter as tk
import datetime as dt

#   Root tk window.
root_main = tk.Tk()
root_main.geometry('600x800')
root_main.title('Food Tracker')

#   Data/storage.
features = ('Create?', 'Update?', 'View?', 'Add?', 'Analyze?', 'Quit?')
nutrients = [nutrient for nutrient in food.all_nuts]
menu = [meal for meal in food.foods]
menu = sorted(menu)
new_items = []
db = 'main.db'

#   Main branch.
options_frame = tk.LabelFrame(root_main, text='What would you like to do?', bg='teal', fg='yellow', font=('Gabriola', 33))
options_frame.grid(row=0, column=0)
choice = tk.StringVar()
choice.set('Create?')

#   Features.
create_button = tk.Radiobutton(options_frame, text=features[0], value=features[0], variable=choice, font=('Georgia Bold', 20), bg='teal', fg='orange')
create_button.grid(row=0, column=0)
update_button = tk.Radiobutton(options_frame, text=features[1], value=features[1], variable=choice, font=('Georgia Bold', 20), bg='teal', fg='orange')
update_button.grid(row=1, column=0)
view_button = tk.Radiobutton(options_frame, text=features[2], value=features[2], variable=choice, font=('Georgia Bold', 20), bg='teal', fg='orange')
view_button.grid(row=2, column=0)
add_some_foods_btn = tk.Radiobutton(options_frame, text=features[3], value=features[3], variable=choice, font=('Georgia Bold', 20), bg='teal', fg='orange')
add_some_foods_btn.grid(row=3, column=0)
analyze_btn = tk.Radiobutton(options_frame, text=features[4], value=features[4], variable=choice, font=('Georgia Bold', 20), bg='teal', fg='orange')
analyze_btn.grid(row=4, column=0)
quit_btn = tk.Radiobutton(options_frame, text=features[5], value=features[5], variable=choice, font=('Georgia Bold', 20), bg='teal', fg='orange')
quit_btn.grid(row=5, column=0)
#   Feature branch.
choice_set_button = tk.Button(root_main, text='Continue...', command=lambda: fns.feature_branch(choice.get(), root_main, menu, new_items, db))
choice_set_button.grid(row=0, column=1)

root_main.mainloop()

