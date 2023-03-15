# Embed Thumbnail with ffmpeg
A python script that automates the shell commands required to embed external `png` thumbnail images to `mp4` video files. I have not tested the script with different file formats, but you can teset it after making the necessary changes in the code.

## How to use (Windows):
- Install [ffmpeg](https://ffmpeg.org/). You just have to download the executable file and add it's filepath to the `Path` environment variable. There are several tutorials on YouTube that explain it much better than I ever could with words alone, so if you are confused please refer to one of those.
- Place all the video and thumbnail files you want to embed in the same directory as the `main.py` file.
- Ensure that each thumbnail file has the same name as it's corresponding video file (except for the file extension of course).
- Execute the script with the command `python main.py`.
- The resulting videos should be generated in the `output` folder with the same name as the input file.

## Thank you and enjoy!