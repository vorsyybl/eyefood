import tkinter as tk
import sqlite3 as sql
import pandas as pd
import food
import time as t
import subprocess


#   Buttons
#   ADD FIRST ITEM TO NEW ITEM BOX
def add_item_btn(new_items, menu, meal_menu, root_win):
    #   Meal Menu Buttons.
    add_button = tk.Button(text='ADD', command=lambda: add_new_item(new_items, menu, meal_menu, root_win))
    return add_button
#   CREATE NEW TABLE
def create_btn(db, new_items):
    create_button = tk.Button(text='CREATE', command=lambda: create_table(db, new_items))
    create_button.grid(row=2, column=1)
    return create_button
#   REMOVE ITEM FROM NEW ITEMS BOX
def rem_btn(root_win, box, new_items):
    remove_button = tk.Button(text='REMOVE', command=lambda: remove_item(root_win, box, new_items))
    return remove_button
#   RESET NEW ITEMS BOX
def rst_btn(root_win, new_items):
    reset_button = tk.Button(text='RESET', command=lambda: reset_new_items(root_win, new_items))
    return reset_button
#   UPDATE TABLE BUTTON
def upd_btn(db, entries, tables, root_win, menu, new_items):
    update_button = tk.Button(text='UPDATE', command=lambda: update_table(db, entries, tables, root_win, menu, new_items))
    return update_button
#   DELETES SELECTED TABLE FROM DB
def del_btn(db, tables_list, tables):
    delete_button = tk.Button(text='DELETE', command=lambda: del_table(db, tables_list, tables))
    return delete_button


#   Boxes
#   ENTRIES BOX
def table_list(db, root_win):
    conn = sql.connect(db)
    c = conn.cursor()
    c.execute('select name from sqlite_master where type="table"')
    tables = [table for table in c.fetchall()]

    #   Create the new items frame.
    tables_frame = tk.LabelFrame(root_win, text='ENTRIES')
    tables_frame.grid(row=1, column=0)
    #   create a new list box object and populate it using the appended list
    tables_box = tk.Listbox(tables_frame, cursor='cross', bg='grey', fg='yellow', selectbackground='green',
                            selectmode='browse', font=('Arial', 13))
    tables_box.config(border=2, relief='sunken')
    for table in tables:
        tables_box.insert(tk.END, table)

    return tables_box
#   NEW ITEMS BOX
def new_items_box(root_win, new_items):
    #   Create the new items frame.
    new_items_frame = tk.LabelFrame(root_win, text='New Items')
    new_items_frame.grid(row=1, column=1)
    #   create a new list box object and populate it using the appended list
    new_box = tk.Listbox(new_items_frame, cursor='cross', bg='grey', fg='yellow', selectbackground='green',
                         selectmode='browse', font=('Arial', 13))
    new_box.config(border=2, relief='sunken')
    for new_item in new_items:
        new_box.insert(tk.END, new_item)

    return new_box
#   MEALS BOX
def meals_menu(root_win, menu, new_items, db):
    #   Create the menu frame.
    new_items_frame = tk.LabelFrame(root_win, text='Add meals...')
    new_items_frame.grid(row=1, column=0)

    #   Create the meal box object, populate it, and grid the menu within the menu frame.
    meal_menu = tk.Listbox(new_items_frame, cursor='cross', bg='grey', fg='yellow', selectbackground='green',
                           selectmode='browse', font=('Arial', 13))
    meal_menu.config(border=2, relief='sunken')
    for meal in menu:
        meal_menu.insert(tk.END, meal)

    #   Make and add a scrollbar to the meal box object.
    menu_scrollbar = tk.Scrollbar(root_win, orient=tk.VERTICAL, command=meal_menu.yview)
    menu_scrollbar.grid(row=1, column=1, sticky='nsw', rowspan=2)
    meal_menu['yscrollcommand'] = menu_scrollbar.set

    return meal_menu

