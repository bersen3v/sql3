import sqlite3
import pandas as pd
import tkinter as tk
from pandastable import Table


connection = sqlite3.connect("databese2.db")
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
    school = "school"
    teachers = "teachers"
    students = "students"

class C:
    discipline_code = 'discipline_code'
    student_code = 'student_code'

    discipline_name = 'discipline_name'
    teacher_name = 'teacher_name'

    student_surname = 'student_surname'
    student_name = 'student_name'

class C9s:
    teachers_to_school = f"{T.teachers}_to_{T.school}"
    students_to_school = f"{T.students}_to_{T.school}"


for table in [T.school, T.students, T.teachers]:
    cursor.execute(
        f'''
            DROP TABLE {table};
        '''
    )
    
cursor.execute(
    f'''
        CREATE TABLE IF NOT EXISTS {T.school}(
            {C.discipline_code} INT PRIMARY KEY,
            {C.student_code} INT NOT NULL
        )
    '''
)

cursor.execute(
    f'''
        CREATE TABLE IF NOT EXISTS {T.teachers}(
            {C.discipline_code} INTEGER PRIMARY KEY,
            {C.discipline_name} TEXT NOT NULL,
            {C.teacher_name} TEXT NOT NULL,
            CONSTRAINT {C9s.teachers_to_school}
            FOREIGN KEY ({C.discipline_code})  REFERENCES {T.school} ({C.discipline_code})
        )
    '''
)

cursor.execute(
    f'''
        CREATE TABLE IF NOT EXISTS {T.students}(
            {C.student_code} INT PRIMARY KEY,
            {C.student_name} TEXT NOT NULL,
            {C.student_surname} TEXT NOT NULL,
            CONSTRAINT {C9s.students_to_school}
            FOREIGN KEY ({C.student_code})  REFERENCES {T.school} ({C.student_name})
        )
    '''
)

cursor.execute(
    f'''
        INSERT INTO {T.school} VALUES (1,2)
    '''
)

cursor.execute(
    f'''
        INSERT INTO {T.teachers} VALUES (1, "Математика", "Иван Иванов")
    '''
)

cursor.execute(
    f'''
        INSERT INTO {T.students} VALUES (2, "Степан", 'Степанов')
    '''
)

show_window(T.school)
show_window(T.students)
show_window(T.teachers)


connection.commit()
connection.close()