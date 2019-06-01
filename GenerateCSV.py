#!/usr/bin/python

# Import of the libraries
import csv
import random


# def - is a function
def createCsvLine(arr):
  # print(arr)
  return '"'  + '","'.join(arr) + '"\n'

#number of the inserts
records=1000
#print("Making %d records\n" % records)

# names of the columns
fieldnames=['id','name','age','city']

#open file, w - is for write
writer = open("people2.csv", "w")

# base of names and cities
names=['Deepak', 'Sangeeta', 'Geetika', 'Anubhav', 'Sahil', 'Akshay']
cities=['Delhi', 'Kolkata', 'Chennai', 'Mumbai']

# column names write in file
writer.write(createCsvLine(fieldnames))

# loop must start empty value
item = []
for i in range(0, records):
  # str(i) - id to string
  # random.choice(names) - random choice from names
  # str is for string
  #
  item = [str(i),random.choice(names),str(random.randint(24,26)), random.choice(cities)]
  # push item to the file
  writer.write(createCsvLine(item))

writer.close()


