import tkinter as tk
from PIL import Image, ImageTk
import io, urllib.request, json

def returnImage():
    with urllib.request.urlopen("https://dog.ceo/api/breeds/image/random") as randomURL:
        image = json.loads(randomURL.read().decode())["message"]
        with urllib.request.urlopen(image) as imageURL:
            imageFile = io.BytesIO(imageURL.read())
    return imageFile

# root = tk.Tk()
# img = Image.open(returnImage())
# tkimage = ImageTk.PhotoImage(img)
# tk.Label(root, image=tkimage).pack()
# root.mainloop()
