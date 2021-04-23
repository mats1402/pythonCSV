import csv
 
with open('hrdata_modified.csv') as dataframe:
    reader = csv.reader(dataframe)
 
    found = 0
    success = 0
 
    employee = input('Enter Employee Name: ')
    employeeID = input('Enter ID# (XX-XXX-XXXX): ')
 
    for row in reader:
        if employee in row[0]:
            found = 1
            if row[4] == employeeID:
                success = 1
    if found == 1:
        print('Employee found')
        if success == 1:
            print('Access Granted')
        else:
            print('Access denied')
    else:
        print('Employee not found')