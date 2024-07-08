'''
응용예제

다음 지시사항을 읽고 책 제목과 저자 정보를 저장할 수 있는 Book클래스를 생성하세요.

지시사항
1. 책 제목과 저자 정보를 출력하는 print_info() 메서드를 구현하세요.
2. 다음과 같은 방법으로 book1과 book2 인스턴스를 생성하세요.

#book1, book2 인스턴스의 생성
book1 = Book()
book2 = Book()

#book1, book2 제목과 저자 정보 저장
book1.set_info("파이썬", "민경태")
book2.set_info("어린왕자", "생텍쥐페리")

실행 예
책 제목 : 파이썬
책 저자 : 민경태
책 제목 : 어린왕자
책 저자 : 생텍쥐페리
'''

'''
아래는 지시사항을 바탕으로 `Book` 클래스를 작성한 예제입니다.

```python
class Book:
    def __init__(self):
        self.title = ""
        self.author = ""

    def set_info(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print(f"책 제목 : {self.title}")
        print(f"책 저자 : {self.author}")

# book1, book2 인스턴스의 생성
book1 = Book()
book2 = Book()

# book1, book2 제목과 저자 정보 저장
book1.set_info("파이썬", "민경태")
book2.set_info("어린왕자", "생텍쥐페리")

# 정보 출력
book1.print_info()
book2.print_info()
```

### 코드 설명

1. **클래스 정의**
    - `Book` 클래스를 정의합니다.
    - `__init__` 메서드를 사용하여 `title`과 `author` 인스턴스 변수를 초기화합니다. 초기값은 빈 문자열입니다.

2. **set_info 메서드**
    - `set_info` 메서드는 두 개의 매개변수를 받습니다: `title`과 `author`.
    - 이 메서드는 인스턴스 변수 `title`과 `author`를 각각 입력 받은 값으로 설정합니다.

3. **print_info 메서드**
    - `print_info` 메서드는 인스턴스 변수 `title`과 `author`의 값을 출력합니다.
    - f-string을 사용하여 출력 형식을 지정합니다.

4. **인스턴스 생성 및 정보 설정**
    - `book1`과 `book2` 인스턴스를 생성합니다.
    - `set_info` 메서드를 호출하여 각각의 책 제목과 저자 정보를 설정합니다.

5. **정보 출력**
    - `print_info` 메서드를 호출하여 책의 제목과 저자 정보를 출력합니다.

### 실행 예
위 코드를 실행하면 다음과 같은 출력이 나타납니다:

```
책 제목 : 파이썬
책 저자 : 민경태
책 제목 : 어린왕자
책 저자 : 생텍쥐페리
```

이렇게 하면 각 책 객체에 대해 제목과 저자 정보를 설정하고 출력할 수 있습니다.
'''

class Book:
    # def __init__(self):
    #     self.title = ""
    #     self.author = ""

    def set_info(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print(f"책 제목 : {self.title}")
        print(f"책 저자 : {self.author}")

# book1, book2 인스턴스의 생성
book1 = Book()
book2 = Book()

# book1, book2 제목과 저자 정보 저장
book1.set_info("파이썬", "민경태")
book2.set_info("어린왕자", "생텍쥐페리")

# 정보 출력
book1.print_info()
book2.print_info()