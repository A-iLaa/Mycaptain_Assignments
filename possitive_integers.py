# -*- coding: utf-8 -*-
"""Possitive_Integers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XRikvbdlNWwSu8dJ6atimkzqDjs7r7Cc
"""

l=[1,-2,9,-5]
for i in l:
  if i<=0:
    l.remove(i)
print(l)