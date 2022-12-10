# A simple program that searches through the text of some images to find words, and analyse it.


from PIL import Image
from pytesseract import pytesseract
import os

pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
folder_dir = r"C:/tessearch/images"
images = [f"{folder_dir}/{image}" for image in os.listdir(folder_dir)]


def remove_ext(string):
    """removes the extension of the file in the filepath"""
    return string[:string.rindex(".")]


def isolate_filename(string):
    """isolates the file name taking only the last part of its path before the extension"""
    return string[string.rindex("/") + 1:string.rindex(".")]


def clean_txt(txt):
    """cleans the text from all the special characters and returns the cleaned text"""
    txt = txt.lower()
    set_text = set(txt)
    for c in set_text:
        if c not in "abcdefghijklmnopqrstuwvxyz1234567890 ":
            txt = txt.replace(c, "")
    return txt


def most_common_words(list_words, n, show_text=False):
    """returns a dictionary with words as keys and the number of occurrencies as value"""
    words_set = set(list_words)
    count = {word: list_words.count(word) for word in words_set}
    restricted_dict = {}
    while len(restricted_dict) <= n:
        highest_n = max(count, key=lambda x: count[x])
        restricted_dict[highest_n] = count[highest_n]
        del count[highest_n]
    if show_text:
        for elem in restricted_dict:
            print(f"The word {elem} is counted {restricted_dict[elem]} times.")
    return restricted_dict


def extrapolate(join=False, write=False, words=False, show_text=False):
    """if join is True it extrapolates all the text from all the images in a single text file
    otherwise it creates a text file for each image with its file name.
    if words is True it returns a list of words present in the text.
    """
    texts = {}
    for image in images:
        img = Image.open(image)
        filepath = "all_texts.txt" if join else f"{remove_ext(image)}.txt"
        textrev = pytesseract.image_to_string(img)
        text = textrev[:-1]
        texts[isolate_filename(image)] = clean_txt(text).split() if words else text
        if show_text:
            print(f"{image} contains the following text: \n {text}")
        if write:
            with open(filepath, 'a' if join else 'w') as f:
                f.write(text)
    return texts


def test():
    words_list = extrapolate(words=True)
    common = most_common_words(words_list["book1"], 5, show_text=True)
    print(common)
