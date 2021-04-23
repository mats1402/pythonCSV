import csv

with open('testCSV.csv') as csv_file:
    csv_reader = csv.reader(csv_file, skipinitialspace=True)
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {​​​​​​​",".join(row)}​​​​​​​​')
            line_count += 1
        else:
            print(f'\t{​​​​​​​​row[0]}​​​​​​​​ Cost {​​​​​​​​row[1]}​​​​​​​​, Sold {​​​​​​​​row[2]}​​​​​​​​, Profit {​​​​​​​​row[3]}​​​​​​​​.')
            line_count += 1
    print(f'Processed {​​​​​​​​line_count}​​​​​​​​ lines.')