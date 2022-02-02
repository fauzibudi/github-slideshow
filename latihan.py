#latihaan -----0++++++5-------8++++++++11--------

print('\nLatihan\t-----0++++++5-------8++++++++11--------\n')
#latihan ------0++++++++++5----------

inputuser= float(input('Masukkan nilai ='))
a = inputuser > 0
b = inputuser < 5

hasil1 = a and b

#latihan ++++++++++5---------8+++++++++
a = inputuser < 5
b = inputuser > 8

hasil2 = a or b

#latihan ------8++++++++++11----------
a = inputuser > 8
b = inputuser < 11 

hasil3 = a and b

hasiltotal = hasil1 or hasil2 and hasil3
print('maka nilai total adalah', hasiltotal)

#latihan +++++0-----5+++++++8------11+++++++

print('\nLatihan\t+++++0-----5+++++++8------11+++++++\n')
inputuser = float(input('Input ='))
a = inputuser < 0
b = inputuser > 5
c = inputuser < 8
d = inputuser > 11
hasil = ((a or b) and c) or d
print('maka hasil total adalah', hasil) 
