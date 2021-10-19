import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text,auther text, year integer, ISBN integer)")
    conn.commit()
    conn.close()

def insert(title,auther,year,ISBN):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,auther,year,ISBN))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",auther="",year="",ISBN=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? or auther=? or year=? or ISBN=?",(title,auther,year,ISBN))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book where id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,auther,year,ISBN):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?,auther=?, year=?,ISBN=? WHERE id=?",(title,auther,year,ISBN,id))
    conn.commit()
    conn.close()

connect()
#insert("rails with trails","himanshu ",2021,7410841566)
#delete(3)
update(2,"wap5","shubh",2019,74198765)
print(view())
print(search(auther="myself"))
