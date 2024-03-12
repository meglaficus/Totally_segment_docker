## Building and running TotalSegmentator in Docker container

1. Clone this repository
  - (Optional) Edit first line of dockerfile if using AMD GPU
2. Navigate to the repository directory
3. Build docker container

```
docker build -t meglaficus/totally_segment .
```
4. Have this kind of folder structure ready:
```
├── files
│   ├── CT
│   │   ├── 00001.nii.gz
│   │   ├── 00002.nii.gz
│   │   ├── 00003.nii.gz
│   │   ├── ...
│   ├── TotalSeg
```

5. Run the container (change command to include path to "files" directory)

```
docker run --gpus all -it -v /path/to/files/directory/:/home/app/files --shm-size=24gb meglaficus/totally_segment

```

6. Execute the program
```
cd ../home/app
python totally_segment.py
exit
```
