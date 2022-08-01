import cv2
import os

### 프레임 단위로 이미지를 따올 거기 때문에 한 번에 모든 동영상을 다 처리해버리면 컴퓨터가 과부화가 걸림
### 코드는 폴더에 있는 동영상 모두 처리할 수 있게 짰지만 그냥 한 동영상씩 처리하고 이미지 선택하고 지우고 이런 식으로 하는 걸 추천

video_folder = r'C:\Users\kht96\Desktop\datasets\videos'  # 이미지를 따올 비디오가 있는 폴더
image_folder = r'C:\Users\kht96\Desktop\datasets\images' # 이미지를 저장할 폴더
video_list = os.listdir(video_folder)
print(f'video_list : {video_list}')

if not os.path.exists(image_folder) :
    os.mkdir(image_folder)

idx = '' #각 비디오마다 파일명이 겹치지 말라고 인덱스 지정
count = 0
for i in range(len(video_list)):
    print(video_list[i])
    video_dir = os.path.join(video_folder,video_list[i])
    print(f'video_dir : {video_dir}')
    video = cv2.VideoCapture(video_dir)

    if not video.isOpened():
        print("Could not Open :", video_list[i])
        exit(0)
        continue

    #불러온 비디오 파일의 정보 출력
    # length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    # width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    # height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    # print("length :", length)
    # print("width :", width)
    # print("height :", height)
    print("fps :", fps)

    #프레임을 저장할 디렉토리를 생성
    try:
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
    except OSError:
        print ('Error: Creating directory. ' + image_folder)

    while (video.isOpened()):
        ret, img = video.read()
        if ret:
            cv2.imshow("video", img)
            # if (int(video.get(1)) // (fps/2) != count):
            count += 1
            cv2.imwrite(image_folder + f"\\{idx}{str(count).zfill(6)}.png", img)
            cv2.waitKey(1)
        if not ret:
            break
    video.release()
    cv2.destroyAllWindows()