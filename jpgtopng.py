
from PIL import Image
import os

def convert_jpg_to_png(input_path):
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Error: File {input_path} does not exist")
        return
    
    # Check if input file is a jpg/jpeg
    if not input_path.lower().endswith(('.jpg', '.jpeg')):
        print("Error: Input file must be a JPG/JPEG file")
        return
    
    # Create output filename by replacing extension with .png
    output_path = os.path.splitext(input_path)[0] + '.png'
    
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Convert and save as PNG
            img.save(output_path, 'PNG')
        print(f"Successfully converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Error converting image: {str(e)}")

def main():
    # Get input file path from user
    input_path = input("Enter the path to your JPG file: ")
    convert_jpg_to_png(input_path)

if __name__ == "__main__":
    main()