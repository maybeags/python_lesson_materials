from prettytable import PrettyTable

table = PrettyTable()
table.field_names = [ "구분", "부모 클래스", "자식 클래스" ]
table.add_row(["의미", "상속해주는 클래스", "상속받는 클래스"])
table.add_row(["용어", "슈퍼 클래스/기반 클래스", "서브 클래스/파생 클래스"])
print(table)

'''
p 283

상속

1. 상속이란?
    어떤 클래스가 가지고 있는 기능을 그대로 물려받아서 사용할 수 있는 클래스를 생성 가능한데,
    클래스의 기능을 물려받을 때 상속받는다는 표현을 사용함.
    상속 관계에 있는 클래스를 표현할 때 부모 클래스 / 자식 클래스라는 용어를 사용함.
+------+-------------------------+-------------------------+
| 의미 |    상속해주는 클래스    |     상속받는 클래스     |
| 용어 | 슈퍼 클래스/기반 클래스 | 서브 클래스/파생 클래스 |
+------+-------------------------+-------------------------+

2. 상속 관계 구현
    두 클래스가 상속 관계에 놓이려면 IS-A 관계를 성립해야 함.
    IS-A 관계란 "~은 ~이다"로 해석할 수 있는 관계를 의미. -> "학생은 사람이다"처럼 해석되는 것이 IS-A관계
    
    * IS-A의 원문 : is a kind of
    Dog is a kind of Animal -> 개는 동물의 한 종류이다.
    
    형식 :
class 슈퍼 클래스:
    본문
    
class 서브 클래스(슈퍼 클래스):
    본문
'''

class Person:       # 슈퍼 클래스

    def __init__(self, name):       # 생성자
        self.name = name

    def eat(self, food):
        print(self.name  + "가 " + food + "를 먹습니다.")

class Student(Person):  # 서브 클래스

    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def study(self):
        print(self.name + "는 " + self.school + "에서 공부를 합니다.")


potter = Student("해리포터", "호그와트")
potter.eat("감자")        # 슈퍼 클래스의 메서드 사용
potter.study()           # 서브 클래스의 메서드 사용

'''
3. 서브 클래스의 __init__()

서브 클래스는 슈퍼 클래스가 없으면 존재할 수 없습니다. 그러나 서브 클래스의 생성자를 구현할 때는 반드시
슈퍼 클래스의 생성자를 먼저 호출하는 코드를 작성해야만 합니다.

super -> 슈퍼 클래스를 의미. 즉, Student의 생성자를 호출하면 super().__init__(name)에 의해서
슈퍼 클래스인 Person의 생성자가 먼저 호출되면서 슈퍼 클래스가 '생성'됩니다.
이후 슈퍼 클래스에서 생성된 인스턴스 변수인 name이 서브 클래스로 전달되고, 이후에 서브 클래스에서 school 인스턴스 변수를 정의하여
값을 저장하면서 생성됩니다.

4. 서브 클래스의 인스턴스 자료형

슈퍼 클래스 객체는 슈퍼 클래스의 인스턴스
하지만 서브 클래스 객체는 서브 클래스의 인스턴스이면서 동시에 슈퍼 클래스의 인스턴스
Student의 객체는 Student의 인스턴스이면서 동시에 Person의 인스턴

어떤 객체가 어떤 클래스의 인스턴스인지 확인하기 위해서 isinstance() 함수를 사용

형식 :

isinstance(객체, 클래스)
'''

print(isinstance(potter, Student))
print(isinstance(potter, Person))
'''
True / False를 반환함

응용 예제

1. 다음 지시사항을 읽고 이름과 전체 인구수를 저장할 수 있는 Person 클래스를 생성하세요.

지시사항
1. 다음과 같은 방법으로 man과 woman 인스턴스를 생성하세요
man = Person("james")
woman = Person("emily")

2. man과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 처리하세요.
james is born.
emily is born.

3. 다음 코드를 통해서 전체 인구수를 조회할 수 있도록 처리하세요.
print(f"전체 인구수 : {Person.get_population()} 명")

4. 다음과 같은 방법으로 man 인스턴스를 삭제하세요.
del man

5. man 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 처리하세요.
james is dead.
'''

class Person:
    population = 0  # 클래스 변수: 전체 인구수를 나타내는 변수

    def __init__(self, name):
        self.name = name
        print(f"{self.name} is born.")
        Person.population += 1  # 인스턴스가 생성될 때마다 전체 인구수 증가

    @staticmethod
    def get_population():
        return Person.population

    def __del__(self):
        print(f"{self.name} is dead.")
        Person.population -= 1  # 인스턴스가 삭제될 때마다 전체 인구수 감소


