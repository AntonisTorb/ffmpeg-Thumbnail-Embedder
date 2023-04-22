# FFMPEG tools with Python
A few python scripts that use ffmpeg through the subprocess module.

## Table of Contents
- [Requirements](#requirements)
- [Clip video]()
- [Embed thumbnail to video file](#embed-thumbnail-to-video-file)
- [Scale videos and Convert](#scale-videos-and-convert)
- [Transfer subtitle](#transfer-subtitle)


## Requirements
Install [ffmpeg](https://ffmpeg.org/). You just have to download the executable file and add it's filepath to the `Path` environment variable. There are several tutorials on YouTube that explain it much better than I ever could with words alone, so if you are confused please refer to one of those.

## Clip video
A python script that automates the ffmpeg shell command required to get a clip from a video.

**How to use (Windows):**
- Specify the `input_file_name`, `start_time` and `duration` in the `main.py` script file.
- Execute the script with the command: `python main.py`.
- The resulting video should be generated in the `output` folder with the same name as the input file.

## Embed thumbnail to video file
A python script that automates the ffmpeg shell commands required to embed external `png` thumbnail images to `mp4` video files. I have not tested the script with different file formats, but you can teset it after making the necessary changes in the code.

**How to use (Windows):**

- Place all the video and thumbnail files you want to embed in the same directory as the `main.py` file.
- Ensure that each thumbnail file has the same name as it's corresponding video file (except for the file extension of course).
- Execute the script with the command: `python main.py`.
- The resulting videos should be generated in the `output` folder with the same name as the input file.

## Scale videos and Convert
A python script that automates the ffmpeg shell commands required to scale a video to a different resolution, as well as convert it to a different filetype. Everything is re-encoded.

**How to use (Windows):**
- Place all the video files you want to scale and/or convert in the same directory as the `main.py` file.
- Execute the script with the command: `python main.py`.
- The resulting videos should be generated in the `output` folder with the same name as the input file.

## Transfer subtitle
A python script that automates the ffmpeg shell command required to transfer a subtitle stream from one media/subtitle file to another media file.

**How to use (Windows):**
- Specify the `main_input_file`, `sub_input_file` and `required_maps` in the `main.py` script file.
- Execute the script with the command: `python main.py`.
- The resulting video should be generated in the `output` folder with the same name as the input file.

## Thank you and enjoy!