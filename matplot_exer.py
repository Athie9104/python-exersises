# Example 1
import matplotlib.pyplot as plt
import numpy as np

x= np.array(["A", "B", "C", "D"])
y= np.array([3, 8, 1, 10])
plt.bar(x, y)
plt.show()

# Exercise 1
import matplotlib.pyplot as plt
cities=['East London', 'Cape Town', 'Kimberley', 'Durban']
rainfall= [140,  200, 120, 157]
x_pos = [i for i, _ in enumerate(cities)] #labels on the x-axis
#labeling and visuals
plt.bar(x_pos, rainfall, color='cyan')
plt.xlabel("cities")
plt.ylabel("Rainfall in (mm)")
plt.title("Rainfall for the 4 main cities in SA")
plt.xticks(x_pos, cities)
plt.show()


# Exercise 2
import matplotlib.pyplot as plt
import numpy as np

Testmarks =([98,78, 68, 73, 72, 97, 88, 60, 94, 95,
             80, 73, 82, 80, 99, 91, 74, 88, 70, 94,
             86, 81, 100, 99, 84, 93, 94, 79])
plt.title('Test marks box plot')
plt.boxplot((Testmarks))
plt.show()
