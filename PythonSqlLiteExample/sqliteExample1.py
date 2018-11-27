"""This is a example of creating a new sqllite db and create a table

"""

from sqlite3 import connect

def main():
    cmd = '''create table employees(
        id integer primary key autoincrement,
        firstName varchar(50) not null,
        lastName varchar(50) not null,
        city varchar(50) default 'Bangalore',
        phone varchar(50) unique,
        email varchar(50) unique,
        picture varchar(255),
        salary integer
    )
    '''
    # if db is not present it will create a new one, if it exist it will connect that one
    conn = connect('my_db.sqlite3')

    cur = conn.cursor()

    try:
        cur.execute(cmd)
        print('Table Employees created')
    except Exception as e:
        print('There is an error', e)
    finally:
        conn.close()


if __name__ == '__main__' : main()