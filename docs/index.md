# Index

Se presenta un implementacion en Python del metodo de la cuadratura gausiana para el calculo numerico de integrales. En este caso especifico se busca calcular el resultado de la integral 

\begin{align}
\int_1^3 {\rm{d}}x [x^6-x^2\sin(2x)]
\end{align}
Lo anterior utilizando modulos de python como Scipy y Numpy.
Algunas ventajas y desventajas de este metodo son:

* Pros:
  - La ecuación para evaluar los errores es muy complicada. Sin embargo, la aproximación mejora con un error que decrece por un factor ${\rm{const.}} / N^2$ cuando se incrementa el número de subregiones de discretización en uno.
  - Ejemplo: Pasar de $N=10$ a $N=11$, mejora el resultado de la estimación por un factor de $\approx 100$. Esto indica que la convergencia ocurre con muy pocos puntos de muestreo.
  
* Cons:
  - Sólo funciona bien su la función a integrar es relativamente bien comportada. Si no lo es, se requiren más puntos de muestreo cerca de las regiones problemáticas.
  - Es muy complicado evaluar el error de manera precisa si lo necesitamos.


