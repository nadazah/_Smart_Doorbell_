import face_recognition
import cv2
import pickle
import json
import base64
from PIL import Image
import io

# Function to convert image to base64
def image_to_base64(image_path):
    with Image.open(image_path) as image:
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")  # You can change JPEG to PNG if necessary
        return base64.b64encode(buffered.getvalue()).decode()



# Load the known faces and embeddings
encodingsP = "/home/aymen/face_recognition/facial_recognition/encodings.pickle"
data = pickle.loads(open(encodingsP, "rb").read())

# DroidCam URL (replace with your DroidCam stream URL)
stream_url = 'http://192.168.137.192:4747/video'

# Connect to the DroidCam stream
vs = cv2.VideoCapture(stream_url)

# Capture a single image
ret, frame = vs.read()
if not ret:
    print(json.dumps({"error": "unable to capture an image from DroidCam"}))
    vs.release()
    cv2.destroyAllWindows()
    exit(1)

# Resize the image (optional, depending on the needed resolution)
frame = cv2.resize(frame, (500, 500))

# Detect the face boxes and perform prediction
boxes = face_recognition.face_locations(frame)
encodings = face_recognition.face_encodings(frame, boxes)
names = []
result=True

for encoding in encodings:
    matches = face_recognition.compare_faces(data["encodings"], encoding)
    name = "Unknown" if not matches else max(
        (data["names"][i] for i, match in enumerate(matches) if match),
        key=lambda n: data["names"].count(n)
    )
    names.append(name)
prediction_id="".join(names)
if prediction_id=="" or prediction_id=="Unknown":
    result=False
    prediction_id="Unknown"

# Save the frame as an image file
cv2.imwrite('/home/aymen/face_recognition/facial_recognition/captured_frame.jpg', frame)

# Construct the output as JSON
#output = {
#    "prediction": names,
#    "image_path": "/home/aymen/face_recognition/facial_recognition/captured_frame.jpg"
#}

# Example usage
image_path = "/home/aymen/face_recognition/facial_recognition/captured_frame.jpg"  # Replace with your image path
base64_string = image_to_base64(image_path)
with open(image_path, "rb") as image_file:
    # Read the file and encode it in Base64
    base64_string = base64.b64encode(image_file.read()).decode('utf-8')
output = {
    "id":prediction_id,
    "image": base64_string,
    "resultat":result
}

#print(base64_string)
print(json.dumps(output))

# Cleanup
vs.release()
cv2.destroyAllWindows()
