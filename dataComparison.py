import csv

views = []

def read_csv_file():
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



def higest_views():
    sorted_data = sorted(views, key=lambda i: i['view'])
    top_view = sorted_data[-1]
    second_top = sorted_data[-2]
    third_top = sorted_data[-3]
    return top_view,second_top,third_top


