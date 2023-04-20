from pathlib import Path
from subprocess import run

def main():
    video_format = "mp4"
    thumbnail_format = "png"

    cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    output_dir = cur_dir / "output"
    output_dir.mkdir(exist_ok=True)

    file_list = list(cur_dir.glob(f"*.{video_format}"))
    
    for file in file_list:
        thumb_file = f"{file.name[:-len(video_format)]}{thumbnail_format}"
        output_file = f"{output_dir.name}\{file.name}"

        command = f"ffmpeg -i {file.name} -i {thumb_file} -map 1 -map 0 -c copy -disposition:0 attached_pic {output_file}"
        
        # print(command)
        run(command)

if __name__ == "__main__":
    main()