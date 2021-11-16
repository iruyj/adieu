import json
from json_use import UseJSON as json


class User:
    def __init__(self):  # 원래 등록된 user들 가져오기
        self.name = ""
        self.id = ''
        self.zip_code =''
        self.introduce = ''
        self.pw = ''
        self.age = 000000
        self.gender = 'w'
        self.number = ''
        self.input_list = []

    def check_all(self, input_list, gender):
        # inputList : [name, age, id, pw, pw_check, zipcode, call_number, introduce]
        # gender : 성별구분 라디오버튼 잇음 -> 1 = 여자 / 2 = 남자
        # 각자 빈칸 & 형식체크 후 self변수에 값 넣기 / 체크에서 오류날경우 해당 메세지 반환/ 잘들어갔을경우 True반환
        self.input_list = input_list
        # user 객체 보내기 :이름 입력받기
        self.set_name()
        # 비밀번호 설정
        self.set_pw()
        # 생년월일
        self.set_age()
        # 성별
        self.set_gender()
        # 전화번호
        self.set_number()
    
    # 중복체크
    def set_name(self):  # 매개변수로 이름
        ids = json.get_user_json(self)
        # 중복되는 이름이 없으면 나옴
        if self.input_list[2] in ids:   # 이미 이름이 있으면 false 반환
            return True
        return 2     # 이름 없으면 이름 인덱스 반환

    # 비밀번호 입력
    def set_pw(self):
        pw = input('비밀번호 입력 → ')

        while True:
            ver_pw = input('비밀번호 확인 → ')

            if pw == ver_pw:
                self.pw = pw
                break
            else:
                print('꒦꒷꒷꒦꒦꒷잘못 입력했습니다(>_<｡)💦 다시 입력하세요꒦꒷꒷꒦꒷꒦꒷')

    # 나이 입력
    def set_age(self):
        while True:
            age = input('생일 ex(20040810) → ')
            if len(age) == 8:
                self.age = age
                break
            else:
                print('꒦꒷꒷꒦꒦꒷잘못 입력했습니다(>_<｡)💦 다시 입력하세요꒦꒷꒷꒦꒷꒦꒷')

    # 성별 입력
    def set_gender(self):
        while True:
            gender = input('성별 w/m → ')
            if gender == 'w' :
                self.gender = '여자'
                break
            elif gender == 'm':
                self.gender = '남자'
                break
            else:
                print('꒦꒷꒦꒷꒦꒷잘못 입력했습니다(>_<｡)💦 다시 입력하세요꒦꒷꒷꒦꒷꒦꒷')

    # 전화번호 입력
    def set_number(self):
        while True:
            number = input('전화번호 (숫자만) → ')

            if number.isdigit() == True:
                self.number = number
                break
            else:
                print('잘못 입력했습니다(>_<｡)💦 다시 입력하세요')

    # 올린 게시물이나 신청한 게시물 동물이름 리스트를 넘겨주면 이름과 종류 리스트를 반환한다.
    def show_uplist(self, this_list):     # 사용자 데이터의 올린게시물 리스트 가져오기
        if len(this_list) == 0:
            return 'none'

        animals = json.get_animals_json(self)
        apply_name =[]
        apply_kind =[]
        for i in this_list:
            apply_name.append(i)   # 게시물 이름
            apply_kind.append(animals[i]['species'])   # 게시물 종류
            # 올린 동물들 이름과 종류만

        return apply_name, apply_kind   # 이름과 종류 리스트 반환


    # 사용자 정보 확인
    def __str__(self):
        # 사용자 정보로 수정
        return f'  ✔ 이름 : {self.name}\n  ✔ 성별 : {self.gender}\n  ✔ 전화번호 : {self.number}'