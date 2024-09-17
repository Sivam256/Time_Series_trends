# Time_Series_trends
Code to calculate Trend and seasonality 
This code is done using modules pandas, matplotlib.pyplot, and statsmodels.tsa.seasonal


Formulas used:

    d=2q
    if Odd: m^t = (1/(2*q)+1)∑Xt-j, where summation from j=-q to q
    if Even: m^t = (0.5Xt-q + Xt-q+1 + ... + 0.5Xt+q)/d

    w^k = avg({Xk+jd - m^k+jd, q<k+jd<n-q})
            w1=> j=0,1,2,...

    S^k = wk - d^-1∑wi, where summation from i=1 to d

Then the points are plotted in graph to show visualizations.

