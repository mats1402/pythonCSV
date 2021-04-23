from csv import writer
 
newEntry=['Ryan Curtis', '2012-02-14',76000.0,5]
 
with open('hrdata_modified.csv', 'a') as employee.file:
    employee.writer = writer(employee_file)
    employee_writer.writerow(newEntry)
 
    employee_file.close