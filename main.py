#!/usr/bin/env python
# coding: utf-8

# In[3]:


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
from PyQt5.uic import loadUiType

import pymysql as MySQLdb


ui,_=loadUiType('netflix.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.label_3.hide()
        self.Handle_Buttons()
        
        
    
    def Handle_Buttons(self):
        self.pushButton.clicked.connect(self.login)
    
    def login(self):
        try:
            self.db=MySQLdb.connect(host='localhost', user='root', password='', db='netflix1')
            self.cur=self.db.cursor()
            
            usr=self.lineEdit.text()
            psw=self.lineEdit_2.text()
            
        
            
           
        except ConnectionRefusedError:
                print('No connection')
                self.label_3.show()
        
          
        else:
            
            
            
            
            if self.cur.execute('''SELECT * FROM record WHERE username=%s AND password=%s''',(usr,psw)):
                self.label_3.hide()
                print('Welcome')
                
            else:
                print('No data found')
                self.label_3.show()
            
            self.db.commit()
            
            
        
        
        
        
       
            
    
        
    
    
    
def main():
    app=QApplication(sys.argv)
    window=MainApp()
    window.show()
    app.exec()
    
if __name__=='__main__':
    main()


# In[ ]:




