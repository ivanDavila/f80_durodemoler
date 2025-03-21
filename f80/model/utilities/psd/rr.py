import numpy as np
import statsmodels.api as sm


def rosin_rammler(sizes:np.array, percentage:np.array, cumarray:np.array):
    y_fd = np.log(np.log(1/(1-(percentage/100))))
    x_d = np.log(sizes)

    # OLS - Minimos Cuadrados Ordinarios
    x_dex = sm.add_constant(x_d, prepend=True)
    model = sm.OLS(y_fd, x_dex)
    linear_reg = model.fit()

    # Prediccion
    b, m = linear_reg.params
    # print("exponente %0.3f" % m)

    d = np.exp(-b/m)
    # print("d %0.3f" % d)

    # step = (diameters[1] - diameters[0])/delta
    cumulative = []
    rocksize = []
    for cum in cumarray:
        rsize = (d)*(np.power(-np.log(1-(cum/100)),1/m))

        rocksize.append(rsize)
        cumulative.append(cum)

    # n_esferas: Cantidad de particulas
    # dk: Diametro por familia

    return b, m, rocksize, cumulative

def rosin_rammler2(sizes, percentage, diameters, rho, alpha, delta):
    y_fd = np.log(np.log(1/(1-(percentage/100))))
    x_d = np.log(sizes)

    # OLS - Minimos Cuadrados Ordinarios
    x_dex = sm.add_constant(x_d, prepend=True)
    model = sm.OLS(y_fd, x_dex)
    linear_reg = model.fit()

    # Prediccion
    b, m = linear_reg.params
    print("exponente %0.3f" % m)

    d = np.exp(-b/m)
    print("d %0.3f" % d)

    step = (diameters[1] - diameters[0])/delta
    rocksize = sizes
    cumulative = []
    rocksize = []
    for i in range(delta):
        size = step * i + diameters[0]
        rocksize.append(size)
        cum = 100*(1-np.exp(-np.power(size/d,m)))
        cumulative.append(cum)

    # n_esferas: Cantidad de particulas
    # dk: Diametro por familia

    return rocksize, cumulative

if __name__ == '__main__':
    import pandas as pd
    import matplotlib.pyplot as plt
    from pathlib import Path

    diam = [0.1, 70]
    alpha = 40 
    rho = 2.8

    data = pd.read_csv(str(Path(__file__).parent / 'data_rockdist.csv'))
    cumarray=np.arange(10,110, 10)
    n, b, size, cumulative = rosin_rammler(data['size'][1:-1], data['cum'][1:-1], cumarray)
    size2, cumulative2 = rosin_rammler2(data['size'][1:-1], data['cum'][1:-1], diam, rho, alpha, 10)

    plt.plot(size,  cumulative, c='b',marker = 'o',linewidth=2)
    plt.plot(size2, cumulative2, c='r',marker = '*',linewidth=2)
    # plt.plot(data['size'], data['cumulative'], c='g',marker = '',linewidth=2)
    plt.xlabel('size(mm)')
    plt.ylabel('cumulative')
    plt.show()
