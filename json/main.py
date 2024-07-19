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

json_string = json.dumps(dict_list)

with open("dictList.json", "w") as file:
    file.write(json_string)

print("dictList.json 파일이 생성되었습니다.")