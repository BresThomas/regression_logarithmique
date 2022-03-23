import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

df = pd.read_csv("/Users/Thomas/PycharmProjects/regression_logarithmique/BCHAIN-MKPRU.csv")
df = df.iloc[::-1]
df = df[df['Value'] > 0]
df['Date'] = pd.to_datetime(df['Date'])

def funct(x, a, b):
    """Equation de fonction y = a*log(x)+b"""
    #return a*np.log(x)+b
    return (a *x + b)

# valeur x = 1 à len(df) et y = log de df['Value']
xdata = np.array([x+1 for x in range(len(df))])
log_ydata = np.log(df['Value'])
ydata = (df['Value'])

# curve_fit() function takes the test-function
# x-data and y-data as argument and returns
# the coefficients a and b in param and
# the estimated covariance of param in param_cov
#popt, pcov = curve_fit(funct, xdata, ydata, p0=(3.0, -10))
popt, pcov = curve_fit(funct, xdata, log_ydata)
print("a")
print(popt[0])
print("b")
print(popt[1])

fittedydata = funct(xdata, popt[0], popt[1])


plt.style.use("dark_background")

#plt.semilogy(df['Date'], df['Value'])
plt.semilogy(df['Date'], df['Value'])

#for i in range(-3, 5):
#    plt.fill_between(df['Date'], np.exp(fittedydata + i - 1), np.exp(fittedydata + i))

# calcul de r^2
r2 = r2_score(log_ydata, (fittedydata))
print("r2")
print(r2)


plt.fill_between(df['Date'], np.exp(fittedydata + 0.01), np.exp(fittedydata))


plt.ylim(bottom=1)

plt.show()
