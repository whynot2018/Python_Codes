#
#   PyThon Learning  @Faymaz
#       @programirez
#
# ----   .py   -----------
# pip install imageio
import imageio
filenames = ["./1.png","./2.png","./3.png","./4.png"]

images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave("./logo.gif",images,"GIF",duration=1)
