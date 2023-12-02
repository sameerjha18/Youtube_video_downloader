import csv

def read_csv_file():
    views = []
    with open("youtubeData.csv", "r",) as file:
        data = csv.reader(file)
        header = next(data)
        for x in data:
            # views.append(x[1])
            # name.append(x[0])
            globals 
            videoData = {
                "name": x[0],
                "view": x[1],
            }
            views.append(videoData)
    return views



def higest_views(views, n):
    sorted_data = sorted(views, key=lambda i: i['view'], reverse= True)
    topView = sorted_data[:n]
    return topView



