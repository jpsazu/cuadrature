#!usr/bin/env python3
from scipy.special import legendre
import numpy as np

def gaussxwab(a, b, x, w):
    """Ajusta las raices "x" y los pesos "w" del polinomio de legendre de cierto grado tal que sirvan para evaluar una integral con limites "a" y "b" mediante la cuadratura
    gauseana.
    
    Ejemplos:
        >>> gaussxwab(0,2, array([-0.77459667,  0.        ,  0.77459667]), array([0.55555556, 0.88888889, 0.55555556]))
        
        (array([0.22540333, 1.        , 1.77459667]), array([0.55555556, 0.88888889, 0.55555556]))
       

    Args:
        a(float): primer argumento
        b(float): segundo argumento
        x(array): tercer argumento
        w(array): cuarto argumento

    Returns:
        (array):raices del polinomio de legendre de cierto grado ajustadas para evaluar una integral con limites "a" y "b" mediante la cuadratura gauseana.
        (array):pesos asociados a cada raiz del polinomio de legendre de cierto grado ajustados para evaluar una integral con limites "a" y "b" mediante la cuadratura gauseana.
        
    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w
