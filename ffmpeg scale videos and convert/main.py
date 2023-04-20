from pathlib import Path
from subprocess import run

def main():

    input_format = "mkv"
    output_format = "mp4"
    scale = "1280:720"
    crf = 18
    slow = True

    cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    output_dir = cur_dir / "output"
    output_dir.mkdir(exist_ok=True)

    file_list = list(cur_dir.glob(f"*.{input_format}"))

    for file in file_list:
        output_file = f"{output_dir.name}\{file.name[:-len(input_format)]}{output_format}"
        
        if scale:
            scale_cmd = f"-vf scale={scale}"
        else:
            scale_cmd = ""
        if crf:
            crf_cmd = f"-crf {crf}"
        else:
            crf_cmd = ""
        if slow:
            preset_cmd = "-preset slow"
        else:
            preset_cmd = ""
        
        command = f"ffmpeg -i {file.name} {scale_cmd} {preset_cmd} {crf_cmd} {output_file}"
        
        print("-"*50)
        print(f"Converting {file.name}...")
        print("-"*50)
        
        # print(command)
        run(command)
    
    print("Done!")

if __name__ == "__main__":
    main()