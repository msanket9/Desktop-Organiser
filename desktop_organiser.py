from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
import json
import shutil
from datetime import datetime
from time import gmtime, strftime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'Hrishikesh':
                # try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'

                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")

                    folder_destination_path = extensions_folders[extension]
                    
                    year_exists = False
                    month_exists = False
                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == year:
                            folder_destination_path = extensions_folders[extension] + "/" +year
                            year_exists = True
                            for folder_month in os.listdir(folder_destination_path):
                                if month == folder_month:
                                    folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                    month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "/" + year)
                        folder_destination_path = extensions_folders[extension] + "/" + year
                    if not month_exists:
                        os.mkdir(folder_destination_path + "/" + month)
                        folder_destination_path = folder_destination_path + "/" + month


                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    src = folder_to_track + "/" + filename

                    new_name = folder_destination_path + "/" + new_name
                    os.rename(src, new_name)
                # except Exception:
                #     print(filename)

extensions_folders = {
#No name
    'noname' : "/home/hrishikesh/Desktop/Hrishikesh/Other/Uncategorized",
#Audio
    '.aif' : "/home/hrishikesh/Desktop/Hrishikesh/Media/Audio",
    '.cda' : "/home/hrishikesh/Desktop/Hrishikesh/Media/Audio",
    '.mid' : "/home/hrishikesh/Desktop/Hrishikesh/Media/Audio",
    '.midi' : "/home/hrishikesh/Desktop/Hrishikesh/Media/Audio",
    '.mp3' : "/home/hrishikesh/Desktop/Hrishikesh/Media/Audio",
    '.mpa' : "/home/hrishikesh/Desktop/Hrishikesh/Media/Audio",
    '.ogg' : "/home/hrishikesh/Desktop/Hrishikesh/Media/Audio",
    '.wav' : "/home/hrishikesh/Desktop/Hrishikesh/Media/Audio",
    '.wma' : "/home/hrishikesh/Desktop/Hrishikesh/Media/Audio",
    '.wpl' : "/home/hrishikesh/Desktop/Hrishikesh/Media/Audio",
    '.m3u' : "/home/hrishikesh/Desktop/Hrishikesh/Media/Audio",
#Text
    '.txt' : "/home/hrishikesh/Desktop/Hrishikesh/Text/TextFiles",
    '.doc' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Document/Microsoft",
    '.docx' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Document/Microsoft",
    '.odt ' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Document",
    '.pdf': "/home/hrishikesh/Desktop/Hrishikesh/Text/Document/PDF",
    '.rtf': "/home/hrishikesh/Desktop/Hrishikesh/Text/Document",
    '.tex': "/home/hrishikesh/Desktop/Hrishikesh/Text/TextFiles",
    '.wks ': "/home/hrishikesh/Desktop/Hrishikesh/Text/TextFiles",
    '.wps': "/home/hrishikesh/Desktop/Hrishikesh/Text/Document",
    '.wpd': "/home/hrishikesh/Desktop/Hrishikesh/Text/Document",
#Video
    '.3g2': "/home/hrishikesh/Desktop/Hrishikesh/Media/Video",
    '.3gp': "/home/hrishikesh/Desktop/Hrishikesh/Media/Video",
    '.avi': "/home/hrishikesh/Desktop/Hrishikesh/Media/Video",
    '.flv': "/home/hrishikesh/Desktop/Hrishikesh/Media/Video",
    '.h264': "/home/hrishikesh/Desktop/Hrishikesh/Media/Video",
    '.m4v': "/home/hrishikesh/Desktop/Hrishikesh/Media/Video",
    '.mkv': "/home/hrishikesh/Desktop/Hrishikesh/Media/Video",
    '.mov': "/home/hrishikesh/Desktop/Hrishikesh/Media/Video",
    '.mp4': "/home/hrishikesh/Desktop/Hrishikesh/Media/Video",
    '.mpg': "/home/hrishikesh/Desktop/Hrishikesh/Media/Video",
    '.mpeg': "/home/hrishikesh/Desktop/Hrishikesh/Media/Video",
    '.rm': "/home/hrishikesh/Desktop/Hrishikesh/Media/Video",
    '.swf': "/home/hrishikesh/Desktop/Hrishikesh/Media/Video",
    '.vob': "/home/hrishikesh/Desktop/Hrishikesh/Media/Video",
    '.wmv': "/home/hrishikesh/Desktop/Hrishikesh/Media/Video",
#Images
    '.ai': "/home/hrishikesh/Desktop/Hrishikesh/Media/Images",
    '.bmp': "/home/hrishikesh/Desktop/Hrishikesh/Media/Images",
    '.gif': "/home/hrishikesh/Desktop/Hrishikesh/Media/Images",
    '.ico': "/home/hrishikesh/Desktop/Hrishikesh/Media/Images",
    '.jpg': "/home/hrishikesh/Desktop/Hrishikesh/Media/Images",
    '.jpeg': "/home/hrishikesh/Desktop/Hrishikesh/Media/Images",
    '.png': "/home/hrishikesh/Desktop/Hrishikesh/Media/Images",
    '.ps': "/home/hrishikesh/Desktop/Hrishikesh/Media/Images",
    '.psd': "/home/hrishikesh/Desktop/Hrishikesh/Media/Images",
    '.svg': "/home/hrishikesh/Desktop/Hrishikesh/Media/Images",
    '.tif': "/home/hrishikesh/Desktop/Hrishikesh/Media/Images",
    '.tiff': "/home/hrishikesh/Desktop/Hrishikesh/Media/Images",
    '.CR2': "/home/hrishikesh/Desktop/Hrishikesh/Media/Images",
#Internet
    '.asp': "/home/hrishikesh/Desktop/Hrishikesh/Other/Internet",
    '.aspx': "/home/hrishikesh/Desktop/Hrishikesh/Other/Internet",
    '.cer': "/home/hrishikesh/Desktop/Hrishikesh/Other/Internet",
    '.cfm': "/home/hrishikesh/Desktop/Hrishikesh/Other/Internet",
    '.cgi': "/home/hrishikesh/Desktop/Hrishikesh/Other/Internet",
    '.pl': "/home/hrishikesh/Desktop/Hrishikesh/Other/Internet",
    '.jsp': "/home/hrishikesh/Desktop/Hrishikesh/Other/Internet",
    '.part': "/home/hrishikesh/Desktop/Hrishikesh/Other/Internet",
    '.php': "/home/hrishikesh/Desktop/Hrishikesh/Other/Internet",
    '.rss': "/home/hrishikesh/Desktop/Hrishikesh/Other/Internet",
    '.xhtml': "/home/hrishikesh/Desktop/Hrishikesh/Other/Internet",
#Compressed
    '.7z': "/home/hrishikesh/Desktop/Hrishikesh/Other/Compressed",
    '.arj': "/home/hrishikesh/Desktop/Hrishikesh/Other/Compressed",
    '.deb': "/home/hrishikesh/Desktop/Hrishikesh/Other/Compressed",
    '.pkg': "/home/hrishikesh/Desktop/Hrishikesh/Other/Compressed",
    '.rar': "/home/hrishikesh/Desktop/Hrishikesh/Other/Compressed",
    '.rpm': "/home/hrishikesh/Desktop/Hrishikesh/Other/Compressed",
    '.tar.gz': "/home/hrishikesh/Desktop/Hrishikesh/Other/Compressed",
    '.z': "/home/hrishikesh/Desktop/Hrishikesh/Other/Compressed",
    '.zip': "/home/hrishikesh/Desktop/Hrishikesh/Other/Compressed",
#Disc
    '.bin': "/home/hrishikesh/Desktop/Hrishikesh/Other/Disc",
    '.dmg': "/home/hrishikesh/Desktop/Hrishikesh/Other/Disc",
    '.iso': "/home/hrishikesh/Desktop/Hrishikesh/Other/Disc",
    '.toast': "/home/hrishikesh/Desktop/Hrishikesh/Other/Disc",
    '.vcd': "/home/hrishikesh/Desktop/Hrishikesh/Other/Disc",
#Data
    '.csv': "/home/hrishikesh/Desktop/Hrishikesh/Programming/Database",
    '.dat': "/home/hrishikesh/Desktop/Hrishikesh/Programming/Database",
    '.db': "/home/hrishikesh/Desktop/Hrishikesh/Programming/Database",
    '.dbf': "/home/hrishikesh/Desktop/Hrishikesh/Programming/Database",
    '.log': "/home/hrishikesh/Desktop/Hrishikesh/Programming/Database",
    '.mdb': "/home/hrishikesh/Desktop/Hrishikesh/Programming/Database", 
    '.sav': "/home/hrishikesh/Desktop/Hrishikesh/Programming/Database",
    '.sql': "/home/hrishikesh/Desktop/Hrishikesh/Programming/Database",
    '.tar': "/home/hrishikesh/Desktop/Hrishikesh/Programming/Database",
    '.xml': "/home/hrishikesh/Desktop/Hrishikesh/Programming/Database",
    '.json': "/home/hrishikesh/Desktop/Hrishikesh/Programming/Database",
#Executables
    '.apk': "/home/hrishikesh/Desktop/Hrishikesh/Other/Executables",
    '.bat': "/home/hrishikesh/Desktop/Hrishikesh/Other/Executables",
    '.com': "/home/hrishikesh/Desktop/Hrishikesh/Other/Executables",
    '.exe': "/home/hrishikesh/Desktop/Hrishikesh/Other/Executables",
    '.gadget': "/home/hrishikesh/Desktop/Hrishikesh/Other/Executables",
    '.jar': "/home/hrishikesh/Desktop/Hrishikesh/Other/Executables",
    '.wsf': "/home/hrishikesh/Desktop/Hrishikesh/Other/Executables",
#Fonts
    '.fnt': "/home/hrishikesh/Desktop/Hrishikesh/Other/Fonts",
    '.fon': "/home/hrishikesh/Desktop/Hrishikesh/Other/Fonts",
    '.otf': "/home/hrishikesh/Desktop/Hrishikesh/Other/Fonts",
    '.ttf': "/home/hrishikesh/Desktop/Hrishikesh/Other/Fonts",
#Presentations
    '.key': "/home/hrishikesh/Desktop/Hrishikesh/Text/Presentation",
    '.odp': "/home/hrishikesh/Desktop/Hrishikesh/Text/Presentation",
    '.pps': "/home/hrishikesh/Desktop/Hrishikesh/Text/Presentation/Microsoft",
    '.pptx': "/home/hrishikesh/Desktop/Hrishikesh/Text/Presentation/Microsoft",
    '.ppt': "/home/hrishikesh/Desktop/Hrishikesh/Text/Presentation/Microsoft",
#Programming
    '.c': "/home/hrishikesh/Desktop/Hrishikesh/Programming/C&C++",
    '.cpp': "/home/hrishikesh/Desktop/Hrishikesh/Programming/C&C++",
    '.class': "/home/hrishikesh/Desktop/Hrishikesh/Programming/Java",
    '.dart': "/home/hrishikesh/Desktop/Hrishikesh/Programming/Dart",
    '.py': "/home/hrishikesh/Desktop/Hrishikesh/Programming/Python",
    '.sh': "/home/hrishikesh/Desktop/Hrishikesh/Programming/Shell",
    '.swift': "/home/hrishikesh/Desktop/Hrishikesh/Programming/Swift",
    '.html': "/home/hrishikesh/Desktop/Hrishikesh/Programming/HTML",
    '.h': "/home/hrishikesh/Desktop/Hrishikesh/Programming/C&C++",
    '.css': "/home/hrishikesh/Desktop/Hrishikesh/Programming/CSS",
    '.htm': "/home/hrishikesh/Desktop/Hrishikesh/Programming/HTML",
    '.js': "/home/hrishikesh/Desktop/Hrishikesh/Programming/JavaScript",
#Spreadsheets
    '.ods' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Spreadsheet",
    '.xlr' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Spreadsheet/Microsoft",
    '.xls' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Spreadsheet/Microsoft",
    '.xlsx' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Spreadsheet/Microsoft",
#System
    '.bak' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Other/System",
    '.cab' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Other/System",
    '.cfg' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Other/System",
    '.cpl' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Other/System",
    '.cur' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Other/System",
    '.dll' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Other/System",
    '.dmp' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Other/System",
    '.drv' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Other/System",
    '.icns' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Other/System",
    '.ico' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Other/System",
    '.ini' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Other/System",
    '.lnk' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Other/System",
    '.msi' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Other/System",
    '.sys' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Other/System",
    '.tmp' : "/home/hrishikesh/Desktop/Hrishikesh/Text/Other/System",
}

folder_to_track = '/home/hrishikesh/Desktop'
folder_destination = '/home/hrishikesh/Desktop/Hrishikesh'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:           
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
