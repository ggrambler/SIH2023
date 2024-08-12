import os
import tifffile
from PIL import Image

mode = 1# 1 - Tiff to png, 2 - png to Tiff

input_tif = r'/Users/harshit/PycharmProjects/Vibhor/SocketConnection/input_tif'
cropped_tif = r'/Users/harshit/PycharmProjects/Vibhor/SocketConnection/cropped_tif'
cropped_png = r'/Users/harshit/PycharmProjects/Vibhor/SocketConnection/cropped_png'

input_png = r'/Users/harshit/PycharmProjects/Vibhor/SocketConnection/input_png'
output_tif = r'/Users/harshit/PycharmProjects/Vibhor/SocketConnection/output_tif'

tif_px_r, tif_px_c = 5588, 135048
window_size_r, window_size_c = 5587, 5587

def clean_directory(directory_path, file_extension):
    for file in os.listdir(directory_path):
        if file.endswith(file_extension):
            file_path = os.path.join(directory_path, file)
            os.remove(file_path)
            print(f"Removed: {file_path}")

def convert_tiff_to_png(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    clean_directory(output_dir, '.png')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    i = 0
    # Iterate through files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.tif') or filename.endswith('.tiff'):
            input_file_path = os.path.join(input_dir, filename)
            output_file_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.png')

            # Open the TIFF file
            with Image.open(input_file_path) as img:
                # Convert and save as PNG with better quality settings
                img = img.convert("RGB")  # Convert to RGB before saving as PNG
                img.save(output_file_path, format='PNG', quality=95)
                i = i+1
                print(i)
                print(f"Converted: {filename} to PNG")


def convert_png_to_tiff(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    clean_directory(output_dir, '.tif')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.png'):
            input_file_path = os.path.join(input_dir, filename)
            output_file_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.tif')

            # Open the PNG file
            with Image.open(input_file_path) as img:
                # Convert and save as TIFF
                img.save(output_file_path, format='TIFF')
                print(f"Converted: {filename} to TIFF")

def tile(filename, dir_in, dir_out):
    clean_directory(dir_out, '.tif')
    name, ext = os.path.splitext(filename)
    img = tifffile.imread(os.path.join(dir_in, filename))
    print(img.shape)
    i = 0
    row=0
    column=0
    for r in range(0, img.shape[0] - window_size_r, window_size_r):
        row += 1
        for c in range(0, img.shape[1] - window_size_c, window_size_c):
            column += 1
            window = img[r:r + window_size_r, c:c + window_size_c]
            out = os.path.join(dir_out, f'{name}-{row}-{column}_{ext}')
            tifffile.imsave(out, window)
            print(i)
            i = i + 1
        column = 0

    convert_tiff_to_png(cropped_tif, cropped_png)

if mode==1:
    tile('input.tif',
         input_tif,
     cropped_tif)
else:
    convert_png_to_tiff(input_png, output_tif)