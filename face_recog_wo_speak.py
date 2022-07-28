from Features.FaceRecognition import FaceRecognitionWOSpeak
from Features.csv_writer import append_data

l1 = ['unknown','0']
try:
    l1= FaceRecognitionWOSpeak()
    print("l1: ", l1)
except Exception as e:
    print("Exception: ", e)
person = l1[0] 
confidence = l1[1] 
