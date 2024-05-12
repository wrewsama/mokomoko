import PIL
import PIL.ImageDraw
import PIL.ImageFont 
import sys

def get_pixels(char):
    img = PIL.Image.new(mode='1', size=(100, 100), color='white')

    drawer = PIL.ImageDraw.Draw(img) 
    font = PIL.ImageFont.truetype("fonts-japanese-mincho.ttf", 50)

    _, _, w, h = drawer.textbbox((0, 0), char, font=font)
    drawer.text(((100-w) // 2, (100-h) // 2), char, font=font)

    return img.getdata()

def main():
    if len(sys.argv) != 3:
        print("wrong number of args supplied!")

    char1, char2 = sys.argv[1], sys.argv[2]
    pixels1 = get_pixels(char1)
    pixels2 = get_pixels(char2)

    matchCnt = 0
    totalCnt = 0
    for p1, p2 in zip(pixels1, pixels2):
        if p1 == 255 and p2 == 255:
            continue # ignore shared blank space
        if p1 == p2:
            matchCnt += 1
        totalCnt += 1

    print(f'similarity = {matchCnt / totalCnt}')

if __name__ == "__main__":
    main()