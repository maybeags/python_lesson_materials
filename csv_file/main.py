# import fileinput
#
# with open("studentList.csv", "wt") as file:
#     file.write("학번, 이름, 주소, 연락처\n")
#     file.write("10101, 김승별, 서울시 영등포구, 010-1111-1111\n")
#     file.write("10102, 박나라, 서울시 여의도구, 010-2222-2222\n")
#     file.write("10103, 최태욱, 서울시 강남구, 010-3333-3333\n")
#     file.write("10104, 민기홍, 인천시 계양구, 010-4444-4444\n")
#     file.write("10105, 이명숙, 경기도 과천시, 010-5555-5555\n")
# '''
# p 245
#
# 2, CSV 파일 입출력
#     1. CSV 파일 : Comma Speratated Values의 약자로, 쉼표로 분리한 값들, 이란 의미.
#                 데이터베이스나 스프레드 시트 데이터를 저장하기 위해서 사용하는 형식.
#                 쉼표로 구성된 각 항목들이 테이블을 구성하는 각각의 데이터가 되는 방식
#
#     2. CSV 파일 읽기 :
#         문자열 처리 메서드를 활용하면 별도의 외부 모듈이 없어도 읽는 것이 가능함.
#
#             1. 한 줄에 한 데이터가 있기 때문에 readline() 메서드로 한 줄씩 읽는다.
#             2. 쉼표(,)로 분리하기 위해서 split() 메서드를 이용한다.
# '''
#
# student_list = []
# with open("studentList.csv", "rt") as file:
#     file.readline()                     # prettyTable의 fieldnames에 해당함.
#     end_of_list = False
#     while not end_of_list:
#         line = file.readline()          # 각 프로필들을 한 줄씩 읽어오고
#         if not line:                    # line에 아무 값도 없으면
#             break                       # 종료
#         student = line.split(",")       # 읽어온 라인에서 split()메서드 사용, ","를 기준으로 요소 분리
#         student_list.append(student)    # 각 요소들을 student_list에 append()함.
# print(student_list)                     # 리스트 내의 리스트 방식으로 콘솔에 출력함
#
# with open("userList.csv", "wt") as file:
#     file.write('"회원명", 수강과목, 등록일\n')
#     file.write('"강나라", 필라테스, 25\n')
#     file.write('"나유라", 수영, 25일\n')
#     file.write('"이상기", 헬스, 15일\n')
#
# '''
#         간혹 큰따옴표("")를 이용해서 텍스트를 묶는 경우는 큰 따옴표 제거를 해야지 콘솔에서 제대로 불러올 수 있음
# '''
#
# user_list = []
# with open("userList.csv", "rt") as file:
#     file.readline()
#     end_of_list = False
#     while not end_of_list:
#         line = file.readline()
#         if not line:
#             break
#         user = line.split(",")
#         user[0] = user[0].strip('"')
#         user_list.append(user)
# print(user_list)

'''
    문자열 메서드를 사용하여 충분이 이상의 상황들을 분리하여 해결할 수 있지만, 코드 구조가 복잡하다고 느낄 수 있음.
    이 경우 자동으로 CSV 파일을 분석하고 처리하는 모듈인 csv 모듈을 이용할 수 있음.
    
    3. csv 모듈로 CSV 파일 생성하기

        다음은 주차장에 입고된 차량들을 관리하기 위한 carControll.csv파일을 생성하는 코드입니다.
'''

import csv

# with open("carControll.csv", "w") as file:
#     csv_maker = csv.writer(file, delimiter=",")
#     csv_maker.writerow(([1, "08러1234", "2024-07-01,14:00"]))
#     csv_maker.writerow(([2, "25다1234", "2024-07-01,14:10"]))
#     csv_maker.writerow(([3, "28하1234", "2024-07-01,14:20"]))
# print("carControll.csv 파일이 생성되었습니다.")

'''
이상의 코드로 작성할 경우 데이터에 불필요한 라인이 하나씩 더 추가되어있는데, 
이를 막기 위해서 새로운 라인을 추가하지 못하도록 newline 옵션을 사용 가능함.
newline 옵션에 빈 문자열을 지정하고 이를 코드에 반영하면
'''
#
# with open("carControll.csv", "w", newline="") as file:
#     csv_maker = csv.writer(file, delimiter=",")
#     csv_maker.writerow(([1, "08러1234", "2024-07-01,14:00"]))
#     csv_maker.writerow(([2, "25다1234", "2024-07-01,14:10"]))
#     csv_maker.writerow(([3, "28하1234", "2024-07-01,14:20"]))
# print("carControll.csv 파일이 생성되었습니다.")

'''
이상과 같은 코드가 만들어지는데, 여기서도 문제가 잇는게
날짜 다음 쉼표 (,)가 있어 데이터가 3개 row가 아니라 4 row로 인식되어,
prettyTable 기준으로 fieldnames를 지정하게 되면 오류가 생길 수 있음.
이를 위해 quotechar 옵션 사용 가능.
quotechar 옵션은 delimiter 옵션으로 분리되면 안되는 데이터를 묶어주는 문자를 지정할 때 사용 가능함.
이를 ""로 지정하고 반영한 최종 코드는
'''

# with open("carControll.csv", "w", newline="") as file:
#     csv_maker = csv.writer(file, delimiter=",", quotechar='"')
#     csv_maker.writerow(([1, "08러1234", "2024-07-01,14:00"]))
#     csv_maker.writerow(([2, "25다1234", "2024-07-01,14:10"]))
#     csv_maker.writerow(([3, "28하1234", "2024-07-01,14:20"]))
# print("carControll.csv 파일이 생성되었습니다.")

'''
    4. csv 모듈로 CSV 파일 읽기
        CSV 파일을 읽기 위해서는 r 모드로 파일을 열고 생성된 파일 객체를 csv.reader() 메서드로 전달하면
        csv.reader() 메서드는 CSV 파일의 내용을 읽고 그 내용을 저장한 객체(iterator)를 반환합니다.
'''
#
# with open("carControll.csv", "r", newline="") as file:
#     csv_reader = csv.reader(file, delimiter=",", quotechar='"')
#     for line in csv_reader:
#         print(line)


#
# import pandas as pd
#
# # 올바른 파일 경로를 지정합니다.
# file_path = '/Users/angeunsu/python_lesson_evening/csv_file/busanJinCCTV.csv'
# encoding = 'euc-kr'  # 또는 'cp949'
#
# # Pandas를 사용하여 CSV 파일을 읽습니다.
# df = pd.read_csv(file_path, encoding=encoding)
#
# # 데이터프레임을 출력합니다.
# print(df)

