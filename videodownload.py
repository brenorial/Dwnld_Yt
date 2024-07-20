import yt_dlp as youtube_dl
import os

def baixar_video(link, destino):
    try:
        print(f"Tentando baixar o vídeo do link: {link}")
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(destino, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }]
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            arquivo = ydl.prepare_filename(info_dict)
        msg = f'Download do vídeo realizado! Arquivo salvo em: {arquivo}'
    except Exception as e:
        msg = f"Falha no download do vídeo: {str(e)}"
    finally:
        return msg

def baixar_audio(link, destino):
    try:
        print(f"Tentando baixar o áudio do link: {link}")
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(destino, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            arquivo = ydl.prepare_filename(info_dict).replace('.webm', '.mp3').replace('.m4a', '.mp3')
        msg = f'Download realizado!'
    except Exception as e:
        msg = f'Falha no download do áudio: {str(e)}'
    finally:
        return msg
