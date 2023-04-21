from pathlib import Path
from subprocess import run


def clip():

    input_file_name = ""
    start_time = "00:00:00.000"  # (hours):(minutes):(seconds).(milliseconds)
    duration = "00:00:00.000"  # (hours):(minutes):(seconds).(milliseconds)

    cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    
    output_dir = cur_dir / "output"
    output_dir.mkdir(exist_ok=True)
    output_file = f"{output_dir.name}\{input_file_name}"

    command = f'ffmpeg -ss {start_time} -t {duration} -i "{input_file_name}" "{output_file}"'

    # print(command)
    run(command)

if __name__ == "__main__":
    clip()