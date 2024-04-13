import os
import cv2
import face_recognition
import pickle

# Path to the dataset directory
dataset_path = "Path/To/The/trainig/Dataset"

# Initialize variables to store encodings and labels
known_encodings = []
known_labels = []

# Loop through each person's directory
for person_name in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person_name)
    if os.path.isdir(person_path):
        for image_name in os.listdir(person_path):
            image_path = os.path.join(person_path, image_name)
            image = cv2.imread(image_path)
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_image)

            if len(face_locations) == 1:  # Assuming one person per image
                face_encoding = face_recognition.face_encodings(rgb_image, face_locations)[0]
                known_encodings.append(face_encoding)
                known_labels.append(person_name)

# Save the encodings and labels to a pickle file
with open("encodings.pickle", "wb") as f:
    data = {"encodings": known_encodings, "labels": known_labels}
    f.write(pickle.dumps(data))
