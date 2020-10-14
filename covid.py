import csv

temp = []
results = []

with open('C:/Users/amade/Desktop/WHO-COVID-19-global-data.csv', newline='') as database:
    reader = csv.DictReader(database)
    for row in reader:
        if row[' Country_code'] == 'AR':
            temp.append(row['Date_reported'])
            temp.append(row[' New_cases'])
            temp.append(row[' Cumulative_cases'])
            temp.append(row[' New_deaths'])
            temp.append(row[' Cumulative_deaths'])
            results.append(temp)
            temp = []

    
    for result in results:
        print(', '.join(result), end='\n')