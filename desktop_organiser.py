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
            if filename != 'UserName':
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
    'noname' : "%path-to-desktop%/Desktop/UserName/Other/Uncategorized",
#Audio
    '.aif' : "%path-to-desktop%/Desktop/UserName/Media/Audio",
    '.cda' : "%path-to-desktop%/Desktop/UserName/Media/Audio",
    '.mid' : "%path-to-desktop%/Desktop/UserName/Media/Audio",
    '.midi' : "%path-to-desktop%/Desktop/UserName/Media/Audio",
    '.mp3' : "%path-to-desktop%/Desktop/UserName/Media/Audio",
    '.mpa' : "%path-to-desktop%/Desktop/UserName/Media/Audio",
    '.ogg' : "%path-to-desktop%/Desktop/UserName/Media/Audio",
    '.wav' : "%path-to-desktop%/Desktop/UserName/Media/Audio",
    '.wma' : "%path-to-desktop%/Desktop/UserName/Media/Audio",
    '.wpl' : "%path-to-desktop%/Desktop/UserName/Media/Audio",
    '.m3u' : "%path-to-desktop%/Desktop/UserName/Media/Audio",
#Text
    '.txt' : "%path-to-desktop%/Desktop/UserName/Text/TextFiles",
    '.doc' : "%path-to-desktop%/Desktop/UserName/Text/Document/Microsoft",
    '.docx' : "%path-to-desktop%/Desktop/UserName/Text/Document/Microsoft",
    '.odt ' : "%path-to-desktop%/Desktop/UserName/Text/Document",
    '.pdf': "%path-to-desktop%/Desktop/UserName/Text/Document/PDF",
    '.rtf': "%path-to-desktop%/Desktop/UserName/Text/Document",
    '.tex': "%path-to-desktop%/Desktop/UserName/Text/TextFiles",
    '.wks ': "%path-to-desktop%/Desktop/UserName/Text/TextFiles",
    '.wps': "%path-to-desktop%/Desktop/UserName/Text/Document",
    '.wpd': "%path-to-desktop%/Desktop/UserName/Text/Document",
#Video
    '.3g2': "%path-to-desktop%/Desktop/UserName/Media/Video",
    '.3gp': "%path-to-desktop%/Desktop/UserName/Media/Video",
    '.avi': "%path-to-desktop%/Desktop/UserName/Media/Video",
    '.flv': "%path-to-desktop%/Desktop/UserName/Media/Video",
    '.h264': "%path-to-desktop%/Desktop/UserName/Media/Video",
    '.m4v': "%path-to-desktop%/Desktop/UserName/Media/Video",
    '.mkv': "%path-to-desktop%/Desktop/UserName/Media/Video",
    '.mov': "%path-to-desktop%/Desktop/UserName/Media/Video",
    '.mp4': "%path-to-desktop%/Desktop/UserName/Media/Video",
    '.mpg': "%path-to-desktop%/Desktop/UserName/Media/Video",
    '.mpeg': "%path-to-desktop%/Desktop/UserName/Media/Video",
    '.rm': "%path-to-desktop%/Desktop/UserName/Media/Video",
    '.swf': "%path-to-desktop%/Desktop/UserName/Media/Video",
    '.vob': "%path-to-desktop%/Desktop/UserName/Media/Video",
    '.wmv': "%path-to-desktop%/Desktop/UserName/Media/Video",
#Images
    '.ai': "%path-to-desktop%/Desktop/UserName/Media/Images",
    '.bmp': "%path-to-desktop%/Desktop/UserName/Media/Images",
    '.gif': "%path-to-desktop%/Desktop/UserName/Media/Images",
    '.ico': "%path-to-desktop%/Desktop/UserName/Media/Images",
    '.jpg': "%path-to-desktop%/Desktop/UserName/Media/Images",
    '.jpeg': "%path-to-desktop%/Desktop/UserName/Media/Images",
    '.png': "%path-to-desktop%/Desktop/UserName/Media/Images",
    '.ps': "%path-to-desktop%/Desktop/UserName/Media/Images",
    '.psd': "%path-to-desktop%/Desktop/UserName/Media/Images",
    '.svg': "%path-to-desktop%/Desktop/UserName/Media/Images",
    '.tif': "%path-to-desktop%/Desktop/UserName/Media/Images",
    '.tiff': "%path-to-desktop%/Desktop/UserName/Media/Images",
    '.CR2': "%path-to-desktop%/Desktop/UserName/Media/Images",
#Internet
    '.asp': "%path-to-desktop%/Desktop/UserName/Other/Internet",
    '.aspx': "%path-to-desktop%/Desktop/UserName/Other/Internet",
    '.cer': "%path-to-desktop%/Desktop/UserName/Other/Internet",
    '.cfm': "%path-to-desktop%/Desktop/UserName/Other/Internet",
    '.cgi': "%path-to-desktop%/Desktop/UserName/Other/Internet",
    '.pl': "%path-to-desktop%/Desktop/UserName/Other/Internet",
    '.jsp': "%path-to-desktop%/Desktop/UserName/Other/Internet",
    '.part': "%path-to-desktop%/Desktop/UserName/Other/Internet",
    '.php': "%path-to-desktop%/Desktop/UserName/Other/Internet",
    '.rss': "%path-to-desktop%/Desktop/UserName/Other/Internet",
    '.xhtml': "%path-to-desktop%/Desktop/UserName/Other/Internet",
#Compressed
    '.7z': "%path-to-desktop%/Desktop/UserName/Other/Compressed",
    '.arj': "%path-to-desktop%/Desktop/UserName/Other/Compressed",
    '.deb': "%path-to-desktop%/Desktop/UserName/Other/Compressed",
    '.pkg': "%path-to-desktop%/Desktop/UserName/Other/Compressed",
    '.rar': "%path-to-desktop%/Desktop/UserName/Other/Compressed",
    '.rpm': "%path-to-desktop%/Desktop/UserName/Other/Compressed",
    '.tar.gz': "%path-to-desktop%/Desktop/UserName/Other/Compressed",
    '.z': "%path-to-desktop%/Desktop/UserName/Other/Compressed",
    '.zip': "%path-to-desktop%/Desktop/UserName/Other/Compressed",
#Disc
    '.bin': "%path-to-desktop%/Desktop/UserName/Other/Disc",
    '.dmg': "%path-to-desktop%/Desktop/UserName/Other/Disc",
    '.iso': "%path-to-desktop%/Desktop/UserName/Other/Disc",
    '.toast': "%path-to-desktop%/Desktop/UserName/Other/Disc",
    '.vcd': "%path-to-desktop%/Desktop/UserName/Other/Disc",
#Data
    '.csv': "%path-to-desktop%/Desktop/UserName/Programming/Database",
    '.dat': "%path-to-desktop%/Desktop/UserName/Programming/Database",
    '.db': "%path-to-desktop%/Desktop/UserName/Programming/Database",
    '.dbf': "%path-to-desktop%/Desktop/UserName/Programming/Database",
    '.log': "%path-to-desktop%/Desktop/UserName/Programming/Database",
    '.mdb': "%path-to-desktop%/Desktop/UserName/Programming/Database", 
    '.sav': "%path-to-desktop%/Desktop/UserName/Programming/Database",
    '.sql': "%path-to-desktop%/Desktop/UserName/Programming/Database",
    '.tar': "%path-to-desktop%/Desktop/UserName/Programming/Database",
    '.xml': "%path-to-desktop%/Desktop/UserName/Programming/Database",
    '.json': "%path-to-desktop%/Desktop/UserName/Programming/Database",
#Executables
    '.apk': "%path-to-desktop%/Desktop/UserName/Other/Executables",
    '.bat': "%path-to-desktop%/Desktop/UserName/Other/Executables",
    '.com': "%path-to-desktop%/Desktop/UserName/Other/Executables",
    '.exe': "%path-to-desktop%/Desktop/UserName/Other/Executables",
    '.gadget': "%path-to-desktop%/Desktop/UserName/Other/Executables",
    '.jar': "%path-to-desktop%/Desktop/UserName/Other/Executables",
    '.wsf': "%path-to-desktop%/Desktop/UserName/Other/Executables",
