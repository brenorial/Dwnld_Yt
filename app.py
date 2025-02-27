import os.path
import customtkinter
import sys
from tkinter.filedialog import askdirectory
from videodownload import baixar_video, baixar_audio
from PIL import Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.geometry("550x200")
window.title("YouTube Downloader MP4 e MP3")

script_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
img_path = os.path.join(script_dir, "bg.png")


img = customtkinter.CTkImage(Image.open(img_path), size=(430, 510))
img_label = customtkinter.CTkLabel(window, image=img, text='')
img_label.place(x=-5, y=-160)

def baixarmp3():
    msg_lbl.configure(text="")
    link = str(link_entry.get())
    if not link:
        msg_lbl.configure(text="Por favor insira um link.")
        return
    destino = askdirectory()
    if not destino:
        msg_lbl.configure(text="Por favor selecione um diretório.")
        return
    try:
        msg = baixar_audio(link, destino)
        msg_lbl.configure(text=msg)
    except Exception as e:
        msg_lbl.configure(text=str(e))

def baixarmp4():
    msg_lbl.configure(text="")
    link = str(link_entry.get())
    if not link:
        msg_lbl.configure(text="Por favor insira um link.")
        return
    destino = askdirectory()
    if not destino:
        msg_lbl.configure(text="Por favor selecione um diretório.")
        return
    try:
        msg = baixar_video(link, destino)
        msg_lbl.configure(text=msg)
    except Exception as e:
        msg_lbl.configure(text=str(e))

def baixarambos():
    msg_lbl.configure(text="")
    link = str(link_entry.get())
    if not link:
        msg_lbl.configure(text="Por favor insira um link.")
        return
    destino = askdirectory()
    if not destino:
        msg_lbl.configure(text="Por favor selecione um diretório.")
        return
    try:
        msg_audio = baixar_audio(link, destino)
        msg_video = baixar_video(link, destino)
        msg_lbl.configure(text=f"{msg_audio}\n{msg_video}")
    except Exception as e:
        msg_lbl.configure(text=str(e))

link_entry = customtkinter.CTkEntry(window, placeholder_text='URL do Vídeo', width=355, height=28)
link_entry.place(x=170, y=15)

download_btn = customtkinter.CTkButton(window, text='Baixar MP3 e MP4', width=160, height=28, command=baixarambos)
download_btn.place(x=268, y=105)

msg_lbl = customtkinter.CTkLabel(window, text='', width=340, height=28)
msg_lbl.place(x=180, y=150)

mp4_btn = customtkinter.CTkButton(window, text='Baixar em MP4', width=160, height=28, command=baixarmp4)
mp4_btn.place(x=365, y=55)

mp3_btn = customtkinter.CTkButton(window, text='Baixar em MP3', width=160, height=28, command=baixarmp3)
mp3_btn.place(x=170, y=55)

fonte = customtkinter.CTkFont(family='Helvetica', size=10)

texto = customtkinter.CTkLabel(window, text="Desenvolvido por Rial", font=fonte)
texto.place(x=300, y=210)

window.mainloop()
