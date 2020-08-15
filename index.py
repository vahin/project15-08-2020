import plotly.express as px
import csv
from numpy import corrcoef as cf
newX, newY = None, None

# Vahin Sharma

print("===CSV CORRELATION FINDER===\n" + "By: Vahin Sharma")

def getds(dp, x, y):
    global newX
    global newY
    newX = x
    newY = y
    temp = []
    iceCreamSale = []
    with open(dp) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            temp.append(float(row[x]))
            iceCreamSale.append(float(row[y]))
    return {"x":temp, "y":iceCreamSale}

def findCorrelation(ds):
    correlation = cf(ds["x"], ds["y"])
    x = ""
    if round(correlation[0, 1]) == -1.0:
        x = "There is an Inverse correlation"
    elif round(correlation[0, 1]) == 1.0:
        x = "There is a correlation"
    else:
        x = "There is no correlation"
    print(x, "between '{}' and '{}'".format(newX, newY), "({})".format(correlation[0, 1]))

while True:
    ds = getds(input("Enter the path of the CSV file: "), input("Enter the row for X: "), input("Enter the row for Y: "))
    findCorrelation(ds)
