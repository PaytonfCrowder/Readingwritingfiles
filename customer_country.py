import csv

#customers = open('customers.csv', 'r')

#csv_file = csv.reader(customers)    #can use , delimiter="" if it's not a comm (cusomters, dilimiter=)

  #skips a row like a header

#for rec in csv_file:
   # print(rec)
   # print(f"first name: {rec[1]}")  #use the f and the squiggly lines
   # print(f"last name: {rec[2]}")
   # input()     #automatically produces a list and seperates by the commas

customers = open('customers.csv', 'r')

outfile = open('customer_country', 'w')

csv_file = csv.reader(customers)

next(csv_file)

outfile.write("first name, Last name, Country\n")

for rec in csv_file:
    first_name = rec[1]
    last_name = rec[2]
    country = rec[4]
    outfile.write(f"{first_name} {last_name} , {country}\n")