class ThailandPackage:
    def detail(self):
        print("[태국 패키지  3박 5일] 방콕, 파타야 여행(야시장 투어) 50만원")

if __name__ == "__main__": #thailand.py에서 직접 실생할때는 이구문이 실행
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행되요")
    trip_to = ThailandPackage()
    trip_to.detail()

else:
    print("Thailand 외부에서 모듈 호출") #practice.py에서 ThailandPackage를 갖다가 쓸때는 이 구문을 실행
     