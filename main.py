from pytube import YouTube
import csv

urls = ["https://www.youtube.com/watch?v=aJHERLcrPvw","https://www.youtube.com/watch?v=aJHERLcrPvw"]

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
    # youtubeVideoData()
    # keys = detail_of_videos[0].keys()
    # with open('youtubeData.csv', 'w', newline="") as file:
    #     dict_writer = csv.DictWriter(file, keys)
    #     dict_writer.writeheader()
    #     dict_writer.writerows(detail_of_videos)
    youtubeVideoDownload()