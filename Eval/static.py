import os
import argparse

def main():

    parser = argparse.ArgumentParser(description='client and server',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--src', type=str, help='src')
    args = parser.parse_args()

    
    outlog = 'MPEG/tempReserve/time.log'
    video = 'MPEG/tempReserve/temp_video.mp4'

    os.system("ffmpeg -i {0} 2>&1 | grep \"Duration\" > {1}".format(video,outlog))

    statinfo = os.stat(video)
    size = statinfo.st_size


    with open(outlog) as f:
         for line in f:
            info = line.split(':')
            timeinfo = info[3]
            tic = timeinfo.split(',')
            ticc = float(tic[0])
            bandwidth = size/ticc * 8/1000
            print(bandwidth)

if __name__ == '__main__':
    main()

