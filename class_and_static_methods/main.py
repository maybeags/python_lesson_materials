from prettytable import PrettyTable

'''
p 278

1. 클래스 변수

인스턴스 변수 : 인스턴스마다 서로 다른 값을 가지는 경우
클래스 변수 : 모든 인스턴스가 동일한 값을 가지는 경우

+-----------+----------------------------------+-----------------------------------+
|    구분   |          인스턴스 변수           |            클래스 변수            |
+-----------+----------------------------------+-----------------------------------+
|    목적   |   인스턴스마다 다른 값을 저장    |   인스턴스가 공유하는 값을 저장   |
| 접근 방식 | 인스턴스 접근(o) / 클래스접근(x) | 인스턴스 접근(o) / 클래스 접근(o) |
+-----------+----------------------------------+-----------------------------------+
'''

table = PrettyTable()
table.field_names = [ "구분", "인스턴스 변수", "클래스 변수" ]
table.add_row(["목적", "인스턴스마다 다른 값을 저장", "인스턴스가 공유하는 값을 저장"])
table.add_row(["접근 방식","인스턴스 접근(o) / 클래스접근(x)", "인스턴스 접근(o) / 클래스 접근(o)" ])
print(table)


class Korean:

    country = "한국"  # 클래스 변수 country

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


man = Korean("안근수", 37, "부산광역시 연제구")
print(man.country)      # 인스턴스 man을 통한 클래스 변수 접근
print(Korean.country)   # 클래스 Korean을 통한 클래스 변수 접근

# 클래스 변수는 클래스를 통해서 접근하는 것이 권장 사양 -> man.country보다는 Korean.country로 작성할 것

'''
p 279

2. 클래스 메서드

클래스 메서드(class method) : 클래스 변수를 사용하는 메서드.

특징 :

1. 인스턴스 또는 클래스로 호출
2. 생성된 인스턴스가 없어도 호출할 수 있음.
3. @classmethod 데코레이터(decorator)를 표시하고 작성
4. 매개변수 self를 사용하지 않고 cls를 사용

호출 방식 :

클래스.메서드()와 같은 형식으로 호출.
self를 사용하지 않기 때문에 인스턴스 변수에 접근 불가능. cls를 통해 class 변수에 접근 가능.
'''

class Korean2:

    country = "대한민국"    # 클래스 변수

    @classmethod
    def trip(cls, country):
        if cls.country == country:
            print("국내 여행입니다.")
        else:
            print("해외 여행입니다.")


Korean2.trip("대한민국")
Korean2.trip("미국")

'''
Korean2 클래스에 정의된 trip() 메서드는 클래스 메서드임을 알리는 @classmethod로 시작합니다.
첫번째 매개변수인 cls는 클래스의 줄임말로, 여기서는 클래스 Korean2를 의미합니다. 따라서 내부의
cls.country는 Korean.country와 같은 의미. 이를 클래스 내부에서는 cls.country로 표기됨.
클래스 메서드는 인스턴스를 생성하지 않아도 클래스만으로 호출 가능 즉,
Korean2.trip()으로 호출 가능합니다.


p 280
정적 메서드(static method)

정적 메서드 역시 self를 사용하지 않기 때문에 인스턴스 변수를 사용할 수 없습니다.
인스턴스를 생성하지 않아도 사용할 수 있다는 점 때문에 클래스 메서드와 비슷합니다.

특징

1. 인스턴스 또는 클래스로 호출 가능
2. 생성된 인스턴스가 없어도 호출 가능
3. @staticmethod 데코레이터를 표시하고 작성
4. 반드시 작성해야 할 매개변수가 없습니다.

정적 메서드는 self, cls를 다 사용하지 않기 때문에 인스턴스 변수와 클래스 변수를 모두 사용하지 않는 메서드를
정의하는 경우에 적절합니다. 정적 메서드는 클래스에 소속되어 있지만, 인스턴스에는 영향을 주지도 않고 또 인스턴스로부터
영향을 받지도 않습니다.
'''

class Korean3:

    country = "한국"      # 클래스 변수

    @staticmethod
    def slogan():       # 클래스 변수 및 인스턴스 변수를 모두 사용하지 않음
        print("Imagine your Korea")


Korean3.slogan()        # 인스턴스 생성 없이 사용함

'''
기본 예제

다음은 가방을 만들 때마다 현재 만들어진 가방이 몇 개인지 계산할 수 있는 Bag 클래스입니다.
'''

class Bag:

    count = 0       #클래스 변수

    def __init__(self):
        Bag.count += 1

    @classmethod
    def sell(cls):
        cls.count -= 1

    @classmethod
    def reamin_bag(cls):
        return cls.count

print(f"현재 가방 : {Bag.reamin_bag()}")
bag1 = Bag()
bag2 = Bag()
bag3 = Bag()
print(f"현재 가방 : {Bag.reamin_bag()}")
bag1.sell()
bag2.sell()
print(f"현재 가방 : {Bag.reamin_bag()}")

