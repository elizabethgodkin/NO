import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import math

def readFile(path):
    ret = []

    with open(path) as f:
        text = f.read()
    
    text = text.split('\n\n')

    ret = []

    for i in text:
        p = i.split('\n')

        j = {
            'year': int(p[0]),
            'observed': float(p[1]),
            'model1': float(p[2]),
            'model2': float(p[3]),
            'model3': float(p[4])
        }

        ret.append(j)

    return ret

def sortByItemInJson(js, key):
    for i in range(len(js)):
        for j in range(0, len(js)- i - 1):
            if js[j][key] > js[j+1][key]:
                temp = js[j]
                js[j] = js[j+1]
                js[j+1] = temp
    return js

dat = readFile("data/modelling_predictions.txt")
dat = sortByItemInJson(dat, 'year')
n = len(dat) # Number of datapoints

dat_x = []
dat_y_ob = []
dat_y_m1 = []
dat_y_m2 = []
dat_y_m3 = []

for i in dat:
    dat_x.append(i['year'])
    dat_y_ob.append(i['observed'])
    dat_y_m1.append(i['model1'])
    dat_y_m2.append(i['model2'])
    dat_y_m3.append(i['model3'])

# plot data in each array with dat_x as the x axis for each.

#chi-square
c_m1 = 0
c_m2 = 0
c_m3 = 0

for i in dat:
    o = i['observed']
    m1 = i['model1']
    m2 = i['model2']
    m3 = i['model3']

    c_m1 += ((o - m1)**2)/(m1)
    c_m2 += ((o - m2)**2)/(m2)
    c_m3 += ((o - m3)**2)/(m3)


print('Chi-Square for model 1, 2, and 3 respectively')
print(c_m1)
print(c_m2)
print(c_m3)

# root means square error

rmse_m1 = 0
rmse_m2 = 0
rmse_m3 = 0
for i in dat:
    o = i['observed']
    m1 = i['model1']
    m2 = i['model2']
    m3 = i['model3']

    rmse_m1 += (m1 - o)**2
    rmse_m2 += (m2 - o)**2
    rmse_m3 += (m3 - o)**2


rmse_m1 = math.sqrt(rmse_m1/n)
rmse_m2 = math.sqrt(rmse_m2/n)
rmse_m3 = math.sqrt(rmse_m3/n)
print()
print('RMSE of model 1, 2, and 3 respectively')
print(rmse_m1)
print(rmse_m2)
print(rmse_m3)

# Mean absolute error
mae_m1 = 0
mae_m2 = 0
mae_m3 = 0
for i in dat:
    o = i['observed']
    m1 = i['model1']
    m2 = i['model2']
    m3 = i['model3']

    mae_m1 += abs(m1-o)
    mae_m2 += abs(m2-o)
    mae_m3 += abs(m3-o)

mae_m1 = mae_m1/n
mae_m2 = mae_m2/n
mae_m3 = mae_m3/n

# Pearson
sxx = 0

m1_sxy = 0
m2_sxy = 0
m3_sxy = 0

sum_x = 0
sum_x2 = 0

sum_y_m1 = 0
sum_y2_m1 = 0
sum_y_m2 = 0
sum_y2_m2 = 0
sum_y_m3 = 0
sum_y2_m3 = 0

sum_xy_m1 = 0
sum_xy_m2 = 0
sum_xy_m3 = 0

for i in dat:
    sum_y_m1 += i['model1']
    sum_y2_m1 += (i['model1'])**2

    sum_y_m2 += i['model2']
    sum_y2_m2 += (i['model2'])**2

    sum_y_m3 += i['model3']
    sum_y2_m3 += (i['model3'])**2

    sum_x += i['year']
    sum_x2 += (i['year'])**2

    sum_xy_m1 = (i['year']) * (i['model1'])
    sum_xy_m2 = (i['year']) * (i['model2'])
    sum_xy_m3 = (i['year']) * (i['model3'])




sxx = sum_x2 - ((sum_x ** 2)/(n))

m1_sxy = sum_xy_m1 - ((sum_x * sum_y_m1)/n)
m2_sxy = sum_xy_m2 - ((sum_x * sum_y_m2)/n)
m3_sxy = sum_xy_m3 - ((sum_x * sum_y_m3)/n)

m1_b = m1_sxy/sxx
m1_a = (sum_y_m1/n) - (m1_b * (sum_x/n))

m2_b = m2_sxy/sxx
m2_a = (sum_y_m2/n) - (m2_b * (sum_x/n))

m3_b = m3_sxy/sxx
m3_a = (sum_y_m3/n) - (m3_b * (sum_x/n))

print()
print('MAE of model 1, 2, and 3 respectively')
print(mae_m1)
print(mae_m2)
print(mae_m3)

plt.plot(dat_x, dat_y_ob, label='Observed')
plt.plot(dat_x, dat_y_m1, '.-', label='Model1')
plt.plot(dat_x, dat_y_m2, label='Model2')
plt.plot(dat_x, dat_y_m3, label='Model3')

plt.legend()

plt.xlabel("Year")
plt.ylabel("Mean NO2 emissions")
plt.title('Comparison of observed values and models 1, 2, and 3')
plt.show() 