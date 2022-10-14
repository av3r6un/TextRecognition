from Finder import Finder
import cv2


def main():
    f = Finder()
    f.image_path = 'test.jpg'
    my_string = f.detect_data(f.open_image('test.jpg'), 'rus')
    print(my_string)
    f.show_image('My Image', f.do_threshold())


if __name__ == '__main__':
    main()
