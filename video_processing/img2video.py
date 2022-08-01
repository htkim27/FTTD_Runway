import cv2
import glob
import os

fps = 30
base_dir = r'C:\Users\kht96\Desktop\datasets\images'
image_format = 'png'

save_dir = r'C:\Users\kht96\Desktop\datasets'
new_filename = r'merged_SR.mp4'
video_format = 'mp4v'

img_array = []
for filename in glob.glob(base_dir + f'\\*.{image_format}'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

out = cv2.VideoWriter(os.path.join(save_dir,new_filename), cv2.VideoWriter_fourcc(*video_format), fps, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()