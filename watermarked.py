#
#   PyThon Learning  @Faymaz
#       @programirez
#
# ----   .py   -----------
# pip install

from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_image_path, output_image_path, watermark_text):
    original = Image.open(input_image_path).convert("RGBA")
    txt = Image.new("RGBA", original.size, (255, 255, 255, 0))
    font = ImageFont.truetype("arial.ttf", 40)
    draw = ImageDraw.Draw(txt)
    width, height = original.size
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    position = (width - text_width - 10, height - text_height - 10)
    draw.text(position, watermark_text, fill=(255, 255, 255, 128), font=font)
    watermarked = Image.alpha_composite(original, txt)
    watermarked.show()
    watermarked.convert("RGB").save(output_image_path, "JPEG")

add_watermark("resim.jpg", "resim_watermarked.jpg", "@faymaz")
