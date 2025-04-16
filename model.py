from flask import Flask, render_template, request, redirect, url_for
import cv2

app = Flask(__name__)

# Function to detect faces using OpenCV
def detect_faces(image_path):
    # Load the pre-trained Haar Cascade face classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Return the list of detected faces
    return faces

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for attendance page
@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    if request.method == 'POST':
        # Capture image from webcam
        camera = cv2.VideoCapture(0)
        return_value, image = camera.read()
        cv2.imwrite('captured_image.jpg', image)
        camera.release()
        
        # Detect faces in the captured image
        faces = detect_faces('captured_image.jpg')
        
        if len(faces) > 0:
            # If face(s) detected, mark attendance
            # Insert your attendance marking logic here
            
            # For demonstration, assume attendance marking is successful
            return render_template('attendance.html', success=True)
        else:
            return render_template('attendance.html', success=False, error="No face detected!")
    
    return render_template('attendance.html', success=False)

if __name__ == '__main__':
    app.run(debug=True)
