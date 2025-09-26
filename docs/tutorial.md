#Tutorial
Un ejemplo de uso de este codigo es el siguiente:

se desea calcular numericamente la integral:
\begin{align}
\int_1^3 {\rm{d}}x [x^6-x^2\sin(2x)]
\end{align}
primero hay que escribir la **funcion_integrando**  la cual se veria como el siguiente codigo:

    def funcion_integrando(variable):
    
    return variable**6-(variable**2)*np.sin(2*variable)
    
para que la integral de exacta las raices y pesos deben de venir del polinomio de legendre con orden $\ge 2N+1$, con N el orden del polinomio a integrar. En  este caso las raices y pesos deben de venir del polinomio de legendre de orden 11 o mayior por ende debemos obtener estos puntos y pesos agregando la siguiente linea a nuestro codigo:
    
    puntosypesos_11=gaussxw(11)

tercero hay que cambiar los limites de integracion, esto se hace cambiando las primeras dos entradas al invocar la funcion **gaussxwab**, Adicional a lo anterior a la hora de invocarla hay que pasarle los puntos y pesos guardados en puntosypesos_11, para realizar estos dos pasos agregamos la linea al codigo 

    puntosypesos_pond_11=gaussxwab(1, 3, puntosypesos_11[0], puntosypesos_11[1])

finalmente se realiza la sumatoria de los pesos por la funcion evaluada en esos puntos obteniendo el resultado de la integral y imprimiendo el resultado.

    print (integral(puntosypesos_pond_11))
    
obteniendo el resultado:

    317.34424
    



