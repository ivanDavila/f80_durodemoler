import numpy as np
import math
from scipy.optimize import curve_fit


func = lambda x,b,xmax,x50: 100/(1+np.power((np.log(xmax/x)/np.log(xmax/x50)),b))
func2 = lambda cum, b, xmax, x50 :xmax*np.power(xmax/x50, - np.power((100 - cum)/cum, 1/b))

class Swebrec:
    def __init__(self, sizes, percentage):
        Diff_F50 = np.zeros(len(sizes))
        xmax = np.amax(sizes)
        for i in range(len(percentage)):
            Diff_F50[i] = math.fabs(percentage[i]-50)
        X50_pos = np.where(Diff_F50 == np.amin(Diff_F50))[0]
        X50 = sizes[X50_pos][0]
        b = 1
        ini_para_sw = np.array([b,xmax,X50])

        # print("per %s" % percentage)
        # print("size %s" % sizes)
        # print("ini_para_sw %s" % ini_para_sw)

        self.para_sw, pcov = curve_fit(func, sizes, percentage, p0=ini_para_sw, method='lm')

    def cum_func(self, sizes):
        cum_adj = func(sizes, *self.para_sw)
        return cum_adj
    
    def size_func(self, cumulative):
        xsize = func2(cumulative, *self.para_sw)
        return xsize


def swebrec(sizes, percentage):
    Diff_F50 = np.zeros(len(sizes))
    xmax = np.amax(sizes)
    for i in range(len(percentage)):
        Diff_F50[i] = math.fabs(percentage[i]-50)
    X50_pos = np.where(Diff_F50 == np.amin(Diff_F50))[0]
    X50 = sizes[X50_pos][0]
    b = 1
    ini_para_sw = np.array([b,xmax,X50])

    para_sw, pcov = curve_fit(func, sizes, percentage, p0=ini_para_sw, method='lm')
    cum_adj = func(sizes, *para_sw)

    cumarray = np.arange(10,100,10)
    cmplx_cumarray = np.array(cumarray, dtype=np.complex_)
    # xsize = np.zeros(len(cumarray))

    xsize = func2(cmplx_cumarray, *para_sw)

    return sizes, cum_adj, xsize, cumarray

def swebrec_inv(sizes, percentage):
    Diff_F50 = np.zeros(len(sizes))
    xmax = np.amax(sizes)
    for i in range(len(percentage)):
        Diff_F50[i] = math.fabs(percentage[i]-50)
    X50_pos = np.where(Diff_F50 == np.amin(Diff_F50))[0]
    X50 = sizes[X50_pos][0]
    b = 1
    ini_para_sw = np.array([b,xmax,X50])

    para_sw, pcov = curve_fit(func2, sizes, percentage, p0=ini_para_sw, method='lm')
    
    cumarray = np.arange(10,100,10)
    size_adj = func2(cumarray, *para_sw)

    return size_adj, cumarray


if __name__ == '__main__':

    import matplotlib.pyplot as plt
    from pathlib import Path
    import pandas as pd

    data = pd.read_csv(str(Path(__file__).parent / 'data_rockdist.csv'))
    cumarray=np.arange(10,100, 10)
    # xval, size_adj, n_esferas, dk = swebrec(data['size'][1:-1], data['cum'][1:-1], cumarray)

    # size, cumulative  = swebrec(data['size'][1:-1].values, data['cum'][1:-1].values, cumarray)
    swebrecModel = Swebrec(data['size'][1:-1].values, data['cum'][1:-1].values)
    sizes  = data['size'][1:-1].values
    cumulative = swebrecModel.cum_func(sizes)

    cumulative2 = np.arange(10,100, 10)
    sizes2 = swebrecModel.size_func(cumulative2)

    plt.plot(sizes,  cumulative, c='b',marker = 'o',linewidth=2)
    plt.plot(sizes2,  cumulative2, c='r',marker = 'o',linewidth=2)
    # plt.plot(data['size'][1:-1], data['cum'][1:-1], c='r',marker = '*',linewidth=2)
    # plt.plot(size2, cumulative2, c='r',marker = '*',linewidth=2)
    plt.xlabel('size(mm)')
    plt.ylabel('cumulative')
    plt.show()