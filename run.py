import os
from pathlib import Path

splitted_frame_path = "./video_frames"
enhanced_frame_path = "./enhanced_frames"
os.makedirs(enhanced_frame_path,exist_ok = True)

for dir in os.listdir(splitted_frame_path):
    for frames in os.listdir(os.path.join(splitted_frame_path,dir)):
        input_path = Path(os.path.join(splitted_frame_path,dir,frames))
        output_path = os.path.join(enhanced_frame_path,dir)
        os.system("!python inference_realesrgan.py --model_name RealESRGAN_x4plus -i $input_path -o $output_path --outscale 4 --face_enhance --fp32 -dn 1")