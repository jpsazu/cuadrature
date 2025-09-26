#!usr/bin/env python3
from scipy.special import legendre
import numpy as np

def funcion_integrando(variable):
    """Evalua la funcion que se busca integrar en un punto "variable" dado en este caso la funcion es $$ x^6 - x^2 \\sin(2x)$$ con x siendo la variable.
    
    Ejemplos:
        >>> funcion_integrando(3)
        
        731.5147394837903
       

    Args:
        variable(float): primer argumento

    Returns:
        (float):Devuelve el resultado de evaluar $$ x^6 - x^2 \\sin(2x)$$ cuando $x=variable$
        
    """
    return variable**6-(variable**2)*np.sin(2*variable)
