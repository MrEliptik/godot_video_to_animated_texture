import os
import argparse
from PIL import Image
import cv2 as cv

from frames_to_animatedTexture import framesToTres

# Limit imposed by AnimatedTexture in godot
MAX_FRAMES = 256

video_extension = ['.mp4', '.mov', '.webm', '.mkv', '.ogv']

def extractFromGIF(gif):
    frames = []

    # Break GIF into PNG frames.
    with Image.open(args.gif) as im:
        fps = 1 / (im.info['duration'] / 1000.)
        n_frames = im.n_frames

        for i in range(n_frames):
            im.seek(i)
            frames.append(im)

    return frames

def extractFromVideo(video):
    frames = []

    # Break video into frames
    try:
        videocap = cv.VideoCapture(video)
    except expression as identifier:
        print(identifier)
    
    success, frame = videocap.read()
    count = 0
    while success:
        frames.append(frame)

        if count == MAX_FRAMES: break 
        success, frame = videocap.read()
        count += 1

    return frames

def saveFramesToDisk(frames, path, name, image_format):
    for (i, frame) in enumerate(frames):
        cv.imwrite(os.path.join(path, name + '_{}{}'.format(i, image_format)), frame)

def convert(input, output_frames, output_texture, fps, image_format, msg_q=None, progress_q=None):
    name, ext = os.path.splitext(input)

    if ext in video_extension:
        if msg_q:
            msg_q.put('Extracting frames from video..')
        frames = extractFromVideo(input)
    else:
        if msg_q:
            msg_q.put('Extracting frames from GIF..')
        frames = extractFromGIF(input)

    if msg_q:
        msg_q.put('Saving frames to disk..')
    if progress_q:
        progress_q.put(30)
    saveFramesToDisk(frames, output_frames, 'frame', image_format)

    if msg_q:
        msg_q.put('Listing frames..')
    if progress_q:
        progress_q.put(70)
    frames_str = os.listdir(output_frames)
    frames_str = [f.lower() for f in frames_str if f.endswith('.jpeg')]
    sorted(frames_str)

    name, ext = os.path.splitext(input)
    if ext == "": output_texture = os.path.join(name, '.tres')
    if msg_q:
        msg_q.put('Constructing .tres file..')
    if progress_q:
        progress_q.put(90)
    framesToTres(frames_str, fps, output_texture)
    if progress_q:
        progress_q.put(100)
    if msg_q:
        msg_q.put('Finished!')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Convert GIF or videos into frames and then create '
                    'AnimatedTexture .tres')
    parser.add_argument('--input', type=str, required=True, help='path to input (video/gif)')
    parser.add_argument('--output_frames_path', type=str, required=True, help='path where the frames will be saved')
    parser.add_argument('--output_texture_path', type=str, required=True, help='name and path of the AnimatedTexture file generated')
    parser.add_argument('--fps', type=int, default=25, required=False, help='fps target of the AnimatedTexture')
    parser.add_argument('--image_format', choices=['.jpeg', '.jpg', '.png', '.bmp'], type=str, required=False, default='.jpeg', 
        help='frames image format [\'.jpeg\', \'.png\', \'.bmp\']')
    args = parser.parse_args()

    convert(args.input, args.output_frames_path, args.output_texture_path, args.fps, args.image_format)