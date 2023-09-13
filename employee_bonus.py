import csv

customers = open('EmployeePay.csv', 'r')

csv_file = csv.reader(customers)

next(csv_file)

for rec in csv_file:
    bon = int(rec[3])*float(rec[4])
    print(f"first name: {rec[1]}\nlast name: {rec[2]}\nSalary: $ {int(rec[3])}\nBonus:  ${bon:10,.2f}\nPay:    $ {int(rec[3])+bon}\n")
    input()

