# AnimatedTexture creator


## Tests

### MKV H.265

    python convert_to_tres.py --input="C:\Users\Victor\Documents\dev\godot_video_to_animated_texture\tests\medias\big_buck_bunny_short_h265.mkv" --output_frames_path="C:\Users\Victor\Documents\dev\godot_video_to_animated_texture\tests\frames" --output_texture_path="C:\Users\Victor\Documents\dev\godot_video_to_animated_texture\tests\test_mkv_h265.tres" --fps=25 --image_format=".jpeg"

### MOV

    python convert_to_tres.py --input="C:\Users\Victor\Documents\dev\godot_video_to_animated_texture\tests\medias\big_buck_bunny_short.mov" --output_frames_path="C:\Users\Victor\Documents\dev\godot_video_to_animated_texture\tests\frames" --output_texture_path="C:\Users\Victor\Documents\dev\godot_video_to_animated_texture\tests\test_mov.tres" --fps=25 --image_format=".jpeg"

### MP4

    python convert_to_tres.py --input="C:\Users\Victor\Documents\dev\godot_video_to_animated_texture\tests\medias\big_buck_bunny_short.mp4" --output_frames_path="C:\Users\Victor\Documents\dev\godot_video_to_animated_texture\tests\frames" --output_texture_path="C:\Users\Victor\Documents\dev\godot_video_to_animated_texture\tests\test_mp4.tres" --fps=25 --image_format=".jpeg"

### MKV MPEG-4 

    python convert_to_tres.py --input="C:\Users\Victor\Documents\dev\godot_video_to_animated_texture\tests\medias\big_buck_bunny_short_MPEG-4.mkv" --output_frames_path="C:\Users\Victor\Documents\dev\godot_video_to_animated_texture\tests\frames" --output_texture_path="C:\Users\Victor\Documents\dev\godot_video_to_animated_texture\tests\test_mkv_mpeg4.tres" --fps=25 --image_format=".jpeg"

## TODO:

- [ ] Handle file selection (write selected folder/file to textedit, and use this value for the next steps)
    - [ ] Input
    - [ ] Output frames
    - [ ] Output texture
- [ ] Handle input text 
- [ ] Show progress
- [ ] Update log label based on what's happening
- [ ] Handle errors
- [X] Basic layout
- [X] Requires components
- [X] Connect buttons to callback methods