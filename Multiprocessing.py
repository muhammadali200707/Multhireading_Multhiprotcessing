import time
import multiprocessing
from datetime import datetime


def write_to_file(file_path: str, data: str):
    time.sleep(2)
    with open(file_path, 'r+') as file:
        file.write(data)
        print(f"Data written to {file_path}\n")


def main():
    file_path1 = 'db/file_1.txt'
    file_path2 = 'db/file_2.txt'
    file_path3 = 'db/file_3.txt'
    file_path4 = 'db/file_4.txt'
    file_path5 = 'db/file_5.txt'
    file_path6 = 'db/file_6.txt'
    file_path7 = 'db/file_7.txt'
    file_path8 = 'db/file_8.txt'

    data1 = 'Hi from P1!'
    data2 = 'Hi from P2'
    data3 = 'Hi from P3'
    data4 = 'Hi from P4'
    data5 = 'Hi from P5'
    data6 = 'Hi from P6'
    data7 = 'Hi from P7'
    data8 = 'Hi from P8'

    process1 = multiprocessing.Process(target=write_to_file, args=(file_path1, data1,))
    process2 = multiprocessing.Process(target=write_to_file, args=(file_path2, data2,))
    process3 = multiprocessing.Process(target=write_to_file, args=(file_path3, data3,))
    process4 = multiprocessing.Process(target=write_to_file, args=(file_path4, data4,))
    process5 = multiprocessing.Process(target=write_to_file, args=(file_path5, data5,))
    process6 = multiprocessing.Process(target=write_to_file, args=(file_path6, data6,))
    process7 = multiprocessing.Process(target=write_to_file, args=(file_path7, data7,))
    process8 = multiprocessing.Process(target=write_to_file, args=(file_path8, data8,))

    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()
    process7.start()
    process8.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()
    process7.join()
    process8.join()


if __name__ == "__main__":
    print(f"This the beginning --> {datetime.now()}")
    main()
    print(f"This the ending --> {datetime.now()}")
