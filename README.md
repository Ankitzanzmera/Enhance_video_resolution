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

## Download pre-trained model <a href="https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth" target="_blank">Here</a>

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

## you can refer notebook also : notebook_ESRGAN.ipynb

## Since Videos is size of 425MB it can't be share on Github, you can see Video <a href="https://drive.google.com/file/d/1k49ykUxijcOw80YOI4m2kRhQLi2svs-4/view?usp=sharing" target="_blank">Here</a>

## Pls First Download The video and then see, in drive it's not showing perfectly
