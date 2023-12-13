import matplotlib.pyplot as plt

def plot_rotation(time, gyro, rotation):
	plt.plot(time, gyro, 'ro', time, rotation, 'bo')
	plt.show()
