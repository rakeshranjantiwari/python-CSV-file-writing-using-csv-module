import csv
headers = ['Name', 'Mobile', 'Email']
data = [
    ['Tom', '1234567891', 'tom@test.com'],
    ['Vicky', '9988776655', 'vicky@test.com'],
    ['Tropsal', '7766554433', 'troposal@test.com'],
    ['Mahesh', '7464646463', 'mahesh@test.com']
]
#open the csv file in write mode
with open('users.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)
    csv_writer.writerows(data)