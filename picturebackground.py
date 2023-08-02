#
#   PyThon Learning  @Faymaz
#
#
from PIL import Image
input_path = 'resim.jpg'
output_path = 'resim.png'
inp = Image.open(input_path)
output = remve(inp)
output.save(output_path)
