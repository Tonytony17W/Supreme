import sqlite3
from dbase import *

def main():
    adminid = input("Enter admin ID: ")
    check = check_admin(adminid)
    if check:
        print("Admin already exists")
    else:
        try:
            create_admin(adminid)
            create_user_lifetime(adminid)
        except Exception as e:
            print(f'Something went wrong: {e}')
        else:
            print('Admin created...')
    james = fetch_UserData_table()
    print(james)

if __name__ == '__main__':
    main()
