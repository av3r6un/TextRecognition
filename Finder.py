import cv2
from pytesseract import pytesseract


class Finder:
    def __init__(self):
        self.tess = pytesseract
        self.tess.tesseract_cmd = r'C:\Soft\Tesseract-OCR\tesseract.exe'
        self.config = r'--oem 3 --psm 6'
        self.image_path = None

    def open_image(self, image_path):
        self.image_path = image_path
        img = cv2.imread(image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return img

    def do_threshold(self, image_path: str = None):
        if self.image_path:
            ret, thresh = cv2.threshold(self.open_image(self.image_path), 170, 255, cv2.THRESH_BINARY)
            return thresh
        else:
            if image_path:
                img = cv2.imread(image_path)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                ret, thresh = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY)
                return thresh
            else:
                raise UserWarning("IMAGE PATH is defined. Please define image_path")

    @staticmethod
    def show_image(window_title: str, cv2_image):
        h, w = cv2_image.shape[0:2]
        width = 300
        height = int(width*(h/w))
        img = cv2.resize(cv2_image, (width, height))
        cv2.imshow(window_title, img)
        cv2.waitKey(0)

    def detect_data(self, image, lang: str):
        data = self.tess.image_to_data(image, config=self.config, lang=lang)
        return data

    def get_string(self, lang, image_path: str = None):
        if self.image_path:
            data = self.tess.image_to_string(self.do_threshold(), lang=lang, config=self.config)
        else:
            data = self.tess.image_to_string(self.do_threshold(image_path), lang=lang, config=self.config)
        return data

    def find_word_on_image(self, img, lang, word):
        data = self.detect_data(img, lang)
        for i, data in enumerate(data.splitlines()):
            if i == 0:
                continue

            el = data.split()
            try:
                x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
                if el[11].lower().startswith(word):
                    cv2.rectangle(img, (x - 5, y - 5), (w + x + 2, h + y + 2), (0, 0, 255), 1)
            except IndexError:
                continue


