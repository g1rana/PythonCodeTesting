import cv2
import os
import gzip

def generate_thumbnails(video_path, output_folder,intervals_seconds,encoding_type):
    #Open the vedio file
    vedio_capture = cv2.VideoCapture(video_path)
    if not vedio_capture.isOpened():
        raise ValueError(f"Error opening video file: {video_path}")
    #Create output folder if it doesn't exist
    os.makedirs(output_folder,exist_ok=True)

    #Get the frame per seconds(fps) of the video file
    fps = int(vedio_capture.get(cv2.CAP_PROP_FPS))

    print("FPS->",fps)

    #Calculate the number of frames to skip based on the desire interval
    frames_to_skip = fps*intervals_seconds
    #Initialize variables 
    frame_count = 0 
    thumbnail_count = 1

    while True:
        #read the next frame from the video
        ret,frame = vedio_capture.read()
        if not ret:
            #Break the loop if we reach the end of the video
            print("Failed....",ret,frame)
            break
        frame_count +=1
        if frame_count % frames_to_skip == 0:
            #Save the current frame as a thumbnail image
            print("Generating frame {thumbnail_count}")
            thumbnail_path = os.path.join(output_folder,f"thumbnail_{thumbnail_count}.{encoding_type}")
            cv2.imwrite(thumbnail_path,frame)
            thumbnail_count +=1
    
    vedio_capture.release() 

def compress_file(input,output):
    if not os.path.exists(input):
        raise FileNotFoundError("Input file not found")
    with open(input,'rb') as f_in:
        with gzip.open(output,'wb') as f_out:
            f_out.writelines(f_in)

def decompress_file(input_file,output_file):
    if not os.path.exists(input_file):
        raise FileNotFoundError("Input file not found.")
    
    if not input_file.endswith('.gz'):
        raise ValueError("Input file is not in gzip format")
    
    with gzip.GzipFile(input_file,'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            for line in f_in:
                f_out.write(line)


if __name__ == "__main__":
    video_file = "/Users/jeewanrana/Desktop/Screen Shot 2022-05-10 at 10.53.03 AM.png"
    output_folder = "/Users/jeewanrana/ThumbNaiils"
    intervals_seconds = 5
    try:
        generate_thumbnails(video_file,output_folder, intervals_seconds,"jpg")
        print(f"Generate thumbnails at location:{output_folder}")
    except Exception as e:
        print(f"An error occured:{e}")

    
        
        

