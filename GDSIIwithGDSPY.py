import scipy.io
import numpy
import gdspy
import math

data =scipy.io.loadmat('myfile.mat')

xl= data['XP_L4_0']
yl= data['YP_L4_0']
ang = data['angle']

xlim = xl.shape[1]
ylim = xl.shape[0]

layout = gdspy.GdsLibrary()

unit_cell = 0.4
cell = layout.new_cell("MyCell")
x = 0
y = 0
for j in range(ylim):
    for i in range(xlim):
        rad_ang = (ang[j,i]*(math.pi)/180)      #Convert to radians because gdspy works with radians
        L = xl[j,i]     #length
        H = yl[j,i]     #Height
        rectangle = gdspy.Rectangle((x-(L/2), y-(H/2)), (x+(L/2), y+(H/2))) 
        rectangle=rectangle.rotate(rad_ang, (x,y))
        cell.add(rectangle)
        x = x + unit_cell

    y = y - unit_cell
    x = 0

layout.write_gds("rectangle.gds")
