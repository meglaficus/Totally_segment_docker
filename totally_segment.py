import os
import nibabel as nib
from totalsegmentator.python_api import totalsegmentator
from tqdm import tqdm

def main():
    
    for filename in tqdm(os.listdir('files/CT')):    
        segment = totalsegmentator(os.path.join('files/CT', filename), 'TotalSeg', skip_saving=True, device='gpu', fast=False, verbose=False, quiet=True)
        nib.save(segment, os.path.join('files/TotalSeg', filename))


if __name__ == "__main__":
    main()