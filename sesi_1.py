# -*- coding: utf-8 -*-
"""sesi 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HLag0bK0tbgcKqDWD83qLkD2wFQsXgSZ
"""

import numpy as np
import time
print(time.ctime())

k = np.array([[1,2,3],[2,3,2]])
print(k)

def pol():
  print("Kucing terbang")

hah = int(input("Masukkan: "))
if hah == 1:
  pol()

def kuc(lol):
  """
  bala bala mera mera gira gira
  wandahoy
  """
  if lol == 2:
    print(lol + 3)
  else:
     return lol

kum = int(input("Masukkan: "))
kuc(kum)

def my_adder(a,b,c):
  """
  function to sum the 3 numbers
  input: 3 numbers a,b,c
  output: the sum of of a,b,c
  """
  out = a + b + c
  return out

my_adder(2,3,4)

help(my_adder)

def temp(suhu, suhuh):
  if suhu < suhuh - 5:
    status = "Puanas"
  elif suhu > suhuh +5:
    status = "Nyalain AC"
  else:
      status = "matiin"
  return status

status = temp(65,75)
print(status)

status1 = temp(75,65)
print(status1)

status2 = temp(65,63)
print(status2)

h = 3
if h>1 and h<2:
  g = 2
elif h>2 and h<4:
  g = 4
else:
  g = 0

g

f = float(2)

print(f,"\n")
print(int(f))

o = 1
while o < 4:
  print(o)
  o +=1