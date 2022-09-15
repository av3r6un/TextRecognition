import cv2
from pytesseract import pytesseract

pytesseract.tesseract_cmd = r'C:\Soft\Tesseract-OCR\tesseract.exe'
config = r'--oem 3 --psm 6'


def detect():
    img = cv2.imread('test.jpg')
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ret, thresh = cv2.threshold(img_gray, 170, 255, cv2.THRESH_BINARY)
    cv2.imshow('None approximation', thresh)
    cv2.waitKey(0)


def find_character(character):
    img = cv2.imread('table.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    config = r'--oem 3 --psm 6'
    # print(pytesseract.image_to_data(img, config=config, lang='rus'))
    data = pytesseract.image_to_data(img, config=config, lang='rus')
    for i, data in enumerate(data.splitlines()):
        if i == 0:
            continue

        el = data.split()
        try:
            x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
            if el[11].lower().startswith(character):
                cv2.rectangle(img, (x-5, y-5), (w+x+2, h+y+2), (0, 0, 255), 1)
        except IndexError:
            continue

    cv2.imshow('Result', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    detect()
