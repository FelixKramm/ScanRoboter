import csv
import matplotlib.pyplot as plt


def read_csv_file(filename):
    data_array = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:
                if row[0] == 'ego':
                    ego_coords = [eval(coord) for coord in row[1:] if coord != '']
                    data_array.append(['ego'] + ego_coords)
                elif row[0] == 'objects':
                    object_coords = [eval(coord) for coord in row[1:] if coord != '']
                    data_array.append(['objects'] + object_coords)
    return data_array


def plot_coordinates(data_array):
    plt.ion()  # Activate interactive mode
    fig, ax = plt.subplots()
    ego_coords = None

    for row in data_array:
        if row[0] == 'ego':
            ego_coords = [coord for coord in row[1:] if coord != '']
            if len(ego_coords) > 1:
                for i in range(len(ego_coords) - 1):
                    x1, y1 = ego_coords[i]
                    x2, y2 = ego_coords[i + 1]
                    ax.plot([x1, x2], [y1, y2], color='grey', linestyle='-')
            if ego_coords:
                x_last, y_last = ego_coords[-1]
                ax.scatter(x_last, y_last, color='red', label='Last Ego Coordinate')
        elif row[0] == 'objects':
            object_coords = [coord for coord in row[1:] if coord != '']
            x_coords = [coord[0] for coord in object_coords]
            y_coords = [coord[1] for coord in object_coords]
            ax.scatter(x_coords, y_coords, color='black', label='Object Coordinates')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Coordinates')
    ax.legend()
    plt.pause(100000000000)  # Pause to update plot


def main():
    filename = 'X:\data.csv'
    data_array = read_csv_file(filename)
    plot_coordinates(data_array)


if __name__ == "__main__":
    main()