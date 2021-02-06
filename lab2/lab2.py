import tkinter as tk
from tkinter import ttk
from threading import Thread
import os
from maximine import maximine
from maximineImageCreator import maximineImageCreator

def main():

	def onlyDigits(char):
		return char >= "0" and char <= "9"

	def startupUI(btnProcess):
		canvasMain.delete("all")
		labelProcessing = tk.Label(root, text='processing..')
		labelProcessing.place(x = 350, y = 30)
		btnProcess["state"] = "disabled"
		return labelProcessing

	def finalizeUI(labelProcessing, btnProcess):
		labelProcessing.destroy()
		btnProcess["state"] = "normal"

	def cleanImageDirectory(path):
		for filename in os.listdir(path):
			filepath = path + filename
			if os.path.isfile(filepath) or os.path.islink(filepath):
				os.unlink(filepath)

	def startupRecognition():
		imageAmount = int(imageAmountEntry.get())
		if not (1000 <= imageAmount <= 20000):
			return

		labelProcessing = startupUI(btnProcess)
		cleanImageDirectory("./images/")
		workerThread = Thread(target=recognition, args=(imageAmount, canvasMain, labelProcessing, btnProcess, "./images/"))
		workerThread.daemon = True
		workerThread.start()

		return

	def recognition(imageAmount, canvasMain, labelProcessing, btnProcess, imageStoringDirectory):
		imgCreator = maximineImageCreator(canvasMain.winfo_width(), canvasMain.winfo_height(), imageStoringDirectory)

		workObject = maximine(imageAmount, canvasMain.winfo_width(), canvasMain.winfo_height())
		workObject.generateData()

		while True:
			workObject.splitByClasses()

			imgCreator.createNew(workObject.imageList, workObject.classCores)

			workObject.optimizeCores()
			core, dist = workObject.findPotentialCore()
			if not workObject.createNewCore(core, dist):
				break

		workObject.viewData(canvasMain)
		finalizeUI(labelProcessing, btnProcess)
		return

	root = tk.Tk()
	root.title("maximine")
	root.geometry("700x650+300+100")

	labelImageAmount = tk.Label(root, text='image amount:')
	labelImageAmount.place(x = 10, y = 5)
	imageAmountEntry = ttk.Entry(root)
	imageAmountEntry.config(width = 20, font='Arial 9', validate="key", validatecommand=(root.register(onlyDigits), '%S'))
	imageAmountEntry.place(x = 12, y = 30)

	canvasMain = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight() - 130, bg='white')
	canvasMain.place(x=0, y=75)

	btnProcess = tk.Button(root, text="recognize", command=startupRecognition)
	btnProcess.config(width=12, height=1)
	btnProcess.place(x=200, y=28)

	root.mainloop()

if __name__ == "__main__":
	main()
