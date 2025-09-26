#Explanation
## Cuadratura Gaussiana
    
Uno de los métodos más poderosos para evaluar integrales de forma numérica es la **cuadratura Gaussiana**.

La idea principal de la cuadratura gaussiana esta dada por dada por
\begin{align}
\int_a^b {\rm{d}}x f(x) \approx \sum_{k=1}^{N} w_k f(x_k).
\end{align}
donde:
  * $w_k$ son los "pesos"
  * $x_k$ son los puntos de muestreo
  
Para la cuadratura Gaussiana:
  * Los puntos de muestreo se escogen de manera tal que **no son equidistantes**. Esto introduce más grados de libertad para la misma discretización en $N$ subregiones.
  * Es exacta para un polinomio de orden $(2N - 1)$.
  * Es decir, la cuadratura Gaussiana da la misma precisión que un polinomio de orden $(2N - 1)$.
  
De manera muy interesante, existe una **regla universal para escoger** <span class="arithmatex">\( w_k \)</span> y <span class="arithmatex">\( x_k \)</span>. Los pesos y puntos de muestreo se eligen tal que:<span class="arithmatex">\( x_k \)</span> corresponden a las <span class="arithmatex">\( N \)</span> raíces (ceros) de los polinomios de Legendre <span class="arithmatex">\( P_N(x) \)</span> de orden <span class="arithmatex">\( N \)</span>. Los pesos se eligen tal que: <span class="arithmatex">\( \displaystyle w_k = \left[\frac{2}{1-x^2}\left(\frac{dP_N}{dx}\right)^{-2}\right]_{x={x_k}} \)</span>, con <span class="arithmatex">\( x_k \)</span> que cumple <span class="arithmatex">\( P_N(x_k) = 0 \)</span>.






      
## Polinomios de Legendre

Los polinomios de Legendre son un sistema de polinomios ortogonales que pueden ser definidos de manera recursiva. Tenemos:
\begin{align}
\forall (M, N) \in\mathbb N^2, \quad \int_{-1}^1 {\rm{d}}x P_N(x)P_M(x) = \frac{2\delta_{MN}}{2N+1}.
\end{align}
Note que los polinomios están definidos en el intervalo $[-1, 1]$.
Los se definen empezando con
\begin{align}
P_0(x) = 1 \Rightarrow P_1(x) = x,
\end{align}
tal que los siguientes órdenes se generan con la regla de recursividad
\begin{align}
(N+1)P_{N+1}(x) = (2N+1)xP_N(x) -NP_{N-1}(x).
\end{align}
Alternativamente, los polinomios pueden ser definidos de manera iterativa bajo la regla (fórmula de Rodrigues)
\begin{align}
P_N(x) = \frac1{2^N N!}\frac{d^N}{dx^N}\left[(x^2-1)^N\right].
\end{align}

En la computadora, podemos utilizar "SciPy" para obtener los polinomios de Legendre.
La biblioteca Numpy nos permite evaluar los pesos y los puntos de muestreo para utilizar la cuadratura Gaussiana con polinomios de Legendre eso si solo para intervalos de integracion de 
$[-1, 1]$. Para escalar el intervalo a un $[a, b]$ general debemos usar la funcion **gaussxwab** programada en nuestro codigo.
