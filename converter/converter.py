'''
Length Converter

MIT License
Copyright (c) 2022 Andi Dinata

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from pick import pick

LENGTH = {'mm':1000,'cm':100,'m':1,'km':0.001}

options = [x for x in LENGTH.keys()] 
pointer = '=>'

A,_ = pick(options,title = "Select the base unit",indicator=pointer)
B,_ = pick(options,title = "Base unit {} to :".format(A),indicator=pointer)

number = input("INPUT : Enter the number to convert from {} to {} : ".format(A,B))

if LENGTH[A] > LENGTH[B]:
    result = (float(number) * (LENGTH[B] / LENGTH[A]))
elif LENGTH[A] <= LENGTH[B]:
    result = (float(number) / (LENGTH[A]) * LENGTH[B])

print("OUTPUT: {} {} is {:,} {}".format(number,A,result,B))