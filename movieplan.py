import random, os
from collections import OrderedDict

bg_list = os.listdir(r'D:\backgrounds')
gif_list = os.listdir(r'D:\gifs')
song_list = os.listdir(r'D:\songs')

def get_background():
    t = len(bg_list) - 1
    n = random.randint(0,t)
    bg = bg_list[n]
    return bg

def get_gif():
    t = len(gif_list) - 1
    n = random.randint(0,t)
    gif = gif_list[n]
    return gif

def get_gifs(m):
    m2 = random.randint(1, m)
    gifs = []
    while len(gifs) < m2:
        gifs.append(get_gif())
        gifs = list(OrderedDict.fromkeys(gifs))
    return gifs

def get_song():
    t = len(song_list) - 1
    n = random.randint(0, t)
    song = song_list[n]
    return song

def final(max_gifs):
    final = {}
    final['s'] = get_song()
    final['b'] = get_background()
    final['g'] = get_gifs(max_gifs)
    return final