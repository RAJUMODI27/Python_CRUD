import sqlite3
# creating and connecting databse
# _________________________________
con=sqlite3.connect('sqlite_database.db')




# create table
# _______________
# con.execute('''
#     CREATE TABLE STUDENTS (st_id integer primary key Autoincrement,
#     st_name varchar(10),
#     st_class varchar(10) )
# ''')
# con.close()
# __________________


# insert query
# ins=""" insert into students(st_name,st_class) values('dhaval','science')
# """
# con.execute(ins)
# con.commit()
# con.close()



# delete query
# del=""" delete from students where st_name='raju'
# """
# con.execute(del)
# con.commit()
# con.close()


# update query
# upd=""" update students set st_class ='mba' where st_name = 'honey'
# """
# con.execute(upd)
# con.commit()
# con.close()


# select query
# sel=""" select * from students where st_id = 2
# """
#
# x=con.execute(sel)
#
# for i in x:
#     print(i)
# con.commit()
# con.close()


