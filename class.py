import sqlite3 as lite

class Database(object):

    def __init__(self):
        global con
        try:
            con = lite.connect('courses.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to create a DB")

    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO course(name, description, price, is_private) VALUES (?,?,?,?)", data)
            return True
        except Exception:
            return False

    def fetch_data(self):
        try:
            with con:    
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except Exception:
            return False

    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM course WHERE Id = ?"
                cur.execute(sql, [id])
                return True
        except Exception:
            return False


def main():

    db = Database()

    print("Database menu:")
    print("\nPress 1: Insert data into database")
    print("Press 2: Show data from database")
    print("Press 3: Delete data from database")
    print("\n")
    
    choice = input("Choose action ")

    if choice == "1":
        name = input("Enter Name: ")
        description = input("Enter Description: ")
        price = input("Enter Price: ")
        private = input("Private (no/yes): ")

        if db.insert_data([name, description, price, private]):
            print("Inserted successfully")
        else:
            print("Failed to insert")

    elif choice == "2":
        print("\n")
        print("Database: ")

        for index, item in enumerate(db.fetch_data()):
            print("\nItem no: " + str(index + 1))
            print("ID: " + str(item[0]))
            print("Name: " + str(item[1]))
            print("Description: " + str(item[2]))
            print("Price: " + str(item[3]))
            private = 'Yes' if item[4] else 'No'
            print("Is private: " + private)
            print("\n")

        
    elif choice == "3":
        record_id = input("Enter the id: ")

        if db.delete_data(record_id):
            print("Deleted successfully")
        else:
            print("Delete Failed")

    else:
        print("Bad Choice")



if __name__ == '__main__':
    main()