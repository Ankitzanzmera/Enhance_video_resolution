## Enhancing Video Quality

## create direcotry called input_videos and put all input videos in this directory
        input_videos
        ├── test1.mp4                   
        ├── test2.mp4                   
        ├── test3.mp4      

## To Create Environment Write Command in CMD: 
    conda create -p venv/ python==3.9 -y

## Install Dependencies
    pip install -r requirements.txt

## Split Videos into Frames
    python split_into_frames.py

## it will Create Folder called video_frames
    video_frames
        ├── test1
              ├── All frames .jpg
        ├── test2    
              ├── All frames .jpg
        ├── test3      
              ├── All frames .jpg

## Clone ESRGAN repository
    git clone https://github.com/xinntao/Real-ESRGAN.git

## Install all Dependecies that required for ESRGAN
    cd Real-ESRGAN
    pip install -r requirements.txt  # dependecies of Real-ESRGAN

## Install Pre-trained Model
    cd Real-ESRGAN/experiments/pretrained_models/
    !wget Real-ESRGAN\experiments\pretrained_models\RealESRGAN_x4plus.pth
        # Link for Pre-trained model : https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth

## Copy run.py into Real-ESRGAN

## run run.py
    python run.py

## It Will Create Directory called enhanced_frames
        enhanced_frames
        ├── test1
              ├── All frames .jpg
        ├── test2    
              ├── All frames .jpg
        ├── test3      
              ├── All frames .jpg
    
## Merge all thie enhanced frames into videos again
    python frames_to_videos.py

## it will create new directory called output_video
    output_videos
        ├── test1.mp4                   
        ├── test2.mp4                   
        ├── test3.mp4  

## This model enhance frame resolution * 4  
## in my case test1.mp4 enhance from 4.19 MB to 426 MB 

## you can refer notebook also : 
 