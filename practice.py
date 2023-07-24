#숫자 자료형
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))

#문자열
# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋ")
# print("ㅋ"*9)

# #bolean자료형
# #참/거짓 형
# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not(5>10))

#변수
#애완동물을 소개해 주세요
#print("우리집 강아지의 이름은 연탄이에요")
#print("연탄이는 4살이며, 산책을 아주 좋아해요")
#print("연탄이는 어른일까요?  True")

# animal = "고양이"
# name = "해피"
# age = 4
# hobby = "낮잠"
# is_adult = age >= 3

# ''' 이렇게 
# 하면
# 여러문장이
# 주석처리
# 됩니다.'''


# print("우리집 " + animal + "의 이름은 " + name + "에요")
# #print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name,"는 " , age,"살이며, " , hobby,"을 아주 좋아해요")
# print(name + "는 어른일까요? " +str(is_adult))

#quiz ) 변수를 이용하여 다음 문장을 출력하시오

#변수명
# : station

#변수값
# : "사당","신도림","인천공항" 순서대로 입력

# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다.")


# 연산자
# print(1+1) #2
# print(3-2) #1
# print(5*2) #10
# print(6/3) #2

# print(2**3) #2^3
# print(5%3) #나머지 구하기 2
# print (10%3) #1 
# print(5//3) #몫을 구하기 1
# print (10//3) #3

# 비교연산
# print(10>3) #True
# print(4 >= 7) # False
# print(10 < 3) # False
# print( 5 <= 5) # True
# print(3 == 3) # 앞의 항과 뒤의 항이 같다 True
# print(4 == 2) # False
# print(3 + 4 == 7) # True
# print(1 != 3) # 앞뒤가 같지 않다 True
# print(not(1 != 3)) #not은 결과를 반대로 계산 False
# print((3>0) and (3<5)) # True
# print((3>0) & (3<5)) # True (and의 기호 &)
# print((3>0) or (3<5)) # True
# print((3>0) | (3>5)) # True ( or의 기호|)
# print(5>4>3) # True
# print(5>4>7) # False

#간단한 수식
# print(2+3*4) #14
# print((2+3)*4) #20 
# number=2+3*4
# print(number) #14
# number =  number +2
# print(number) #16
# number += 2
# print(number) #18
# number *= 2
# print(number) #36
# number /= 2 
# print(number) #18
# number -= 2 
# print(number) #16
# number %= 5   # 나머지 구하기
# print(number) #1 

#숫자 처리 함수
# print(abs(-5)) # 5 (절대 값 반환하는 함수)
# print(pow(4,2)) # 4^2 =4*4 =16
# print(max(5,12)) # 12 (입력된 값중 가장 큰값을 반환)
# print(min(5,12)) # 5 (입력된 값중 가장 작은 값을 반환)
# print(round(3.14)) # 3 (반올림에서 3을 반환)
# print(round(4.99)) # 5 (반올림 해서 5를 반환)

# from math import * # math library 에 있는 모든 것을 이용하겠다는 의미
# print(floor(4.99)) # 4(소숫점 아래는 내림)
# print(ceil(3.14)) # 4(소숫점 아래는 오림)
# print(sqrt(16)) # 4 (제곱근을 반환)

#랜덤함수
# from random import * # random library에 있는 함수를 사용

# print(random()) #0.0이상 1.0 미만의 임의의 값을 생성
# print(random()*10) #0.0이상 10.0 미만의 임의의 값을 생성
# print(int(random() * 10)) # 0.0이상 10.0 미만의 임의의 정수값을 생성
# print(int(random() * 10)) # 0.0이상 10.0 미만의 임의의 정수값을 생성
# print(int(random() * 10)) # 0.0이상 10.0 미만의 임의의 정수값을 생성
# print(int(random() * 10)+1) # 1.0이상 10.0 이하의 임의의 정수값을 생성
# print(int(random() * 10)+1) # 1.0이상 10.0 이하의 임의의 정수값을 생성
# print(int(random() * 10)+1) # 1.0이상 10.0 이하의 임의의 정수값을 생성
# print(int(random() * 10)+1) # 1.0이상 10.0 이하의 임의의 정수값을 생성
# print(int(random() * 10)+1) # 1.0이상 10.0 이하의 임의의 정수값을 생성
# print(int(random() * 10)+1) # 1.0이상 10.0 이하의 임의의 정수값을 생성

# print(int(random() * 65)+1) # 1.0이상 65.0 이하의 임의의 정수값을 생성(로또)
# print(int(random() * 65)+1) # 1.0이상 65.0 이하의 임의의 정수값을 생성(로또)
# print(int(random() * 65)+1) # 1.0이상 65.0 이하의 임의의 정수값을 생성(로또)
# print(int(random() * 65)+1) # 1.0이상 65.0 이하의 임의의 정수값을 생성(로또)
# print(int(random() * 65)+1) # 1.0이상 65.0 이하의 임의의 정수값을 생성(로또)
# print(int(random() * 65)+1) # 1.0이상 65.0 이하의 임의의 정수값을 생성(로또)
# print(int(random() * 65)+1) # 1.0이상 65.0 이하의 임의의 정수값을 생성(로또)

# print(randrange(1,66)) # 1~66미만의 임의의 값 생성
# print(randrange(1,66)) # 1~66미만의 임의의 값 생성
# print(randrange(1,66)) # 1~66미만의 임의의 값 생성
# print(randrange(1,66)) # 1~66미만의 임의의 값 생성
# print(randrange(1,66)) # 1~66미만의 임의의 값 생성
# print(randrange(1,66)) # 1~66미만의 임의의 값 생성

# print(randint(1,65)) # 1~65이하의 임의의 값 생성
# print(randint(1,65)) # 1~65이하의 임의의 값 생성
# print(randint(1,65)) # 1~65이하의 임의의 값 생성
# print(randint(1,65)) # 1~65이하의 임의의 값 생성
# print(randint(1,65)) # 1~65이하의 임의의 값 생성
# print(randint(1,65)) # 1~65이하의 임의의 값 생성

#퀴즈
# 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
#월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래의 조간에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 :  월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함
# 조건3 :  매월 1~3일은 스터디 준비를 해야하므로 제외

#출력 문 예제
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

# from random import *
# date =(randrange(4,29)) 
# date = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월" + str(date)+ "로 선정되었습니다.")

#문자열
# sentence = '나는 소년입니다.'
# print(sentence) # 나는 소년입니다.
# sentence2 =  "파이썬은 쉬워요."
# print(sentence2) # 파이썬은 쉬워요.
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요.
# """
# print(sentence3)

# 나는 소년이고,
# 파이썬은 쉬워요.

#슬라이싱 (필요한 부분만 잘라서 가져오는것)
# jumin = "990120-1234567" #인덱스는 0부터 시작 즉, 성별의 경우 7의 값이 성별이됨

# print("성별 : " + jumin[7]) # 성별 : 1
# print("연 : " + jumin[0:2]) # 연 : 99, 0부터 2직전까지(0,1)의 인덱스값을 가져와라
# print("월 : " + jumin[2:4]) # 월 : 01, 2부터 4직전까지(2,3)의 인덱스값을 가져와라
# print("일 : " + jumin[4:6]) # 일 : 20, 4부터 6직전까지(4,5)의 인덱스값을 가져와라

