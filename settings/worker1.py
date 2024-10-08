import sqlite3
import pandas as pd
import tkinter as tk
from pandastable import Table


connection = sqlite3.connect("my_database.db")
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
    operations = "operations"
    workers = "workers"
    clients = "clients"

class C:
    tovar = 'tovar'
    kolvo = 'kolvo'
    date = 'date'
    work_id = 'work_id'
    client = 'client'

    surname = 'surname'
    start_date = 'start_date'
    company = 'company'

    city = 'city'

class C9s:
    workers_to_operations = "workers_to_operations"
    clients_to_operations = "clients_to_operations"


for table in [T.clients, T.workers, T.operations]:
    cursor.execute(
        f'''
            DROP TABLE {table};
        '''
    )
    
cursor.execute(
    f'''
        CREATE TABLE IF NOT EXISTS {T.operations}(
            {C.tovar} TEXT PRIMARY KEY,
            {C.kolvo} INTEGER NOT NULL,
            {C.date} TEXT NOT NULL,
            {C.client} TEXT NOT NULL,
            {C.work_id} INTEGER NOT NULL
        )
    '''
)

cursor.execute(
    f'''
        CREATE TABLE IF NOT EXISTS {T.workers}(
            {C.work_id} INTEGER PRIMARY KEY,
            {C.surname} TEXT NOT NULL,
            {C.start_date} TEXT NOT NULL,
            CONSTRAINT {C9s.workers_to_operations}
            FOREIGN KEY ({C.work_id})  REFERENCES {T.operations} ({C.work_id})
        )
    '''
)

cursor.execute(
    f'''
        CREATE TABLE IF NOT EXISTS {T.clients}(
            {C.client} TEXT PRIMARY KEY,
            {C.company} TEXT NOT NULL,
            {C.city} TEXT NOT NULL,
            CONSTRAINT {C9s.clients_to_operations}
            FOREIGN KEY ({C.client})  REFERENCES {T.operations} ({C.client})
        )
    '''
)

cursor.execute(
    f'''
        INSERT INTO {T.operations} VALUES ('Картошка', 20, '10.01.2023', 'Петров', 121313)
    '''
)

cursor.execute(
    f'''
        INSERT INTO {T.workers} VALUES (121313, "Сидоров", '10.02.2023')
    '''
)

cursor.execute(
    f'''
        INSERT INTO {T.clients} VALUES ("Петров", "PetrovCompany", 'Bishkek')
    '''
)

show_table(T.operations)
show_table(T.workers)
show_table(T.clients)

show_window(T.operations)
show_window(T.workers)
show_window(T.clients)


connection.commit()
connection.close()