import pyexiv2
import os
import time

dirpath = r'[Input your dir path here]'
files= os.listdir(dirpath)
#print(files)
for file in files:
    if file == 'desktop.ini':
        continue
    path = dirpath + '/' + file
    exiv2img = pyexiv2.Image(path)
    date=time.strftime("%Y:%m:%d %H:%M:%S",time.localtime(os.path.getmtime(path)))
    #print(date)
    exiv2img.clear_exif()
    dict = {'Exif.Image.Model': '[Device modle]',
            'Exif.Image.DateTime': date,
            'Exif.Photo.DateTimeOriginal': date,
            'Exif.Photo.DateTimeDigitized': date,
            'Exif.Photo.OffsetTime': '+08:00',
            'Exif.Image.Make': '[Device maker]',
            'Exif.GPSInfo.GPSLatitudeRef': '[N/S]',
            'Exif.GPSInfo.GPSLatitude': '[Latitude]',
            'Exif.GPSInfo.GPSLongitudeRef': '[E/W]',
            'Exif.GPSInfo.GPSLongitude': '[Longitude]'
            }
    exiv2img.modify_exif(dict)
    #print(exiv2img.read_exif())
    exiv2img.close()