# print("생년월일 : " + jumin[0:6]) #생년월일 : 990120, 처음 부터 6 직전까지(0,5)의 인덱스 값을 가져와라
# print("생년월일 : " + jumin[:6]) #생년월일 : 990120, 이경우 맨 앞의 인덱스를 생략할수 있음
# print("뒤 7자리 : " + jumin[7:14]) # 뒤 7자리 : 1234567, 7부터 14직전까지(7,13)의 인덱스값을 가져와라
# print("뒤 7자리 : " + jumin[7:]) # 뒤 7자리 : 1234567, 이 경우 맨 뒤의 인덱스를 생략할수 잇음
# print("뒤 7자리(뒤에서 부터) : " + jumin[-7:]) # 뒤 7자리(뒤에서 부터) : 1234567, 맨뒤에서 시작일경우 -1부터 시작


#문자열 처리함수
# python = "Python is Amazing"
# print(python.lower()) #python is amazing, lower : 모든 문자를 소문자로 만든다.
# print(python.upper()) #PYTHON IS AMAZING, upper : 모든 문자를 대문자로 만든다.
# print(python[0].isupper()) #True, 0번 인덱스의 값이 대문자인지 확인
# print(len(python)) #17, len: 전체 문자열의 길이를 반환해줌
# print(python.replace("Python","Java")) #Java is Amazing, replace : 문장안의 Python이라는 값을 Java로 변경가능

# index = python.index("n")
# print(index) #5, index : 문자가 위치해 있는 index를 번호 찾기
# index = python.index("n", index + 1)
# print(index) #15, 처음에 찾은 인텍스 다음의 n의 문자가 있는 index번호를 찾기

# print(python.find("n")) #5, find : index와 비슷한 명령어
# print(python.find("Java")) #-1, find명령어를 사용할때 해당문자가 없을경우 -1을 반환한다.
# print(python.index("Java")) #error발생 ,  index명령어를 사용할 경우 해당문자가 없으면 error를 반환하고 끝낸다.즉 뒤에 문장이 있어서 중간에 끝냄.
# print("hi") # index명령어를 사용시 hi를 print하지 않음

# print(python.count("n")) #2, python이라는 변수에서 n문자가 몇개 있는지 반환

#문자열 포멧
# print("a" + "b")
# print("a","b")

#방법 1
# print("나는 %d살입니다." % 20) #나는 20살입니다., %d : 정수만 반환
# print("나는 %s를 좋아해요." % "파이썬") #나는 파이썬를 좋아해요., %s:문자열 혹은 정수를 반환하겠다는 의미
# print("Apple 은 %c로 시작해요." % "A") #Apple 은 A로 시작해요., %c : character로써 한글자만 받겠다는 의미
# print("나는 %s살입니다." % 20) #나는 20살입니다.
# print("나는 %s색과 %s색을 좋아해요." %("파란","빨간")) #나는 파란색과 빨간색을 좋아해요.

#방법 2
# print("나는 {}살입니다.".format(20)) #나는 20살입니다.
# print("나는 {}색과 {}색을 좋아해요." .format("파란","빨간")) #나는 파란색과 빨간색을 좋아해요.
# print("나는 {0}색과 {1}색을 좋아해요." .format("파란","빨간")) #나는 파란색과 빨간색을 좋아해요.
# print("나는 {1}색과 {0}색을 좋아해요." .format("파란","빨간")) #나는 빨간색과 파란색을 좋아해요.

#방법3
# print("나는{age}살이며, {color}색을 좋아해요.".format(age =20, color="빨간")) #나는20살이며, 빨간색을 좋아해요.
# print("나는{age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20)) #나는20살이며, 빨간색을 좋아해요.

#방법 4
# age =20
# color = "빨간"
# print(f"나는{age}살이며, {color}색을 좋아해요.") #나는20살이며, 빨간색을 좋아해요. 이경우 f를 사용하면 동일한 결과를 얻을수 있다


#탈출문자
#\n : 줄을 바꿔 print한다.
# print("백문이 불여일견 \n벽견이 불여일타") #백문이 불여일견  \n을 이용해서 줄바꿔서 출력할수 있는데 이를 탈출이라고 함.
                                         #벽견이 불여일타

#\" \' : 문장 내에서 따옴표처럼 사용할수 있다
#저는 "나도코딩"입니다.
# print("저는 '나도코딩'입니다.") #저는 '나도코딩'입니다.
# print('저는 "나도코딩"입니다.') #저는 "나도코딩"입니다.
# print("저는 \"나도코딩\"입니다.") #저는 "나도코딩"입니다.
# print("저는 \'나도코딩\'입니다.") #저는 '나도코딩'입니다.

#\\ : 문장내에서는 하나의 \로 바뀌게 된다.
# print("C:\Users\SungSoo Kim\Desktop\PYTHON>") #print하면 error가 발생
# print("C:\\Users\\SungSoo Kim\\Desktop\\PYTHON>") #C:\Users\SungSoo Kim\Desktop\PYTHON>, \\를 사용하면 하나의 \로 변경하여 error가 발생하지 않는다.

#\r : 커서를 맨 앞으로 이동
# print("Red Apple\rpine") #pineApple, pine(4자리)을 맨앞으로 이동한다.

#\b : 백스페이스 역할(한글자 삭제)
# print("Redd\bApple") #RedApple, Redd에서 d한 글자를 삭제한다.

#\t  :탭역할 한다.
# print("Red\tApple") #Red     Apple, 탭역할을 한다.



#퀴즈3
# quiz : 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세글자 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

# 예)생성된 비밀번호 : nav51!
#방법 1 (내가 푼 방법)
# url = "http://naver.com"
# ru1 = url[7:16] #naver.com, url에서 7번~15번 index값을 가져와라
# ru2 = ru1[0:5] #naver, ru1에서 0~4번의 index값을 가져와라
# password = ru2[0:3] + str(len(ru2)) + str(ru2.count("e")) + "!"
# print("{}의 비밀번호는 {}입니다.".format(url,password)) #http://naver.com의 비밀번호는 nav51!입니다.

#방법 2 (강의에서 푼 방법)
# url = "http://naver.com"
# my_str = url.replace("http://","") #naver.com, http://를 빈칸으로 바꿔라
# #print(my_str)
# my_str = my_str[:my_str.index(".")] #naver, 전체 문장에서 .(점)이 있는 index의 앞 까지 가져와라
# # print(my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는 {1}입니다.".format(url,password)) #http://naver.com의 비밀번호는 nav51!입니다.

#리스트 [] :순서를 가지는 집합의 개체

#지하철 칸별로 10명,20명,30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10,20,30]
# print(subway) #[10, 20, 30]

# subway = ["유재석","조세호","박명수"]
# print(subway) # ['유재석', '조세호', '박명수']

# #조세호싸기 몇번째 칸에 타고 있는가?
# print(subway.index("조세호")) #1

