class Car():
    """
    Car class 
    Author : choi
    Date : 2022.01.15
    """

    # 클래스 변수 
    # 클래스 변수(모든 인스턴스가 공유)
    car_count = 0


    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    #사용자 입장
    def __str__(self):
        return 'str: {} - {}'.format(self._company, self._details)

    #객체 그대로 출력 (개발자 입장)
    def __repr__(self):
        return 'repr: {} - {}'.format(self._company, self._details)


    def __del__(self):
        print('del?')
        Car.car_count -= 1


    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))


# self 의미 --> instance 메소드 / 각 고유의 값을 저장하기 위한 예약어 
car1 = Car('Ferrari',{'color':'White','horsepower':400, 'price':8000})
car2 = Car('BMW',{'color':'Black','horsepower':400, 'price':8000})
car3 = Car('Audi',{'color':'Silver','horsepower':400, 'price':8000})

# ID 확인 
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

# dir & __dic__ 확인 
# 포괄적인 list 형태
print(dir(car1))
print(dir(car2))

print()
print()

#dic 형태 
print(car1.__dict__)
print(car2.__dict__)

# Doctring 
# 주석 찾기 
print(Car.__doc__)

print()
print()

car1.detail_info()
car2.detail_info()

print()

#비교
#class는 같지만 id 값은 서로 다름
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__))


# 에러
# 인자를 넘기지 않았기 때문에 에러
Car.detail_info(car2)


# 공유 확인
print(car1.__dict__)
print(car1.car_count)
print(dir(car1))

# 접근
print(car1.car_count)
print(Car.car_count)


del car2
#삭제 확인
print(car1.car_count)
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색 
# 즉, 동일한 이름으로 변수 생성 가능 (인스턴스 검색 후 -> 상위(클래스 변수, 부모클래스 변수))








