
---

# Image Labeling Application for Teach Puter How to Read

## Setup
- **Install Libraries**: Run `pip install` for any necessary libraries you don't have.
- **Change folder locations (near the bottom of the file)**: 
    - This program presumes you have some kind of folder containing a bunch of images. Personally, I used the script in this repo to  
    split the data into batches of size 500. Change `batch_folder` to the path to this folder.
    - Change value of `invalid_images_folder` to wherever you want to save images that you have skipped. 
    - Change value of `csv_file` to wherever you want to save the csv file of labels you make and their associated image paths.

## Using the App
- **Run the App**: Open your command line, navigate to the app's folder, and run `nicer-labelling.py`.
- **Label Images**: 
  - The app displays one image at a time from the 'images' folder.
  - Type a label in the text field and press `Enter` or click 'Submit'.
  - The label is saved in a CSV file along with the image name.
- **Skip Images**: 
  - To skip an image, type '1' and press `Enter` or click 'Skip'.
  - Skipped images are moved to an 'invalid' folder.
- **Exit App**: 
  - To exit, type '9' and press `Enter` or click 'Exit'.
  - The app closes, saving all progress.
- **Resize Window**: The window is resizable for your convenience. Images get cut off if the window is too smol, you might want to tinker with this in my code.

## Input and Output Processing
- **Input**: Labels are inputted via a text field. '1' and '9' are special inputs for skipping and exiting.
- **Output**: Labels are stored in a CSV file with two columns: 'Image Name' and 'Label'. Skipped images are moved to a separate folder.

## IF U REALIZED U MESSED UP: U can just manually adjust the label in the csv file if you really want 

---
