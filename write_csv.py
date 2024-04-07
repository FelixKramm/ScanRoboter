import csv


def write_row(row, input_array):
    # Name of the existing CSV file
    csv_file = "/home/felix/shared/data.csv"

    # Read the existing CSV file
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Modify the second row (index 1)
    row = ["objects"]
    for point in input_array:
        row.append(point)
    data[1] = row 

    # Write the modified data back to the CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("Second row has been modified in", csv_file)
    
def write_ego(input_pos):
    # Name of the existing CSV file
    csv_file = "/home/felix/shared/data.csv"

    # Read the existing CSV file
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Modify the second row (index 1)
    row = ["ego"]
    for point in input_array:
        row.append(point)
    data[0] = row 

    # Write the modified data back to the CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("first row has been modified in", csv_file)
