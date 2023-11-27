import os
import shutil
from math import ceil

source_folder = 'D:\\Data\\scrape-wtf-new\\scrape-wtf-new'  # Path to the folder containing all the images
destination_folder = 'D:\\Data\\batched'  # Path where the batched folders will be created
batch_size = 500  # Number of images per subfolder


def batch_images(src_folder, dest_folder, batch_size):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    files = [f for f in os.listdir(src_folder) if os.path.isfile(os.path.join(src_folder, f))]
    total_batches = ceil(len(files) / batch_size)

    for batch in range(total_batches):
        batch_folder = os.path.join(dest_folder, f'batch_{batch + 1}')
        os.makedirs(batch_folder, exist_ok=True)

        for file in files[batch * batch_size: (batch + 1) * batch_size]:
            shutil.move(os.path.join(src_folder, file), os.path.join(batch_folder, file))

        print(f'Batch {batch + 1} completed.')

    print('All batches are created.')

batch_images(source_folder, destination_folder, batch_size)