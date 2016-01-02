import sqlite3

tut_db_connection = sqlite3.connect('tut.db')

c = tut_db_connection.cursor()


def create_table():
    c.execute('CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)')


def enter_data():
    c.execute("INSERT INTO example VALUES('Python', '2.7', 'Beginner')")
    c.execute("INSERT INTO example VALUES('Python', '3.3', 'Intermediate')")
    c.execute("INSERT INTO example VALUES('Python', '3.4', 'Expert')")
    tut_db_connection.commit()


def enter_dynamic_data():
    lang = input("Enter language: ")
    version = input("Enter version: ")
    level = input("Enter skill level: ")

    c.execute("INSERT INTO example VALUES(?, ?, ?)", (lang, version, level))
    tut_db_connection.commit()


def read_data():

    #what_skill = input("What skill level do you want? ")

    sql = "SELECT * FROM example"

    for row in c.execute(sql):
        print(row)
        #print(row[0])


def update_data():

    oldstr = 'Beginner'
    newstr = 'beginner'
    sql = "UPDATE example SET Skill = ?"

    c.execute(sql, [oldstr])
    tut_db_connection.commit()


def delete_data():

    sql = "DELETE FROM example WHERE Language == 'Ruby'"

    c.execute(sql)
    tut_db_connection.commit()

delete_data()
read_data()

tut_db_connection.close()
