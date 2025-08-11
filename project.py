import os
import pandas as pd
import shutil
import re
path = "/Users/pravija/Desktop/project/embryo_dataset_annotations"
 

dfs = []


for filename in os.listdir(path):
    if filename.endswith(".csv"):
      
        
        filepath = os.path.join(path, filename)
        headers=["label","start","end"]
        df = pd.read_csv(filepath, names=headers)
        pattern = re.compile(r'RUN(\d+)\.jpeg')
        src_name = os.path.splitext(os.path.basename(filename))[0]
        file_path_data="/Users/pravija/Desktop/project/embryo_dataset"
        dest_dir="/Users/pravija/Desktop/project/dataset"
        src_name=src_name.replace("_phases", "")
        for index, row in df.iterrows():
            
            src_path = os.path.join(file_path_data, src_name)
            dest_path = os.path.join(dest_dir, row["label"])
            #print(dest_path)
            if not os.path.exists(dest_path):
                
                os.mkdir(dest_path)
            filenames=[]
            
            
            for file in os.listdir(src_path):
                
                if pattern.search(file):
                    
                    num_str = re.search(r'RUN(\d+)\.jpeg', file).group(1)
                    num = int(num_str)
                    

                    if num >= int(row["start"]) and num <= int(row["end"]):
                        cp_path=os.path.join(src_path,file)
                        dt_path=os.path.join(dest_path,file)
                        shutil.copy(cp_path, dt_path)
                        #filenames.append(file) 
import random

# Set the path to the parent directory containing the subdirectories of images
path_to_parent_directory = '/Users/pravija/Desktop/project/dataset'

# Loop through each subdirectory
for subdir in os.listdir(path_to_parent_directory):
    subdir_path = os.path.join(path_to_parent_directory, subdir)
    if os.path.isdir(subdir_path):
        # Create a list of all image file names in the subdirectory
        image_file_names = [f for f in os.listdir(subdir_path) if f.endswith('.jpeg') or f.endswith('.png')]
        # If there are more than 1000 images, randomly select 1000 and delete the rest
        if len(image_file_names) > 500:
            files_to_delete = set(image_file_names) - set(random.sample(image_file_names, 1000))
            for file_name in files_to_delete:
                os.remove(os.path.join(subdir_path, file_name))
                        
                        
            #print(row["label"],filenames)
            