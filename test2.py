from tkinter import Canvas
import PyQt5
import cv2
import tkinter as tk
from PIL import Image, ImageTk

#Above import and below Makes canvas
root = tk.Tk()
root.title("Facial recognition test")
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
canvas.focus_set()

#Declare variables and also video capture
width, height = 500, 500
video_capture = cv2.VideoCapture(0)

#Set height and width of video capture
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

#Closes canvas when clicking escape
canvas.bind('<Escape>', lambda e: canvas.quit())

def videotest():
    #captures the video in a tuple
    tes, frame = video_capture.read()
    if tes:
        # convert image from GBR to RGB
        colourCon = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Convert to PIL image
        img = Image.fromarray(colourCon)
        #make img tk compatible
        img_tk = ImageTk.PhotoImage(img)
        # display image
        canvas.create_image(0, 0, image=img_tk, anchor = tk.NW)

        canvas.img_tk = img_tk

    canvas.after(10, videotest)

videotest()


root.mainloop()