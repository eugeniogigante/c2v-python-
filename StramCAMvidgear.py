# import required libraries
from vidgear.gears import WriteGear
from vidgear.gears import CamGear
import cv2

# Open your source
stream = cv2.VideoCapture(0)


# define required FFmpeg parameters for your writer
output_params = {"-vcodec":"libx264","-profile:v":"main","-preset:v":"veryfast","-g":60,"-keyint_min":60,"-sc_threshold":0,"-b:v":"2500k","-maxrate":"2500k","-bufsize":"2500k", "-f":"flv"}

#output_params = {"-fourcc": "MJPG", "-fps": 30}
# Define writer with defined parameters and address such as `rtp://127.0.0.1:1234`
writer = WriteGear(output_filename = 'rtp://127.0.0.1:1234', logging =True, **output_params)

# loop over
while True:

    # read frames from stream
    (grabbed, frame) = stream.read()

    # check for frame if Nonetype
    if not grabbed:
        break


    # {do something with the frame here}


    # write frame to writer
    writer.write(frame)

    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.release()

# safely close writer
writer.close()