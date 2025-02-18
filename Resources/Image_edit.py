from PIL import Image, ImageFont, ImageDraw, ImageFilter
import textwrap
# from post import query
#Preprocessing

# bg_img = Image.open('bg images/1.jpg')
# bg_img = bg_img.filter(ImageFilter.GaussianBlur(1.5))
# wd,ht = bg_img.size

# Default Values
content_font = ImageFont.truetype("/app/.fonts/DIN Condensed Bold.ttf",55)
aut_font = ImageFont.truetype("/app/.fonts/GillSans.ttc",30)
water_font = ImageFont.truetype("/app/.fonts/HelveticaNeue.ttc",20)

# draw_con = ImageDraw.Draw(bg_img)



def print_text(con_text,con_font,divisor = 3,t_wd = 25):
    """
    Prints the text on image.
    @params con_text - content
    @params con_font - font style
    returns none
    """

    current_ht,pad = ht//divisor,25
    para = textwrap.wrap(con_text, width = t_wd)
    for line in para:
        text_con_wd,text_con_ht = draw_con.textsize(line, font=con_font)
        draw_con.text(((wd - text_con_wd)/2,current_ht),line, font=con_font)
        current_ht += text_con_ht + pad
    

def watermark(con_font):
    """
    Creates watermark on images.
    @param - con_font - font size
    """
    current_ht,pad = ht//1.20,25
    para = textwrap.wrap("@QuoteInspi",width = 25)
    for line in para:
        text_con_wd,text_con_ht = draw_con.textsize(line,font=con_font)
        draw_con.text(((wd - text_con_wd)/2,current_ht),line,font=con_font,fill=(255,255,255,75))
        current_ht += text_con_ht +pad
    bg_img.save("/app/test.jpg")

#Change the save path if running locally


def image_edit(orientation,quote,author,word):
    """
    The image edit function blurs the image and calls rest functions for processing.
    @params - orientation
    @params - quote
    @params - author
    @params - word
    returns none
    """
    global bg_img
    global wd,ht 
    global draw_con 

    bg_img = Image.open('/app/bg images/'+word+'.jpg')
    bg_img = bg_img.filter(ImageFilter.GaussianBlur(1.5))
    wd,ht = bg_img.size
    draw_con = ImageDraw.Draw(bg_img)

    if orientation =="landscape":
        print_text(quote,content_font,t_wd=50)
        print_text(author,aut_font,divisor = 1.75,t_wd=50)
    else:
        print_text(quote,content_font)
        print_text(author,aut_font,divisor = 1.45)
    watermark(water_font)


# image_edit("Potrait",quote,author)
