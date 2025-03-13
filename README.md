# Simple Metadata Extractor

ExifReveal is a Python tool that extracts metadata from common file types, including images and PDFs. It allows users to view information such as camera settings, author details, and other embedded data.

## Usage

1.  **Clone the repository:**
    ```bash
    git clone [repository URL]
    cd metadata-extractor
    ```
2.  **Run the script:**
    ```bash
    python metadata_extractor.py <filepath>
    ```
    -   `<filepath>`: The path to the image or PDF file.

## Example

```bash
python metadata_extractor.py image.jpg
python metadata_extractor.py document.pdf
```
## Dependencies

Pillow (PIL): For image metadata extraction.

PyPDF2: For PDF metadata extraction.

Install dependencies:
```bash
pip install Pillow PyPDF2
```