# #하하씨가 다음 정류장에서 다음칸에 탐
# subway.append("하하") #append : 맨 뒤에 더하다
# print(subway) #['유재석', '조세호', '박명수', '하하']

# #정형돈씨를 유재석/조세호 사이에 태워봄
# subway.insert(1,"정형돈") #index : 중간에 삽입, index + 문자 순으로 삽입
# print(subway) #['유재석', '정형돈', '조세호', '박명수', '하하']

# #지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop()) #하하, 맨뒤에 있는 사람을 뺀다.
# print(subway)       #['유재석', '정형돈', '조세호', '박명수'] , 맨뒤사람을 빼고 남은 사람들을 print

# # print(subway.pop()) #박명수
# # print(subway)       #['유재석', '정형돈', '조세호']

# # print(subway.pop()) #조세호
# # print(subway)       #['유재석', '정형돈']

# # print(subway.pop()) #정형돈
# # print(subway)       #['유재석']

# #같은 이름의 사람이명 몇 있는지 확인
# subway.append("유재석") #유재석을 맨 마지막에 삽입
# print(subway)                 #['유재석', '정형돈', '조세호', '박명수', '유재석']
# print(subway.count("유재석"))  #2, count를 사용하여 유재석이 몇번 있는지 확인

# #정렬도 가능
# num_list = [5,3,4,2,1]
# num_list.sort()
# print(num_list) #[1, 2, 3, 4, 5]

# #순서 뒤집기 가능
# num_list.reverse()
# print(num_list) #[5, 4, 3, 2, 1]

# #모두 지우기
# num_list.clear()
# print(num_list) #[], 안의 내용을 모두 지우기

# # 다양한 자료형 함께 사용
# num_list = [5,3,4,2,1]
# mix_list = ["조세호",20,True]
# # print(mix_list) #['조세호', 20, True]

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list) #[5, 3, 4, 2, 1, '조세호', 20, True]


#사전 {중괄호를 이용}
# cabinet = {3:"유재석", 100:"김태호"} #key3을 유재석이가 쓰고, key100을  김태호가 쓰고 있다는 의미
# print(cabinet[3]) #유재석
# print(cabinet[100]) #김태호

# print(cabinet.get(3)) #유재석

# print(cabinet[5]) #key5에 값이 없기 때문에 error가 발생
# print(cabinet.get(5)) #None, 5에 값이 없기때문에 None로 표현
# print(cabinet.get(5,"사용가능")) #사용가능

# print(3 in cabinet) #True, key3에 값이 있기 때문에 True를 반환
# print(5 in cabinet) #False, key5에 값이 없기 때문에 False를 반환

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# # print(cabinet["A-3"]) #유재석
# # print(cabinet["B-100"]) #김태호

# #새 손님
# print(cabinet) #{'A-3': '유재석', 'B-100': '김태호'}
# cabinet["A-3"] = "김종국" #A-3에 유재석 대신에 김종국을 삽입
# cabinet["C-20"] = "조세호" #C-20에 조세호를 삽입
# print(cabinet) #{'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# #간 손님
# del cabinet["A-3"] #A-3을 삭제
# print(cabinet) #{'B-100': '김태호', 'C-20': '조세호'}

# #KEY 들만 출력
# print(cabinet.keys()) #dict_keys(['B-100', 'C-20']), key만 print

# #value 들만 출력
# print(cabinet.values()) #dict_values(['김태호', '조세호']), 값들만 print

# #key와 value를 모두 출력
# print(cabinet.items()) #dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# #목욕탕 폐점
# cabinet.clear()
# print(cabinet) #{}


#튜플 (내용변경이나 추가를 할수 없다, 속도가 list보다 빠르다 )
# menu = ("돈까스","치즈까스")
# print(menu[0]) #돈까스
# print(menu[1]) #치즈까스

# # name = "김종국"
# # age = 20
# # hobby = "코딩"
# # print(name,age,hobby) #김종국 20 코딩

# (name,age,hobby) = ("김종국",20,"코딩")
# print(name,age,hobby) #김종국 20 코딩


#세트 (set,집합) => 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3} #
# print(my_set) #{1, 2, 3},중복이 허용되지 않음으로 1,2,3만 들어감

# java = {"유재석","김태호","양세형"}
# python = set(["유재석","박명수"])



# #교집합 (java와 python을 모두 할수 잇는 개발자)
# print(java & python) #{'유재석'}
# print(java.intersection(python)) #{'유재석'}

# #합집합(java 할수 있거나 python도 할수 있는 개발자)
# print(java | python) #{'김태호', '유재석', '양세형', '박명수'}, print하는 순서는 random
# print(java.union(python)) #{'김태호', '유재석', '양세형', '박명수'}

# #차집합(java는 할수 있지만 python은 할줄 모르는 개발자)
# print(java - python) #{'양세형', '김태호'}
# print(java.difference(python)) #{'양세형', '김태호'}

# #python을 할 주 ㄹ 아는 사람이 들어남
# python.add("김태호") #김태호 삽입
# print(python) #{'김태호', '유재석', '박명수'}

#  #java를 잊어 버림
# java.remove("김태호") #김태호 삭제
# print(java) #{'양세형', '유재석'}



#자료 구조의 변경
 #커피숍
# menu = {"커피","우유","주스"}
# print(menu, type(menu)) #{'주스', '커피', '우유'} <class 'set'>, 중괄호는 set

# menu = list(menu)
# print(menu, type(menu)) #['커피', '우유', '주스'] <class 'list'>, 대괄호는 list

# menu = tuple(menu)
# print(menu, type(menu)) #('커피', '우유', '주스') <class 'tuple'>, 소괄호는 tuple

# menu = set(menu)
# print(menu, type(menu)) #{'커피', '우유', '주스'} <class 'set'>


#quiz) 당산의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨,3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 :  편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample을 활요

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하 합니다 --

# (활용 예제)
# from random import *
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# # print(lst)
# shuffle(lst)
# # # print(lst)
# print(sample(lst, 1))

# print("-- 당첨자 발표 --")                          #-- 당첨자 발표 --
# print("치킨 당첨자 : ",sample(lst,1))               #치킨 당첨자 :  [14]
# print("커피 당첨자 : ",sample(lst,3))               #커피 당첨자 :  [17, 5, 13]
# print("-- 축하 합니다 --")                          #-- 축하 합니다 --

# from random import *
# users = range(1,21) #1부터 20까지의 숫자를 생성
# # print(type(users)) #<class 'range'>
# users = list(users)
# # print(type(users))
# print(users)
# shuffle(users)
# print(users)

# winners = sample(users,4)
# print("-- 당첨자 발표 --")                        #-- 당첨자 발표 --
# print("치킨 당첨자 : {}".format(winners[0]))      #치킨 당첨자 : 7
# print("커피 당첨자 : {}".format(winners[1:]))     #커피 당첨자 : [4, 8, 6]
# print("-- 축하 합니다 --")                        #-- 축하 합니다 --




#IF문
# weather = "맑음"
# if weather == "비":
#     print("우산을 챙기세요") #우산을 챙기세요, weather가 "비"인 경우에
# elif weather == "미세먼지":
#     print("마스크를 챙기세요") #마스크를 챙기세요, weather가 "미세먼지"인 경우에
# else:
#     print("준비물 필요 없어요") #준비물 필요 없어요, weather가 "비" 혹은 "미세먼지"가 아닌 경우에

