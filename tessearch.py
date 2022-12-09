# A simple program that searches through the text of some images to find words, and analyse it.


from PIL import Image
from pytesseract import pytesseract
import os

path_to_tesseract = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract
folder_dir = r"C:/tessearch/images"
images = [f"{folder_dir}/{image}" for image in os.listdir(folder_dir)]


def remove_ext(string):
    return string[:string.rindex(".")]


def isolate_filename(string):
    return string[string.rindex("/")+1:string.rindex(".")]


def clean_txt(txt):
    """cleans the text from all the special characters and returns the cleaned text"""
    txt = txt.lower()
    set_text = set(txt)
    for c in set_text:
        if c not in "abcdefghijklmnopqrstuwvxyz1234567890 ":
            txt = txt.replace(c, "")
    return txt


def extrapolate(join=False, write=False, words=False):
    """if join is True it extrapolates all the text from all the images in a single text file
    otherwise it creates a text file for each image with its file name"""
    texts = {}
    for image in images:
        img = Image.open(image)
        filepath = "all_texts.txt" if join else f"{remove_ext(image)}.txt"
        textrev = pytesseract.image_to_string(img)
        text = textrev[:-1]
        texts[get_filename(image)] = clean_txt(text).split() if words else text
        print(f"{image} contains the following text: \n {text}")
        if write:
            with open(filepath, 'a' if join else 'w') as f:
                f.write(text)
    return texts
