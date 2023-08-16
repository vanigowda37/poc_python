import os
import platform
from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_data(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    if exif_data is not None:
        exif = {
            TAGS[tag]: value
            for tag, value in exif_data.items()
            if TAGS.get(tag)
        }
        return exif
    return {}

def get_file_metadata(file_path):
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' does not exist.")
            return

        # Get file statistics
        file_stat = os.stat(file_path)

        # Print the metadata
        print("File Path:", file_path)
        print("File Size:", file_stat.st_size, "bytes")
        print("Creation Time:", os.path.getctime(file_path))
        print("Modification Time:", os.path.getmtime(file_path))
        print("Access Time:", os.path.getatime(file_path))
        print("Owner ID:", file_stat.st_uid if hasattr(file_stat, 'st_uid') else "N/A")
        print("Group ID:", file_stat.st_gid if hasattr(file_stat, 'st_gid') else "N/A")
        print("File Mode:", oct(file_stat.st_mode))

        # Check if it's an image file
        if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            exif_data = get_exif_data(file_path)
            if exif_data:
                print("\nEXIF Metadata:")
                for tag, value in exif_data.items():
                    print(f"{tag}: {value}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to access '{file_path}'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    file_path = r"/mnt/c/Users/vg31/Downloads/photoprocessing/photoprocessing/download.jpg"  # Replace with the actual file path
    get_file_metadata(file_path)
