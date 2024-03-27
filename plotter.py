import matplotlib.pyplot as plt

def plot_rotation(time, gyro, rotation, x, y, z):
	plt.plot(time, gyro, 'ro', time, rotation, 'bo')
	plt.show()
	print(z)
	plt.plot(time, x, 'r', time, y, 'ro', time, z, 'b')
	plt.show()
	
