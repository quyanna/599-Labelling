import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import shutil
import csv

class LabelingApp:
    def __init__(self, root, folder, csv_path, invalid_folder):
        self.root = root
        self.folder = folder
        self.csv_path = csv_path
        self.invalid_folder = invalid_folder
        self.existing_labels = self.read_existing_labels(csv_path)
        self.image_files = iter([f for f in os.listdir(folder) if f not in self.existing_labels])
        self.current_image = None

          # Set the window size
        self.root.geometry('1024x768')  # Width x Height

        self.frame = tk.Frame(root)
        self.frame.pack()

        # Image display area with a fixed size
        self.image_label = tk.Label(self.frame)
        self.image_label.pack()

        self.label_entry = tk.Entry(self.frame)
        self.label_entry.pack()

        self.submit_button = tk.Button(self.frame, text="Submit [Enter]", command=self.submit_label)
        self.submit_button.pack()

        # Button to skip image
        self.skip_button = tk.Button(self.frame, text="Skip [1]", command=self.skip_image)
        self.skip_button.pack()

        # Button to exit application
        self.exit_button = tk.Button(self.frame, text="Exit[9]", command=self.exit_app)
        self.exit_button.pack()

        # Bind the Enter key to the submit_label function
        self.root.bind('<Return>', self.submit_label)

        self.load_next_image()

    def read_existing_labels(self, csv_path):
        labels = {}
        if os.path.isfile(csv_path):
            with open(csv_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    labels[row[0]] = row[1]
        return labels

    def load_next_image(self):
        try:
            self.current_image = next(self.image_files)
            img = Image.open(os.path.join(self.folder, self.current_image))
            img.thumbnail((800, 600))  # Resize if necessary
            self.photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.photo)
        except StopIteration:
            self.root.destroy()  # Close the app if no more images

    def submit_label(self, event=None):
        label = self.label_entry.get().strip()

        # Check the label and perform the corresponding action
        if label == '1':  # Skip the image
            self.skip_image()
        elif label == '9':  # Exit the application
            self.exit_app()
        else:  # Submit the label
            with open(self.csv_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([self.current_image, label])
            self.load_next_image()

        self.label_entry.delete(0, tk.END)  # Clear the entry field

    def skip_image(self, event=None):
        shutil.move(os.path.join(self.folder, self.current_image), self.invalid_folder)
        self.load_next_image()

    def exit_app(self, event=None):
        print("Exiting labeling process...")
        self.root.destroy()
        self.root.quit()


# Paths
batch_folder = 'D:\\Data\\VFR_real_test'  #  CHANGE TO YOUR BATCH FOLDER
csv_file = 'C:\\Users\\Quyanna\\Desktop\\CPSC599\\Labelling\\599-Labelling\\real_test.csv'       # CHANGE TO WHERE YOU WANT TO SAVE THE CSV FILE

# Additional path for invalid images (ones skipped by the user) - CHANGE TO WHERE U WANT TO SAVE INVALID IMAGES
invalid_images_folder = 'D:\\Data\\VFR_real_test\\invalid_images'

# Create CSV file if it doesn't exist
if not os.path.isfile(csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Image Name', 'Label'])

# Create invalid images folder if it doesn't exist
if not os.path.exists(invalid_images_folder):
    os.makedirs(invalid_images_folder)

# Create the main window
root = tk.Tk()
app = LabelingApp(root, batch_folder, csv_file, invalid_images_folder)

# Start the application
root.mainloop()
