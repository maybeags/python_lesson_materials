'''
p 250

JSON 파일 입출력

JSON - Java Script Object Notation
속성 - 값 쌍으로 구성된 데이터들이 순서 없이 모여있는 구조. 중괄호를 이용하여 나타내 python의 딕셔너리와 같은 모습

JSON 파일 생성

'''

import json

dict_list = [
    {
        "name":"james",
        "age":20,
        "spec":[
            175.5,
            70.5
        ]
    },
    {
        "name": "alice",
        "age": 21,
        "spec": [
            168.5,
            60.5
        ]
    }
]

json_string = json.dumps(dict_list, indent=4)

with open("dictList.json", "w") as file:
    file.write(json_string)

print("dictList.json 파일이 생성되었습니다.")

'''
    4. JSON 파일 읽기
        반대로 JSON 데이터를 파이썬 객체로 변환하는 과정을 확인합니다.
        인콛ㅇ된 JSON 파일을 다시 파이썬 객체로 변경하는 것을 JSON 디코딩(decoding)이라고 함.
        json.loads() 메서드 : 디코딩 처리
'''

with open("dictList.json", "r") as file:
    json_reader = file.read()
    dict_list2 = json.loads(json_reader)

for dic in dict_list2:
    print(f"이름 : {dic["name"]}")
    print(f"나이 : {dic["age"]}")
    print(f"키 : {dic["spec"][0]}")
    print(f"몸무게 : {dic["spec"][1]}")
    print()

'''
 먼저 dictList.json 파일을 read() 메서드로 한 번에 읽어 json_reader에 저장합니다.
 그리고 json.loadS(json_reader)를 통해서 인코딩이 이루어지면 파이썬 객체인 dict_list2가 생성,
 dict_list2는 리스트 내부에 2개의 딕셔너리가 저장된 구조이기 때문에 반복문을 통해 전체 출력할 수 있음.
'''
