import matplotlib.pyplot as plt
import pandas as pd

# Assigning dataframe
df = pd.read_csv("climate.csv")

# Taking the data from each column and adding it to the respective lists using .tolist() method
temp = df["Temperature"].tolist()
co2 = df["CO2"].tolist()
years = df["Year"].tolist()


plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

