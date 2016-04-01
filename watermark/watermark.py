#coding=utf8
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import glob, os, sys
 
def add_watermark( text, fontname, fontsize, position, angle, opacity, imagefile, output_dir):
    img = Image.open(imagefile).convert('RGBA')
    # PIL.Image.new(mode, size, color=0)  color Default is black
    watermark = Image.new('RGBA', img.size)
    n_font = ImageFont.truetype(fontname, fontsize)
    n_width, n_height = n_font.getsize(text.decode(sys.getfilesystemencoding()))  
    draw = ImageDraw.Draw(watermark, 'RGBA')
    x_posinon = watermark.size[0] - n_width  # (x,0)
    y_posinon = watermark.size[1] - n_height # (0,y)
    if (position == "UL"):  #左上 upper left (UL)
        draw.text((0,0),text.decode(sys.getfilesystemencoding()), font=n_font)         
    if (position == "CL"):  #左中 center left (CL)   
        draw.text((0, y_posinon / 2), text.decode(sys.getfilesystemencoding()), font=n_font)                     
    if (position == "LL"):  #左下 lower left (LL)
        draw.text((0, y_posinon), text.decode(sys.getfilesystemencoding()), font=n_font)                         
    if (position == "CU"):  #中上 center upper (CU) 
        draw.text((x_posinon / 2, 0), text.decode(sys.getfilesystemencoding()), font=n_font)  
    if (position == "CT"):  #中間 center (CT)
        draw.text((x_posinon / 2, y_posinon / 2),text.decode(sys.getfilesystemencoding()), font=n_font)
    if (position == "CL"):  #中下 center lower (CL)  
        draw.text((x_posinon / 2, y_posinon), text.decode(sys.getfilesystemencoding()), font=n_font)
    if (position == "UR"):  #右上 upper right (UR) 
        draw.text((x_posinon, 0), text.decode(sys.getfilesystemencoding()), font=n_font)
    if (position == "CR"):  #右中 center right (CR)
        draw.text((x_posinon, y_posinon / 2), text.decode(sys.getfilesystemencoding()), font=n_font)
    if (position == "LR"):  #右下 lower right (LR)
        draw.text((x_posinon, y_posinon), text.decode(sys.getfilesystemencoding()), font=n_font)
          
    watermark = watermark.rotate(angle) # 預設為 Counterclockwise Rotation 逆時針 旋轉
    alpha = watermark.split()[3]
    #enhance(factor)  Factor 1.0 always returns a copy of the original image, lower factors mean less color (brightness, contrast, etc), and higher values more
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    watermark.putalpha(alpha)
    # PIL.Image.composite(image1, image2, mask)
    Image.composite(watermark, img, watermark).save(output_dir + "wm_" + imagefile, 'JPEG') 
    # 可參考 https://pillow.readthedocs.org/en/3.0.0/reference/Image.html    
    
def main() :
    #找出路徑下全部的圖片檔案
    types = ('*.png', '*.jpg', '*.jpeg' ,'*.bmp' ,'*.gif')
    all_image_files = []
    for files in types:
        all_image_files.extend(glob.glob(files)) 

    output_dir = "watermark_images/"
    
    #建立儲存資料夾
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
        
    # python example.py 簽名 超世紀粗行書.TTF 50  CT 0 0.8
    # python example.py [文字] [字型] [字型大小] [位置] [旋轉] [透明度] 
    text, fontname, fontsize ,position, angle, opacity =  sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]
    
    for image_file in all_image_files:
        add_watermark( text, fontname, int(fontsize), position, int(angle), float(opacity), image_file, output_dir)
 
if __name__ == "__main__":
    main()
    