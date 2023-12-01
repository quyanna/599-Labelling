#if you need to pip install any of these, do it 
import os
import csv
import cv2
import shutil 

# Paths
batch_folder = 'D:\\Data\\real_world_test\\batch_1'  #  CHANGE TO YOUR BATCH FOLDER
csv_file = 'D:\\Data\\real_world_test\\batch_1\\batch_1_labels.csv'       # CHANGE TO WHERE YOU WANT TO SAVE THE CSV FILE

# Additional path for invalid images (ones skipped by the user) - CHANGE TO WHERE U WANT TO SAVE INVALID IMAGES
invalid_images_folder = 'D:\\Data\\real_world_test\\invalid_images'


# Create CSV file if it doesn't exist
if not os.path.isfile(csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Image Name', 'Label'])

# Create invalid images folder if it doesn't exist
if not os.path.exists(invalid_images_folder):
    os.makedirs(invalid_images_folder)

# Function to read existing labels (from the csv file - like a saved game)
def read_existing_labels(csv_path):
    labels = {}
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            labels[row[0]] = row[1]
    return labels

def label_images(folder, csv_path, invalid_folder):
    existing_labels = read_existing_labels(csv_path)

    for image_name in os.listdir(folder):
        if image_name in existing_labels:
            continue  # Skip already labeled images

        image_path = os.path.join(folder, image_name)
        image = cv2.imread(image_path)
        cv2.imshow('Image', image)
        cv2.waitKey(1)  # Display the image

        action = input(f"Image: {image_name}\nType label, 'skip', or 'exit': ").strip().lower()

        cv2.destroyAllWindows()

        if action == 'skip':
            shutil.move(image_path, os.path.join(invalid_folder, image_name))
        elif action == 'exit':
            print("Exiting labeling process...")
            break
        else:
            with open(csv_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([image_name, action])

    print("Batch labeling completed or exited.")


# Actually do the thing :)
label_images(batch_folder, csv_file, invalid_images_folder)

#I don't know if we are labelling case sensitive or insensitive, but if we want to normalize
# labels to lowercase, here is a function to do that to the labels in the csv file

def normalize_labels(csv_path):
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        rows = []
        for row in reader:
            rows.append([row[0], row[1].lower()])  # Normalize label to lowercase

    with open(csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Image Name', 'Label'])
        writer.writerows(rows)