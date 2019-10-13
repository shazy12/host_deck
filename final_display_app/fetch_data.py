import mysql.connector


def mysql_connect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Admin@123",
        database="deck-db",
    )
    return mydb


def fetch_from_db(id):
    mydb = mysql_connect()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT uid_status, CASE  WHEN isnull(final_answer) = 0 THEN final_answer ELSE -1 END as "
                     "finalanswer FROM app_status where uid = " + str(id))
    fetch_one = mycursor.fetchall()[0]
    if fetch_one[0].lower() == "running":
        return "It is running"
    elif fetch_one[0].lower() == "final answer":
        return str(fetch_one[1])
    else:
        return "Go for new PIN, the game has stopped"


mysql_connect()
# fetch_from_db(1234)