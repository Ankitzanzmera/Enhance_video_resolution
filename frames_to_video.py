import os
import cv2
from tqdm import tqdm

path = "enhanced_frames/test1"
out_path = "output_videos/test1_output.mp4"

list_image_files = os.listdir(path=path)
list_image_files = sorted(list_image_files,key = lambda x: int(x.split("_")[0]))  ## sorting all files
print(list_image_files)

merge_images = []
for image_file in tqdm(list_image_files):
    image = cv2.imread(f"{path}/{image_file}")
    merge_images.append(image)

print(merge_images)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter(out_path,fourcc,30,(merge_images[0].shape[1],merge_images[0].shape[0]))

for image in merge_images:
    video_writer.write(image)

video_writer.release()
cv2.destroyAllWindows()