# weather = input("오늘 날씨 어때요? ") #오늘 날씨 어때요? print하면서 input을 기다린다.
# if weather == "비":
#     print("우산을 챙기세요") #우산을 챙기세요, input이 "비"인 경우에
# elif weather == "미세먼지":
#     print("마스크를 챙기세요") #마스크를 챙기세요, input이 "미세먼지"인 경우에
# else:
#     print("준비물 필요 없어요") #준비물 필요 없어요, input이 "비" 혹은 "미세먼지"가 아닌 경우에

# weather = input("오늘 날씨 어때요? ") #오늘 날씨 어때요? print하면서 input을 기다린다.
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요") #우산을 챙기세요, input이 "비" 혹은 "눈"인 경우에
# elif weather == "미세먼지":
#     print("마스크를 챙기세요") #마스크를 챙기세요, input이 "미세먼지"인 경우에
# else:
#     print("준비물 필요 없어요") #준비물 필요 없어요, input이 "비","눈" 혹은 "미세먼지"가 아닌 경우에

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요.나가지 마세요")   #너무 더워요.나가지 마세요, temp가 30도 이상인 경우
# elif 10 <= temp and temp <30:
#     print("괜찮은 날씨에요")            #괜찮은 날씨에요, temp가 10도이상 30도 미만인 경우
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")            #외투를 챙기세요, temp가 0도이상 10도 미만인 경우
# else:
#     print("너무 추워요. 나가지 마세요")  #너무 추워요. 나가지 마세요, temp가 0도 미만인 경우


#for 문 (반복문)
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in[0,1,2,3,4]:
#     print("대기번호 : {0}".format(waiting_no)) #대기번호 : 0 , 0부터 4번까지 순차적으로 waiting_no에 숫자를 넣어서print한다.
#                                                #대기번호 : 1
#                                                #대기번호 : 2
#                                                #대기번호 : 3
#                                                #대기번호 : 4


# for waiting_no in range(5): #0부터 4까지 번호를 생성해서 waiting_no에 넣는다.
    # print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(1,6): #1부터 5까지 번호를 생성해서 waiting_no에 넣는다.
#     print("대기번호 : {0}".format(waiting_no)) #대기번호 : 1부터 5까지 print한다.

# starbucks = ["아이언맨","토르","아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer)) #아이언맨, 커피가 준비되었습니다. #토르, 커피가 준비되었습니다. 아이엠 그루트, 커피가 준비되었습니다.

#반복문 while(조건을 만족 할때까지 수행)
# customer = "토르"
# index =5
# while index >= 1:
#     print("{0},커피가 준비되었습니다. {1}번 남았어요".format(customer,index))
#     index -= 1 #인덱스를 하나씩 줄인다.
#     if index == 0:
#         print("커피는 폐기 처분되었습니다.") 

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0},커피가 준비되었습니다. 호출 {1}회".format(customer,index))
#     index += 1


# customer = "토르"
# person = "Unknown"

# while person != customer : #person이 customer와 동일하지않으면 while문을 반복
#     print("{0},커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ") #person을 입력


#continue와 break
# absent = [2,5]
# for student in range(1,11): #1,2,3,4,5,6,7,8,9,10의 번호를 생성
#     if student in absent: #absent가 student에 안에 있다면 loop반복을 진행함
#         continue
#     print("{0}, 책을 읽어봐".format(student)) #2번과 5번은 absent에 있음으로 continue를 진행하지 않고 다음 반복으로 넘어감



# absent = [2,5]
# no_book = [7]
# for student in range(1,11): #1,2,3,4,5,6,7,8,9,10의 번호를 생성
#     if student in absent: #absent가 student에 안에 있다면 loop반복을 진행함
#         continue
#     elif student in no_book:
#         print("오늘 수업은 여기까지.{0}은 교무실로 따라와".format(student))
#         break # no_book을 만족한다면 여기서 강제 종료
#     print("{0}, 책을 읽어봐".format(student)) #2번과 5번은 absent에 있음으로 continue를 진행하지 않고 다음 반복으로 넘어감


#한 줄 for
#예제 1
# #출석 번호가 1 2 3 4, 앞에100을 붙이기로 함 >> 101,102,103,104
# students = [1,2,3,4,5]
# print(students) #[1, 2, 3, 4, 5]
# students = [i+100 for i in students]
# print(students) #[101, 102, 103, 104, 105]

#예제 2
#학생 이름을 길이로 변환 (문자를 길이로 변환)
# students = ["Iron man","Thor","I am groot"]
# students = [len(i) for i in students]
# print(students) #[8, 4, 10]

#예제 3
#학생이름을 대문자로 변환
# students = ["Iron man","Thor","I am groot"]
# students = [i.upper() for i in students]
# print(students) #['IRON MAN', 'THOR', 'I AM GROOT']


#Quiz 5
# 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번재 손님 (소요시간 : 16분)

# 총 탑승 승객  :2분

# from random import *
# cnt = 0 #총 탑승 승객수
# for i in range(1,51): # 1~50 이라는 수(승객 수)
#     time = randrange(5,51) # 5분 ~ 50분 소요시간(조건1)
#     if 5 <= time <= 15:  # 5분 ~ 15분 이내의 손님 매칭 성공(조건2), 탑승 승객 증가 처리
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else: # 매칭 실패한 경우기 이기 때문에 cnt를 증가하지 않음
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
 
# print("총 탑승 승객  : {0}분".format(cnt))


# #함수
# # def open_account(): #함수를 정의할때는 def로 정의함
# #     print("새로운 계좌가 생성되었습니다.") #함수는 호출을 하기 전까지는 정의만 할 뿐이지 실행되지 않음 
# # open_account() #새로운 계좌가 생성되었습니다., 함수를 호줄

# #전달값과 반환값
# #입금
# def open_account(): #함수를 정의할때는 def로 정의함
#     print("새로운 계좌가 생성되었습니다.") #함수는 호출을 하기 전까지는 정의만 할 뿐이지 실행되지 않음 

# def deposit(balance, money): #입금의 함수에는 잔액과 현재 입금하려는 금액을 받아서 활요
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money)) #입금이 완료되었습니다. 잔액은 1000 원입니다.
#     return balance + money

# balance = 0
# balance = deposit(balance,1000)
# print(balance) #1000

# 출금
# def open_account(): #함수를 정의할때는 def로 정의함
#     print("새로운 계좌가 생성되었습니다.") #함수는 호출을 하기 전까지는 정의만 할 뿐이지 실행되지 않음  
#     open_account()

# def deposit(balance, money): #입금의 함수에는 잔액과 현재 입금하려는 금액을 받아서 활요
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money)) #입금이 완료되었습니다. 잔액은 1000 원입니다.
#     return balance + money

