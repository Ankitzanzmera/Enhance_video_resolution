import cv2
import os
from tqdm import tqdm

for video_name in os.listdir("input_videos"):

    dir_name = f"video_frames/{video_name.split('.')[0]}"
    os.makedirs(dir_name,exist_ok=True)

    video_cap = cv2.VideoCapture(f"input_videos/{video_name}")  
    
    frame_count = int(video_cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(frame_count)
        
    for i in tqdm(range(frame_count)):    ## tqdm shows the progress bar of FOR loop
        is_success,frames = video_cap.read()
        cv2.imwrite(f"{dir_name}/{i}.jpg",frames)   
    video_cap.release()
    print(f'Successfully Splitted video in frames at {dir_name} location...')   