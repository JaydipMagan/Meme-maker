from PIL import Image, ImageDraw, ImageFont
import textwrap

# Load the image
im = Image.open("man_of_quality.png")
draw = ImageDraw.Draw(im)
im_width, im_height = im.size

# Load font
font = ImageFont.truetype(font="impact.ttf", size=int(im_height/10))

# Wrap text so that it doesn't overflow from the image and goes to new line instead
top_text = "When you make a meme using Python"
top_text = top_text.upper()
bottom_text = ""
bottom_text = bottom_text.upper()

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

# save meme
im.save('meme-' + im.filename.split('/')[-1])

im.show()
