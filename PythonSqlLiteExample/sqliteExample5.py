"""This is a example will show how to update an existing record

"""

from sqlite3 import connect

def main():
    employeeId = input('Please Enter id for which you want to update:')
    firstName = input('Please Enter First Name:')
    lastName = input('Please Enter Last Name:')
    city = input('Please Enter city:')
    phone = input('Please Enter Phone:')
    email = input('Please Enter Email:')
    picture = input('Please Enter Picture:')
    salary = input('Please Enter Salary:')

    # Proper way one
    cmd = """update employees set firstName = :firstName,lastName =:lastName ,
    city = :city , phone = :phone, email = :email, picture = :picture , salary = :salary where id = :id"""
     
    # if db is not present it will create a new one, if it exist it will connect that one
    conn = connect('my_db.sqlite3')
    cur = conn.cursor()

    try:
        cur.execute(cmd, { 'firstName': firstName, 'lastName': lastName, 'city': city, 'phone': phone, 'email': email, 'picture': picture, 'salary': salary, 'id': employeeId})
        conn.commit()
        print('Employee data updated')
    except Exception as e:
        print('There is an error', e)
    finally:
        conn.close()


if __name__ == '__main__' : main()