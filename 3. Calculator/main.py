from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit,QPushButton
import sys
class Window(QWidget):
    
    def __init__(self):
        super(Window,self).__init__()
        self.set_UI()

    def set_UI(self):
        
        def crpad(bt):
            num=0
            for y in 1,2,3:
                for x in 1,2,3:
                    bt[num].setGeometry(50*x,50+50*y,50,50)
                    bt[num].setText(str(num+1))
                    num+=1

        def crbtn(bt,x,y,xr,yr,t):
            bt.setGeometry(50*x,50+50*y,50*xr,50*yr)
            bt.setText(t)

        self.setWindowTitle('Калькулятор')
        self.setGeometry(600,450,300,350)

        self.leOut=QLineEdit(self)
        self.leOut.setGeometry(25,20,250,30)      
        # self.leOut.setReadOnly(True)
        self.leOut.setPlaceholderText("Введите 2 числа разделив их знаком.")
        
        b1=self.btn1=QPushButton(self)#Begin of btons` creation 
        b2=self.btn2=QPushButton(self)
        b3=self.btn3=QPushButton(self)
        b4=self.btn4=QPushButton(self)
        b5=self.btn5=QPushButton(self)
        b6=self.btn6=QPushButton(self)
        b7=self.btn7=QPushButton(self)
        b8=self.btn8=QPushButton(self)
        b9=self.btn9=QPushButton(self)
        b0=self.btn0=QPushButton(self)
        bPl=self.btnPl=QPushButton(self)
        bMn=self.btnMn=QPushButton(self)
        bMl=self.btnMl=QPushButton(self)
        bDv=self.btnDv=QPushButton(self)
        bEq=self.btnEq=QPushButton(self)
        bD=self.btnD=QPushButton(self)
        bClean=self.btnCl=QPushButton(self)#End of creation
        
        btlt=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
        crpad(btlt)#begin of redaction
        crbtn(bClean,1,0,3,1,"Clean the field")
        crbtn(b0,2,4,2,1,"0")                
        crbtn(bPl,4,1,1,1,"+") 
        crbtn(bMn,4,2,1,1,"-") 
        crbtn(bMl,4,3,1,1,"*") 
        crbtn(bDv,4,4,1,1,"/")
        crbtn(bEq,4,0,1,1,"=")
        crbtn(bD,1,4,1,1,".") #end of redaction
        
        b1.clicked.connect(lambda: self.padclick(b1))#begin of connections creation
        b2.clicked.connect(lambda: self.padclick(b2))
        b3.clicked.connect(lambda: self.padclick(b3))
        b4.clicked.connect(lambda: self.padclick(b4))
        b5.clicked.connect(lambda: self.padclick(b5))
        b6.clicked.connect(lambda: self.padclick(b6))
        b7.clicked.connect(lambda: self.padclick(b7))
        b8.clicked.connect(lambda: self.padclick(b8))
        b9.clicked.connect(lambda: self.padclick(b9))
        b0.clicked.connect(lambda: self.padclick(b0))
        bD.clicked.connect(lambda: self.padclick(bD))
        bPl.clicked.connect(lambda: self.padclick(bPl))
        bMl.clicked.connect(lambda: self.padclick(bMl))
        bDv.clicked.connect(lambda: self.padclick(bDv))
        bMn.clicked.connect(lambda: self.padclick(bMn))
        bEq.clicked.connect(self.eqclick)
        bClean.clicked.connect(self.cleanclick)#end 
        
        self.show()

    def cleanclick(self):
        self.leOut.setText("")
    
    def padclick(self, bt):
        if len(self.leOut.text())>0:

            char=self.leOut.text()[len(self.leOut.text())-1]
            if bt.text()==char:
                return
            if bt.text()=='+' and char=='-':
                self.leOut.setText(self.leOut.text()[0:len(self.leOut.text())-1]+bt.text())
            elif bt.text()=='-' and char=='+':
                self.leOut.setText(self.leOut.text()[0:len(self.leOut.text())-1]+bt.text())
            elif bt.text()=='*' and char=='/':
                self.leOut.setText(self.leOut.text()[0:len(self.leOut.text())-1]+bt.text())
            elif bt.text()=='/' and char=='*':
                self.leOut.setText(self.leOut.text()[0:len(self.leOut.text())-1]+bt.text())        
            else:
                self.leOut.setText(self.leOut.text()+bt.text())
        else:
            self.leOut.setText(self.leOut.text()+bt.text())
    
    def eqclick(self):

        char=self.leOut.text()
        dict=["1","2","3","4","5","6","7","8","9","0","."] 
        for num in range(len(dict)):
            char=char.replace(dict[num],"")

        if len(char)>1:
            if char.find('*')+1:
                char=char[char.find('*')]
            elif char.find('/')+1:
                char=char[char.find('/')]
            else:
                char=char[1]

        if char:
            if self.leOut.text().find("-")==0:
                nums=self.leOut.text()[1:].split(char)
                nums[0]="-"+nums[0]
            else: 
                nums=self.leOut.text().split(char)
            for id in range(len(nums)):
                nums[id]=float(nums[id])
            if char=="+":
                self.leOut.setText(str(nums[0]+nums[1]))
            elif char=="-":
                self.leOut.setText(str(nums[0]-nums[1]))
            elif char=="*":
                self.leOut.setText(str(nums[0]*nums[1]))
            elif char=="/":
                if nums[1]==0:
                    self.leOut.setText("ERROR. Division by zero")
                else:
                    self.leOut.setText(str(nums[0]/nums[1]))
        else:
            self.leOut.setText("ERROR")

if __name__ =='__main__':
    app=QApplication(sys.argv)
    window=Window()
    sys.exit(app.exec())
        