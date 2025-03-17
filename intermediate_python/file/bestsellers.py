import csv

# # Open the CSV file in 'read' mode
# with open('example.csv', 'r') as file:
# # Create a CSV reader object
#     csv_reader = csv.reader(file)

# for row in csv_reader:
#     print(row)

# # Data to be written to the CSV file
# data_to_write = [
#   ['Name', 'Age', 'Grade'],
#   ['Alice', 25, 'A'],
#   ['Bob', 22, 'B'],
#   ['Charlie', 28, 'A+']
# ]

# # Open the CSV file in 'write' mode
# with open('output.csv', 'w', newline='') as file:
# # Create a CSV writer object
#     csv_writer = csv.writer(file)

# # Write the data to the CSV file
#     csv_writer.writerows(data_to_write)

csv_file_path = 'Bestseller - Sheet1.csv'

best_selling_book = None
max_sales = 0

with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)

    csv_file.readline()

    for row in csv_reader:
        current_sales = float(row[4])
        if current_sales > max_sales:
            max_sales = current_sales
            best_selling_book = row

output_file_path = 'bestseller_info.csv'
with open(output_file_path, 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)

    csv_writer.writerrow(['Book', 'Author', 'Sales in Millions'])

    csv_writer.writerrow(
        [best_selling_book[0], best_selling_book[1], best_selling_book[4]])

print('Bestselling info written to', output_file_path)