#
#   PyThon Learning  @Faymaz
#       @programirez
#
# ----   .py   -----------
# pip install
# Not working

from rembg import remove
from PIL import Image, ImageOps

input_path = '/home/faymaz/resim.jpg'
output_path = '/home/faymaz/resim.png'

inp = Image.open(input_path)
output = remove(inp)
silhouette = output.convert("L")
silhouette = silhouette.point(lambda x: 0 if x > 0 else 255)
background = Image.new('RGB', silhouette.size, (255, 255, 255))
background.paste(ImageOps.colorize(silhouette, black="black", white="white"), mask=silhouette)
background.save(output_path)
