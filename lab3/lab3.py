import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from BayesDivision import BayesDivision

def plotScatter(x1, y1, x2, y2, title=None):
	plt.plot(x1, y1, label="first")
	plt.plot(x2, y2, label="second")
	plt.xlabel('x')
	plt.ylabel('y')
	plt.grid(True)
	plt.title(title)
	plt.legend(loc='lower right')
	plt.show()

def main():

	def onlyDigits(char):
		return char >= "0" and char <= "9" or char == "."

	def startupRecognition():
		p1 = float(probability1Entry.get())
		p2 = float(probability2Entry.get())

		if not (0 <= p1 <= 1) or not (0 <= p2 <= 1) or not (p1 + p2 == 1):
			return

		workObject = BayesDivision(p1, p2)
		workObject.generateData()
		m1, m2, s1, s2 = workObject.findDistributionParams()
		x1, y1, x2, y2 = workObject.dividePoints(m1, m2, s1, s2)

		plotScatter(x1, y1, x2, y2)

		return

	root = tk.Tk()
	root.title("Bayes")
	root.geometry("350x170+300+100")

	labelProbability1 = tk.Label(root, text='p1:')
	labelProbability1.place(x = 10, y = 5)
	probability1Entry = ttk.Entry(root)
	probability1Entry.config(width = 20, font='Arial 9', validate="key", validatecommand=(root.register(onlyDigits), '%S'))
	probability1Entry.place(x = 12, y = 30)

	labelProbability2 = tk.Label(root, text='p2:')
	labelProbability2.place(x = 10, y = 60)
	probability2Entry = ttk.Entry(root)
	probability2Entry.config(width = 20, font='Arial 9', validate="key", validatecommand=(root.register(onlyDigits), '%S'))
	probability2Entry.place(x = 12, y = 80)

	btnProcess = tk.Button(root, text="recognize", command=startupRecognition)
	btnProcess.config(width=12, height=1)
	btnProcess.place(x=12, y=120)

	labelFalseAlarm = tk.Label(root, text='false alarm error:')
	labelFalseAlarm.place(x = 170, y = 5)
	falseAlarmEntry = ttk.Entry(root)
	falseAlarmEntry.config(width = 20, font='Arial 9', state="readonly")
	falseAlarmEntry.place(x = 172, y = 30)

	labelMissingDetecting = tk.Label(root, text='missing detecting error:')
	labelMissingDetecting.place(x = 170, y = 60)
	missingDetectingEntry = ttk.Entry(root)
	missingDetectingEntry.config(width = 20, font='Arial 9', state="readonly")
	missingDetectingEntry.place(x = 172, y = 80)

	labelTotalClassification = tk.Label(root, text='total classification error:')
	labelTotalClassification.place(x = 170, y = 110)
	totalClassificationEntry = ttk.Entry(root)
	totalClassificationEntry.config(width = 20, font='Arial 9', state="readonly")
	totalClassificationEntry.place(x = 172, y = 130)

	root.mainloop()

if __name__ == "__main__":
	main()