#   Branches
#   Create Branch
#   ADDS NEW ITEM TO NEW ITEMS BOX / LIST
def add_new_item(new_items, items, meal_box, root_win):
    #   Add selected item to items to add list
    new_items.append(items[selected_item(meal_box)])

    new_box = new_items_box(root_win, new_items)
    new_box.grid(row=1, column=1)

    #   After adding all items, create the table in db along with data
    rmv_btn = rem_btn(root_win, new_box, new_items)
    rmv_btn.grid(row=3, column=0)
    reset_btn = rst_btn(root_win, new_items)
    reset_btn.grid(row=4, column=0)

    #   Creates a new table within the main database using the current datetime.
    def create_table(db, data):
        timestamp = t.localtime()
        date = f'{timestamp[0]}-{timestamp[1]}-{timestamp[2]}'
        table_name = f'"{date}"'
        #   Check if one has already been created for that day.
        pass

        #   Connect to main db.
        conn = sql.connect(db)
        c = conn.cursor()

        #   Create a new table using datetime as the table name.
        c.execute(f'drop table if exists {table_name}')
        c.execute(
            f'create table {table_name} (calories int, protein int, carbs int, fiber int, fat int, cholesterol int, '
            f'calcium int, iron int, magnesium int, sodium int, zinc int, vitamin_a int, thiamine int, '
            f'vitamin_e int, riboflavin int, niacin int, vitamin_b6 int, vitamin_c int, vitamin_b12 int, '
            f'selenium int, sugar int, vitamin_d int)')

        #   Populate the new table.
        insert_data(db, table_name, data)
#   REMOVE SELECTED ITEM FROM NEW ITEMS BOX
def remove_item(root_win, items_box, new_items):
    selection = selected_item(items_box)
    new_items.pop(selection)
    new_box = new_items_box(root_win, new_items)
    new_box.grid(row=1, column=1)
#   REMOVE ALL ITEMS FROM NEW BOX
def reset_new_items(root_win, new_items):
    new_items.clear()
    new_box = new_items_box(root_win, new_items)
    new_box.grid(row=1, column=1)
#   Update Branch
#   UPDATE SELECTION FROM ENTRIES (CALLED BY "UPD_BTN")
def update_table(db, entries_box, entries, root_win, menu, new_items):
    #   CLEAR SPACE
    selection = entries[selected_item(entries_box)][0]
    new_items.clear()
    print(selection)

    meals_box = meals_menu(root_win, menu, new_items, db)
    meals_box.grid(row=1, column=0)
    add_items_button = add_item_btn(new_items, menu, meals_box, root_win)
    add_items_button.grid(row=2, column=0)
    update_data_button = tk.Button(text='UPDATE DATA', command=lambda: insert_data(db, selection, new_items))
    update_data_button.grid(row=2, column=1)
#   DELETE SElECTED ENTRY IN ENTRIES LIST
def del_table(db, box, entries):
    selection = entries[selected_item(box)][0]

    conn = sql.connect(db)
    c = conn.cursor()
    c.execute(f'drop table "{selection}"')

    box.grid_remove()
#   View Branch
def view_table(db, box, entries, btn):
    selection = entries[selected_item(box)]
    file_name = 'view_selection.csv'

    conn = sql.connect(db)
    c = conn.cursor()
    c.execute(f'select * from "{selection[0]}"')
    results = c.fetchall()[0]

    calories, protein, carbs, fiber, fat, cholesterol, calcium, iron, magnesium, sodium, zinc, vitamin_a, thiamine, \
    vitamin_e, riboflavin, niacin, vitamin_b6, vitamin_c, vitamin_b12, selenium, sugar, vitamin_d = results
    columns = ['CALORIES', 'PROTEIN', 'CARBS', 'FIBER', 'FAT', 'CHOLESTEROL', 'CALCIUM', 'IRON', 'MAGNESIUM', 'SODIUM',
               'ZINC', 'VITAMIN_A', 'THIAMINE', 'VITAMIN_E', 'RIBOFLAVIN', 'NIACIN', 'VITAMIN_B6', 'VITAMIN_C',
               'VITAMIN_B12', 'SELENIUM', 'SUGAR', 'VITAMIN_D']
    values = [calories, protein, carbs, fiber, fat, cholesterol, calcium, iron, magnesium, sodium, zinc, vitamin_a,
              thiamine, vitamin_e, riboflavin, niacin, vitamin_b6, vitamin_c, vitamin_b12, selenium, sugar, vitamin_d]
    view_selection = pd.DataFrame([values], columns=columns)

    view_selection.to_csv(file_name, index=False)
    subprocess.call(['open', file_name])

    btn.grid_remove()
    box.grid_remove()


