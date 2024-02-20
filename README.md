# OCR Django App
<div id="header" align="center">
  <img src="previews/demo.gif" width="500"/>
</div>

<br/>

## Learning Goals and Objectives
- Practicing Django Skills
- Exploring OCR Techniques and integrating in Django project

## Features
- Upload images in various formats (e.g., JPG, PNG).
- Extract text from the uploaded images using a robust OCR engine.
- Display the extracted text on the user interface.

## Requirements
- Python >= 3.8 (https://www.python.org/downloads/)
- Django framework (https://www.djangoproject.com/start/)
- OCR library (Tesseract: https://github.com/tesseract-ocr/tesseract?tab=readme-ov-file#installing-tesseract)

## Installation

1. Clone this repository to your local machine or download and extract the ZIP file.

2. Navigate to the project directory using your terminal or command prompt.

3. Create a virtual environment to isolate your project dependencies:
   ```bash
   python -m venv myenv
   ```

4. Activate the virtual environment:
     ```
    > On windows -> venv\Scripts\activate
    > On linux -> source myenv/bin/activate
     ```

5. Install the project dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

6. Navigate to 'src' of the project directory and run the database migrations to set up the database:
    ```bash
    python manage.py migrate
    ```
7. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

  1. Access the application in your web browser at http://localhost:8000/.
  2. Click the "Browse" button and select an image to upload.
  3. Click the "Scan" button.
  4. The extracted text will be displayed on the page.


## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)


#### **Thank you for visiting the OCR Django App! If you have any questions, suggestions or encounter any issues, please don't hesitate to [DM me](https://twitter.com/randomdotfloat)**