import os
import sys

parent_list = os.listdir("/data/movies")
i = 0
drive = sys.argv[0]
for file in parent_list:
    if i < 3000:
        os.system('rclone delete {}:phim-le/{}'.format(drive, file))
        i = i + 1
    else:
        break
