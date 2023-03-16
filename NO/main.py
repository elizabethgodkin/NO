import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def readFile(filepath):
    ret = []
    with open(filepath) as f:
        lines = [line.rstrip() for line in f]
        for i in lines:
            ret.append(i.split())
    return ret

def sortByItemInJson(js, key):
    for i in range(len(js)):
        for j in range(0, len(js)- i - 1):
            if js[j][key] > js[j+1][key]:
                temp = js[j]
                js[j] = js[j+1]
                js[j+1] = temp
    return js

def main():
    data = readFile("data/data.txt")
    js = []

    for i in data:
        j = {
            "sitetype": i[0],
            "year": i[1],
            "mean": i[2],
            "ci": i[3]
        }
        js.append(j)

    rural = []
    urban_bg = []
    urban_tra = []
    for i in js:
        x = i["sitetype"]
        if x == "Rural_Background":
            rural.append(i)
        elif x == 'Urban_Background':
            urban_bg.append(i)
        elif x == 'Urban_Traffic':
            urban_tra.append(i)
    
    rural = sortByItemInJson(rural, "year")
    urban_bg = sortByItemInJson(urban_bg, "year")
    urban_tra = sortByItemInJson(urban_tra, "year")
    
    rural_x = []
    rural_y = []
    rural_ci_u = []
    rural_ci_l = []
    for i in rural:
        rural_x.append(int(i["year"]))
        rural_y.append(float(i["mean"]))

        rural_ci_u.append(float(i['mean']) + float(i['ci']))
        rural_ci_l.append(float(i['mean']) - float(i['ci']))

    urban_bg_x = []
    urban_bg_y = []
    urban_bg_ci_u = []
    urban_bg_ci_l = []
    for i in urban_bg:
        urban_bg_x.append(int(i["year"]))
        urban_bg_y.append(float(i["mean"]))

        urban_bg_ci_u.append(float(i['mean']) + float(i['ci']))
        urban_bg_ci_l.append(float(i['mean']) - float(i['ci']))

    urban_tra_x = []
    urban_tra_y = []
    urban_tra_ci_u = []
    urban_tra_ci_l = []
    for i in urban_tra:
        urban_tra_x.append(int(i["year"]))
        urban_tra_y.append(float(i["mean"]))

        urban_tra_ci_u.append(float(i['mean']) + float(i['ci']))
        urban_tra_ci_l.append(float(i['mean']) - float(i['ci']))

    plt.plot(rural_x, rural_y, 'g-', label="Rural Background")
    plt.plot(urban_bg_x, urban_bg_y, 'b-', label='Urban Background')
    plt.plot(urban_tra_x, urban_tra_y, 'r-' , label='Urban Traffic')


    plt.plot(rural_x, rural_ci_u, 'g.-')
    plt.plot(rural_x, rural_ci_l, 'g.-')

    plt.plot(urban_bg_x, urban_bg_ci_u, 'b.-')
    plt.plot(urban_bg_x, urban_bg_ci_l, 'b.-')
    
    plt.plot(urban_tra_x, urban_tra_ci_u, 'r.-')
    plt.plot(urban_tra_x, urban_tra_ci_l, 'r.-')
    
    plt.xlabel("Year")
    plt.ylabel("Mean NO2 emissions")
    plt.legend()
    plt.title('Annual NO2 emissions 1997-2021')
    plt.show()

if __name__ == "__main__":
    main()