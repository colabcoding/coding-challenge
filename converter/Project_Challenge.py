'''
Length Converter
MIT License
Copyright (c) 2022 Jonathan Sugianto
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
title = 'Select the base unit:'
options = ['mm','cm','m','km']
#Arrow (Indicator)
Arrow = '->'
#Base Unit and Target Unit
baseunit, indexbaseunit = pick(options, title, indicator=Arrow)
title = 'Base unit {} to:'.format(baseunit)
targetunit, indextargetunit = pick(options,title, indicator=Arrow)

#Milimeter
if baseunit == 'mm':
    if targetunit == 'mm':
        factor = 1
    if targetunit == 'cm':
        factor = 0.1
    if targetunit == 'm':
        factor = 0.001
    if targetunit == 'km':
        factor = 0.0000001

#Centi Meter        
if baseunit == 'cm':
    if targetunit == 'mm':
        factor = 10
    if targetunit == 'cm':
        factor = 1
    if targetunit == 'm':
        factor = 0.01
    if targetunit == 'km':
        factor = 0.000001

#Meter
if baseunit == 'm':
    if targetunit == 'mm':
        factor = 1000
    if targetunit == 'cm':
        factor = 100
    if targetunit == 'm':
        factor = 1
    if targetunit == 'km':
        factor = 0.001

#Kilometer
if baseunit == 'km':
    if targetunit == 'mm':
        factor = 1000000
    if targetunit == 'cm':
        factor = 100000
    if targetunit == 'm':
        factor = 1000
    if targetunit == 'km':
        factor = 1
        
#Input and Output        
Input = float(input("Input  : Enter the number to convert from {} to {}: ".format(baseunit,targetunit)))
Output = round(Input * factor,2)

print('Output : {} {} is {} {}'.format(Input, baseunit, Output, targetunit))

