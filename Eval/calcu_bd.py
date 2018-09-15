


import argparse

def main():
    parser = argparse.ArgumentParser(description='calcu bandwidth',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--Bytes', type=float, help='total Bytes')
    parser.add_argument('--fps', type=float, help='fps ')
    parser.add_argument('--frames', type=float, help='total frames')
    args = parser.parse_args()

    fps = args.fps
    frames = args.frames
    Bytes = args.Bytes
    
    bandwidth = (Bytes / frames) * fps * 8 / 1000
    print(bandwidth)

    #go_bd = (32567666. / 1581.) * fps * 8/1000
    #print "go real bd : ",go_bd,"kb/s"



if __name__ == '__main__':
    main()
