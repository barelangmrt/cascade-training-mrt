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
dim = (200, 200)
res_frame = ""

resized_dir = os.path.join(os.getcwd(), "pos_res")

if not (os.path.exists(resized_dir)):
    os.mkdir(resized_dir)

it = 0

for file in os.listdir(args.dir):
    if file.endswith(".jpg"):
        img_path = os.path.join(args.dir, file)
        frame = cv2.imread(img_path)
        res_frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        filename = f"{it}.jpg"
        save_path = os.path.join(resized_dir, filename)
        print(save_path)
        cv2.imwrite(save_path, res_frame)
        it = it + 1

print("all images already saved to: ", resized_dir)