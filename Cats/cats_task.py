import Image,os
cats_list = []
for root_dir, dirs, files in os.walk("E:\\cats"):
    for file_name in files:
        path = os.path.join(root_dir, file_name)
        cats_list.append(path)
print cats_list
for item in cats_list:
    try:
       im = Image.open(item)
       new_im = im.resize((im.size[0]/2, im.size[1]/2),Image.ANTIALIAS)
       new_im.save("resized_{}".format(item[8:]), "JPEG")
    except IOError:
        print ("Error: the given file isn't an image.")

