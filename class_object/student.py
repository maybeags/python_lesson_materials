'''
p 258

1. 클래스 도입의 필요성
'''

def student_info(name, department, professor, phone, address, grade):
    print(name)
    print(department)
    print(professor)
    print(phone)
    print(address)
    print(grade)


name1 = "emily"
department1 = "computer engineering"
professor1 = "james"
phone1 = "010-1111-2222"
address1 = "seoul"
grade1 = "A"

student_info(name1, department1, professor1, phone1, address1, grade1)

'''
지금까지 배운 방식의 함수와 매개변수, 인수를 통해 여섯개의 변수를 잘 처리했습니다만, 만들어야 할
변수가 많아 관리하기가 쉽지 않습니다. 그리고 이 변수들을 출력하기 위해서 
student_info() 함수에 모두 전달해야 하는 것도 좀 불편합니다.
또한 학생들 한 명 더 추가한다고 가정했을 때,
'''

name2 = "alice"
department2 = "chemical engineering"
professor2 = "david"
phone2 = "010-3333-4444"
address2 = "busan"
grade2 = "B"

student_info(name2, department2, professor2, phone2, address2, grade2)

'''
해당 방식을 이용하면 학생 1명을 추가할 때마다 변수가 6개씩 늘어나는 상황이 생깁니다.

이런 상황을 벗어나기 위해 클래스와 객체를 이용할 수가 있습니다.
'''

'''
p 260 

클래스의 개념

클래스란? 객체를 만드는 도구 -> 청사진 / 설계도 등으로 비유됨.
하나의 클래스를 통해 여러 개의 객체를 만들 수 있습니다.
자동차 설계도 -> 클래스
설계도를 통해 생성된 자동차들 -> 객체

같은 설계도로 만든 자동차라 하더라도 서로 다른 옵션을 가질 수 있습니다.
마찬가지로 같은 클래스로 만든 객체라 하더라도 객체들은 서로 다른 값을 가질 수 있습니다.

인스턴스(instance) 역시 클래스를 이용해서 생성한 객체를 가리키는 용어입니다.
객체와 인스턴스는 그 둘을 바라보는 관점의 차이로 볼 수 있습니다.

1. 자동차설계도 클래스로 만든 자동차는 객체(object)입니다.
2. 자동차는 자동차설계도 클래스의 인스턴스(instance)입니다.

'''

'''
p 261

클래스 정의

클래스를 작성하는 것을 클래스 정의라고 합니다 -> 함수 정의를 생각하세요.

형식 :

class 클래스:
    본문
    
객체 생성

형식:
객체 = 클래스()
'''

class WaffleMachine:
    pass                # 나중에 코드를 작성하겠다는 의미로 이 경우 실행시켜도 오류가 나지 않음

waffle = WaffleMachine()

print(waffle)
'''
print()를 실행하보면 object라고 적혀있다는 점에서 WaffleMachine의 객체임을 확인할 수 있음.
'''

'''
p 264

클래스의 구성

1. 클래스의 기본 구성

'''