import os
from PIL import Image
import configparser
import time

config = configparser.ConfigParser()
config.read('denta_config.ini')

in_directory = config['ImageConverter']['ImageDirectory']
out_directory = config['ImageConverter']['OutputDirectory']
quality = int(config['ImageConverter']['JpegQuality'])
update_interval = int(config['ImageConverter']['UpdateInterval'])

while True:
    # with os.scandir(path) as files:
    #     for file in it:
    #         if not entry.name.startswith('.') and entry.is_file():
    for dir_path, dirs, files in os.walk(in_directory):
        path = dir_path.split(os.sep)
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            # -2 is filename before extension
            basename = os.path.splitext(file)[-2]

            # basename[-1] is last symbol of filename (meaning thumbnails)
            if ext == ".bmp" and basename[-1] != 't':
                file_path = os.path.join(dir_path, file)
                # print('found file:', file_path)
                try:
                    img = Image.open(file_path)
                except Exception:
                    pass

                out_file_path = out_directory + os.sep + basename + '.jpg'
                if os.path.isfile(out_file_path):
                    pass  # print('exists, skipping')
                else:
                    try:
                        img.save(out_directory + os.sep + basename + '.jpg', quality=quality)
                    except Exception:
                        pass
    time.sleep(update_interval)
