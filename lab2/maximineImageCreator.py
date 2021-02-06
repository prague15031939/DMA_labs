from PIL import Image, ImageDraw
import threading

class maximineImageCreator:

    def __init__(self, width, height, directory):
        self.imageWidth = width
        self.imageHeight = height
        self.__coreColores = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fff799', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080']
        self.__directory = directory
        self.__name = 0

    def createNew(self, imageList, classCores):
        img = Image.new("RGB", (self.imageWidth, self.imageHeight), (255, 255, 255))
        drawObject = ImageDraw.Draw(img)

        for vector in imageList:
            pointColor = self.__coreColores[vector[2]]
            drawObject.ellipse((vector[0] - 1, vector[1] - 1, vector[0] + 1, vector[1] + 1), fill=pointColor)

        for vector in classCores:
            drawObject.ellipse((vector[0] - 3, vector[1] - 3, vector[0] + 3, vector[1] + 3), fill="#000000")

        img.save(f"{self.__directory}{self.__name}.jpg")
        self.__name += 1
