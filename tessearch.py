# A simple program that searches through the text of some images to find words, and analyse it.


from PIL import Image
from pytesseract import pytesseract
import os

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract
folder_dir = r"C:\tessearch\images"
images = [f"{folder_dir}/{image}" for image in os.listdir(folder_dir)]


def make_files(join=False):
    texts, c = [], 1
    if join:
        filepath = "texts.txt"
    for image in images:
        if not join:
            filepath = f"{str(c)}.txt"
        img = Image.open(image)
        textrev = pytesseract.image_to_string(img)
        text = textrev[:-1]
        texts.append(text)
        print(f"{image} contains the following text: \n {text}")
        with open(filepath, 'a' if join else 'w') as f:
            f.write(text)
        c += 1
