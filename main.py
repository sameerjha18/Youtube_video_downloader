from pytube import YouTube
import csv
from dataComparison import higest_views, read_csv_file

urls = ["https://www.youtube.com/watch?v=kZC12U6EhTc","https://www.youtube.com/watch?v=hGDJkqESz0k","https://www.youtube.com/watch?v=1-Iu__4R_b0&t=517s",
        "https://www.youtube.com/watch?v=1-Iu__4R_b0&t=517s","https://www.youtube.com/watch?v=vX-QPzNppGY","https://www.youtube.com/watch?v=RZsFHyKxir4","https://www.youtube.com/watch?v=tgOLVIiI8WY"]

detail_of_videos = []

def youtubeVideoData():
    try:
        for link in urls:
            yt = YouTube(link)

            detail_of_video = {
                "Title:": yt.title,
                "view": yt.views,
            }
            detail_of_videos.append(detail_of_video)
    except Exception as e:
        print("OOPS!!! We get an error here." + str(e))

def youtubeVideoDownload():
    try:
        for link in urls:
            yt = YouTube(link, 
                         use_oauth=True, 
                         allow_oauth_cache=True)

            yd = yt.streams.get_highest_resolution()

            yd.download()

            print("Download Completed")
    except Exception as e:

        print("OOPS!!! We get an error here." + str(e))

if __name__ == '__main__':
    youtubeVideoData()
    keys = detail_of_videos[0].keys()
    with open('youtubeData.csv', 'w', newline="") as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(detail_of_videos)
    read_csv_file()
    print(higest_views())

    # youtubeVideoDownload()