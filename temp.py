import os
import cv2
from tqdm import tqdm

for dir_name in os.listdir("video_frames"):
    total_frames = len(os.listdir(f"video_frames/{dir_name}"))

    for file_name in tqdm(range(total_frames)):
        image = cv2.imread(f"video_frames/{dir_name}/{file_name}.jpg")
        cv2.imshow("Frames",image)
        
        if cv2.waitKey(1) & 0xff == ord('q'):
            break