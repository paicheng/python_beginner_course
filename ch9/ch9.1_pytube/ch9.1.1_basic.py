from pytube import YouTube
import os

cur_dir = os.path.dirname(__file__)
os.system("cls")

# pytube use BeautifulSoup with "lxml" pharse HTML
# So, install lxml first

# pytube documentation: https://python-pytube.readthedocs.io/en/latest/index.html

# Rugby World Cup NZ vs WAL
# yt = YouTube("https://www.youtube.com/watch?v=Iqo09ice4Z0")
# 李永樂
yt = YouTube("https://www.youtube.com/watch?v=aBTDvlteZcs")
# 江南大叔
# yt = YouTube("https://www.youtube.com/watch?v=9bZkp7q19f0")
print("="*20)
# get title
print(yt.title)
print("="*20)
# get all video attributes
videos = yt.streams.all()
print("There are {} videos".format(len(videos)))
print("="*20)
for v in videos:
    print(v)
print("="*20)

# filter the videos with DASH (adaptive)
videos = yt.streams.filter(adaptive=True).all()
print("There are {} videos in DASH".format(len(videos)))
print("="*20)
for v in videos:
    print(v)
print("="*20)

# filter the videos with progressive
videos = yt.streams.filter(progressive=True).all()
print("There are {} videos in progressive".format(len(videos)))
print("="*20)
for v in videos:
    print(v)
print("="*20)

# filter audio-only videos
videos = yt.streams.filter(only_audio=True).all()
print("There are {} audio-only videos".format(len(videos)))
print("="*20)
for v in videos:
    print(v)
print("="*20)

# filter MPEG-4 videos
videos = yt.streams.filter(file_extension="mp4").all()
print("There are {} mp4 videos".format(len(videos)))
print("="*20)
for v in videos:
    print(v)
print("="*20)

# filter with more criterias
videos = yt.streams.filter(file_extension="mp4", adaptive=True).all()
print("There are {} mp4 videos with DASH".format(len(videos)))
print("="*20)
for v in videos:
    print(v)
print("="*20)

# get video by itag
video = yt.streams.get_by_itag("22")

# download video to given directory
video.download(cur_dir)

# download video to given directory and filename
video.filename = "a.mp4"
video.download(cur_dir)

# subtitle
subs = yt.captions.all()
print("There are {} subtitles".format(len(subs)))
print("="*20)
for s in subs:
    print(s)
print("="*20)

sub = yt.captions.get_by_language_code("zh-Hant")
print(sub.xml_captions)     # 字幕以XML格式呈現
print(sub.generate_srt_captions())  # 字幕以序列格式呈現


# video.download(cur_dir)


# yt.streams.first().download(cur_dir)
# yt.streams.first().download(cur_dir)
# print(yt.streams.all())
# print(type(yt.streams.first()))