# def withdraw(balance, money): #현재 잔액과 출금하려는 금액
#     if balance >= money :
#         print("출금이 완료되었습니다. 잔약은 {0}원입니다.".format(balance - money))
#         return balance - money
#     else :
#         print("잔액이 부족합니다. 현재 잔액은 {0}원입니다.".format(balance)) #잔액이 부족합니다. 현재 잔액은 1000원입니다., 2000원을 출금하는 경우
#                                                                           #출금이 완료되었습니다. 잔약은 500원입니다., 500원을 출금하는 경우
#         return balance

# def withdraw_night(balance,money):
#     commission = 100
#     return commission, balance - money - commission

# balance = 0
# balance = deposit(balance,1000)
# # balance = withdraw(balance,2000)
# # balance = withdraw(balance,500)
# commission, balance =  withdraw_night(balance,500)
# print("commission은 {0}이며, 잔액은 {1}입니다.".format(commission,balance)) #commission은 100이며, 잔액은 400입니다.

#함수에서의 기본값
# def profile(name,age,main_lang):
#     print("이름 : {0}\t 나이 : {1}\t주 사용언어 : {2}"\
#           .format(name,age,main_lang)) #tip : 화면의 할줄에 다 담을수 없을시 문장에 \를 한후에 엔터를 처서 줄을 바꿀수 있다(줄은바꼈지만 한줄에 쓰여진것과 같음)
    
# profile("유재석",20,"파이썬")
# profile("김태호",20,"자바")

# #같은 학교 같은 학년 같은 반 같은 수업을 듣는 경우

# def profile(name,age=17,main_lang="파이썬"):
#         print("이름 : {0}\t 나이 : {1}\t주 사용언어 : {2}".format(name,age,main_lang))

# profile("유재석")
# profile("김태호")

#키워드값
# def profile(name,age,main_lang):
#     print(name,age,main_lang)

# profile(name="유재석", main_lang="파이썬",age=20) #키워드의 순서가 바뀌어 있어도 매개변수의 값을 잘 전달해 줌
# profile(main_lang="자바",age=25,name="김태호")


#가변인자를 이용한 함수 호출
# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ") #end=" " 의 이미는 줄바꾸지 않고 다음 문장을 실행한다는의미
#     print(lang1,lang2,lang3,lang4,lang5)
# profile("유재석", 20, "Python", "Java", "C", "C++","C#") #이름 : 유재석   나이 : 20        Python Java C C++ C#
# profile("김태호", 25, "Kotlin", "Swift", "", "","") #이름 : 김태호   나이 : 25        Kotlin Swift


#가변인자(서로 다른 갯수의 값을 넣어 줄때에 가변인자를 사용)
# def profile(name,age,*language):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ") #end=" " 의 이미는 줄바꾸지 않고 다음 문장을 실행한다는의미
#     for lang in language:
#         print(lang,end=" ")
#     print()

# profile("유재석", 20, "Python", "Java", "C", "C++","C#","Javascript") #이름 : 유재석   나이 : 20        Python Java C C++ C#
# profile("김태호", 25, "Kotlin", "Swift" ) #이름 : 김태호   나이 : 25        Kotlin Swift

#지역변수(함수내에서만 쓸수 있는것)와 전역변수(프로그램 어디서든 호출할수 있는것)
#지역변수
# gun = 10
# def checkpoint(soldiers) : #경계근무
#     gun = 20
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2) #2명이 경계근무 나감, 함수 호출
# print("남은 총 : {0}".format(gun))

#전역변수
# gun = 10
# def checkpoint(soldiers) : #경계근무
#     global gun #전역 공간에 있는 gun이라는 변수를 checkpoint 함수내에서 사용하겠다는 의미
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2) #2명이 경계근무 나감, 함수 호출
# print("남은 총 : {0}".format(gun))



# gun = 10
# def checkpoint(soldiers) : #경계근무
#     global gun #전역 공간에 있는 gun이라는 변수를 checkpoint 함수내에서 사용하겠다는 의미
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun,solders):
#     gun = gun - solders
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# # checkpoint(2) #2명이 경계근무 나감, 함수 호출
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))
# 

# Quiz 표중 체중을 구하는 프로그램을 작성하시오

# * 표준 체중  : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자  : 키(m) X 키(m) X 22
# 여자  : 키(m) X 키(m) X 21

# 조건1 : 표중 체중은 별도의 함수 내에서 계사
#        *함수 명 : std_weight
#        *전달 값 : 키(height), 성별(gender)
# 조건2 : 표중 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg입니다.

#방법 1
# def std_weight(height,gender): #키 m단위(실수),성별 "남자"/"여자"
#    if gender == "남자" :
#       return height * height * 22
#    else:
#       return height * height * 21

# height = int(input("키가 얼마에요?"))
# gender = input("성별을 입력하세요[남자 혹은 여자]?")

# weight = round(std_weight(height/100 , gender),2)
 
# print("키{0}cm {1}의 표준 체중은 {2}kg입니다.".format(height,gender,weight))

#방법 2
# def std_weight(height,gender): #키 m단위(실수),성별 "남자"/"여자"
#    if gender == "남자" :
#       weight = height * height * 22
#    else:
#       weight = height * height * 21

#    return weight
# height = int(input("키가 얼마에요[cm]?"))
# gender = input("성별을 입력하세요[남자 혹은 여자]?")

# weight = round(std_weight(height/100 , gender),2)
 
# print("키{0}cm {1}의 표준 체중은 {2}kg입니다.".format(height,gender,weight))

#표준 입출력
# print("Python","Java") #Python Java, (,)를 사용시 Python과 Java사이에 뛰어쓰기가 됨
# print("Python"+"Java") #PythonJava, (+)를 사용시 Python과 Java사이에 붙여쓰기가 됨
# print("Python","Java", sep=",") #Python,Java, sep을 사용하면 사이에 (,)가 들어가게 된다.
# print("Python","Java","JavaScript", sep=" vs ") #Python vs Java vs JavaScript
# print("Python","Java", sep=",", end="?") #Python,Java?무엇이 더 재밌을까요?, end="?"의 의미는 문장의 끝부분을 ?로 바꾸어 달라는 의미
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python","Java", file=sys.stdout) #Python Java, stdout는 표준 출력으로 처리되는 것
# print("Python","Java", file=sys.stderr) #Python Java, stderr는 표준 error로 처리되는것

#시험 성적 예제1
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items(): #items를 사용시 key와 value를 쌍으로 반환, 여기서 key는 subject이며, value는 score임.
#     print(subject,score)

#결과
#수학 0
#영어 50
#코딩 100

#시험 성적예제2
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items(): #items를 사용시 key와 value를 쌍으로 반환, 여기서 key는 subject이며, value는 score임.
#     print(subject.ljust(8),str(score).rjust(4),sep=":") #ljust(8) : left로 정렬하는데 총 8칸을 확보한 상태에서 정렬, rjust(4) : right로 4칸 확보해서 정렬
#                                                         #score는 정수값이기 때문에 str를 사용해서 문자열로 변경

# #결과
# 수학      :   0
# 영어      :  50
# 코딩      : 100

