import tkinter as tk 
from tkinter import messagebox, ttk
from media_item import MediaItem
## Choix pour dropdown ##
media_types = ["Music","Movie", "Tv-Show", "Podcast"]
formats = ["Mp3", "Mp4", "Flac", "CD", "DVD","Streaming"]

### Saving media ###
def save_media():
    media_type = media_type_var.get()
    format_ = format_var.get()
    title = title_entry.get()
    artist = artist_entry.get()
    year = year_entry.get()

    try:
        year = int(year)
    except ValueError:
        messagebox.showerror("invalid Input", "Year must be an integer")
        return
    
    item = MediaItem(media_type, format_, title, artist, year)
    item.add_item_to_list()
    MediaItem.save_json()
    messagebox.showinfo("Success",f"Media {title} added and saved!!")

## montrez tout les medias enregistré ##
def show_all_media():
    global media_listbox
    MediaItem.load_from_json()
    media_listbox.delete(0,tk.END)

    if not MediaItem.all_media:
        media_listbox.insert(tk.END, "No media items found.\n")
    else:
        for i, item in enumerate(MediaItem.all_media, start=1):
            media_listbox.insert(tk.END,f"{i}. {item.title} ({item.year}) - {item.artist} [{item.media_type} | {item.format}]\n")

def clear_all_media():
    MediaItem.all_media = []
    MediaItem.save_json()
    media_listbox.delete(0, tk.END)
    messagebox.showinfo("Cleared", "All media items have been deleted.")

def clear_selected_media():
    selection = media_listbox.curselection()
    if not selection: 
        messagebox.showwarning("No selected media", "Please select a media to delete.")
        return
    index = selection[0]
    del MediaItem.all_media[index]
    MediaItem.save_json()
    show_all_media()

def load_selected_media():
    selection = media_listbox.curselection()
    if not selection:
        return
    index = selection[0]
    item = MediaItem.all_media[index]
    title_entry.delete(0, tk.END)
    title_entry.insert(0, item.title)

    artist_entry.delete(0, tk.END)
    artist_entry.insert(0, item.artist)

    year_entry.delete(0, tk.END)
    year_entry.insert(0, str(item.year))

    media_type_var.set(item.media_type)
    format_var.set(item.format)

def edit_selected_media():
    selection = media_listbox.curselection()
    if not selection:
        messagebox.showwarning("No selection","Please select a media to edit")
        return
    index = selection[0]

    new_title = title_entry.get()
    new_artist = artist_entry.get()
    new_year = year_entry.get()
    new_media_type = media_type_var.get()
    new_format = format_var.get()

    try:
        new_year = int(new_year)
    except ValueError:
        messagebox.showerror("Invalid Input", "Year must be an integer.")
        return

    item = MediaItem.all_media[index]
    item.title = new_title
    item.artist = new_artist
    item.year = new_year
    item.media_type = new_media_type
    item.format = new_format

    MediaItem.save_json()
    show_all_media()
    messagebox.showinfo("Success", f"Media {new_title} update successfully!")

## Opening window ##
root = tk.Tk()
root.title("Media Library")
root.geometry("800x600")
root.configure(bg="#F5F5F5")

entry_frame = tk.Frame(root, bg="#F5F5F5")
entry_frame.grid(row=10,column=0 , padx=10,pady=10)

## Entry fields for creating media ##
tk.Label(entry_frame, text="Media type", bg="#F5F5F5").grid(row=0,column=0, sticky="W")
media_type_var = tk.StringVar()
media_type_var.set(media_types[0])#Valeur de défaut
media_type_dropdown = tk.OptionMenu(entry_frame, media_type_var,*media_types) # the * is to unpack the contents of the list 
media_type_dropdown.grid(row=0, column=1)

tk.Label(entry_frame, text="Format", bg="#f5f5f5").grid(row=1, column=0, sticky="w")
format_var = tk.StringVar(root)
format_var.set(formats[0])
format_var_dropdown =tk.OptionMenu(entry_frame, format_var,*formats)
format_var_dropdown.grid(row=1, column=1)


tk.Label(entry_frame, text="Title", bg="#f5f5f5").grid(row=2, column=0, sticky="w")
title_entry = tk.Entry(entry_frame)
title_entry.grid(row=2, column=1)


tk.Label(entry_frame, text="Artist", bg="#f5f5f5").grid(row=3, column=0, sticky="w")
artist_entry = tk.Entry(entry_frame)
artist_entry.grid(row=3, column=1)


tk.Label(entry_frame, text="Year", bg="#f5f5f5").grid(row=4, column=0, sticky="w")
year_entry = tk.Entry(entry_frame)
year_entry.grid(row=4, column=1)


# Buttons Frame
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.grid(row=1, column=0 ,padx=10, pady=10)

ttk.Button(button_frame, text="Submit", command=save_media).grid(row=0, column=0, padx=5)
ttk.Button(button_frame, text="Show All Media", command=show_all_media).grid(row=0, column=2, padx=5)
ttk.Button(button_frame, text="Edit Selected Media", command=edit_selected_media).grid(row=1, column=0, padx=5)
ttk.Button(button_frame, text="Delete Selected Media", command=clear_selected_media).grid(row=1, column=2, padx=5)
ttk.Button(button_frame, text="Clear All Media", command=clear_all_media).grid(row=2, column=1, padx=5)


# Listbox with Scrollbar
listbox_frame = tk.Frame(root)
listbox_frame.grid(row=0,column=0, padx=10,pady=10)

scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

media_listbox = tk.Listbox(listbox_frame, height=10, width=80, yscrollcommand=scrollbar.set)
media_listbox.pack(side=tk.LEFT)
scrollbar.config(command=media_listbox.yview)


media_listbox.bind("<<ListboxSelect>>", lambda event: load_selected_media())


root.mainloop()
