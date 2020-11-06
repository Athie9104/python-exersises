# Box and whisker
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

a=[1.3, 3.4, 2.3, 9.8]
b=[3.5, 4.9, 1.3, 2.2]
c=[9.7, 1.5, 4.3, 0.9, 11.2]
data1=[a,b,c]

plt.boxplot(data1)
plt.xlabel("Colleges")
plt.ylabel("Scores")
plt.title("Boxplot for Colleges")

plt.show()

# Pie Chart
sizes=[25,20,45,10]
labels=['Cats','Dogs','Tigers','Goats']
data1=[a,b,c]
plt.pie(sizes,labels=labels, autopct='%.2f')
plt.axes().set_aspect('equal')
plt.show()


# Scater Plot
x=[5,7,8,7,2,17,2,9,4,11,12,9,6]
y=[99,86,87,111,86,103,87,94,78,77,85,86,77]
plt.scatter(x,y)
plt.show()

# Line of best fit
y = np.array([220, 330, 190, 340, 410, 445, 415])
x = np.array([14.2, 16.5, 11.8, 15.3, 18.8, 22.5, 19.5])

slope, intercept, r, p, std_err = stats.linregress(x, y)

def my_line_func(x):
    return slope * x + intercept
my_line_model = list(map(my_line_func, x))
plt.title("Soup sale in relation to temperature")
plt.xlabel("Temperature (degrees celcius)")
plt.ylabel("Price in Rands")
plt.scatter(x,y)
plt.plot(x, my_line_model)
plt.show()
