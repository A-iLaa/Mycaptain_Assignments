# -*- coding: utf-8 -*-
"""Fibonocci.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tIk7E42RTv7pPW57iAsd2sjNAfrldW-5
"""

#Fibonacci series
n=int(input("Enter a number"))
fib=[0,1]
for i in range(2,n):
  fib.append(fib[i-2]+fib[i-1])
print(fib)