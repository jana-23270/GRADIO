# -*- coding: utf-8 -*-
"""Gradio.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_SWI5uYiKlDD4W6gcf-LeNAzShYDpTeB
"""

name=str(input("what is your name : "))
name

pip install gradio

import gradio as gr

def greet(name):
  return "Hello" + name + "!"

a=gr.Interface(fn=greet,inputs="text",outputs="text")
a.launch()

a=int(input("first num: "))
b=int(input("Second  num: "))
c=int(input("third num: "))
if a>b and a>c:
  print("a is greatest")
elif b>a and b>c:
  print("b is greatest")
else:
  print("c is greatest")

def greatestnum(A,B,C):
  if A>B and A>C:
    output1="A is Greatest"
  elif B>C and B>A:
    output1="B is Greatest"
  else:
    output1="C is Greatest"
  return output1

b=gr.Interface(fn=greatestnum,inputs=['number','number','number'],outputs="text")
b.launch(debug=True)

def factorial(a):
  fact=1
  for i in range(1,a+1):
    fact=fact*i
  output=fact
  return output

c=gr.Interface(fn=factorial,inputs="number",outputs="number")
c.launch(debug=True)