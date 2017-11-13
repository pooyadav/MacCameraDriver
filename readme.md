# Accessing Macbook inbuild camera and streaming frame through python flask server

To run the server for streaming video frames:

python3 camserver.py 

To see the frame: Open in a browser: 
```http://localhost:5000/video_feed```
Everytime you refresh page it gets a frame.

To set the frames to capture, set camera parameters.

Frames per second

cap.set(1,frame_no);

