import sys      
from math import *  

from diferenciacion import * #Debe modificar según su caso
from PyQt5.QtWidgets import * #Siempre incluirlo
from PyQt5.QtGui import * #se importa para validar DOUBLES

class diferenciacionnumerica(QtWidgets.QMainWindow): #Siempre incluirlo
    def __init__(self):                     #Siempre incluirlo
        super().__init__()                  #Siempre incluirlo
        self.ui = Ui_Dialog()               #Siempre incluirlo
        self.ui.setupUi(self)               #Siempre incluirlo

        self.ui.txtresultado_atras.setEnabled(False)
        self.ui.txtresultado_ade.setEnabled(False)
        self.ui.txtresultado_cen.setEnabled(False)


        
        self.ui.txtxi_atras.setValidator(QDoubleValidator())
        self.ui.txth_atras.setValidator(QDoubleValidator())
        
        
        self.ui.txtxi_ade.setValidator(QDoubleValidator())
        self.ui.txth_ade.setValidator(QDoubleValidator())

        self.ui.txtxi_cen.setValidator(QDoubleValidator())
        self.ui.txth_cen.setValidator(QDoubleValidator())

        
        self.ui.btn_atras.clicked.connect(self.atras)

        self.ui.btn_ade.clicked.connect(self.adelante)

        self.ui.btn_cen.clicked.connect(self.centrado)

        
    def atras(self):
        xi=self.ui.txtxi_atras.text()
        h=self.ui.txth_atras.text()

        mensaje = QMessageBox()
        mensaje.setWindowTitle("Información")

        if len(xi):
            if len(h):
                try:
                    xi = float(xi)
                except:
                    mensaje.setIcon(QMessageBox.Warning)
                    mensaje.setText("El valor A debe ser numérico")
                    mensaje.exec_()


                try:
                    h = float(h)
                except:
                    mensaje.setIcon(QMessageBox.Warning)
                    mensaje.setText("El valor B debe ser numérico")
                    mensaje.exec_()

                

                #f(xi)
                fxi=round(((-1/10)*(xi**4)-3/20*(xi**3)-1/2*(xi**2)-1/4*(xi)+6/5),4)
                self.ui.txtfxi_atras.setText(str(fxi))

                #xi-1
                xi_1=round(xi-h,4)
                self.ui.txtxi_1_atras.setText(str(xi_1))

                #xi-2
                xi_menos2=round(xi-(2*h),4)
                self.ui.txtxi_menos2_atras.setText(str(xi_menos2))

                #f(xi-1)
                fxi_1=round(((-1/10)*(xi_1**4)-3/20*(xi_1**3)-1/2*(xi_1**2)-1/4*(xi_1)+6/5),4)
                self.ui.txtfxi_1_atras.setText(str(fxi_1))

                #f(xi-2)
                fxi_2=round(((-1/10)*(xi_menos2**4)-3/20*(xi_menos2**3)-1/2*(xi_menos2**2)-1/4*(xi_menos2)+6/5),4)
                self.ui.txtfxi_menos2_atras.setText(str(fxi_2))
                
                #derivada
                d=round((fxi-(2*fxi_1)+fxi_2)/(h**2), 4)
                self.ui.txtresultado_atras.setText(str(d))

            else:
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.setText("Debe ingresar un número h")
                mensaje.exec_()

        else:
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setText("Debe ingresar un número xi")
            mensaje.exec_()


    def adelante(self):
        xi=self.ui.txtxi_ade.text()
        h=self.ui.txth_ade.text()
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Información")

        if len(xi):
            if len(h):
                try:
                    xi = float(xi)
                except:
                    mensaje.setIcon(QMessageBox.Warning)
                    mensaje.setText("El valor A debe ser numérico")
                    mensaje.exec_()


                try:
                    h = float(h)
                except:
                    mensaje.setIcon(QMessageBox.Warning)
                    mensaje.setText("El valor B debe ser numérico")
                    mensaje.exec_()

                

                #f(xi)
                fxi=round(((-1/10)*(xi**4)-3/20*(xi**3)-1/2*(xi**2)-1/4*(xi)+6/5),4)
                self.ui.txtfxi_ade.setText(str(fxi))

                #xi+1
                xi_mas1=xi+h
                self.ui.txtxi_1_ade.setText(str(xi_mas1))
                
                #xi+2
                xi_mas2=round(xi+(2*h),4)
                self.ui.txtxi_mas2_ade.setText(str(xi_mas2))
                
                #f(xi+1)
                fxi_mas1=round(((-1/10)*(xi_mas1**4)-3/20*(xi_mas1**3)-1/2*(xi_mas1**2)-1/4*(xi_mas1)+6/5),4)
                self.ui.txtfxi_1_ade.setText(str(fxi_mas1))
                
                #f(x+2)
                fxi_mas2=round(((-1/10)*(xi_mas2**4)-3/20*(xi_mas2**3)-1/2*(xi_mas2**2)-1/4*(xi_mas2)+6/5),4)
                self.ui.txtfxi_mas2_ade.setText(str(fxi_mas2))

                #derivada
                d=round((fxi_mas2-(2*fxi_mas1)+fxi)/(h**2), 4)
                self.ui.txtresultado_ade.setText(str(d))

            else:
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.setText("Debe ingresar un número h")
                mensaje.exec_()

        else:
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setText("Debe ingresar un número xi")
            mensaje.exec_()


    def centrado(self):
        xi=self.ui.txtxi_cen.text()
        h=self.ui.txth_cen.text()
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Información")

        if len(xi):
            if len(h):
                try:
                    xi = float(xi)
                except:
                    mensaje.setIcon(QMessageBox.Warning)
                    mensaje.setText("El valor A debe ser numérico")
                    mensaje.exec_()


                try:
                    h = float(h)
                except:
                    mensaje.setIcon(QMessageBox.Warning)
                    mensaje.setText("El valor B debe ser numérico")
                    mensaje.exec_()

                
                
                #xi+1
                xi_mas1=round(xi+h,4)
                self.ui.txtxi_mas1_cen.setText(str(xi_mas1))
                #xi-1
                xi_1=round(xi-h,4)
                self.ui.txtxi_menos1_cen.setText(str(xi_1))
                
                #f(xi)
                fxi=round(((-1/10)*(xi**4)-3/20*(xi**3)-1/2*(xi**2)-1/4*(xi)+6/5),4)
                self.ui.txtfxi_cen.setText(str(fxi))
                #f(xi+1)
                fxi_mas1=round(((-1/10)*(xi_mas1**4)-3/20*(xi_mas1**3)-1/2*(xi_mas1**2)-1/4*(xi_mas1)+6/5),4)
                self.ui.txtfxi_mas1_cen.setText(str(fxi_mas1))

                #f(xi-1)
                fxi_1=round(((-1/10)*(xi_1**4)-3/20*(xi_1**3)-1/2*(xi_1**2)-1/4*(xi_1)+6/5),4)
                self.ui.txtfxi_1_cen.setText(str(fxi_1))
                
                #derivada
                d=round((fxi_mas1-(2*fxi)+fxi_1)/(h**2), 4)
                self.ui.txtresultado_cen.setText(str(d))

            else:
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.setText("Debe ingresar un número h")
                mensaje.exec_()

        else:
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setText("Debe ingresar un número xi")
            mensaje.exec_()

    
    
   


if __name__=="__main__":                    #Siempre incluirlo
    app=QtWidgets.QApplication(sys.argv)    #Siempre incluirlo
    myapp=diferenciacionnumerica()                  #Siempre incluirlo, invocar clase según su caso
    myapp.show()                            #Siempre incluirlo
    sys.exit(app.exec_())