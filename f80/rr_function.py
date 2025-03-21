import statsmodels.api as sm
import numpy as np

def RR(s: np.array, dsize: np.array) -> list:
    #F_Acum y d(size) total para predicción, en donde se consideran todos los datos
    F_dExp      = s
    d_Expt      = dsize #np.array([304.8, 355.6,254, 203.2, 152.4, 101.6, 76.2, 63.5, 50.8, 38.1, 31.75, 25.4])

    ### AJUSTE FUNCIÓN ROSIN - RAMMLER
    #Linear Transformation Ln - Ln
    Y_Fd       = np.log(np.log(1/(1-(F_dExp/100))))
    X_d        = np.log(d_Expt)

    #OLS - Minimos Cuadrados Ordinarios
    X_dEX      =sm.add_constant(X_d,prepend=True)
    model      =sm.OLS(Y_Fd,X_dEX)
    linear_reg = model.fit()

    # Pendiente / Slope 
    m          = linear_reg.params[1]
    # Intercepto / Intercept
    b          = linear_reg.params[0]
    #Param - Exponent 'd'
    d         =np.exp(-b/m)

    # Ln -Ln  %F(d) Ajustado
    Y_FdAdj  = m*X_d + b

    #Predicción Ajustada RLS - Regresión Lineal Simple
    F_dAdj      = 100*(1-np.exp(-np.power(d_Expt/d,m)))
    return [m, d, F_dAdj, F_dExp]

def ESC_FF(Arr, FF):
    l=len(Arr)
    step=(100-FF)/(l)
    #print(np.arange(0, 100-FF, step))
    return 100 - np.arange(0, 100-FF, step)