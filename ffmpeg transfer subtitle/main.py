from pathlib import Path
from subprocess import run


def transfer_sub():
    main_input_file = ""
    sub_input_file = ""
    required_maps = ["0:0", "0:1", "1:2", "1:3"]  
    # for example above, 
    # first 2 are the video and audio streams from 'main_input_file'(index 0, streams 0 and 1), 
    # last 2 are the subtitle and font streams from 'sub_input_file'(index 1, streams 2 and 3).

    cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    output_dir = cur_dir / "output"
    output_dir.mkdir(exist_ok=True)

    output_file = f"{output_dir.name}/{main_input_file}"
    
    map_cmd = ""
    for mapping in required_maps:
        map_cmd = f'{map_cmd}-map {mapping} '
    
    command = f'ffmpeg -i "{main_input_file}" -i "{sub_input_file}" {map_cmd}-c copy -disposition:s:0 default "{output_file}"'
    
    # print(command)
    run(command)


if __name__ == "__main__":
    transfer_sub()