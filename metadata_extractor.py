import argparse
import os
from PIL import Image
from PIL.ExifTags import TAGS
import PyPDF2

def extract_image_metadata(filepath):
    """Extracts metadata from image files."""
    try:
        img = Image.open(filepath)
        exif_data = img.getexif()
        metadata = {}
        if exif_data:
            for tag, value in exif_data.items():
                decoded_tag = TAGS.get(tag, tag)
                metadata[decoded_tag] = value
        return metadata
    except Exception as e:
        return {"error": str(e)}

def extract_pdf_metadata(filepath):
    """Extracts metadata from PDF files."""
    try:
        with open(filepath, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            metadata = pdf_reader.metadata
            if metadata:
                return dict(metadata)
            else:
                return {"message": "No metadata found in PDF."}
    except Exception as e:
        return {"error": str(e)}

def main():
    """Main function to parse arguments and run the metadata extractor."""
    parser = argparse.ArgumentParser(description="Simple Metadata Extractor")
    parser.add_argument("filepath", help="Path to the file")
    args = parser.parse_args()

    filepath = args.filepath
    _, file_extension = os.path.splitext(filepath)
    file_extension = file_extension.lower()

    if file_extension in ['.jpg', '.jpeg', '.png']:
        metadata = extract_image_metadata(filepath)
        print("Image Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")
    elif file_extension == '.pdf':
        metadata = extract_pdf_metadata(filepath)
        print("PDF Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")
    else:
        print("Unsupported file type.")

if __name__ == "__main__":
    main()
