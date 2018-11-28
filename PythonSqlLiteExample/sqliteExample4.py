"""This is a example will show how to Delete record

"""

from sqlite3 import connect

def main():
    email = input('Please enter email:')
    cmd = 'delete from employees where email = ?'
    conn = connect('my_db.sqlite3')
    cur = conn.cursor()
    try:
        cur.execute(cmd, (email,))
        conn.commit()
        print('Record Deleted')
    except Exception as e:
        print('There is an error', e)
    finally:
        conn.close()


if __name__ == '__main__' : main()