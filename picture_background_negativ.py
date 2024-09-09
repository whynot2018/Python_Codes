#
#   PyThon Learning  @Faymaz
#       @programirez
#
# ----   .py   -----------
# pip install
from rembg import remove
from PIL import Image

input_path = '/home/faymaz/resim.jpg'
output_path = '/home/faymaz/resim.png'

inp = Image.open(input_path)
output = remove(inp)
output = output.convert("L")
output.save(output_path)
