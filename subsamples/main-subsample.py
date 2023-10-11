import subsamples as s
import argparse

parser = argparse.ArgumentParser(description='Header Added to ffmpeg using python as wrapper')
parser.add_argument('-i','--input',type=str,metavar='',help='Input image name',required=True)
parser.add_argument('-o','--output',type=str,metavar='',help='Output image name',required=True)
parser.add_argument('-t','--type',type=str,metavar='',help='type format, being 420,411,422 or 440')
args = parser.parse_args()

if __name__ == '__main__':
    if(args.input == None):
        print('No image name was informed, exiting program')
        exit(-1)
    if(args.output == None):
        print('No image output was informed, exiting program')
        exit(-1)
    if(args.type == None):
        print('No type was especified, exiting program')
        exit(-1)
    elif(args.type == 420):
        result = s.To_420(args.input)
        print('writing result...\n')
        s.cv2.imwrite(args.output,result)
    elif(args.type == 440):
        result = s.To_440(args.input)
        print('writing result...\n')
        s.cv2.imwrite(args.output,result)
    elif(args.type == 411):
        result = s.To_411(args.input)
        print('writing result...\n')
        s.cv2.imwrite(args.output,result)
    elif(args.type == 422):
        result = s.To_422(args.input)
        print('writing result...\n')
        s.cv2.imwrite(args.output,result)
    else:
        print('Type especified not found, exitign program')
        exit(-1)
                