#은행 대기 순번표
#001,002,003,...
# for num in range(1,21):
#     print("대기번호 : " + str(num))
# #결과
# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# 대기번호 : 4
# 대기번호 : 5
# 대기번호 : 6
# 대기번호 : 7
# 대기번호 : 8
# 대기번호 : 9
# 대기번호 : 10
# 대기번호 : 11
# 대기번호 : 12
# 대기번호 : 13
# 대기번호 : 14
# 대기번호 : 15
# 대기번호 : 16
# 대기번호 : 17
# 대기번호 : 18
# 대기번호 : 19
# 대기번호 : 20

# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3)) #zfill : 0을 채우는것 zfill(3)은 3만큼의 공간을 확보한 후 값이 없는 공간에 대해서는 0을 채우는것

# #결과
# 대기번호 : 001
# 대기번호 : 002
# 대기번호 : 003
# 대기번호 : 004
# 대기번호 : 005
# 대기번호 : 006
# 대기번호 : 007
# 대기번호 : 008
# 대기번호 : 009
# 대기번호 : 010
# 대기번호 : 011
# 대기번호 : 012
# 대기번호 : 013
# 대기번호 : 014
# 대기번호 : 015
# 대기번호 : 016
# 대기번호 : 017
# 대기번호 : 018
# 대기번호 : 019
# 대기번호 : 020


# answer = input("아무값이나 입력하세요 : ") # input으로 받으면 항상 문자열(str) 형태로 받는다.
# print("입력하시 값은 " +  answer +"입니다.")
#결과
# 아무값이나 입력하세요 : 나도코딩
# 입력하시 값은 나도코딩입니다.


# #다양한 출력 포맷
# #빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리의 공간을 확보
# print("{0: >10}".format(500))#       500, >:오른쪽 정렬의미

# #양수일땐 +로 표시, 음수 일땐 -로 표시
# print("{0: >+10}".format(500))  #      +500
# print("{0: >+10}".format(-500)) #      -500

# #왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))  #+500______
# print("{0:_<+10}".format(-500)) #-500______

# #3자리마다 콤마를 찍어주기
# print("{0:,}".format(10000000000000)) #10,000,000,000,000

# #3자리마다 콤마를 찍어주기,+-부호도 붙이기
# print("{0:+,}".format(10000000000000)) #+10,000,000,000,000
# print("{0:+,}".format(-10000000000000)) #-10,000,000,000,000

# #3자리마다 콤마를 찍어주기, 부호도 붙이고, 자릿수도 확보하기
# #돈이 많으면 행복하니까 빈자리는 ^로 채워주기
# print("{0:^<+30,}".format(10000000000000000)) #+10,000,000,000,000,000^^^^^^^

# #소수점 출력
# print("{0:f}".format(5/3)) #1.666667

# #소수점 특정 자리수 까지만 표시(소수점 3째 자리에서 반올림)
# print("{0:.2f}".format(5/3)) #1.67

#파일 입출력 (파일을 하나 열어서 어떤 점수 정보를 쓰는 학습)
# score_file = open("score.txt", "w", encoding="utf8") 
# #open을 통해서 file를 열수가 있음, score.txt : 파일명, w: write의미 , encoding을 utf8로 정의를 해주어야지 한글 정보를 정상적으로 인식할수 있음
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close() #file을 열었을 시에는 항상 close를 해주어야 한다.

# score_file = open("score.txt", "a", encoding="utf8") #덮어 쓰기기 아닌 내용을 이어서 추가할 경우 a(append)를 사용
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100") #file.write를 사용할 경우 자동 줄바꿈이 없기 때문에  \n을 추가해서 줄바꿈을 해주어야 한다.
# score_file.close() 

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read()) #file에 있는 모든 값을 읽어와라
# score_file.close() 

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) #줄별로 읽기, 한줄 일고 커서는 다름줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

#줄바꿈을 안하고 싶을 경우
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(),end="") #end=""를 추가할 경우 줄바꿈을 하지 않는다.
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# score_file.close()

#line이 몇줄인지 모르는 경우(줄바꿈이 없는 겨우)
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line: #line이 없을 경우 멈춘다.
#         break
#     print(line,end="")
# score_file.close()


# score_file = open("score.txt", "r", encoding="utf8")
# lines =  score_file.readlines() #score_file에 있는 모든 line의 값을 lines에 넣어라
# for line in lines:              #lines에 있는 값을 하나씩 line에 넣는다.
#     print(line, end="")         #line에 있는 값을 하나씩 print한다.
# score_file.close()


#pickle(프로그램 상에서 우리가 사용하고 data를 file형태로 저장해 주는것)
#파일에 data를 쓰기
# import pickle
# profile_file = open("profile.pickle", "wb") #wb: w는 write 이며,b: binary의 의미이며, pickle를 사용하기 위해서는 항상 binary type을 정의 해주어야 한다.그리고 pickle에서는 encoding을 설정할 필요가 없음
# profile = {"이름":"박명수","나이":30, "취미":["축구","골프","코딩"]} #{}:사전형태로 만들때 사용, []:list형태로 만들때 사용
# print(profile) #{'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
# pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
# profile_file.close()

#파일에서 data를 가져오기
# import pickle
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #load를 이용해서 file에 있는 정보를 profile에 불러오기
# print(profile) #{'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
# profile_file.close()


#with
#pickle를 사용하는 경우
# import pickle
# with open("profile.pickle","rb") as profile_file: #profile.pickle의 data를 가져와서 profile_file에 저장해라
#     print(pickle.load(profile_file)) #{'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
#  #with문의 경우 file을 close를 할 필요없이 자동으로  close를 해준다.

#파일쓰기 : pickle를 사용하지 않는 경우
# with open("study.txt","w",encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

#파일 읽어오기  : pickle를 사용하지 않는 경우
# with open("study.txt","r",encoding="utf8") as study_file:
#     print(study_file.read()) #파이썬을 열심히 공부하고 있어요


#quiz7
# 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 : 
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 :  차리명은 '1주차.txt', '2주차.txt', ...와 같이 만듭니다.

# for i in range(1,51):
#     with open(str(i) + "주차.txt","w",encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 -".format(i))
#         report_file.write(" \n부서 : ")
#         report_file.write(" \n이름 : ")
#         report_file.write(" \n업무 요약 : ")

# with open("2주차.txt","r",encoding="utf8") as report_file:
#     print(report_file.read())


#클래스
#마린 : 공격유닛, 군인.총을 쓸 수 있음

# name = "마린"
# hp = 40
# damage = 5

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0},공격력 {1}\n".format(hp,damage)) #\n : 줄바꿈을 해준다

# #탱크 : 공격 유닛,탱크. 포를 쏠수 있는데, 일반모드 / 시즈 모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0},공격력 {1}\n".format(tank_hp,tank_damage))

# #탱크2 : 공격 유닛,탱크. 포를 쏠수 있는데, 일반모드 / 시즈 모드.
# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0},공격력 {1}\n".format(tank2_hp,tank2_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다.[공격력{2}]".format(name,location,damage))

# attack(name,"1시",damage)
# attack(tank_name,"1시",tank_damage)
# attack(tank2_name,"1시",tank2_damage)


# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력{0}, 공력력{1}".format(self.hp,self.damage))

# marine1 = Unit("마린",40,5)
# marine2 = Unit("마린",40,5) 
# tank = Unit("탱크",150,35) 

