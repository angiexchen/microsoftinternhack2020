import cv2 
import os
from PIL import Image
from skimage.measure import compare_ssim

def filter_by_ccsine_similarity(image_files):
    prev = None
    hasPrev = False
    pruned = [] 
    for image_file in image_files: 
        current = cv2.cvtColor(cv2.imread('./static/' +image_file), cv2.COLOR_BGR2GRAY)
        if hasPrev: 
            score = compare_ssim(current, prev)
            if score < 0.95: 
                pruned.append(image_file)
        prev = current
        hasPrev = True
    return pruned

def get_images(): 
    image_files = [] 
    for i in range(1,len(os.listdir('./static/data'))):
        image_files.append('data/frame' + str(i) + '.jpg')
    return filter_by_ccsine_similarity(image_files)

def convert_video_to_frames(): 
    # Read the video from specified path 
    cam = cv2.VideoCapture("index.mp4") 
    
    try: 
        
        # creating a folder named data 
        if not os.path.exists('frame_data'): 
            os.makedirs('frame_data2') 
    
    # if not created then raise error 
    except OSError: 
        print ('Error: Creating directory of data') 
    
    # frame 
    currentframe = 0
    while(True): 
        
        # reading from frame 
        ret,frame = cam.read() 
    
        if ret: 
            # if video is still left continue creating images 
            name = './data/frame' + str(currentframe) + '.jpg'
            print ('Creating...' + name) 

            # writing the extracted images 
            cv2.imwrite(name, frame) 
    
            # increasing counter so that it will 
            # show how many frames are created 
            currentframe += 1
        else: 
            break
    
    # Release all space and windows once done 
    cam.release() 
    cv2.destroyAllWindows()