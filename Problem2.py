import pandas as pd

cars = pd.read_csv('cars.csv')
rows = cars.iloc[[0,2,4,6,8],[0,2,4,6,8,10]]
print ('\nFirst five rows with odd-numbered columns: \n')
print (rows)

mazda = cars[:1]
print ('\nMazda RX4 Cars:\n')
print (mazda)

Z28cylinders = cars.loc[[23],['Model','cyl']]
print ('\nCamaro Z28 Cylinders:\n')
print (Z28cylinders)

cylindersgears = cars.loc[[1,28,18],['Model','cyl','gear']]
print ('\nMazda RX4 Wag, Ford Pantera L, and Honda Civic Cylinders and Gears:\n')
print (cylindersgears)