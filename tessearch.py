# A simple program that searches through the text of some images to find words, and analyse it.


from PIL import Image
from pytesseract import pytesseract
import os

path_to_tesseract = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract
folder_dir = r"C:/tessearch/images"
images = [f"{folder_dir}/{image}" for image in os.listdir(folder_dir)]


def make_files(join=False):
    """if join is True it extrapolates all the text from all the images in a single text file
    otherwise it creates a text file for each image with its file name"""
    texts = []
    for image in images:
        img = Image.open(image)
        # if file extension has more than 3 character the output will be unexpected.
        filepath = "all_texts.txt" if join else f"{image[:-4]}.txt"
        textrev = pytesseract.image_to_string(img)
        text = textrev[:-1]
        texts.append(text)
        print(f"{image} contains the following text: \n {text}")
        with open(filepath, 'a' if join else 'w') as f:
            f.write(text)


make_files()
