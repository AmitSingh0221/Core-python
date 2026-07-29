import shutil

source = "C:/Users/aarti singh/Desktop/photos/photo1.png.png";
target = "C:/Users/aarti singh/Desktop/IO - file/photo1.png.png";

shutil.copyfile(source, target)
print(source + " is copied to " + target)