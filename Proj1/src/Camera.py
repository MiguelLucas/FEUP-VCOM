import cv2
import Utils


def captureCamera():
    cap = cv2.VideoCapture(0)
    img = None
    while True:
        ret, frame = cap.read()
        cv2.imshow('Camera', frame)
        key = cv2.waitKey(1)

        if key == Utils.SPACE_KEY:
            img = frame
            break
        if key == Utils.ESC_KEY:
            break
    cap.release()
    cv2.destroyAllWindows()
    return img
