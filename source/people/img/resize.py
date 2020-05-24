from PIL import Image
from pathlib import Path

from resizeimage import resizeimage


def th(src_path, dst_folder="thumbs"):
    dst_path = Path(dst_folder) / src_path
    with open(src_path, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_thumbnail(image, [150, 150])
            cover.save(dst_path, image.format)

def src(filename):
  return f"[![](img/thumbs/{filename})](img/{filename})"
            
for file in Path(".").glob("*.j*"):
   th(str(file)) 
   print(src(file))
   
   
