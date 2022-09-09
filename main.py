from pytube import YouTube, Playlist
import os
import subprocess


def download_video():
    yt = YouTube(url)

    print('Baixando video', yt.title)

    yt.streams\
        .filter(progressive=True, file_extension='mp4')\
        .order_by('resolution')\
        .desc()\
        .first()\
        .download(path)


def download_all_videos_in_playlist():
    global url

    p = Playlist(url)

    print('Baixando videos da playlist', p.title)

    for video_url in p.video_urls:
        url = video_url
        download_video()


def download_audio():
    yt = YouTube(url, on_complete_callback=convert_to_mp3)

    print('Baixando audio', yt.title)

    yt.streams\
        .filter(only_audio=True)\
        .first()\
        .download(path)


def convert_to_mp3(stream, file_path):
    audio_path = file_path.replace('mp4', 'mp3')
    ffmpeg = f'ffmpeg -i "{file_path}" "{audio_path}"'
    subprocess.run(ffmpeg)
    os.remove(file_path)
    print(f'Áudio {audio_path} baixado com sucesso!')


def download_all_audios_in_playlist():
    global url

    p = Playlist(url)

    print('Baixando audios da playlist', p.title)

    for video_url in p.video_urls:
        url = video_url
        download_audio()


if __name__ == '__main__':
    print('\nBem-vindo ao baixador de videos e áudios do YouTube!\n')

    url = input('Informe a URL do vídeo: ')
    path = input('Informe a pasta onde o arquivo deve ser baixado: ')

    print('Opções de download:', '1 - Video', '2 - Audio', '3 - Todos os vídeos de uma playlist',
          '4 - Todos os áudios de uma playlist', sep='\n')

    action = int(input('Informe o número da ação desejada: '))

    match action:
        case 1:
            download_video()
        case 2:
            download_audio()
        case 3:
            download_all_videos_in_playlist()
        case 4:
            download_all_audios_in_playlist()


