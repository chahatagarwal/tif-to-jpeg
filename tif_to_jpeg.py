import os
#Python image Library
from PIL import Image

# "image_output" -> Directory name
image_output = "image_output_path/image_output"

#To automate for n number of .tif files
for root, dirs, files in os.walk("tiff_path"):
    for j in files :
        #if .tif files then start converting to .jpg images
        if j.split(".")[1] == "tif":
            #for a single .tif file, it has many pages. Hence, iterating all the pages as frames
            count = 0
            outfile = "".join(j.split(".")[0])
            im = Image.open(root + "/" + j)
            while True:
                try:   
                    im.seek(count)
                    out = im.convert("RGB")
                    out.save(image_output + "/" + outfile + "_{}.jpeg".format(count), "JPEG", quality=90)
                except EOFError:
                    break       
                count += 1          