# 지시사항에 따라 인스턴스 생성 및 테스트
man = Person("James")
woman = Person("Emily")

# 전체 인구수 조회
print(f"전체 인구수 : {Person.get_population()} 명")

# man 인스턴스 삭제
del man

# 전체 인구수 재조회
print(f"전체 인구수 : {Person.get_population()} 명")

'''
2. 다음 지시사항을 읽고 가게의 매출을 구할 수 있는 Shop 클래스를 구현하세요.

지시사항
1. Shop 클래스는 다음과 같은 클래스 변수를 가지고 있습니다. total은 전체 매출액을 의미하고, menu_list의 각
요소는 {메뉴명:가격}으로 구성된 딕셔너리입니다.
total = 0
menu_list [{"떡볶이": 3000}, {"순대":3000}, {"튀김":500}, {"김밥":2000}]

2. 매출이 생기면 다음과 같은 방식으로 메뉴와 판매량을 작성합니다.
Shop.sales("떡볶이", 1)    # 떡볶이를 1개 판매
Shop.sales("김밥", 2)     # 김밥을 2개 판매
Shop.sales("튀김", 5)     # 튀김을 5개 판매

3. 모든 매출을 작성한 뒤 다음과 같은 방식으로 전체 매출액을 확인합니다.
print(f"매출 : {Shop.total}원")
'''

class Shop:
    total = 0  # 전체 매출액을 나타내는 클래스 변수
    menu_list = [{"떡볶이": 3000}, {"순대": 3000}, {"튀김": 500}, {"김밥": 2000}]  # 메뉴와 가격 정보

    @classmethod
    def sales(cls, item, quantity):
        for menu in cls.menu_list:
            if item in menu:
                price = menu[item]
                total_price = price * quantity
                cls.total += total_price
                print(f"{item}을(를) {quantity}개 판매하였습니다.")
                break
        else:
            print(f"{item}은(는) 메뉴에 없습니다.")

    @classmethod
    def show_total_sales(cls):
        return cls.total

# 매출 기록 예시
Shop.sales("떡볶이", 1)
Shop.sales("김밥", 2)
Shop.sales("튀김", 5)

# 전체 매출액 확인
print(f"매출 : {Shop.show_total_sales()}원")

'''
3. 다음 지시사항을 읽고 Hybrid 클래스를 구현하세요.

지시사항
1. 다음과 같은 슈퍼 클래스 Car를 가지고 있는 서브 클래스 Hybrid를 구현하세요.
'''

class Car:

    max_oil = 50 # 최대 주유량

    def __init__(self, oil):
        self.oil = oil

    def add_oil(self, oil):
        if oil <= 0:    # 0 이하의 주유는 진행하지 않음
            return
        self.oil += oil
        if self.oil > Car.max_oil:  # 주유 후 최대 주유량 초과상태이면
            self.oil = Car.max_oil  # 현재 주유량을 최대 주유량으로 설정

    def car_info(self):
        print(f"현재 주유상태 : {self.oil}")
'''
2. 서브 클래스 Hybrid는 다음과 같은 특징을 가지고 있습니다.
최대 배터리 충전량은 30입니다.
배터리를 충전하는 charge() 메서드가 있습니다. 최대 충전량을 초과하도록 충전할 수 없고, 0보다 작은 값으로
충전할 수 없습니다.
현재 주유량과 충전량을 모두 확인할 수 있는 hybrid_info() 메서드가 있습니다.

3. 다음과 같은 방식으로 전체 동작을 확인할 수 있습니다.
car = Hybrid(0, 0)
car.add_oil(100)
car.charge(50)
car.hybrid_info() # 현재 주유상태 : 50 # 현재 충전상태 : 30
'''

class Hybrid(Car):
    max_battery = 30  # 최대 배터리 충전량

    def __init__(self, oil, battery):
        super().__init__(oil)
        self.battery = battery

    def charge(self, amount):
        if amount <= 0:
            return
        self.battery += amount
        if self.battery > Hybrid.max_battery:
            self.battery = Hybrid.max_battery

    def hybrid_info(self):
        print(f"현재 주유상태 : {self.oil}")
        print(f"현재 충전상태 : {self.battery}")


# 테스트 예시
car = Hybrid(0, 0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()  # 현재 주유상태 : 50, 현재 충전상태 : 30
