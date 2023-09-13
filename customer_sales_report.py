import csv

custid = '250'
total = 0
#open read and crete new file

sales = open('sales.csv', 'r')

outfile = open('salesreport.csv', 'w')

csv_file = csv.reader(sales)

next(csv_file)

outfile.write("Customer ID, Total\n")

for rec in csv_file:
    if custid == rec[0]:
        total += float(rec[3]) + float(rec[4]) +float(rec[5])

    else:
        outfile.write(f"{custid}, {total:10,.2f}\n")
        #write the custid, total to the outfile

        custid = rec[0]
        total = float(rec[3]) + float(rec[4]) + float(rec[5])

outfile.write(f"{custid}, {total:10,.2f}\n")