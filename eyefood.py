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

# c.execute(f'insert into days_doses values ({calories}, {protein}, {carbs}, {fiber}, {fat}, {cholesterol}, {calcium}, {iron}, {magnesium}, {potassium}, {sodium}, {zinc}, {vitamin_a}, {thiamine}, {vitamin_e}, {riboflavin}, {niacin}, {vitamin_b6}, {folate}, {vitamin_c}, {vitamin_b12}, {selenium}, {sugar}, {vitamin_d})')
# conn.commit()
#
# c.execute(f'update days_doses set calories = {calories+calories_new}, protein = {protein+protein_new}, carbs = {carbs+carbs_new}, fiber = {fiber+fiber_new}, fat = {fat+fat_new}, cholesterol = {cholesterol+cholesterol_new}, calcium = {calcium+calcium_new}, iron = {iron+iron_new}, magnesium = {magnesium+magnesium_new}, potassium = {potassium+potassium_new}, sodium = {sodium+sodium}, zinc = {zinc+zinc_new}, vitamin_a = {vitamin_a+vitamin_a_new}, thiamine = {thiamine+thiamine_new}, vitamin_e = {vitamin_e+vitamin_e_new}, riboflavin = {riboflavin+riboflavin_new}, niacin = {niacin+niacin_new}, vitamin_b6 = {vitamin_b6+vitamin_b6_new}, folate = {folate+folate_new}, vitamin_c = {vitamin_c+vitamin_c_new}, vitamin_b12 = {vitamin_b12+vitamin_b12_new}, selenium = {selenium+selenium_new}, sugar = {sugar+sugar_new}, vitamin_d = {vitamin_d+vitamin_d_new}')
# conn.commit()


