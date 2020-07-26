# 795×300 pixels.
# 72dpi or 92dpi

# _1977
# aden
# brannan
# brooklyn
# clarendon
# earlybird
# gingham
# hudson
# inkwell
# kelvin
# lark
# lofi
# maven
# mayfair
# moon
# nashville
# perpetua
# reyes
# rise
# slumber
# stinson
# toaster
# valencia
# walden
# willow
# xpro2


import os
from PIL import Image
from PIL import ImageOps
from PIL import ImageEnhance
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageFont
from PIL.ImageFilter import (
    RankFilter, MedianFilter, MinFilter, MaxFilter, EDGE_ENHANCE,
)
import pilgram.css
import shutil

from img_temperature import set_temperature

pilgramfilters_name = [
    #'_1977',
    # 'aden',
    # 'brannan',
    # 'brooklyn',
    'clarendon',
    # 'earlybird',
    'gingham',
    'hudson',
    # 'inkwell',
    # 'kelvin',
    'lark',
    # 'lofi',
    # 'maven',
    # 'mayfair',
    # 'moon',
    # 'nashville',
    # 'perpetua',
    'reyes',
    'rise',
    'slumber',
    'stinson',
    # 'toaster',
    'valencia',
    'walden',
    # 'willow',
    # 'xpro2'
]


base_path = '/Users/cadu/Downloads/fotos_originais'
images_abs_paths = [os.path.join(base_path, f) for f in os.listdir(base_path) if f.endswith('jpg')]
# image_abs_path = images_abs_paths[0]
# image = PIL.Image.open(image_abs_path)

out_dir = os.path.join(os.path.normpath(base_path + os.sep + os.pardir), 'fotosout')

watermark_text = " ©  Necto Systems® - www.necto.com.br  "

font = ImageFont.truetype('/Users/cadu/Library/Fonts/MYRIADPRO-REGULAR.OTF', 20)

try:
    os.makedirs(out_dir)
    print('diretorio recem criado')
except FileExistsError:
    # os.rmdir(out_dir)  # does not remove non empty directorys
    shutil.rmtree(out_dir)
    os.makedirs(out_dir)
    print('diretorio foi apagado, e recriado')

for image_abs_path in images_abs_paths:
    image = None
    image = Image.open(image_abs_path)
    image.thumbnail((600, 600))
    # image = ImageOps.equalize(image)
    # image = image.filter(MaxFilter(size=3))

    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(0.2)

    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(1.4)

    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.2)

    drawing = ImageDraw.Draw(image)
    text_w, text_h = drawing.textsize(watermark_text, font)
    image_width, image_height = image.size
    text_position = image_width - text_w, (image_height - text_h) - 20
    text_image = Image.new('RGB', (text_w, (text_h)), color='#000000')
    text_image.putalpha(20)
    drawing.text((text_position[0], text_position[1]), watermark_text, fill="#ffffff", font=font)

    for filter_name in pilgramfilters_name:
        pilgram_filter = getattr(pilgram, filter_name)
        # o filtro não pode retornar para a mesma var !!!!
        image_filtered = pilgram_filter(image)

        image_filtered = set_temperature(image_filtered, 9100)
        image_filtered.paste(text_image, text_position, text_image)
        image_filtered.save(os.path.join(out_dir, f'{filter_name}_{os.path.basename(image_abs_path)}'), quality=72)



print(f'Exit directory: {out_dir}')