#__init__ : 파이손에서 쓰이는 생성자 이다. 개체 : class로 부터 만들어지는 것들을 개체라고 표현
#init에 정의된 갯수 만큼을 똑같이 만들어 주야야 한다.


#멤버 변수 : class내에서 정의된 변수
        # self.name = name
        # self.hp = hp
        # self.damage = damage   

#레이스 : 공중유닛,비행기.클로킹(상대방에게 보이지않음)
# wraith1 = Unit("레이스",80,5)
# print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))


# #마인드 컨트롤 : 상대방 유닛을 내것으로 만드는것
# wraith2 = Unit("뻬앗은 레이스",80,5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0}은 현재 클로킹 상태입니다.".format(wraith2.name))

# #일반유닛
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력{0}, 공력력{1}".format(self.hp,self.damage))

# #공격유닛
# class AttackUnit:
#      def __init__(self, name, hp, damage):
#             self.name = name
#             self.hp = hp
#             self.damage = damage   
    
#      def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
#      def damaged(self,damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
#         if self.hp <= 0:
#              print("{0} : 파괴되었습니다.".format(self.name))

# #파이어뱃 : 공격유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")

# #공격을 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)


#상속
#일반유닛
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

# #공격유닛
# class AttackUnit(Unit):
#      def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage   
    
#      def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
#      def damaged(self,damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
#         if self.hp <= 0:
#              print("{0} : 파괴되었습니다.".format(self.name))

# # #파이어뱃 : 공격유닛, 화염방사기.
# # firebat1 = AttackUnit("파이어뱃",50,16)
# # firebat1.attack("5시")

# # #공격을 2번 받는다고 가정
# # firebat1.damaged(25)
# # firebat1.damaged(25)




# #다중상속 : 부모가 둘이 상인것(unit : 부모,attackunit : 자녀)
# #드랍쉽 : 공중 유닛, 수송기.마린/파이어뱃/탱크등을 수송.공격X

# #날수 있는 기능을 가진 클래스
# class Flyable:
#        def __init__(self, flying_speed):
#              self.flying_speed = flying_speed
#        def fly(self,name, location):
#          print("{0} : {1}방향으로 날아갑니다.[속도 : {2}]"\
#                .format(name, location, self.flying_speed)) 

# #공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit,Flyable):
#        def __init__(self, name, hp, damage, flying_speed):
#              AttackUnit.__init__(self, name, hp, damage)
#              Flyable.__init__(self,flying_speed)

# #발키리  :공중 공격 유닛, 한번에 14발 미사일 발사
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")


#메소드 오버라이딩

# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#        print("[지상 유닛 이동]")
#        print("{0} : {1}방향으로 이동합니다.[속도 {2}]"\
#              .format(self.name, location, self.speed))


# #공격유닛
# class AttackUnit(Unit):
#      def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage   
    
#      def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
#      def damaged(self,damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
#         if self.hp <= 0:
#              print("{0} : 파괴되었습니다.".format(self.name))



# #다중상속 : 부모가 둘이 상인것(unit : 부모,attackunit : 자녀)
# #드랍쉽 : 공중 유닛, 수송기.마린/파이어뱃/탱크등을 수송.공격X

# #날수 있는 기능을 가진 클래스
# class Flyable:
#        def __init__(self, flying_speed):
#              self.flying_speed = flying_speed
#        def fly(self,name, location):
#          print("{0} : {1}방향으로 날아갑니다.[속도 : {2}]"\
#                .format(name, location, self.flying_speed)) 

# #공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit,Flyable):
#        def __init__(self, name, hp, damage, flying_speed):
#              AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed는 0
#              Flyable.__init__(self,flying_speed)
#        def move(self,location):
#              print("[공중 유닛 이동]")
#              self.fly(self.name, location)

# #벌쳐 :  지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐",80, 10, 20)

# #배틀크루저 : 공중유닛, 체력도 굉장히 좋음, 공격력도 좋음.
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")


# # #PASS
# from random import *

# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))

#     def move(self, location):
#        print("{0} : {1}방향으로 이동합니다.[속도 {2}]"\
#              .format(self.name, location, self.speed))
       
#     def damaged(self,damage):
#        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
#        self.hp -= damage
#        print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
#        if self.hp <= 0:
#              print("{0} : 파괴되었습니다.".format(self.name))   


# #공격유닛
# class AttackUnit(Unit):
#      def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage   
    
#      def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
# #마린
# class Marine(AttackUnit):
#       def __init__(self):
#           AttackUnit.__init__(self, "마린", 40, 1, 5)
#        # 스팀팩: 일정시간동안 이동 및 공격 속도를 증가, 체력 10감소
#       def stimpack(self):
#          if self.hp > 10:
#             self.hp -= 10
#             print("{0} 스팀팩을 사용합니다.[체력 10감소]".format(self.name))
#          else:
#             print("{0} 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# class Tank(AttackUnit):
#        #시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
#       seize_developed = False # 시즈모드 개발여부

#       def __init__(self):
#          AttackUnit.__init__(self, "탱크", 150, 1, 35)
#          self.seize_mode = False

#       def set_seize_mode(self):
#          if Tank.seize_developed == False:
#             return
#          #현재 시즈모드가 아닐 때 -> 시즈 모드
#          if self.seize_mode == False:
#                 print("{0} : 시즈 모드로 전환합니다.".format(self.name))
#                 self.damage *= 2
#                 self.seize_mode = True
#          #현재 시즈모드일 때 -> 시즈모드 해제
#          else:
#                 print("{0} : 시즈 모드를 해제합니다.".format(self.name))
#                 self.damage /= 2
#                 self.seize_mode = False         

# #날수 있는 기능을 가진 클래스
# class Flyable:
#        def __init__(self, flying_speed):
#              self.flying_speed = flying_speed
#        def fly(self,name, location):
#          print("{0} : {1}방향으로 날아갑니다.[속도 : {2}]"\
#                .format(name, location, self.flying_speed)) 

# #공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit,Flyable):
#        def __init__(self, name, hp, damage, flying_speed):
#              AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed는 0
#              Flyable.__init__(self,flying_speed)
#        def move(self,location):
#              self.fly(self.name, location)

# #레이스
# class wraith(FlyableAttackUnit):
#        def __init__(self):
#              FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#              self.clocked = False   #클로킹 모드(해제 상태)

#        def clocking(self):
#              if self.clocked == True: #클로킹 모두 -> 모드 해제
#                    print("{0} : 클로킹 모드 해제합니다.".format(self.name))
#                    self.clocked = False
#              else: # 클로킹 모두 해제 -> 모드 설정
#                    print("{0} :  클로킹 모두 설정합니다.".format(self.name))
#                    self.clocked = True

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("Player : gg") #good game
#     print("[Player] 님이 퇴장하셨습니다.")
       

# #게임 시작
# game_start( )

# #마린 3기 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# #탱크 2기 생성
# t1 = Tank()
# t2 = Tank()

# #레이스 1기 생성
# w1 = wraith()

