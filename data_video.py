import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from PIL import Image
from pytube import YouTube
from popup import POPUP
import io
import requests
import os
import cv2

class download:
    def __init__(self, video):
        self.user = os.getlogin()
        self.video = YouTube(video)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.menu()


    def menu(self):
        self.root = tk.Toplevel()
        self.root.resizable(False, False)
        self.root.title("Data video")
        self.frm = tk.Frame(self.root, padx=10, pady=10)
        self.frm.grid()
        self.root.focus_set()
        
        self.image_video()
        self.description()

        tk.Label(self.frm, text=f"Title: {self.video.title}", font=("Source Code Pro Black", 8)).grid(
            column=1, row=1)

        tk.Label(self.frm, text=f"Length: {self.video.length /60:.2f} minutes",
                 font=("Source Code Pro Black", 8)).grid(column=0, row=2, sticky="we")

        tk.Label(self.frm, text=f"Author: {self.video.author}", font=("Source Code Pro Black", 8)).grid(
            column=0, row=3)

        self.views_video()

        tk.Label(self.frm, text=f"Date: {self.video.publish_date}", font=("Source Code Pro Black", 8)).grid(
            column=0, row=1)

        tk.Checkbutton(self.frm, text="Hight quality", variable=self.var1, onvalue=1, offvalue=0).grid(
            column=1, row=2)

        tk.Checkbutton(self.frm, text="Low quality", variable=self.var2, onvalue=1, offvalue=0).grid(
            column=1, row=3)

        tk.Checkbutton(self.frm, text="Audio only", variable=self.var3, onvalue=1, offvalue=0).grid(
            column=1, row=4)

        tk.Button(self.frm, text="New url", font=("Source Code Pro Black", 8),
                  command=self.new_url, cursor="hand2").grid(column=3, row=2)

        tk.Button(self.frm, text="Save", width=8, font=("Source Code Pro Black", 8),
                 command=self.save, cursor="hand2").grid(column=4, row=2)

        self.root.grab_set()




    def image_video_download(self):
        check = os.path.exists(f"/home/{self.user}/youtube_gui")
        image = self.video.thumbnail_url
        response = requests.get(image)
        image_byte = io.BytesIO(response.content)
        img = Image.open(image_byte)
        if check:
            img.save(f"/home/{self.user}/youtube_gui/.image/image_video.png")

            #Edit image width
            src = cv2.imread(f"/home/{self.user}/youtube_gui/.image/image_video.png", cv2.IMREAD_UNCHANGED)
            new_width =  200

            dsize = (new_width, src.shape[0])

            # resize image
            output = cv2.resize(src, dsize, interpolation = cv2.INTER_AREA)
            #Save image 
            cv2.imwrite(f"/home/{self.user}/youtube_gui/.image/image_video.png",output)

            #Edit image height
            src2 = cv2.imread(f"/home/{self.user}/youtube_gui/.image/image_video.png", cv2.IMREAD_UNCHANGED)
            new_height =  200

            dsize = (new_height, src2.shape[1])

            # resize image
            output = cv2.resize(src2, dsize, interpolation = cv2.INTER_AREA)
            #Save image
            cv2.imwrite(f"/home/{self.user}/youtube_gui/.image/image_video.png",output)
        else:
            os.mkdir(f"/home/{self.user}/youtube_gui")
            os.mkdir(f"/home/{self.user}/youtube_gui/.image")
            img.save(f"/home/{self.user}/youtube_gui/.image/image_video.png")

            #Edit image width
            src = cv2.imread(f"/home/{self.user}/youtube_gui/.image/image_video.png", cv2.IMREAD_UNCHANGED)
            new_width =  200

            dsize = (new_width, src.shape[0])

            # resize image
            output = cv2.resize(src, dsize, interpolation = cv2.INTER_AREA)
            #Save image 
            cv2.imwrite(f"/home/{self.user}/youtube_gui/.image/image_video.png",output)

            #Edit image height
            src2 = cv2.imread(f"/home/{self.user}/youtube_gui/.image/image_video.png", cv2.IMREAD_UNCHANGED)
            new_height =  200

            dsize = (new_height, src2.shape[1])

            # resize image
            output = cv2.resize(src2, dsize, interpolation = cv2.INTER_AREA)
            #Save image
            cv2.imwrite(f"/home/{self.user}/youtube_gui/.image/image_video.png",output)


    def image_video(self):
        self.image_video_download()
        self.img = PhotoImage(file="/home/p-rod/youtube_gui/.image/image_video.png")
        tk.Label(self.frm, image=self.img).grid(column=0, row=0)


    def description(self):
        video_descrip = self.video.description

        with open(f"/home/{self.user}/youtube_gui/.image/description.txt", "w")as file:
            file.writelines(video_descrip)

        with open(f"/home/{self.user}/youtube_gui/.image/description.txt")as file2:
            var1 = file2.read()

        text = tk.Text(self.frm, height=12)
        text.insert(INSERT, f"{var1} \n")
        text.grid(column=1, row=0, columnspan=4, sticky="we")
        
    def views_video(self):
        views = self.video.views
        if views < 1000 :
            tk.Label(self.frm, text=f"Views: {self.video.views}", font=("Source Code Pro Black", 8)).grid(
                column=0, row=4)
        elif views > 1000 and views <1000000:
            tk.Label(self.frm, text=f"Views: {self.video.views}K", font=("Source Code Pro Black", 8)).grid(
                column=0, row=4)
        elif views > 1000000:
            tk.Label(self.frm, text=f"Views: {self.video.views}M", font=("Source Code Pro Black", 8)).grid(
                column=0, row=4)


    def save(self):
        if self.var1.get() == 1 and self.var2.get() == 0 and self.var3.get() == 0:
            with open(f"/home/{self.user}/youtube_gui/{self.video.title}.txt", "w")as file:
                file.writelines(self.video.description)
            self.video.streams.get_highest_resolution().download(f"/home/{self.user}/youtube_gui")
            POPUP()
            
        elif self.var2.get() == 1 and self.var1.get() == 0 and self.var3.get() == 0:
            with open(f"/home/{self.user}/youtube_gui/{self.video.title}.txt", "w")as file:
                file.writelines(self.video.description)
            self.video.streams.get_lowest_resolution().download(f"/home/{self.user}/youtube_gui")
            POPUP()
            
        elif self.var3.get() == 1 and self.var1.get() == 0 and self.var2.get() == 0:
            with open(f"/home/{self.user}/youtube_gui/{self.video.title}.txt", "w")as file:
                file.writelines(self.video.description)
            self.video.streams.get_audio_only().download(f"/home/{self.user}/youtube_gui")
            POPUP()
            
        elif self.var1.get() == 1 and self.var2.get() == 1 and self.var3.get() == 1:
            with open(f"/home/{self.user}/youtube_gui/{self.video.title}.txt", "w")as file:
                file.writelines(self.video.description)
            self.video.streams.get_audio_only().download(f"/home/{self.user}/youtube_gui/Audio")
            self.video.streams.get_highest_resolution().download(f"/home/{self.user}/youtube_gui/Hight quality")
            self.video.streams.get_lowest_resolution().download(f"/home/{self.user}/youtube_gui/Low quality")
            POPUP()
            
        elif self.var1.get() == 1 and self.var2.get() == 1 and self.var3.get() == 0:
            self.video.streams.get_highest_resolution().download(f"/home/{self.user}/youtube_gui/Hight quality")
            self.video.streams.get_lowest_resolution().download(f"/home/{self.user}/youtube_gui/Low quality")
            POPUP()

        elif self.var1.get() == 1 and self.var2.get() == 0 and self.var3.get() == 1:
            self.video.streams.get_audio_only().download(f"/home/{self.user}/youtube_gui/Audio")
            self.video.streams.get_highest_resolution().download(f"/home/{self.user}/youtube_gui/Hight quality")
            POPUP()
            
        elif self.var2 == 1 and self.var1.get() == 1 and self.var3 == 0:
            self.video.streams.get_lowest_resolution().download(f"/home/{self.user}/youtube_gui/Low quality")
            self.video.streams.get_highest_resolution().download(f"/home/{self.user}/youtube_gui/Hight quality")
            POPUP()

        elif self.var.get() == 1 and self.var1.get() == 0 and self.var3.get() == 1:
            self.video.streams.get_lowest_resolution().download(f"/home/{self.user}/youtube_gui/Low quality")
            self.video.streams.get_audio_only().download(f"/home/{self.user}/youtube_gui/Audio")
            POPUP()
            
        elif self.var3.get() == 1 and self.var1 == 1 and self.var2.get() == 0:
            self.video.streams.get_audio_only().download(f"/home/{self.user}/youtube_gui/Audio")
            self.video.streams.get_highest_resolution().download(f"/home/{self.user}/youtube_gui/Hight quality")
            POPUP()
            
        elif self.var3.get() == 1 and self.var1.get() == 0 and self.var2.get() == 1:
            self.video.streams.get_audio_only().download(f"/home/{self.user}/youtube_gui/Audio")
            self.video.streams.get_lowest_resolution().download(f"/home/{self.user}/youtube_gui/Low quality")
            POPUP()

    def new_url(self):
        self.root.destroy()