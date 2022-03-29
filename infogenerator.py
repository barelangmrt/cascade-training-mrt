# import the opencv library
from tkinter import filedialog
import cv2
import os
import argparse

#argument(s) parser
parser = argparse.ArgumentParser()

parser.add_argument('--dir', '-d', required=True, type=str)
args = parser.parse_args()

img_path = ""

annot_dir = os.getcwd()

if not (os.path.exists(annot_dir)):
    os.mkdir(annot_dir)
    
file_dir = os.path.join(annot_dir, "info.dat")
f = open(file_dir, "w")

for file in os.listdir(args.dir):
    if file.endswith(".jpg"):
        img_path = os.path.join(args.dir, file)
        frame = cv2.imread(img_path)
        line = f"{img_path} 1 0 0 {frame.shape[0]-1} {frame.shape[1]-1}\n"
        f.write(line)

f.close()
print ("file saved to:", file_dir)
