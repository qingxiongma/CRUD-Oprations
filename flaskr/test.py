cur = con.cursor()
person_name = 'Kim'
statement = 'select id, name, age, notes from cx_people where name = :name'
cur.execute(statement, {'name':person_name})
res = cur.fetchall()
print (res)



cur = con.cursor()
statement = 'update cx_people set age = :1 where id = :2'
cur.execute(statement, (31, 1))
con.commit()


cur = con.cursor()
statement = 'update cx_people set notes = :1 where id = :2'
cur.execute(statement, ("I like cats", 1))
con.commit()

cur = con.cursor()
statement = 'update cx_pets set owner = :1 
             where owner = :2 and type = :3'
cur.execute(statement, (2, 1, 'dog'))
con.commit()

cur = con.cursor()
statement = 'update cx_pets set owner = :1 where id = :2'
cur.execute(statement, (1, 6))
con.commit()
print('Number of rows updated: ' + str(cur.rowcount))
print(' ')


CREATE OR REPLACE PROCEDURE get_order_count(
    salesman_code NUMBER, year NUMBER, order_count OUT NUMBER)
IS     
BEGIN     
.....................................
END; 

try:
    # create a connection to the Oracle Database
    with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn:
        # create a new cursor
        with conn.cursor() as curs:
            # create a new variable to hold the value of the
             # OUT parameter
            order_count = curs.var(int)
            # call the stored procedure
            cursor.callproc('get_order_count', [salesman_id, year, order_count])
            return order_count.getvalue()
except cx_Oracle.Error as error:
    print(error)