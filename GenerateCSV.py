#!/usr/bin/python
import csv
import random

def createCsvLine(arr):
  print(arr)
  return '"'  + '","'.join(arr) + '"\n'


records=1000
print("Making %d records\n" % records)

fieldnames=['id','name','age','city']
writer = open("people2.csv", "w")

names=['Deepak', 'Sangeeta', 'Geetika', 'Anubhav', 'Sahil', 'Akshay']
cities=['Delhi', 'Kolkata', 'Chennai', 'Mumbai']

writer.write(createCsvLine(fieldnames))
item = []
for i in range(0, records):
  item = [str(i),random.choice(names),str(random.randint(24,26)), random.choice(cities)]
  writer.write(createCsvLine(item))

writer.close()


