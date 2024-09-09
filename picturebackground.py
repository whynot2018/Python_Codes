#
#   PyThon Learning  @Faymaz
#       @programirez
#
# ----   .py   -----------
# pip install

import sys
from rembg import remove
from PIL import Image

input_path = sys.argv[1]
output_path = input_path.split('.')[0] + '_new.png'
input_path = '/home/faymaz/' + input_path
output_path = '/home/faymaz/' + output_path
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)