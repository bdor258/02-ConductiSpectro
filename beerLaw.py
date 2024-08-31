# Goal: Create calibration curves and find the concentration of a unknown solution of potassium permanganate 
# import usefull libraries: panda and pyplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress

# First, using Beer's Law.
# Wavelength = 544 nm, concentration in mM/L
 

# Import data using panda's dataframe
data = pd.read_csv("data.csv")


# Figure
plt.plot(data.Concentration, data.Absorbance, "+", label = "données")
plt.xlabel("Concentration")
plt.ylabel("Absorbance")

# Compute and add a trendline

# Compute the slope and intercept of the trendline, and get covariant matrix
fit =  linregress(data.Concentration, data.Absorbance)
print(f"a = {fit[0]}")
print(f"b = {fit[1]}")
print(fit)
trendline = np.poly1d(fit[0:2])


plt.plot(data.Concentration, trendline(data.Concentration), color="r", label=f"{fit[0:2]}")
plt.legend()

plt.show()



# Second using conductivity
# molar ionic conductivity of ions: 
# K+ -> 73.5 .10^(-4)(S.m^2.mol^(-1)), MnO4 -> 61.3 .10^(-4)(S.m^2.mol^(-1)), resistivity in 10^(-4)S.m^(-1)
