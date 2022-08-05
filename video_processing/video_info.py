import cv2

file_dir = r'/Users/htkim/PycharmProjects/FTTD_Runway/video_processing/src/video/taemin Male Model TAEMIN PARK (박태민)  RUNWAY COMPILATION.mp4'

cap = cv2.VideoCapture(file_dir)
if not cap.isOpened():
    print('could not open :', file_dir)
    exit(0)

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

msg = f"length : {length}\n" \
      f"width : {width}\n" \
      f"height : {height}\n" \
      f"fps : {fps}"

print(msg)