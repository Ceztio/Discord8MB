import os
import subprocess as sp
import sys
import ffmpy

try:
    input_file_name = sys.argv[1]
    filename = "8mb-"+os.path.basename(input_file_name)
    print(input_file_name)

    def get_length(filename):
        result = sp.run(["ffprobe", "-v", "error", "-show_entries",
                                "format=duration", "-of",
                                "default=noprint_wrappers=1:nokey=1", filename],
            stdout=sp.PIPE,
            stderr=sp.STDOUT)
        return float(result.stdout)


    seconds = get_length(input_file_name)
    kBps = 8 * 8192 / seconds
    kBps=kBps - 128
    size = str(kBps)+"k"

    ff = ffmpy.FFmpeg(
    inputs={input_file_name: None},
    outputs={filename: "-c:v libx264 -b:v "+size+" -c:a aac -b:a 128k"
    }
)
    ff.run()


except IndexError:
    input("Please drop a file.")