# import the opencv library
from tkinter import filedialog
import os
import argparse

#argument(s) parser
parser = argparse.ArgumentParser()

parser.add_argument('--dir', '-d', required=True, type=str)
args = parser.parse_args()

img_path = ""

neg_dir = os.path.join(os.getcwd(), args.dir)

if not (os.path.exists(neg_dir)):
    os.mkdir(neg_dir)

file_dir = os.path.join(os.getcwd(), "neg.txt")
f = open(file_dir, "w")

for file in os.listdir(args.dir):
    if file.endswith(".jpg"):
        img_path = os.path.join(args.dir, file)
        line = f"{img_path} \n"
        f.write(line)

f.close()
print ("file saved to:", file_dir)