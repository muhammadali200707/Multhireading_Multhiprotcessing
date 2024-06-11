import time
import multiprocessing
from database import Database
from datetime import datetime


def insert_data(query, query_type):
    time.sleep(3)
    print(Database.connect(query, query_type))


def process():
    query_1 = "INSERT INTO cars VALUES('BMW', 45000)"
    query_2 = "INSERT INTO cars VALUES('Mercedes', 30000)"
    query_3 = "INSERT INTO cars VALUES('Hyundai', 20000)"
    query_4 = "INSERT INTO cars VALUES('Ford', 15000)"
    query_5 = "INSERT INTO cars VALUES('Ferari', 200000)"
    query_6 = "INSERT INTO cars VALUES('Bugatti', 980000)"
    query_7 = "INSERT INTO cars VALUES('Rolls Royce', 45980)"
    query_8 = "INSERT INTO cars VALUES('Nissan', 340000)"
    query_9 = "INSERT INTO users VALUES('John', 21)"
    query_10 = "INSERT INTO users VALUES('Smith', 12)"
    query_11 = "INSERT INTO users VALUES('Ali', 43)"
    query_12 = "INSERT INTO users VALUES('Hasan', 23)"
    query_13 = "INSERT INTO users VALUES('Jack', 54)"
    query_14 = "INSERT INTO users VALUES('Rock', 23)"
    query_15 = "INSERT INTO users VALUES('Alina', 32)"
    query_16 = "INSERT INTO users VALUES('Muhammad Ali', 31)"
    query_type_1 = 'insert'
    query_type_2 = 'insert'
    query_type_3 = 'insert'
    query_type_4 = 'insert'
    query_type_5 = 'insert'
    query_type_6 = 'insert'
    query_type_7 = 'insert'
    query_type_8 = 'insert'
    query_type_9 = 'insert'
    query_type_10 = 'insert'
    query_type_11 = 'insert'
    query_type_12 = 'insert'
    query_type_13 = 'insert'
    query_type_14 = 'insert'
    query_type_15 = 'insert'
    query_type_16 = 'insert'
    process1 = multiprocessing.Process(target=insert_data, args=(query_1, query_type_1))
    process2 = multiprocessing.Process(target=insert_data, args=(query_2, query_type_2))
    process3 = multiprocessing.Process(target=insert_data, args=(query_3, query_type_3))
    process4 = multiprocessing.Process(target=insert_data, args=(query_4, query_type_4))
    process5 = multiprocessing.Process(target=insert_data, args=(query_5, query_type_5))
    process6 = multiprocessing.Process(target=insert_data, args=(query_6, query_type_6))
    process7 = multiprocessing.Process(target=insert_data, args=(query_7, query_type_7))
    process8 = multiprocessing.Process(target=insert_data, args=(query_8, query_type_8))
    process9 = multiprocessing.Process(target=insert_data, args=(query_9, query_type_9))
    process10 = multiprocessing.Process(target=insert_data, args=(query_10, query_type_10))
    process11 = multiprocessing.Process(target=insert_data, args=(query_11, query_type_11))
    process12 = multiprocessing.Process(target=insert_data, args=(query_12, query_type_12))
    process13 = multiprocessing.Process(target=insert_data, args=(query_13, query_type_13))
    process14 = multiprocessing.Process(target=insert_data, args=(query_14, query_type_14))
    process15 = multiprocessing.Process(target=insert_data, args=(query_15, query_type_15))
    process16 = multiprocessing.Process(target=insert_data, args=(query_16, query_type_16))

    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()
    process7.start()
    process8.start()
    process9.start()
    process10.start()
    process11.start()
    process12.start()
    process13.start()
    process14.start()
    process15.start()
    process16.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()
    process7.join()
    process8.join()
    process9.join()
    process10.join()
    process11.join()
    process12.join()
    process13.join()
    process14.join()
    process15.join()
    process16.join()


if __name__ == '__main__':
    print(f"This is the beginning --> {datetime.now()}")
    process()
    print(f"This is the ending --> {datetime.now()}")
