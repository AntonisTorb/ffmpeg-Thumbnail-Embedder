from pathlib import Path
from subprocess import run

def main():

    cur_dir = Path.cwd()
    output_dir = cur_dir / "output"

    file_list = list(cur_dir.glob("*.mp4"))

    for file in file_list:
        thumb_file = f"{file.name[:-3]}png"
        output_file = f"{output_dir.name}\{file.name}"

        print(f"Now embedding {thumb_file}...")
        run(
            [
                "ffmpeg",
                "-i",
                f"{file.name}",
                "-i",
                f"{thumb_file}",
                "-map",
                "1",
                "-map",
                "0",
                "-c",
                "copy",
                "-disposition:0",
                "attached_pic",
                f"{output_file}"
            ]
        )
    
    print("Done!")

if __name__ == "__main__":
    main()