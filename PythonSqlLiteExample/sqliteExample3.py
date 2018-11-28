"""This is a example will show how to fetch record

"""

from sqlite3 import connect

def main():
    lastName = input('Please enter last name:')
     
    # Approch one
    cmd1 = 'select * from employees where lastName = ?'
    
    # Approch two
    cmd2 = 'select * from employees where lastName = :lastName'
     
    # if db is not present it will create a new one, if it exist it will connect that one
    conn = connect('my_db.sqlite3')
    cur = conn.cursor()

    try:
        cur.execute(cmd1, (lastName,))
        data = cur.fetchone()
        print('Fetch single data with approch one')
        print(data)
        cur.execute(cmd2, { 'lastName': lastName})
        data = cur.fetchall()
        print('Fetch All data with approch two')
        print(data)
    except Exception as e:
        print('There is an error', e)
    finally:
        conn.close()


if __name__ == '__main__' : main()