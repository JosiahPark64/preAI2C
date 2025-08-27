import csv
import os

with open('pittsburgh-weather-2024.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        #print(row['Day'], row['High'], row['Low'], row['Precipitation'], row['Snow'])
        print(row)



#open using fileIO
#create list of high temps
#calc alverage daily high temp for the year