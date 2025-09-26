#!usr/bin/env python3
from scipy.special import legendre
import numpy as np

def integral (puntosypesos_pond):
    """Realiza la cuadratura gaussiana para evaluar la integral de una funcion, en este caso la funcion $$ x^6 - x^2 \\sin(2x)$$, con limites definidos por los puntos y pesos los cuales 
    pueden o no haber sido ponderados para limites particulares
    
    Ejemplos:
        >>> integral(array([0.22540333, 1.        , 1.77459667]), array([0.55555556, 0.88888889, 0.55555556]))
        
        18.11297368216817
       

    Args:
        puntosypesos_pond(array): primer argumento

    Returns:
        (float):Devuelve el producto escalar de  puntosypesos_pond[1] con la funcion integrando, en este caso $$ x^6 - x^2 \\sin(2x)$$, evaluada en puntosypesos_pond[0]
        
    """
    return np.dot(puntosypesos_pond[1],funcion_integrando(puntosypesos_pond[0]))
