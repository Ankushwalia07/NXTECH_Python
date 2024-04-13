import cv2
import pickle
import pandas as pd
from datetime import datetime

# Load the encodings and labels from the pickle file
with open("encodings.pickle", "rb") as f:
    data = pickle.load(f)
    known_encodings = data["encodings"]
    known_labels = data["labels"]

# Load the Haarcascade classifier
face_cascade = cv2.CascadeClassifier("haarcascade_profileface.xml")

# Load the video capture
video_capture = cv2.VideoCapture(0)  # You can change to a video file if needed

# Initialize variables for attendance
attendance = {}

while True:
    ret, frame = video_capture.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face_roi = gray_frame[y:y + h, x:x + w]
        face_encoding = face_recognition.face_encodings(face_roi)

        if len(face_encoding) == 0:
            continue

        face_encoding = face_encoding[0]

        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            matched_indices = [i for i, match in enumerate(matches) if match]
            counts = {}
            for i in matched_indices:
                name = known_labels[i]
                counts[name] = counts.get(name, 0) + 1
            name = max(counts, key=counts.get)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

        # Mark attendance
        if name != "Unknown":
            now = datetime.now()
            date_string = now.strftime("%Y-%m-%d")
            if name not in attendance:
                attendance[name] = [date_string]
            else:
                if date_string not in attendance[name]:
                    attendance[name].append(date_string)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()

# Convert attendance dictionary to DataFrame and save to CSV
attendance_df = pd.DataFrame(attendance)
attendance_df.to_csv("attendance.csv", index=False)
