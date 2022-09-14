import cv2 as cv

def get_image():
    camera = camera = cv.VideoCapture(0, cv.CAP_DSHOW)
    status, frame = camera.read()
    if status ==True:
        return frame
    camera.release()
    cv.destroyAllWindows()