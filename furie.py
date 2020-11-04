#!/usr/bin/python
# -*- coding: utf-8 -*
import sys
from scipy.integrate import quad # модуль для интегрирования
import matplotlib.pyplot as plt # модуль для графиков
import numpy as np # модуль для операций со списками и массивами
from PyQt5 import QtWidgets
import design

class FurieApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.visualize)

    def visualize(self):
        T=np.pi; w=2*np.pi/T# период и круговая частота
        a=[];b=[];c=10;g=[];m=np.arange(0,c,1);q=np.arange(0,2*np.pi,0.01)# подготовка списков для численного анализа
        a=[round(2*quad(self.func_1, 0, T, args=(k,w))[0]/T,3) for k in m]# интеграл для a[k], k -номер гармоники
        b=[round(2*quad(self.func_2, 0, T, args=(k,w))[0]/T,3) for k in m]# интеграл для b[k], k -номер гармоники
        
        F1=[a[0]*np.cos(w*1*t)+b[0]*np.sin(w*1*t) for t in q]#функции для гармоник
        F2=[a[1]*np.cos(w*2*t)+b[1]*np.sin(w*2*t) for t in q]
        F3=[a[2]*np.cos(w*3*t)+b[2]*np.sin(w*3*t) for t in q]
        F4=[a[3]*np.cos(w*4*t)+b[3]*np.sin(w*4*t) for t in q]
        F5=[a[4]*np.cos(w*5*t)+b[4]*np.sin(w*5*t) for t in q]
        F6=[a[5]*np.cos(w*6*t)+b[5]*np.sin(w*6*t) for t in q]
        F7=[a[6]*np.cos(w*7*t)+b[6]*np.sin(w*7*t) for t in q]
        F8=[a[7]*np.cos(w*8*t)+b[7]*np.sin(w*8*t) for t in q]
        F9=[a[8]*np.cos(w*9*t)+b[8]*np.sin(w*9*t) for t in q]
        F10=[a[9]*np.cos(w*10*t)+b[9]*np.sin(w*10*t) for t in q]

        plt.figure()
        plt.title("Классический гармонический анализ функции \n при t<pi  f(t)=cos(t)  при t>=pi  f(t)=-cos(t)")
        plt.plot(q, F1, label='1 гармоника')
        plt.plot(q, F2, label='2 гармоника')
        plt.plot(q, F3, label='3 гармоника')
        plt.plot(q, F4, label='4 гармоника')
        plt.plot(q, F5, label='5 гармоника')
        plt.plot(q, F6, label='6 гармоника')
        plt.plot(q, F7, label='7 гармоника')
        plt.plot(q, F8, label='8 гармоника')
        plt.plot(q, F9, label='9 гармоника')
        plt.plot(q, F10, label='10 гармоника')
        plt.xlabel("Время t")
        plt.ylabel("Амплитуда А")
        plt.legend(loc='best')
        plt.grid(True)

        F = np.array(a[0]/2)+np.array([0*t for t in q-1])# подготовка массива для анализа с a[0]/2

        for k in np.arange(1,c,1):
                F = F + np.array([a[k]*np.cos(w*k*t) + b[k]*np.sin(w*k*t) for t in q])# вычисление членов ряда Фурье

        plt.figure()
        P=[self.func(t) for t in q]
        plt.title("Классический гармонический синтез")
        plt.plot(q, P, label='f(t)')
        plt.plot(q, F, label='F(t)')
        plt.xlabel("Время t")
        plt.ylabel("f(t),F(t)")
        plt.legend(loc='best')
        plt.grid(True)
        plt.show()

    def func(self, t):# анализируемая функция
        if t<np.pi:
                p=np.cos(t)
        else:
                p=-np.cos(t)
        return p

    def func_1(self,t,k,w):# функция для расчёта коэффициента a[k] 
        if t<np.pi:
                z=np.cos(t)*np.cos(w*k*t)
        else:
                z=-np.cos(t)*np.cos(w*k*t)
        return z

    def func_2(self,t,k,w):#функция для расчёта коэффициента b[k] 
        if t<np.pi:
                y=np.cos(t)*np.sin(w*k*t)
        else:
                y=-np.cos(t)*np.sin(w*k*t)
        return y
    

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = FurieApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()