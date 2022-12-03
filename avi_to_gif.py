from moviepy.editor import VideoFileClip
import os
import glob


print(os.path.dirname(os.path.realpath(__file__)))

# Set dir of the skript a parent dir  
parent_dir = os.path.dirname(os.path.realpath(__file__))
 
# Make shure these dirs exist, otherwhise error will occure
pre_converted_dir = "/avi_files_to_convert"
converted_dir = "/gif_files_converted"

path = parent_dir + pre_converted_dir
results = parent_dir + converted_dir

os.chdir(path)
for file in glob.glob("*.avi"): 
    os.chdir(path)
    # Get video file that is an mp4 from an dir
    videoClip = VideoFileClip(file)
    # Create new file that is an .gif
    os.chdir(results)
    videoClip.write_gif(os.path.splitext(file)[0]+".gif")

print("Success! All files where created! Have fun!")
