#Developer :- Sarbajyoti Mallik
#copyright(2019-2040)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Artificial Intelligence For Diabetic Retinopathy>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from PyQt5 import QtGui
from PyQt5.QtCore import QDir,QSize,QRect,Qt,QBasicTimer,QTimer
from PyQt5.QtGui import QIcon,QPixmap,QFont,QImage,QPalette,QBrush,QTextCursor
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip,QPushButton,QWidget,QLineEdit,QLabel,QFileDialog,QTextEdit,QSplashScreen,QProgressBar
import sys
import time
import webbrowser
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label3=QLabel(self)
        pix=QPixmap("computerr.png")
        self.label3.setPixmap(pix)
        self.label3.setGeometry(0,0, 1400, 850)
        self.title = "Artificial Intelligence For Diabetic Retinopathy(S.Mallik)"        
        self.top = 100        
        self.left = 100        
        self.width = 1400        
        self.height = 850

        self.InitWindow()
        # self.button()
    
    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon('brain.ico'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.progressbar=QProgressBar(self)
        self.progressbar.setGeometry(80,500,400,30)
        self.timer=QBasicTimer()
        self.step=0
        button = QPushButton("BROWSE FOLDER",self)
        button.setGeometry(80,100,110,60)
        button.setStyleSheet("background-color: cyan;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;")
        button.setToolTip("Click To select image")
        button.clicked.connect(self.main2)

        button2 = QPushButton("RESULT",self)
        button2.setGeometry(80,200,110,60)
        button2.setToolTip("Click To see result")
        button2.setStyleSheet("background-color:magenta;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;")
        button2.clicked.connect(self.main)

        button3 = QPushButton("DOCTOR NEAR ME",self)
        button3.setGeometry(80,300,110,60)
        button3.setToolTip("doctors near you & contacts")
        button3.setStyleSheet("background-color:yellow;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;")
        button3.clicked.connect(self.buttonn)

        button4 = QPushButton("SYMPTOMS AND TREATMENTS",self)
        button4.setGeometry(80,400,250,60)
        button4.setToolTip("symptoms and treatments of your problemn")
        button4.setStyleSheet("background-color:red;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;")
        button4.clicked.connect(self.buttonn2)
        self.label=QLabel(self)
        self.label.setGeometry(500,150,400,400)
        # self.label.setStyleSheet("background-color:#ffffff")

        self.label2=QLabel(self)
        self.label2.setStyleSheet("font: 30pt Comic Sans MS;color: red")
        self.label2.resize(1000,50)
        self.label2.move(450,600)

        self.label3=QLabel(self)
        self.label3.setStyleSheet("font: 15pt Comic Sans MS;color:red")
        # self.label3.setFont(QFont('Arial', 10))
        self.label3.resize(2000,100)
        self.label3.move(50,700)

        self.label4=QLabel(self)
        self.label4.setStyleSheet("font: 20pt Comic Sans MS;color: green")
        self.label4.setGeometry(110,520,500,90)

        self.show()

    def main2(self):
        # self.label=QLabel('hii')
        fname = QFileDialog.getOpenFileName(self, 'Open file',"Image files (.jpg .gif)")
        imagePath = fname[0]
        self.path=imagePath
        self.image=QImage(self.path)
        self.pixmapimage=QPixmap.fromImage(self.image)
        self.label.setPixmap(self.pixmapimage)
        self.label.setScaledContents(True)
    
    def buttonn(self):
        url="https://www.google.com/maps/search/"
        search="Diabetic retinopathy doctors near me"
        webbrowser.open_new_tab(url+search)

    def buttonn2(self):
        url="https://aifordiabeticretinopathy.blogspot.com/"
        webbrowser.open_new_tab(url)
   
    def main(self):
        self.label4.setText("Loading....")
        import keras
        from keras.models import Sequential
        from keras.layers import Dense
        from keras.layers import Convolution2D
        from keras.layers import MaxPooling2D
        from keras.layers import Flatten
        from keras.layers import Dropout
        from keras.models import Model,load_model
        import numpy as np
        from keras.preprocessing import image
        self.completed=0
        while self.completed < 100:
            self.completed += 0.00001
            self.progressbar.setValue(self.completed)
        
        # self.label4.setText("Loading....")
        classifier=Sequential()

        classifier.add(Convolution2D(32,3,3,input_shape=(128,128,3),activation='relu'))
        classifier.add(MaxPooling2D(pool_size=(2,2)))

        classifier.add(Convolution2D(32,3,3,activation='relu'))
        classifier.add(MaxPooling2D(pool_size=(2,2)))

        classifier.add(Convolution2D(64,3,3,activation='relu'))
        classifier.add(MaxPooling2D(pool_size=(2,2)))

        classifier.add(Flatten())

        classifier.add(Dense(output_dim=128,activation='relu'))
        classifier.add(Dense(output_dim=128,activation='relu'))
        #classifier.add(Dropout(p=0.1))

        classifier.add(Dense(output_dim=5,activation='softmax'))

        classifier.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

        from keras.preprocessing.image import ImageDataGenerator,img_to_array,load_img
        # train_datagen = ImageDataGenerator(
        #         rescale=1./255,
        #         shear_range=0.2,
        #         zoom_range=0.2,
        #         horizontal_flip=True)

        # test_datagen = ImageDataGenerator(rescale=1./255)

        # training_set = train_datagen.flow_from_directory(
                
        #         "D:/diabatess/training_set",
        #         target_size=(128,128),
        #         batch_size=32,
        #         class_mode='categorical')

        # testing_set = test_datagen.flow_from_directory(
        #         "D:/diabatess/test_test",
        #         target_size=(128,128),
        #         batch_size=32,
        #         class_mode='categorical')

        model=load_model('diafinal.h5')
     
        test_image=image.load_img(self.path,target_size=(128,128))
        print(self.path)
        test_image=image.img_to_array(test_image)
        test_image=np.expand_dims(test_image,axis=0)
        
        proba = model.predict(test_image)[0]
        idx = np.argmax(proba)

        self.label4.setText("Loading Complete")
        print(proba)
        if idx==0:
            label="Mild"
        elif idx==1:
            label="Moderate"
        elif idx==2:
            label="No DR"
        elif idx==3:
            label="Proliferative DR"
        else:
            label="Severe"
        label = "{}: {:.2f}%".format(label, proba[idx] * 100)
        print(label)
        self.label2.setText("Result:- "+str(label))
        a=[]
        b=['Mild','Moderate','No DR','Prolifrative DR','Severe']
        for i in proba:
            a.append(round(i*100,3))
            
        c=zip(a,b)
        d=[]
        for i in c:
            d.append(i)
        print(d)
        self.label3.setText( "Chances of: "+str(d))
        
        # timer = QTimer()
        # self.label4.setText(" ")
        
        # timer.timeout.connect(self.label4.setText(" "))
        # timer.start(1000)
        # time.sleep(15)
        # self.label4.setText("  ")
App = QApplication(sys.argv)
splash_pix = QPixmap("output.png")
splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
splash.setMask(splash_pix.mask())
splash.show()
App.processEvents()
# Simulate something that takes time
time.sleep(3)
window = Window()
window.show()
splash.finish(window)

sys.exit(App.exec())




