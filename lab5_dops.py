import tkinter as tk
from PIL import ImageTk, Image
import requests
from io import BytesIO


def get_image():
    # получаем ссылку на картинку
    url = 'https://aws.random.cat/meow'
    resp = requests.get(url)
    img_url = resp.json().get('file')

    # загружаем картинку
    response = requests.get(img_url)
    img_data = response.content

    # преобразуем в тип картинки, а не содержания requests запроса
    img = Image.open(BytesIO(img_data))
    # меняем размер картинки, чтобы они были +- одинаковые
    # Image.Resampling.LANCZOS - сохраняет пропорции
    img = img.resize((500, 500), Image.Resampling.LANCZOS)
    return img

def update_img(lbl):
    # обновляем картинку
    new_img = ImageTk.PhotoImage(get_image())
    lbl.configure(image=new_img)
    lbl.photo = new_img

if __name__=="__main__":
    window = tk.Tk()
    window.title('Meow generator')
    vlabel = tk.Label(window)
    photo = ImageTk.PhotoImage(get_image())
    vlabel.configure(image=photo)
    vlabel.pack()
    switch_bottom = tk.Button(window,text="Lets change meow",command=lambda: update_img(vlabel))
    switch_bottom.pack()
    window.mainloop()