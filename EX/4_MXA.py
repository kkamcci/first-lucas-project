# push test jhlee (102622)
# push test jhlee (110322)
# push test jhlee (110422)
#Download NI-VISA
#pip install keysight
#pip install visa
#pip install -U pyvisa
#import keysight.command_expert_py3

#1102 jhlee changed #2
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pyvisa
import visa
import time
from telnetlib import Telnet
WAIT_TIME = 1 # sec
# git test main 110222
# git test main 110322
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("1_MXA.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #버튼에 기능을 연결하는 코드
        self.pushButton.clicked.connect(self.marker)

    def marker(self):
        #print (self.ip)
        fout_name=time.strftime("%Y%m%d")+"MXA.txt"
        self.ip = '10.10.13.109'
        print (self.ip)
        for i in range(1):
            test_time=time.strftime("%Y%m%d-%H%M%S")
            try:
                with Telnet(self.ip, 5025, timeout=90) as tn:
                    tn.write(bytes(f':READ:ACP?\n', encoding='utf8'))  #str -> byte
                    time.sleep(WAIT_TIME)
                    output = str (tn.read_very_eager(), 'utf-8')
                    #output = tn.read_very_eager()
                    print(output)
                    inlist = list(output)
                    print ("test")
                    print (inlist[1:50])
                    #output_2 = round(float (output),1)
                    #print(output_2)
                    #self.lineEdit.setText(str(output_2))
                    #time.sleep(WAIT_TIME)
                    #f = open(fout_name, 'a') # 파일 열기
                    #print(output_2,"\t",test_time, file=f) # 파일 저장하기
                    #f.close()
            except Exception as err:
                print(err)
            except KeyboardInterrupt:
                print('terminated by the user')
                exit(0)
            finally:
                print('Done.')
                #self.lineEdit.setText(str(output_2))
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
