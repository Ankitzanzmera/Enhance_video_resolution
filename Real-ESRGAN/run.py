import os


for dir in os.listdir("../video_frames"):
    input_dir = f"../video_frames/{dir}"
    output_dir = os.path.join("../","output_frames",dir)
    os.makedirs(output_dir,exist_ok=True)

    # os.system(f"python inference_realesrgan.py --model_name RealESRGAN_x4plus --input {input_dir} --outscale 4 --output {output_dir}")