# Face Detection & Attendance System using Flask and OpenCV

This is a simple **Face Detection & Attendance System** built using **Flask** and **OpenCV**. The application captures an image from the webcam, detects faces using OpenCV's Haar Cascade classifier, and marks attendance if a face is detected.

## 🚀 Features
- 📸 **Capture Image** from the webcam  
- 🧑‍💻 **Detect Faces** using OpenCV's Haar Cascade  
- ✅ **Mark Attendance** if a face is detected  
- 🌐 **Flask Web Interface**  

## 🛠️ Tech Stack
- **Python** 🐍  
- **Flask** 🌎  
- **OpenCV** 📷  
- **HTML/CSS** 🎨 (for rendering templates)  

## 📂 Project Structure
/project-directory │-- app.py # Main Flask Application │-- templates/ │ │-- index.html # Home Page │ │-- attendance.html # Attendance Page │-- static/ │ │-- captured_image.jpg # Stores the captured image │-- README.md # Project



## 🔧 Installation & Setup
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/yourusername/face-detection-attendance.git
   cd face-detection-attendance
2. **Install dependencies**
   ```bash
   pip install flask opencv-python
3.**Run the application**
   ```bash
   python app.py