# #모든 유닛을 리스트에 집어넣어 유닛 일관 관리(생선된 모든 유닛 append)
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# #탱크 시즈모드 개발
# Tank.seize_developed = True
# print("[알림] 태크 시즈 모드 개발이 완료되었습니다.")

# # 공격 모드 준비(마린: 스팀팩, 탱크 : 시즈 모드, 레이스: 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine):
#           unit.stimpack()
#     elif isinstance(unit, Tank):
#           unit.set_seize_mode() 
#     elif isinstance(unit, wraith):
#           unit.clocking()

# #전군 공격
# for unit in attack_units:
#     unit.attack("1시") 

# #전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5,21)) #공격은 랜덤으로 받음(5~20)

# # 게임 종료
# game_over()

#퀴즈 8
# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제)
# 총 3대의 매물이 있습니다
# 강남 아파트 매매 10억 2010면
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# # [코드]
# class House:
#    #매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location =  location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year



#    #매물 정보 표시
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)


# #list로 만들기
# houses = []
# house1 = House("강남", "아피트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2000년")

# houses.append(house1)
# houses.append(house2) 
# houses.append(house3)

# print("총 {0}대의 매물이 있습니다".format(len(houses)))

# for house in houses:
#     house.show_detail()



#예외처리(어떤 error가 발생했을시 처리해주는 것)
# try:
#    print("나누기 전용 계산기 입니다.")
#    nums = []
#    nums.append(input("첫 번째 숫자를 입력하세요 : "))
#    nums.append(input("두 번째 숫자를 입력하세요 : "))
#    # nums.append(int(nums[0]) / int(nums[1]))
#    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2] ))

# except ValueError:
#    print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#    print(err)
# except Exception as err:
#    print("알수 없는 에러가 발생하였습니다.")
#    print(err)


#에러 발생 시키기
# try:
#     print("한 자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))				
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >=10 or num2 >=10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력 하였습니다. 한 자리 숫자만 입력하세요")		



# #사용자 정의 예외처리
# class BigNumvberError(Exception):
#        pass

# try:
#     print("한 자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))				
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >=10 or num2 >=10:
#         raise BigNumvberError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력 하였습니다. 한 자리 숫자만 입력하세요")

# except BigNumvberError:
#      print("에러가 발생하였습니다. 한 자리 숫자만 입력해 주세요")


#사용자 정의 예외처리
# class BigNumberError(Exception):
#       def __init__(self,msg):
#          self.msg = msg
#       def __str__(self):
#          return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))				
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >=10 or num2 >=10:
#         raise BigNumberError("입력값 : {0},{1}".format(num1,num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력 하였습니다. 한 자리 숫자만 입력하세요")

# except BigNumberError as err:
#      print("에러가 발생하였습니다. 한 자리 숫자만 입력해 주세요")
#      print(err)


#finally(예외처리 구문에서 정상적으로 수행하던, error가 발생하던지 무조건 수행 진행 )
# class BigNumberError(Exception):
#       def __init__(self,msg):
#          self.msg = msg
#       def __str__(self):
#          return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))				
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >=10 or num2 >=10:
#         raise BigNumberError("입력값 : {0},{1}".format(num1,num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력 하였습니다. 한 자리 숫자만 입력하세요")

# except BigNumberError as err:
#      print("에러가 발생하였습니다. 한 자리 숫자만 입력해 주세요")
#      print(err)

# finally:
#     print("계산기를 이용해 주셔서 감사합니다.") #error가 발생하도라도 무조근 수행


#quiz 9
# Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올때는 ValueError로 처리
#         출력 메시지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#         치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#         출력 메시지 :  "제고가 소진되어 더 이상 주문을 받지 않습니다."

# [코드]

# class SoldOutError(Exception):
#    pass


# chicken = 10
# waiting =1 # 홀 안에는 현재 만석. 대기번호 1부터 시작
# while(True):
#        try:
#           print("남은 치킨 : {0}".format(chicken))
#           order = int(input("치킨 몇 마리 주문하시겠습니다까?"))
#           if order > chicken:
#             print("재료가 부족합니다.")
#           elif order <= 0:
#              raise ValueError
#           else:
#             print("[대기번호{0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order
#           if chicken == 0:
#                raise SoldOutError
#        except ValueError:
#           print("잘못된 값을 입력하였습니다.")
#        except SoldOutError:
#           print("제고가 소진되어 더 이상 주문을 받지 않습니다")
#           break #while문 탈출




#모듈
# import theater_module
# theater_module.price(3) #3명이서 영화 보러 갔을때 가격
# theater_module.price_morning(4) #4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_solder(5) #5명의 군인이 영화 보러 갔을때

# import theater_module as mv #이름이 길때 줄여서 사용할수 있는 방법
# mv.price(3)
# mv.price_morning(4)
# mv.price_solder(5)


# from theater_module import *
# price(3)
# price_solder(4)
# price_morning(5)

# from theater_module import price, price_morning #특정한 조건만 불러와서 사용할수 있음
# price(3)
# price_morning(4)

# from theater_module import price_solder as price # price_solder를 줄임말로 사용할수 있음
# price(5)

#패키지 (모듈들을 모아 놓은 집합)
# import travel.thailand #import에는 모듈이나 패키지만 가능(class는 불가능)
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage #from ~ import를 사용시에는 class를 직접 가져올수 있음
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# #__all__
# from travel import *
# # # trip_to = vietnam.VietnamPackage() #__init__.py에 vietnam을 추가해주어야 함
# trip_to = thailand.ThailandPackage() #__init__.py에 thailand를 추가해주어야 함
# trip_to.detail()


# #모듈 직접 실행

#패키지 및 모듈위치
# # from travel import *
# import inspect
# import random
# print(inspect.getfile(random)) #random이라는 모듈이 어느 위치에 있는지 파일 위치를 알려주는것
# print(inspect.getfile(thailand))

#pip install #pip로 패키지 설치하기
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


#내장함수
#input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}는 아주 좋은 언어입니다.!".format(language))

#dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# # print(dir())
# import random #외장 함수
# # print(dir())
# # import pickle
# # print(dir())

# print(dir(random))

# lst = [1,2,3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))

#외장 함수
 #glob : 경로 내의 폴더 / 파일 목록 조회(윈도우 dir)
# import glob
# print(glob.glob("*.py")) #확정자가 py인 모든 파일에 대해서 알려달라.


#os : 운영체제에서 제공하는 기본 기능
#  
# print(os.getcwd()) #현재 디렉토리를 표시해달라

# folder = " sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print("폴더를 삭제하였습니다.")

# else:
#     os.makedirs(folder) #폴더 생성하기
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())

#time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%m/%d/%y %H:%M:%S"))

# import datetime
# # print("오늘 날짜는 " , datetime.date.today())

# #timedelta :두 날짜 사이의 간격
# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print(" 우리가 만난지 100일은", today + td)


#quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

# 조건  : 모듈 파일명은 byme.py 로 작성
# (모듈 사용 예제)

import byme
byme.sign()

# (출력 예제)
# 이 프로그램은 나도코딩에 의해 만들어 졌습니다.
# 유튜브 : http://youtube.com
# 이메일 : nadocoding@mail.com


print("this is fresh man first project")