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
객체를 만들어내는 클래스는 객체가 가져야 할 구성요소를 가지고 있습니다. 객체를 생성하기 위해서 클래스는 객체가 가져야 할 값과 기능을 가지고 있어야 합니다.
값 = 속성
기능 = 메서드


클래스를 구성하는 변수는 2 가지로 분리할 수 있습니다. 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수인 클래스 변수와
모든 인스턴스들이 개별적으로 가지는 변수인 인스턴스 변수입니다.

메서드는 특징에 따라서
클래스 메서드, 정적 메서드, 인스턴스 메서드로 분리가능합니다.

인스턴스 변수 : 클래스를 기반으로 만들어지는 모든 인스턴스들이 각각 따로 저장하는 변수를 의미.
모든 인스턴스 변수는 self라는 키워드를 앞에 붙여줍니다. 인스턴스 메서드는 인스턴스 변수를 사용하는 메서드입니다.
인스턴스 변수값에 따라서 각 인스턴스마다 다르게 동작합니다.
인스턴스 메서드는 첫번째 매개변수로 self를 추가해야합니다.

인스턴스 변수와 인스턴스 메서드는 객체 지향 프로그래밍(OOP)에서 중요한 개념입니다. 이 두 가지는 클래스와 객체의 상태와 동작을 정의하는 데 사용됩니다.

### 인스턴스 변수
인스턴스 변수는 클래스의 각 인스턴스(객체)마다 개별적으로 유지되는 변수입니다. 이 변수들은 주로 객체의 상태를 나타내기 위해 사용됩니다. 인스턴스 변수는 객체가 생성될 때마다 새롭게 할당되며, 각 객체는 고유한 인스턴스 변수 값을 가질 수 있습니다.

#### 정의
인스턴스 변수는 일반적으로 클래스의 생성자 메서드(`__init__`) 내에서 `self` 키워드를 사용하여 정의됩니다.

#### 예시
```python
class Pokemon:
    def __init__(self, number, name, type):
        self.number = number   # 인스턴스 변수
        self.name = name       # 인스턴스 변수
        self.type = type       # 인스턴스 변수

# 객체 생성
pokemon1 = Pokemon(1, "이상해씨", "풀/독")
pokemon2 = Pokemon(4, "파이리", "불꽃")

print(pokemon1.name)  # 출력: 이상해씨
print(pokemon2.name)  # 출력: 파이리
```
여기서 `number`, `name`, `type`이 인스턴스 변수입니다. 각 `Pokemon` 객체는 독립적인 인스턴스 변수 값을 가집니다.

### 인스턴스 메서드
인스턴스 메서드는 클래스의 각 인스턴스에서 호출될 수 있는 메서드입니다. 이 메서드는 주로 객체의 동작을 정의합니다. 인스턴스 메서드는 첫 번째 매개변수로 항상 `self`를 받아야 하며, 이를 통해 해당 메서드가 호출된 객체에 접근할 수 있습니다.

#### 정의
인스턴스 메서드는 클래스 내부에서 정의되며, 첫 번째 매개변수로 `self`를 받습니다.

#### 예시

class Pokemon:
    def __init__(self, number, name, type):
        self.number = number
        self.name = name
        self.type = type

    def display_info(self):   # 인스턴스 메서드
        print(f"번호: {self.number}, 이름: {self.name}, 속성: {self.type}")

# 객체 생성
pokemon1 = Pokemon(1, "이상해씨", "풀/독")
pokemon2 = Pokemon(4, "파이리", "불꽃")

# 인스턴스 메서드 호출
pokemon1.display_info()  # 출력: 번호: 1, 이름: 이상해씨, 속성: 풀/독
pokemon2.display_info()  # 출력: 번호: 4, 이름: 파이리, 속성: 불꽃
```
여기서 `display_info` 메서드는 인스턴스 메서드입니다. 이 메서드는 객체의 인스턴스 변수에 접근하여 객체의 정보를 출력합니다.

### 인스턴스 변수와 인스턴스 메서드의 관계
- **인스턴스 변수**는 객체의 데이터를 저장합니다. 예를 들어, `pokemon1` 객체의 `name` 인스턴스 변수는 "이상해씨"라는 값을 가집니다.
- **인스턴스 메서드**는 이 데이터를 사용하여 동작을 수행합니다. 예를 들어, `display_info` 메서드는 객체의 `name` 인스턴스 변수를 사용하여 해당 객체의 이름을 출력합니다.
- 인스턴스 메서드는 `self` 키워드를 사용하여 객체의 인스턴스 변수에 접근할 수 있습니다. 이를 통해 객체 내부의 데이터를 조작하거나 참조할 수 있습니다.

이러한 관계를 통해 인스턴스 변수와 인스턴스 메서드는 객체의 상태와 동작을 정의하고 관리하는 중요한 역할을 합니다.
'''

class Person:

    def who_am_i(self, name, age, tel, address):
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

boy = Person()
boy.who_am_i("안근수", 37, "010-7445-7113", "부산광역시 연제구")
print(boy.name)
print(boy.age)
print(boy.tel)
print(boy.address)

