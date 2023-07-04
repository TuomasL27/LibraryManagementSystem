import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="LibraryManagement"
)

cursor = db.cursor()

print("Welcome To The Library Management System! Type help if you are new.")

commands = [
    ["help", "Shows the user all the possible commands."],
    ["book <book_name>", "Shows the status and information about a book."],
    ["author <first_name> <last_name>", "Shows the contact information of an author."],
    ["add <book_name> <category> <shelf> <author_first_name> <author_last_name>", "Adds a new book to the database."],
    ["new_author <first_name> <last_name> <phone>", "Adds a new author to the database."],
    ["new_loan <card_number> <book_name> <date_out> <due_date>", "Creates a new book loan."],
]

while True:
    cmd = input("-> ")
    if "help" in cmd:
        for command in commands:
            print(f"{command[0]} - {command[1]}")
    if " " in cmd:
        cmd_list = cmd.split(" ")
        if cmd_list[0] == "book":
            book_name = " ".join(cmd_list[1:])
            cursor.execute(f"SELECT * FROM tbl_book WHERE book_Name='{book_name}'")
            result = cursor.fetchall()
            if result:
                for row in result:
                    print(f"Name: {row[1]}\nAuthor: {row[2]}\nBook Shelf: {row[4]}\nCategory: {row[3]}\nBook ID: {row[0]}")
            else:
                print("Book not found.")
        elif cmd_list[0] == "author":
            first_name = cmd_list[1]
            last_name = cmd_list[2]
            cursor.execute(f"SELECT * FROM tbl_author WHERE Author_AuthorName='{first_name} {last_name}'")
            result = cursor.fetchall()
            if result:
                for row in result:
                    print(f"Author: {row[0]}\nPhone: {row[1]}")
            else:
                print("Author not found.")
        elif cmd_list[0] == "add":
            book_name = " ".join(cmd_list[1:-4]).replace("'", "''")
            category = cmd_list[-4]
            shelf = int(cmd_list[-3])  # Adjusted index to -3
            author_first_name = cmd_list[-2]
            author_last_name = cmd_list[-1]
            
            cursor.execute(f"SELECT * FROM tbl_author WHERE Author_AuthorName='{author_first_name} {author_last_name}'")
            author_result = cursor.fetchall()
            
            if author_result:
                author_name = author_result[0][0]
                
                cursor.execute("INSERT INTO tbl_book (book_Name, book_AuthorName, book_Category, book_Shelf) "
                               f"VALUES ('{book_name}', '{author_name}', '{category}', {shelf})")
                db.commit()
                print("Book added successfully.")
            else:
                print("Author not found. Please add the author first using the 'new_author' command.")
        elif cmd_list[0] == "new_author":
            first_name = cmd_list[1]
            last_name = cmd_list[2]
            phone = cmd_list[3]
            
            cursor.execute(f"INSERT INTO tbl_author (Author_AuthorName, Author_AuthorPhone) "
                           f"VALUES ('{first_name} {last_name}', '{phone}')")
            db.commit()
            print("Author added successfully.")
        elif cmd_list[0] == "new_loan":
            card_number = int(cmd_list[1])
            book_name = " ".join(cmd_list[2:len(cmd_list)-2]).replace("'", "''")
            date_out = cmd_list[len(cmd_list) - 2]
            due_date = cmd_list[len(cmd_list) - 1]
            
            cursor.execute(f"SELECT * FROM tbl_book WHERE book_Name='{book_name}'")
            book_result = cursor.fetchall()
            
            if book_result:
                book_id = book_result[0][0]
                
                cursor.execute("INSERT INTO tbl_book_loans (book_loans_CardNo, book_loans_BookID, book_loans_DateOut, book_loans_DueDate) "
                               f"VALUES ({card_number}, {book_id}, '{date_out}', '{due_date}')")
                db.commit()
                print("Loan created successfully.")
            else:
                print("Book not found.")
