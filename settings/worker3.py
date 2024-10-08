import sqlite3
import pandas as pd
import tkinter as tk
from pandastable import Table


connection = sqlite3.connect("databese3.db")
cursor = connection.cursor()

def show_table(name):
    df = pd.read_sql(sql=f"SELECT * FROM {name}", con=connection)
    print(df)

def show_window(name):
    df = pd.read_sql(sql=f"SELECT * FROM {name}", con=connection)
    root = tk.Tk()
    root.title(f'{name}')
    frame = tk.Frame(root)
    frame.pack(fill='both', expand=True)
    pt = Table(frame, dataframe=df)
    pt.show()
    root.mainloop()

class T:
    stuff = "stuff"
    operations= "operations"
    contacts = "contacts"

class C:
    id = 'id'
    surname = 'surname'
    rank = 'rank'

    operation = 'operation'
    gift = 'gift'

    cabinet = 'cabinet'
    number = 'number'

class C9s:
    operations_to_stuff = f"{T.operations}_to_{T.stuff}"
    contacts_to_stuff = f"{T.contacts}_to_{T.stuff}"


for table in [T.stuff, T.operations, T.contacts]:
    cursor.execute(
        f'''
            DROP TABLE {table};
        '''
    )
    
cursor.execute(
    f'''
        CREATE TABLE IF NOT EXISTS {T.stuff}(
            {C.id} INT PRIMARY KEY,
            {C.surname} TEXT NOT NULL,
            {C.rank} TEXT NOT NULL
        )
    '''
)

cursor.execute(
    f'''
        CREATE TABLE IF NOT EXISTS {T.operations}(
            {C.id} INTEGER PRIMARY KEY,
            {C.operation} TEXT NOT NULL,
            {C.rank} TEXT NOT NULL,
            CONSTRAINT {C9s.operations_to_stuff}
            FOREIGN KEY ({C.id})  REFERENCES {T.stuff} ({C.id})
        )
    '''
)

cursor.execute(
    f'''
        CREATE TABLE IF NOT EXISTS {T.contacts}(
            {C.id} INT PRIMARY KEY,
            {C.cabinet} INT NOT NULL,
            {C.number} INT NOT NULL,
            CONSTRAINT {C9s.contacts_to_stuff}
            FOREIGN KEY ({C.id})  REFERENCES {T.stuff} ({C.id})
        )
    '''
)

cursor.execute(
    f'''
        INSERT INTO {T.stuff} VALUES (1,'Иванов','Полковник')
    '''
)

cursor.execute(
    f'''
        INSERT INTO {T.operations} VALUES (1, "Карибский кризис", "Кабриолет")
    '''
)

cursor.execute(
    f'''
        INSERT INTO {T.contacts} VALUES (1, 1232131, 79233692550)
    '''
)

show_window(T.stuff)
show_window(T.operations)
show_window(T.contacts)


connection.commit()
connection.close()