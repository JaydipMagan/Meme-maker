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

    def parse_args(self,string):
        parser = ArgumentParser.ArgumentParser()
        req_args = parser.add_argument_group("Required arguments")
        req_args.add_argument('-temp',"--template", type=int, help="The meme template to use", choices=self.templates, required=True, default=0)
        req_args.add_argument('-text',"--text", type=str, help="The meme text", required=True, default="Meme text")
        try:
            args = parser.parse_args(string.split())
        except:
            return ("error",self.usage_message)
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
