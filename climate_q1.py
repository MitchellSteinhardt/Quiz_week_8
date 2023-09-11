import matplotlib.pyplot as plt

# Importing sqlite3
import sqlite3

# Moved Tables above database querying
years = []
co2 = []
temp = []

# Connection to db, cursor and query created
connection = sqlite3.connect('climate.db')
cursor = connection.cursor()
query = "SELECT Year, co2, Temperature FROM ClimateData"
cursor.execute(query)


# For each row at the cursor's fetchall, append to respective list
for row in cursor.fetchall():
    years.append(row[0])
    co2.append(row[1])
    temp.append(row[2])

cursor.close()
connection.close()


# Printing lists for clarity
print("Year data:", years)
print("co2 data:", co2)
print("Temp data:", temp)
        


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
plt.savefig("co2_temp_1.png") 
