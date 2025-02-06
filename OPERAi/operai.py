import os
from ultralytics import YOLO
import cv2
import numpy as np
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
from datetime import datetime
import random

# Load YOLO model paths
script_dir = os.path.dirname(os.path.abspath(__file__))
weights_path = os.path.join(script_dir, "yolov3.weights")
config_path = os.path.join(script_dir, "yolov3.cfg")
names_path = os.path.join(script_dir, "coco.names")

# Load both models
model1 = YOLO(r"B:\nurbi\Downloads\Hackathon-new\Hackathon-new\.venv\best.pt")
model2 = YOLO(r"B:\nurbi\Downloads\Hackathon-new\Hackathon-new\.venv\yolo11x.pt")

# Load COCO class labels
# with open(names_path, "r") as f:
#     classes = [line.strip() for line in f.readlines()]

# Initialize the color map for class labels
color_map = {}

# Random color generator for classes
def random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

# Initialize the camera
cap = cv2.VideoCapture(1)  # Use 0 for the default camera
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Create the main GUI window (GUI Setup)
root = tk.Tk()
root.title("OPERAi")
root.state("zoomed")  # Maximize window based on the PC screen resolution


# Load and resize logo image
logo_path = r"B:\nurbi\Downloads\logo.png"
logo_image = Image.open(logo_path).resize((500, 200), Image.LANCZOS)
logo_tk = ImageTk.PhotoImage(logo_image)

# Label to display logo at the top center
logo_label = Label(root, image=logo_tk)
logo_label.place(relx=0.5, y=5, anchor='n')  # Center at the top

# Load and resize logo2 image
logo2_path = r"B:\nurbi\Downloads\logo2.png"
logo2_image = Image.open(logo2_path).resize((330, 50), Image.LANCZOS)
logo2_tk = ImageTk.PhotoImage(logo2_image)

# Label to display logo2 at the bottom center
logo2_label = Label(root, image=logo2_tk)
logo2_label.place(relx=0.5, y=740, anchor='n')  # Center at the bottom

# Create a frame for instruction
instruction_frame = tk.Frame(root, width=420, height=120)
instruction_frame.place(x=50, y=250)  # Adjust x and y as needed

# Add the instruction label inside the frame
instruction_label = tk.Label(
    instruction_frame,
    text="Press 'Start Detection' to begin object detection.\nClick 'Screenshot' to save a snapshot.",
    font=("Arial", 12),
    justify="center",
    bg='yellow', fg='black', disabledforeground='black'
)
instruction_label.pack(expand=True, fill='both')

# Title label for the camera feed
camera_title = tk.Label(root, text="Camera Input", font=("Arial", 16), bg='black', fg='white')
camera_title.place(x=860, y=220)  # Position it above the camera feed

# Label to show camera feed (left center) with black background
camera_label = Label(root)
camera_label.place(x=860, y=250)  # Adjust position as needed

# State variable to control detection status
is_detection_running = False

# Object detection function
def detect_objects():
    global is_detection_running
    if not is_detection_running:  # If detection is paused, don't proceed
        return

    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        return

    # Run predictions on the same frame with both models
    results1 = model1.predict(source=frame, save=False, verbose=False)
    results2 = model2.predict(source=frame, save=False, verbose=False)

    # Extract detections and draw them on the frame
    for results in [results1, results2]:
        for box in results[0].boxes:
            # Unpack box information
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
            confidence = box.conf[0]  # Confidence score
            class_id = int(box.cls[0])  # Class ID
            label = results[0].names[class_id]  # Class label

            # Assign a unique color to each class if it hasn't been assigned already
            if label not in color_map:
                color_map[label] = random_color()

            # Get the color for the current label
            color = color_map[label]

            # Draw the bounding box and label on the frame
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Convert the frame to RGB and display it in the GUI
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame_rgb)
    img_tk = ImageTk.PhotoImage(image=img)
    camera_label.imgtk = img_tk
    camera_label.configure(image=img_tk)
    camera_label.after(10, detect_objects)

    # Save the current frame to be accessible for screenshot
    camera_label.current_frame = frame_rgb

# Screenshot function
def screenshot():
    if hasattr(camera_label, 'current_frame'):
        img = Image.fromarray(camera_label.current_frame)

        # Create a timestamp for the filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Create the OPERAi_screenshot folder on the Desktop
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        screenshots_dir = os.path.join(desktop_path, "OPERAi_screenshot")
        os.makedirs(screenshots_dir, exist_ok=True)  # Create the directory if it doesn't exist

        # Create the final filename
        file_name = f"screenshot_{timestamp}.png"
        file_path = os.path.join(screenshots_dir, file_name)

        img.save(file_path)
        print(f"Screenshot saved to {file_path}")
    else:
        print("No frame available to save.")

# Start detection function
def start_detection():
    global is_detection_running
    is_detection_running = True
    detect_objects()  # Start detecting objects

# Pause detection function
def stop_detection():
    global is_detection_running
    is_detection_running = False  # Pause the detection
    camera_label.configure(image='')  # Optionally clear the image display

# Quit function
def quit_application():
    if cap:
        cap.release()
    cv2.destroyAllWindows()
    root.quit()

# Create Start, Stop, Screenshot, and Quit buttons with specified colors
start_button = tk.Button(root, text="Start Detection", command=start_detection, bg='green', fg='white')
start_button.place(x=650, y=200)  # Position on the left

stop_button = tk.Button(root, text="Stop Detection", command=stop_detection, bg='red', fg='white')
stop_button.place(x=750, y=200)  # Position below the Start button

screenshot_button = tk.Button(root, text="Screenshot", command=screenshot, bg='blue', fg='white')
screenshot_button.place(x=150, y=310)  # Position on the right

quit_button = tk.Button(root, text="Quit", command=quit_application, bg='black', fg='white')
quit_button.place(x=250, y=310)  # Position next to the Screenshot button

# Run the Tkinter main loop
root.mainloop()

# Cleanup after GUI is closed
if cap:
    cap.release()
cv2.destroyAllWindows()