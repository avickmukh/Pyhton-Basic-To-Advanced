"""This is a example will show how to create new record

"""

from sqlite3 import connect

def main():
    firstName = input('Please Enter First Name:')
    lastName = input('Please Enter Last Name:')
    city = input('Please Enter city:')
    phone = input('Please Enter Phone:')
    email = input('Please Enter Email:')
    picture = input('Please Enter Picture:')
    salary = input('Please Enter Salary:')

    #sql injection way:
    cmd = "insert into employees(firstName, lastName, city, phone, email, picture, salary) values('{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(firstName, lastName, city, phone, email, picture, salary)

     
    # Proper way one
    cmd1 = """insert into employees(firstName, lastName, city, phone, email, picture, salary) values(?,?,?, ?, ?, ?, ?)"""

    # Proper way one
    cmd2 = """insert into employees(firstName, lastName, city, phone, email, picture, salary) values( :firstName,
     :lastName , :city , :phone, :email, :picture , :salary)"""
     
    # if db is not present it will create a new one, if it exist it will connect that one
    conn = connect('my_db.sqlite3')
    cur = conn.cursor()

    try:
        #cur.execute(cmd)
        #cur.execute(cmd, (firstName, lastName, city, phone, email, picture, salary))
        cur.execute(cmd2, { 'firstName': firstName, 'lastName': lastName, 'city': city, 'phone': phone, 'email': email, 'picture': picture, 'salary': salary})
        conn.commit()
        print('Employee data created')
    except Exception as e:
        print('There is an error', e)
    finally:
        conn.close()


if __name__ == '__main__' : main()