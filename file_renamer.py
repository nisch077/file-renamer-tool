import os

def rename_files(directory):
    """
    Renames image and video files in a directory with IMG-XXX and VID-XXX patterns.

    Args:
        directory (str): The path to the directory containing the files.
    """
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}
    video_extensions = {".mp4", ".avi", ".mov", ".wmv", ".mkv", ".flv", ".m4v"}
    image_count = 1
    video_count = 1

    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            name, ext = os.path.splitext(filename.lower())
            new_name = None

            if ext in image_extensions:
                new_name = f"IMG-{image_count:03d}{ext}"
                image_count += 1
            elif ext in video_extensions:
                new_name = f"VID-{video_count:03d}{ext}"
                video_count += 1

            if new_name:
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed '{filename}' to '{new_name}'")

if __name__ == "__main__":
    target_directory = input("Enter the directory path: ")
    if os.path.isdir(target_directory):
        rename_files(target_directory)
        print("File renaming process completed.")
    else:
        print("Invalid directory path.")