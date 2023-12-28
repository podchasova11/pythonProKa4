import sqlite3
import pytest
import requests


@pytest.fixture()
def connect_data_base():
    connection = sqlite3.connect("test.db")
    print("Мы подключили БД")
    return connection


cursor = connect_data_base().cursor()
cursor.execute("SELECT *FROM employees")
cursor.fetchall()  # собери все записи и запринть
connect_data_base().close()   #закрывает БД


def connect_database2():
    connect2 = sqlite3.connect("test2.db")
    return connect2


cursor2 = connect_database2().cursor()
cursor2.execute("SELECT * FROM employees")
print(cursor2.fetchall())
connect_database2().close()
