import matplotlib.pyplot as plt
from random import randint
import numpy as np
import scipy.cluster.hierarchy as shc

def main():

	amount = int(input("points amount: "))
	x = np.array([[randint(1, amount + 5), randint(1, amount + 5)] for i in range(amount)])

	plt.figure(figsize=(10, 7))
	plt.title("dendrogram (min)")
	dend = shc.dendrogram(shc.linkage(x, method='single'))
	plt.show()

	plt.figure(figsize=(10, 7))
	plt.title("dendrogram (max)")
	dend = shc.dendrogram(shc.linkage(x, method='complete'))
	plt.show()

if __name__ == "__main__":
	main()
