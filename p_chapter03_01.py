#객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트 등 
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡 
# 클래스 중심 -> 데이터 중심 -> 객체로 관리 

class Car():
    """
    Car class 
    Author : choi
    Date : 2022.01.15
    Description : Class, Static, Instance Method
    """

    # 클래스 변수 
    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0


    def __init__(self, company, details):
        self._company = company
        self._details = details
        

    #사용자 입장
    def __str__(self):
        return 'str: {} - {}'.format(self._company, self._details)

    #객체 그대로 출력 (개발자 입장)
    def __repr__(self):
        return 'repr: {} - {}'.format(self._company, self._details)

    #Instance Method
    #self : 객체의 고유한 속성값 사용
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))
    

    #Instance Method
    def get_price(self):
        return 'Before Car Price -> company : {}, Price : {}'.format(self._company, self._details.get('price'))
    
    #Instance Method
    def get_price_cul(self):
        return 'After Car Price -> company : {}, Price : {}'.format(self._company, self._details.get('price')* Car.price_per_raise)
    

    #Class Method / 모든 클래스 공유
    @classmethod
    def raise_price(cls, per):
        #cls = Car
        if per <= 1:
            print('Please Enter 1 or more')
            return
        cls.price_per_raise = per
        print('Succeed!')
    

    #Static Method / parameter 없음
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'BMW':
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry, This car is not BMW'
    

     
    
# self 의미 --> instance 메소드 / 각 고유의 값을 저장하기 위한 예약어 
car1 = Car('Ferrari',{'color':'White','horsepower':400, 'price':8000})
car2 = Car('BMW',{'color':'Black','horsepower':400, 'price':8000})

#가격정보 // 직접 접근은 권장하지 않음
print(car1._details.get('price'))

#가격정보 (인상 전)
print(car1.get_price())
print(car2.get_price())

#가격 인상 (클래스 메소드 미사용)
Car.price_per_raise = 1.4

print(car1.get_price_cul())
print(car2.get_price_cul())

#클래스 메소드 사용
Car.raise_price(3)

#인스턴스 호출
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

#클래스 메소드로 출력 가능 / 유연하게 사용 가능
print(Car.is_bmw(car1))


