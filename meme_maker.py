from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
import ArgumentParser
class mememaker:

    def __init__(self):
        self.help_message = "mememaker - Creates a meme using the template and text provided"
        self.usage_message = "Try follow : mememaker [template] [text]"
        self.name = "mememaker"
        self.path = os.path.dirname(os.path.abspath(__file__))
        templates = os.listdir(self.path+"/Templates")
        self.templates = {i : templates[i] for i in range(len(templates))}


    def display_meme_templates(self):
        print("Meme templates available: ")
        for k, v in self.templates.items():
            print(k, ".", v)

    def split(self,string):
        args = string.split()
        text = ""
        append,index = False,0
        for i in range(0,len(args)):
            x = args[i]
            if x[0]=="'" or x[0]=='"':
                append = True
                index = i
            if append==True:
                text+= x+" "
            if x[-1]=="'" or x[-1]=='"':
                append = False
        args[index] = text
        return args[:index+1]

    def parse_args(self,string):
        parser = ArgumentParser.ArgumentParser()
        pos_args = parser.add_argument_group("Positional arguments")
        pos_args.add_argument("template", type=int, help="The meme template to use", choices=self.templates, default=0)
        pos_args.add_argument("text", type=str, help="The meme text", default="Meme text")
        try:
            args = parser.parse_args(self.split(string))
        except:
            return("error",self.usage_message)
        self.template = args.template
        self.text = args.text
        return ("image",self.generate_meme())

    def generate_meme(self):
        # Load the image
        im = Image.open(self.path+"/Templates/"+self.templates[self.template])
        draw = ImageDraw.Draw(im)
        im_width, im_height = im.size
        # Load font
        use_font = self.path+"/Fonts/impact.ttf"
        font = ImageFont.truetype(font=use_font, size=int(im_height/10))
        # Size of each character
        char_width, char_height = font.getsize('A')
        char_width -= len(self.text)//3
        char_height -= len(self.text)//3
        char_per_line = im_width // char_width
        top_lines = textwrap.wrap(self.text, char_per_line)
        # Top text
        y = 10
        for line in top_lines:
            line_width, line_height = font.getsize(line)
            x = (im_width - line_width)/2
            colour = 'black'
            draw.text((x, y), line, fill=colour, font=font)
            y += line_height
        # Open the image
        # im.show()
        # Save meme
        return self.save_meme_(im,"meme.png")

    def save_meme_(self,im,name):
        if not os.path.exists(self.path+"/Saved"):
            os.makedirs(self.path+"/Saved")
        # save meme
        im.save(self.path+"/Saved/" + name, 'PNG')
        return self.path+"/Saved/"+name

    def save_meme(self, im):
        name = input("Enter meme name: ")
        # save meme
        im.save(self.path+"/Saved/" + name, 'PNG')
        print()

    def help_message(self):
        return self.help_message
