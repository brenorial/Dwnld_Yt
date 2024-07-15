from pytube import YouTube
import os


def baixar_video(link, destino):
    try:
        video = YouTube(link).streams.get_highest_resolution()
        arquivo = video.download(output_path=destino)
        msg = 'Download do vídeo realizado!'
    except Exception as e:
        msg = f"Falha no download do vídeo: {str(e)}"
    finally:
        return msg


def baixar_audio(link, destino):
    try:
        audio = YouTube(link).streams.filter(only_audio=True).first()
        arquivo = audio.download(output_path=destino)

        # salvando o arquivo como mp3
        base, ext = os.path.splitext(arquivo)
        novo_nome = f"{base}.mp3"
        os.rename(arquivo, novo_nome)

        msg = 'Download do áudio realizado.'
    except Exception as e:
        msg = f'Falha no download do áudio: {str(e)}'
    finally:
        return msg
