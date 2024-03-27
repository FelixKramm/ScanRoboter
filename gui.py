import csv
import matplotlib.pyplot as plt

def read_csv_file(filename):
    data_array = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == 'ego':
                ego_coords = [eval(coord) for coord in row[1:] if coord != '']
                data_array.append(['ego'] + ego_coords)
            elif row[0] == 'objects':
                object_coords = [eval(coord) for coord in row[1:] if coord != '']
                data_array.append(['objects'] + object_coords)
    return data_array

def plot_coordinates(data_array):
    for row in data_array:
        if row[0] == 'ego':
            color = 'red'
        elif row[0] == 'objects':
            color = 'black'
        coords = row[1:]
        x_coords = [coord[0] for coord in coords]
        y_coords = [coord[1] for coord in coords]
        plt.scatter(x_coords, y_coords, color=color, label=row[0])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Coordinates')
    plt.legend()
    plt.show()


def main():
    filename = 'X:\data.csv'
    plt.ion()  # Activate interactive mode
    fig, ax = plt.subplots()

    while True:
        data_array = read_csv_file(filename)
        ax.clear()  # Clear the previous plot
        for row in data_array:
            if row[0] == 'ego':
                color = 'red'
            elif row[0] == 'objects':
                color = 'black'
            coords = row[1:]
            x_coords = [coord[0] for coord in coords]
            y_coords = [coord[1] for coord in coords]
            ax.scatter(x_coords, y_coords, color=color, label=row[0])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Coordinates')
        ax.legend()
        plt.pause(1)  # Pause to update plot


if __name__ == "__main__":
    main()