#Fonts
    '.fnt': "%path-to-desktop%/Desktop/UserName/Other/Fonts",
    '.fon': "%path-to-desktop%/Desktop/UserName/Other/Fonts",
    '.otf': "%path-to-desktop%/Desktop/UserName/Other/Fonts",
    '.ttf': "%path-to-desktop%/Desktop/UserName/Other/Fonts",
#Presentations
    '.key': "%path-to-desktop%/Desktop/UserName/Text/Presentation",
    '.odp': "%path-to-desktop%/Desktop/UserName/Text/Presentation",
    '.pps': "%path-to-desktop%/Desktop/UserName/Text/Presentation/Microsoft",
    '.pptx': "%path-to-desktop%/Desktop/UserName/Text/Presentation/Microsoft",
    '.ppt': "%path-to-desktop%/Desktop/UserName/Text/Presentation/Microsoft",
#Programming
    '.c': "%path-to-desktop%/Desktop/UserName/Programming/C&C++",
    '.cpp': "%path-to-desktop%/Desktop/UserName/Programming/C&C++",
    '.class': "%path-to-desktop%/Desktop/UserName/Programming/Java",
    '.dart': "%path-to-desktop%/Desktop/UserName/Programming/Dart",
    '.py': "%path-to-desktop%/Desktop/UserName/Programming/Python",
    '.sh': "%path-to-desktop%/Desktop/UserName/Programming/Shell",
    '.swift': "%path-to-desktop%/Desktop/UserName/Programming/Swift",
    '.html': "%path-to-desktop%/Desktop/UserName/Programming/HTML",
    '.h': "%path-to-desktop%/Desktop/UserName/Programming/C&C++",
    '.css': "%path-to-desktop%/Desktop/UserName/Programming/CSS",
    '.htm': "%path-to-desktop%/Desktop/UserName/Programming/HTML",
    '.js': "%path-to-desktop%/Desktop/UserName/Programming/JavaScript",
#Spreadsheets
    '.ods' : "%path-to-desktop%/Desktop/UserName/Text/Spreadsheet",
    '.xlr' : "%path-to-desktop%/Desktop/UserName/Text/Spreadsheet/Microsoft",
    '.xls' : "%path-to-desktop%/Desktop/UserName/Text/Spreadsheet/Microsoft",
    '.xlsx' : "%path-to-desktop%/Desktop/UserName/Text/Spreadsheet/Microsoft",
#System
    '.bak' : "%path-to-desktop%/Desktop/UserName/Text/Other/System",
    '.cab' : "%path-to-desktop%/Desktop/UserName/Text/Other/System",
    '.cfg' : "%path-to-desktop%/Desktop/UserName/Text/Other/System",
    '.cpl' : "%path-to-desktop%/Desktop/UserName/Text/Other/System",
    '.cur' : "%path-to-desktop%/Desktop/UserName/Text/Other/System",
    '.dll' : "%path-to-desktop%/Desktop/UserName/Text/Other/System",
    '.dmp' : "%path-to-desktop%/Desktop/UserName/Text/Other/System",
    '.drv' : "%path-to-desktop%/Desktop/UserName/Text/Other/System",
    '.icns' : "%path-to-desktop%/Desktop/UserName/Text/Other/System",
    '.ico' : "%path-to-desktop%/Desktop/UserName/Text/Other/System",
    '.ini' : "%path-to-desktop%/Desktop/UserName/Text/Other/System",
    '.lnk' : "%path-to-desktop%/Desktop/UserName/Text/Other/System",
    '.msi' : "%path-to-desktop%/Desktop/UserName/Text/Other/System",
    '.sys' : "%path-to-desktop%/Desktop/UserName/Text/Other/System",
    '.tmp' : "%path-to-desktop%/Desktop/UserName/Text/Other/System",
}

folder_to_track = '%path-to-desktop%/Desktop'
folder_destination = '%path-to-desktop%/Desktop/UserName'
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
