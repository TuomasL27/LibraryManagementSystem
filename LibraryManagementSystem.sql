-- Create the LibraryManagement database
CREATE DATABASE LibraryManagement;

-- Create the tbl_author table to store author information
CREATE TABLE tbl_author (
    Author_AuthorName VARCHAR(100) PRIMARY KEY NOT NULL,
    Author_AuthorPhone VARCHAR(50) NOT NULL
);

-- Create the tbl_book table to store book information
CREATE TABLE tbl_book (
    book_ID INT PRIMARY KEY UNIQUE AUTO_INCREMENT,
    book_Name VARCHAR(100) NOT NULL,
    book_AuthorName VARCHAR(100) NOT NULL,
    book_Category VARCHAR(50) NOT NULL,
    book_Shelf INT NOT NULL,
    FOREIGN KEY (book_AuthorName) REFERENCES tbl_author(Author_AuthorName)
);

-- Create the tbl_borrower table to store borrower information
CREATE TABLE tbl_borrower (
    borrower_CardNo INT PRIMARY KEY UNIQUE NOT NULL,
    borrower_Name VARCHAR(100) NOT NULL
);

-- Create the tbl_book_loans table to store book loan information
CREATE TABLE tbl_book_loans (
    book_loans_ID INT PRIMARY KEY UNIQUE NOT NULL,
    book_loans_CardNo INT UNIQUE NOT NULL,
    book_loans_BookID INT UNIQUE NOT NULL,
    book_loans_DateOut DATE NOT NULL,
    book_loans_DueDate DATE NOT NULL,
    FOREIGN KEY (book_loans_CardNo) REFERENCES tbl_borrower(borrower_CardNo),
    FOREIGN KEY (book_loans_BookID) REFERENCES tbl_book(book_ID)
);