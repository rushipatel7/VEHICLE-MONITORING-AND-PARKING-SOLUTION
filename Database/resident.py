import psycopg2
from prettytable import PrettyTable

x = PrettyTable()

try:
    connection = psycopg2.connect(user="",
                                  password="",
                                  host="",
                                  port="",
                                  database="")  # Database connection
    # print("connected")

    # create a cursor object
    cursor = connection.cursor()
    resident_tb = cursor.execute("SELECT * from resident")

    rows = cursor.fetchall()
    for row in rows:
        list = []
        x.field_names = ["SR NO","REGISTRED NAME","NUMBER PLATE","MOBILE NUMBER","ALLOTED SLOT","CURRENT PERSON PARKED","CURRENT PERSON MOB NUMBER"]
        for i in range(0,7):
            list.append(row[i])
            # print(row[i],end=" | ")
        x.add_row(list)

    print(x)
except IOError:
    print("Fail to connect")

finally:
    connection.close()
