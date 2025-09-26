#!usr/bin/env python3
from scipy.special import legendre
import numpy as np

def gaussxw(N):
    """Encuentra las raices x y los pesos w de estas raices, para el polinomio de legendre de grado N.
    
    Ejemplos:
        >>> gaussxw(3)
        
        (array([-0.77459667,  0.        ,  0.77459667]), array([0.55555556, 0.88888889, 0.55555556]))

    Args:
        N(int): primer argumento

    Returns:
        (array):raices del polinomio de legendre de grado N
        (array):pesos asociados a cada raiz para calcular la cuadratura gausseana de orden N
        
    """
    x, w = np.polynomial.legendre.leggauss(N)
    
    
    return x, w
