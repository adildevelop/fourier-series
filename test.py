import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
from PyQt5 import QtWidgets
import design

class FurieApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.visualize)

    def visualize(self):
        N = self.label
        K = self.label_2
        Amplitude = self.label_3
        Step = self.label_4

        N = 100
        T = 1.0 / 800.0
        x = np.linspace(0.0, N*T, N)
        y = np.sin(100.0 * 2.0*np.pi*x) + 0.5*np.sin(1000.0 * 2.0*np.pi*x)
        yf = scipy.fftpack.fft(y)
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

        fig, ax = plt.subplots()
        ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
        plt.show()

    
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = FurieApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()