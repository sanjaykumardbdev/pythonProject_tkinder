from tkinter import *
from PIL import Image, ImageTk

# ImageTk function allows to take jgp files:


top = Tk()
top.geometry("455x244")


photo = PhotoImage(file="2_image_png.png")
label_img = Label(image=photo)
label_img.pack()

# how to add jpg immage:  pip install pillow
#PIL: PYTHON IMAGING LIBRARY:

# For JPG images:
image1 = Image.open("2_image_jpg.jpg")
photo1 = ImageTk.PhotoImage(image1)
label_img_jpg = Label(image=photo1)
label_img_jpg.pack()


# For GIF images: not moving:
image2 = Image.open("2_image_gif.gif")
photo2 = ImageTk.PhotoImage(image2)
label_img_jpg = Label(image=photo2)
label_img_jpg.pack()

# add more images to this page: not working:
image31 = Image.open("2_image_jpg_Copy.JPG")
image32 = Image.open("2_image_png1.png")

photo3 = ImageTk.PhotoImage(image31, image31)
label_img_jpg = Label(image=photo3)
#label_img_jpg = Label(image=photo32)
label_img_jpg.pack()


top.mainloop()


