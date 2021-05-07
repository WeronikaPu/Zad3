# -*- coding: utf-8 -*-
"""
Created on Friday May  7 22:30 2021
author: Weronika
"""

def srednia(x,y):
    if x>0 and y>x:
        suma_niepodzielnych=0
        suma=0;
        for i in range(x,y+1):
            if i%2:
                suma_niepodzielnych+=1
                suma=suma+i
                
        print("Śrenia arytmetyczna liczb nieparzystych z przedziału:",x,y,"wynosi:",suma/suma_niepodzielnych)
    else:
        print("Podano nieprwidłowy przedział!")
            
    
   
x=input("Podaj początek przedziału:")
y=input("Podaj koniec przedziału:")

srednia(int(x),int(y))
    
