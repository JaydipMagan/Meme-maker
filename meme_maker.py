from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def generate_meme(template, top_text, bottom_text):
    # Load the image
    im = Image.open("Templates/"+template)
    draw = ImageDraw.Draw(im)
    im_width, im_height = im.size

    # Load font
    font = ImageFont.truetype(font="impact.ttf", size=int(im_height/10))

    # Size of each character
    char_width, char_height = font.getsize('A')
    char_per_line = im_width // char_width

    top_lines = textwrap.wrap(top_text, char_per_line)
    bottom_lines = textwrap.wrap(bottom_text, char_per_line)

    # Top text
    y = 10
    for line in top_lines:
        line_width, line_height = font.getsize(line)
        x = (im_width - line_width)/2
        draw.text((x, y), line, fill='black', font=font)
        y += line_height

    # Bottom text
    y = im_height - char_height * len(bottom_lines) - 10
    for line in bottom_lines:
        line_width, line_height = font.getsize(line)
        x = (im_width - line_width)/2
        draw.text((x,y), line, fill='black', font=font)
        y += line_height

    # Open the image
    im.show()
    # Save meme
    save_meme()


def save_meme():
    save = input("Do you want to save the meme (y/n): ")
    if save == "y":
        name = input("Enter meme name")
    # save meme
    im.save("Saved/" + name)

def display_options():
    print()
    print("1. Top text")
    print("2. Bottom text")
    print("3. Top and Bottom text")
    print()

def get_text():
    display_options()
    option = int(input("Enter option: "))
    print()
    top_text = ""
    bottom_text = ""
    if option == 1:
        top_text = input("Enter top text: ")
    elif option == 2:
        bottom_text = input("Enter bottom text: ")
    else:
        top_text = input("Enter top text: ")
        bottom_text = input("Enter bottom text: ")
    top_text = top_text.upper()
    bottom_text = bottom_text.upper()
    return top_text, bottom_text

def get_meme_template():
    print("Meme templates available:")
    templates = os.listdir("./Templates")
    print()
    for i in range(1, len(templates)):
        name = templates[i].split(".")[0]
        print(str(i)+".", name)
    print()
    option = int(input("Enter meme template: "))
    return templates[option]

print()
print("MEME MAKER")
print()
template = get_meme_template()
top_text, bottom_text = get_text()
generate_meme(template, top_text, bottom_text)
