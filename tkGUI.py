import customtkinter
import tkinter
from tkinter import END
from tkinter import *
from song import Song
import songsSDK

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# keep track of songs for delete func
songs = []

def add_to_list():

    song = Song(title_entry.get(), artist_entry.get())

    # if added and returns rowid
    if(songsSDK.add_song(song)):
        songs.append(song)

        #insert at end of listbox, using values obtained from entry box
        # first arg is where to insert (either index or END)
        listbox.insert(END, song)

        #clear entry boxes after
        title_entry.delete(0, END)
        artist_entry.delete(0, END)

# doesnt remove all copies graphically if duplicates until updated
def remove_from_list():
    #returns tuple with index of current selection
    song_tuple = listbox.curselection()
    #use first elem which is index to pop and store song
    song = songs.pop(song_tuple[0])

    #delete in db using SDK
    if (songsSDK.delete_song(song)):

        #delete graphically using index of current selection
        listbox.delete(song_tuple)

tk = customtkinter.CTk()
tk.title("Library")
tk.geometry("400x600")

#scrollbar
frame = customtkinter.CTkFrame(master=tk)
frame.pack(pady="10")
my_scrollbar = Scrollbar(frame, orient = VERTICAL)


#create LISTBOX
listbox  = tkinter.Listbox(frame, width = "50", height = "20", yscrollcommand = my_scrollbar.set)

#scrollbar config
my_scrollbar.config(command=listbox.yview)
my_scrollbar.pack(side=RIGHT, fill= BOTH)

#add to interface
listbox.pack()

# insert all songs from database
for song in songsSDK.get_songs():
    songs.append(song)
    listbox.insert(END, song)


title = tkinter.Label(tk, text="Song Title:", padx="5", pady ="5")
title.pack(pady = "10")

title_entry = tkinter.Entry(tk)
title_entry.pack()

artist = tkinter.Label(tk, text="Artist:", padx="5", pady ="5")
artist.pack(pady = "10")

artist_entry = tkinter.Entry(tk)
artist_entry.pack()

button = customtkinter.CTkButton(tk, text="Add Song", command = add_to_list)
button.pack(pady = "10")

button = customtkinter.CTkButton(tk, text="Remove Selected Song", command = remove_from_list)
button.pack()

tk.mainloop()