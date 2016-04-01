#coding=utf8
import os, sys
from PIL import Image
from PIL import ImageFile
import glob
 
output_dir = "resized_images" 

def main():
    # 找出路徑下全部的圖片檔案
    types = ('*.png', '*.jpg', '*.jpeg' ,'*.bmp' ,'*.gif') # the tuple of file types
    all_image_files = []
    for files in types:
        all_image_files.extend(glob.glob(files)) 

    # ImageFile.LOAD_TRUNCATED_IMAGES = True
    # 建立儲存資料夾
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
          
    if(sys.argv[1] == "size"):
       # 圖片大小比率縮放    # python resize.py size 200
       if(len(sys.argv) == 3):
          ratio = sys.argv[2]
          setRatio(ratio, all_image_files)        
       # 指定圖片大小   # python resize.py  size 640 360
       if(len(sys.argv) == 4):
          basewidth, baseheight = sys.argv[3],sys.argv[4]    
          setSize(basewidth, baseheight, all_image_files)    
    # 旋轉圖片 # python resize.py rotate 90   
    # 預設為 Counterclockwise Rotation 逆時針旋轉 ，如需順時針請修改為 -90         
    if(sys.argv[1] == "rotate"):
       degree = sys.argv[2]
       setRotate(float(degree), all_image_files) 
                 
def setSize(basewidth, baseheight, all_image_files):
    for image_file in all_image_files:
        print "Processing", image_file, "..."
        img = Image.open(image_file)
        img = img.resize( (int(basewidth), int(baseheight)) ,Image.ANTIALIAS)
        # Image.ANTIALIAS (a high-quality downsampling filter). If omitted, 
        # or if the image has mode “1” or “P”, it is set PIL.Image.NEAREST.
        image_filename = output_dir + "/" + image_file
        print "Save to " + image_filename
        img.save(image_filename)     
        
def setRatio(ratio, all_image_files):
    for image_file in all_image_files:
        print "Processing", image_file, "..."
        img = Image.open(image_file)
        width, height =  img.size
        width = int((width * float(ratio)/100))
        height = int((height * float(ratio)/100)) 
        # Image.resize(size, resample=0)  size – The requested size in pixels, as a 2-tuple: (width, height).  width and height type int 
        img = img.resize( (width ,height) ,Image.ANTIALIAS)
        image_filename = output_dir + "/" + image_file
        print "Save to " + image_filename
        img.save(image_filename)     

def setRotate(degree, all_image_files):
    for image_file in all_image_files:
        print "Processing", image_file, "..."
        img = Image.open(image_file)
        img_rotate = img.rotate(degree)   
        image_filename = output_dir + "/" + image_file
        print "Save to " + image_filename
        img_rotate.save(image_filename)      
       
if __name__ == "__main__":
    main()     