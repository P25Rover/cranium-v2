from dora import Node
import cv2

node = Node()

video_capture = cv2.VideoCapture(3)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

for event in node:
    if event["type"] == "INPUT":
        ret, frame = video_capture.read()
        if ret:
            frame = cv2.resize(frame, (320, 240))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

            node.send_output(
                "image",
                cv2.imencode(".jpg", frame)[1].tobytes(),
                event["metadata"]
            )