#   Misc
def selected_item(box):
    for index in box.curselection():
        return index


def insert_data(db, table, data):
    conn = sql.connect(db)
    c = conn.cursor()

    counts = pd.value_counts(data)
    unique_keys = set(data)

    calories = 0
    protein = 0
    carbs = 0
    fiber = 0
    fat = 0
    cholesterol = 0
    calcium = 0
    iron = 0
    magnesium = 0
    sodium = 0
    zinc = 0
    vitamin_a = 0
    thiamine = 0
    vitamin_e = 0
    riboflavin = 0
    niacin = 0
    vitamin_b6 = 0
    vitamin_c = 0
    vitamin_b12 = 0
    selenium = 0
    sugar = 0
    vitamin_d = 0

    for key in unique_keys:
        count = counts[key]

        calories += food.foods[key]['calories'] * count
        protein += food.foods[key]['protein'] * count
        carbs += food.foods[key]['carbs'] * count
        fiber += food.foods[key]['fiber'] * count
        fat += food.foods[key]['fat'] * count
        cholesterol += food.foods[key]['cholesterol'] * count
        calcium += food.foods[key]['calcium'] * count
        iron += food.foods[key]['iron'] * count
        magnesium += food.foods[key]['magnesium'] * count
        sodium += food.foods[key]['sodium'] * count
        zinc += food.foods[key]['zinc'] * count
        vitamin_a += food.foods[key]['vitamin a'] * count
        thiamine += food.foods[key]['thiamine'] * count
        vitamin_e += food.foods[key]['vitamin e'] * count
        riboflavin += food.foods[key]['riboflavin'] * count
        niacin += food.foods[key]['niacin'] * count
        vitamin_b6 += food.foods[key]['vitamin b6'] * count
        vitamin_c += food.foods[key]['vitamin c'] * count
        vitamin_b12 += food.foods[key]['vitamin b12'] * count
        selenium += food.foods[key]['selenium'] * count
        sugar += food.foods[key]['sugar'] * count
        vitamin_d += food.foods[key]['vitamin d'] * count

    c.execute(
        f'insert into "{table}" values ({calories}, {protein}, {carbs}, {fiber}, {fat}, {cholesterol}, {calcium}, {iron}, '
        f'{magnesium}, {sodium}, {zinc}, {vitamin_a}, {thiamine}, {vitamin_e}, {riboflavin}, {niacin}, {vitamin_b6}, '
        f'{vitamin_c}, {vitamin_b12}, {selenium}, {sugar}, {vitamin_d})')

    conn.commit()


def exit_loop(root_win):
    root_win.destroy()


#   Feature Branch.
def feature_branch(choice, root_win, menu, new_items, db):
    if choice == 'Create?':
        meal_box = meals_menu(root_win, menu, new_items, db)
        meal_box.grid(row=1, column=0)
        add_btn = add_item_btn(new_items, menu, meal_box, root_win)
        add_btn.grid(row=2, column=0)
        crt_btn = create_btn(db, new_items)
        crt_btn.grid(row=2, column=1)
    elif choice == 'Update?':
        entries_list = table_list(db, root_win)
        entries_list.grid(row=1, column=0)

        conn = sql.connect(db)
        c = conn.cursor()
        c.execute('select name from sqlite_master where type="table"')
        tables = [table for table in c.fetchall()]

        #   Buttons.
        update_button = upd_btn(db, entries_list, tables, root_win, menu, new_items)
        update_button.grid(row=2, column=0)
        delete_button = del_btn(db, entries_list, tables)
        delete_button.grid(row=3, column=0)
    elif choice == 'View?':
        tables_list = table_list(db, root_win)
        tables_list.grid(row=1, column=0)

        conn = sql.connect(db)
        c = conn.cursor()
        c.execute('select name from sqlite_master where type="table"')
        tables = [table for table in c.fetchall()]

        view_btn = tk.Button(text='VIEW', command=lambda: view_table(db, tables_list, tables, view_btn))
        view_btn.grid(row=2, column=0)
    elif choice == 'Quit?':
        exit_loop(root_win)

