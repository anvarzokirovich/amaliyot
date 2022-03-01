import PyQt5.QtWidgets as qt
import PyQt5.QtGui as qtw

class MainWindow(qt.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Anvar")
        
        self.setLayout(qt.QVBoxLayout())
        
        b_qator=qt.QLabel("1-qiymatni kiriting:")
        self.layout().addWidget(b_qator)
        
        qiymat_k=qt.QLineEdit()
        qiymat_k.setObjectName('q_k')
        qiymat_k.setText("")
        self.layout().addWidget(qiymat_k)
        
        i_qator=qt.QLabel("2-qiymatni kiriting:")
        self.layout().addWidget(i_qator)
        
        qiymat_k2=qt.QLineEdit()
        qiymat_k2.setObjectName('q_k2')
        qiymat_k2.setText("")
        self.layout().addWidget(qiymat_k2)
        
        bosish_t=qt.QPushButton("+", clicked=lambda:qosh())
        self.layout().addWidget(bosish_t)
        
        ayiruv_t=qt.QPushButton("-", clicked=lambda:ayir())
        self.layout().addWidget(ayiruv_t)
        
        kopaytruv_t=qt.QPushButton("*", clicked=lambda:kopaytr())
        self.layout().addWidget(kopaytruv_t)
        
        boluv_t=qt.QPushButton("/", clicked=lambda:bol())
        self.layout().addWidget(boluv_t)
        
        def qosh():
            qiymat1=qiymat_k.text()
            qiymat2=qiymat_k2.text()
            try:
                qiymat1=float(qiymat1)
                qiymat2=float(qiymat2)
            except ValueError:
                xato_j=qt.QLabel("Siz son kiritmadingiz!")
                self.layout().addWidget(xato_j)
                qiymat_k.setText("")
                qiymat_k2.setText("")
            else:
                qoshish=qt.QLabel(f"{int(qiymat1+qiymat2)}")
                self.layout().addWidget(qoshish)
                
                qiymat_k.setText("")
                qiymat_k2.setText("")
        def ayir():
            qiymat1=qiymat_k.text()
            qiymat2=qiymat_k2.text()
            try:
                qiymat1=float(qiymat1)
                qiymat2=float(qiymat2)
            except ValueError:
                xato_j=qt.QLabel("Siz son kiritmadingiz!")
                self.layout().addWidget(xato_j)
                qiymat_k.setText("")
                qiymat_k2.setText("")
            else:
                qoshish=qt.QLabel(f"{int(qiymat1-qiymat2)}")
                self.layout().addWidget(qoshish)
                
                qiymat_k.setText("")
                qiymat_k2.setText("")
        def kopaytr():
            qiymat1=qiymat_k.text()
            qiymat2=qiymat_k2.text()
            try:
                qiymat1=float(qiymat1)
                qiymat2=float(qiymat2)
            except ValueError:
                xato_j=qt.QLabel("Siz son kiritmadingiz!")
                self.layout().addWidget(xato_j)
                qiymat_k.setText("")
                qiymat_k2.setText("")
            else:
                qoshish=qt.QLabel(f"{int(qiymat1*qiymat2)}")
                self.layout().addWidget(qoshish)
                
                qiymat_k.setText("")
                qiymat_k2.setText("")
        def bol():
            qiymat1=qiymat_k.text()
            qiymat2=qiymat_k2.text()
            try:
                qiymat1=float(qiymat1)
                qiymat2=float(qiymat2)
            except ValueError:
                xato_j=qt.QLabel("Siz son kiritmadingiz!")
                self.layout().addWidget(xato_j)
                qiymat_k.setText("")
                qiymat_k2.setText("")
            else:
                try:
                    x=int(qiymat1/qiymat2)
                except ZeroDivisionError:
                    xato_j=qt.QLabel("Nolga bo'lib bo'lmaydi!")
                    self.layout().addWidget(xato_j)
                    
                else:
                    qoshish=qt.QLabel(f"{x}")
                    self.layout().addWidget(qoshish)
                
                qiymat_k.setText("")
                qiymat_k2.setText("")
        
        self.show()
        
app=qt.QApplication([])
mw=MainWindow()
app.exec_()
        