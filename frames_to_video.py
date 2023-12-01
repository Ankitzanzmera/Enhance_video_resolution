import os
import cv2
from tqdm import tqdm
from pathlib import Path


def merge_frames_to_videos():
    input_video_path = "input_videos/"
    enhanced_frame_path = "enhanced_frames/"
    out_path = "output_videos"
    os.makedirs(out_path,exist_ok=True)

    for frame_dir in os.listdir(enhanced_frame_path):

        video_path = os.path.join(input_video_path,f"{frame_dir}.mp4")
        video_capture = cv2.VideoCapture(video_path)
        fps = video_capture.get(cv2.CAP_PROP_FPS)  ## Gets FPS from Original Video files
        
        list_image_files = os.listdir(os.path.join(enhanced_frame_path,frame_dir))
        list_image_files = sorted(list_image_files,key = lambda x: int(x.split("_")[0]))  ## sorting all files
        print(list_image_files)

        merge_images = []
        for image_file in tqdm(list_image_files):
            image = cv2.imread(f"{enhanced_frame_path}/{frame_dir}/{image_file}")
            merge_images.append(image)
        # print(merge_images)

        output_path = os.path.join(out_path,f"{frame_dir}.mp4")
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        video_writer = cv2.VideoWriter(output_path,fourcc,fps,(merge_images[0].shape[1],merge_images[0].shape[0]))

        for image in tqdm(merge_images):
            video_writer.write(image)

        video_writer.release()
        cv2.destroyAllWindows()

if __name__ =="__main__":
    merge_frames_to_videos()