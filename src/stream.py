
# https://gist.github.com/Mxhmovd/41e7690114e7ddad8bcd761a76272cc3?permalink_comment_id=4745619#gistcomment-4745619

import cv2
import pafy

video_url = input("Enter the YouTube video URL: ")
youtube = pafy.new(video_url)

best = youtube.getbest(preftype="mp4")
capture = cv2.VideoCapture(best.url)

while True:
    # Read the next frame from the video.
    ret, frame = capture.read()

    # Check if the frame is successfully read.
    if ret:
        # Display the frame.
        cv2.imshow("Video", frame)

        # Wait for 25 ms to display the next frame.
        cv2.waitKey(25)

    # If the frame is not successfully read, break out of the loop.
    else:
        break

# Release the VideoCapture object.
capture.release()

# Close all windows.
cv2.destroyAllWindows()
