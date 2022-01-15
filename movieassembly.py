from movieplan import final
from moviepy.editor import AudioFileClip, ImageClip, VideoFileClip, TextClip, CompositeVideoClip
import time
main_directory = r'D:'
song_directory = main_directory+r'\songs\\'
background_directory = main_directory+r'\backgrounds\\'
gifs_directory = main_directory+r'\gifs\\'
w = 1920
h = 1080

def prepare_assets(max_gifs):
    movdict = final(max_gifs)
    song = movdict['s']
    bg = movdict['b']
    gifs = movdict['g']
    return song, bg, gifs

def assets_as_objects(song, bg, gifs):
    mpaudio = AudioFileClip(song_directory+song)
    song_duration = mpaudio.duration
    bg = ImageClip(background_directory+bg).set_duration(song_duration)
    bg.audio = mpaudio
    gif_list = []
    gif_names = []
    if len(gifs) == 1:
        gif_list.append(VideoFileClip(gifs_directory+gifs[0], has_mask=True).set_duration(song_duration).resize((w/8,h/8)).set_pos(('right','top')).loop(duration=song_duration))
        gif_names.append(gifs[0])
    if len(gifs) == 2:
        gif_list.append(VideoFileClip(gifs_directory+gifs[0], has_mask=True).set_duration(song_duration).resize((w/8,h/8)).set_pos(('right','top')).loop(duration=song_duration))
        gif_list.append(VideoFileClip(gifs_directory+gifs[1], has_mask=True).set_duration(song_duration).resize((w/8,h/8)).set_pos(('left','top')).loop(duration=song_duration))
        gif_names.append(gifs[0])
        gif_names.append(gifs[1])
    if len(gifs) == 3:
        gif_list.append(VideoFileClip(gifs_directory+gifs[0], has_mask=True).set_duration(song_duration).resize((w/8,h/8)).set_pos(('right','top')).loop(duration=song_duration))
        gif_list.append(VideoFileClip(gifs_directory+gifs[1], has_mask=True).set_duration(song_duration).resize((w/8,h/8)).set_pos(('right','bottom')).loop(duration=song_duration))
        gif_list.append(VideoFileClip(gifs_directory+gifs[2], has_mask=True).set_duration(song_duration).resize((w/8,h/8)).set_pos(('left','bottom')).loop(duration=song_duration))
        gif_names.append(gifs[0])
        gif_names.append(gifs[1])
        gif_names.append(gifs[2])
    asset_list = [mpaudio, bg, gif_list, song_duration]
    asset_index = [song, bg, gif_names]
    return asset_list, asset_index

def assemble_movie(assets, song_name):
    txt = TextClip(song_name, font='Amiri-regular',color='white',fontsize=24)
    border = txt.on_color(size=(txt.w+10,txt.h+10),color=(0,0,0), pos=(6,'center'), col_opacity=0.6)
    text = border.set_pos(lambda t: (max(w/30,int(w-0.5*w*t)),max(5*h/6,int(100*t))))
    if len(assets[2]) == 1:
        finalvideo = CompositeVideoClip([assets[1], assets[2][0], text])
    if len(assets[2]) == 2:
        finalvideo = CompositeVideoClip([assets[1], assets[2][0], assets[2][1], text])
    if len(assets[2]) == 3:
        finalvideo = CompositeVideoClip([assets[1], assets[2][0], assets[2][1], assets[2][2], text])
    title = str(int(time.time())) 
    print(title[-3])
    finalvideo.subclip(0, assets[3]).write_videofile(title+'.mp4', fps=24, codec='mpeg4')
    return title+'.mp4'


def create_movie(max_gifs):
    song, bg, gifs = prepare_assets(max_gifs)
    alist, aindex = assets_as_objects(song, bg, gifs)
    movie = assemble_movie(alist, aindex[0])
    return movie, alist[3]