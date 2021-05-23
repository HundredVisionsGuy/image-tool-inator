"""Main module."""
import clerk
from PIL import Image

def get_exif_data(file_path):
    image = Image.open(file_path)
    return image._getexif()

def get_all_exif_data(path):
    all_images = clerk.get_all_project_files(path)
    exif_data_list = []
    for image in all_images:
        try: 
            exif_data_list.append(get_exif_data(image))
        except:
            print("Problem: with " + image)
    return exif_data_list

if __name__ == "__main__":
    path_to_images = clerk.get_full_path_string("image_tool_inator/input/")
    
    data = get_all_exif_data(path_to_images)
    for el in data:
        print(el)
