from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
import ArgumentParser


class mememaker:

    def __init__(self):
        self.help_message = "mememaker - Creates a meme using the template and text provided"
        self.usage_message = "Try follow : mememaker [template] [text]"
        self.name = "mememaker"
        templates = os.listdir("./Templates")
        self.templates = {i : templates[i] for i in range(len(templates))}


    def display_meme_templates(self):
        print("Meme templates available: ")
        for k, v in self.templates.items():
            print(k, ".", v)

    def parse_args(self,string):
        parser = ArgumentParser.ArgumentParser()
        opt_args = parser.add_argument_group("Optional arguments")
        opt_args.add_argument('-temp',"--template", type=int, help="The meme template to use", choices=template_choices, required=True, default=0)
        opt_args.add_argument('-text',"--text", type=str, help="The meme text", required=True, default="Meme text")
        args = parser.parse_args(string.split())
        self.template = args.temp
        self.text = args.text

    def generate_meme(self):
        # Load the image
        im = Image.open("Templates/"+self.templates[self.template])
        draw = ImageDraw.Draw(im)
        im_width, im_height = im.size
        # Load font
        use_font = "Fonts/impact.ttf"
        font = ImageFont.truetype(font=use_font, size=int(im_height/10))
        # Size of each character
        char_width, char_height = font.getsize('A')
        char_per_line = im_width // char_width
        top_lines = textwrap.wrap(top_text, char_per_line)
        # Top text
        y = 10
        for line in top_lines:
            line_width, line_height = font.getsize(line)
            x = (im_width - line_width)/2
            colour = 'black'
            draw.text((x, y), line, fill=colour, font=font)
            y += line_height
        # Open the image
        im.show()
        # Save meme
        self.save_meme(im)

    def save_meme(self, im):
        name = input("Enter meme name: ")
        # save meme
        im.save("Saved/" + name, 'PNG')
        print()

    def help_message(self):
        return self.help_message
