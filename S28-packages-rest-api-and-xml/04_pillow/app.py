'''Pillow (PIL): working with images.

    pip install -r requirements.txt
'''

import os

try:
    from PIL import Image
except ModuleNotFoundError:
    raise SystemExit('Run "pip install -r requirements.txt" first.')

SOURCE = 'harry.jpg'


def main() -> None:
    if not os.path.exists(SOURCE):
        print(f'{SOURCE} is missing.')
        return

    # 1. Open an image.
    with Image.open(SOURCE) as img:
        print('Original size:', img.size)      # (width, height)
        print('Format:', img.format, '| mode:', img.mode)

        # 2. thumbnail() resizes IN PLACE and keeps the proportions.
        img.thumbnail((600, 600))
        print('Size after thumbnail:', img.size)

        # 3. Rotate; expand=True enlarges the canvas so nothing is cut off.
        img.rotate(45, expand=True).save('rotated_sample.png')

        # 4. Convert to grey ('L' = luminance).
        img.convert('L').save('bw_sample.jpg')

        # 5. Crop a rectangle: (left, top, right, bottom).
        if img.width > 400 and img.height > 400:
            img.crop((0, 0, 400, 400)).save('cropped_sample.jpg')

        # 6. resize() forces an exact size (the proportions may change).
        img.resize((200, 200)).save('square_sample.jpg')

    print('The new images were written next to the script.')


if __name__ == '__main__':
    main()
