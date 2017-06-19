from PIL import ImageDraw


class ImageUtils:
    def __init__(self):
        pass

    @staticmethod
    def encode_img(image_path):
        print("encoding image " + image_path)
        with open(image_path, "rb") as imageFile:
            f = imageFile.read()
            b = bytearray(f)
            return b

    @staticmethod
    def draw_box(top, left, width, height, image, outline_color='blue'):
        img_width = image.size[0]
        img_height = image.size[1]

        box_top = img_height * top
        box_left = img_width * left
        box_right = box_left + (img_width * width)
        box_bottom = box_top + (img_height * height)

        draw = ImageDraw.Draw(image)
        draw.rectangle(((box_left, box_top), (box_right, box_bottom)), outline=outline_color)
        return image
