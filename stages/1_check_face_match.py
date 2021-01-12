import face_recognition

def check_if_faces_match(face_1_encoding, face_2_encoding):
    # Compare the two face encodings with `compare_faces`!
    results = face_recognition.compare_faces([face_1_encoding], face_2_encoding)
    
    # You can pass an array of encodings as first param to `compare_faces` function above
    # in this case we just want to get the result of comparison of the first encoding
    if results[0] == True:
        print("They are the same person")
    else:
        print("They are not the same person")

picture_of_kylie = face_recognition.load_image_file("kylie.jpg")
# get the first face in the photo
kylie_face_encoding = face_recognition.face_encodings(picture_of_kylie)[0]

# kylie_face_encoding now contains a universal 'encoding' of Kylie's facial features that can be compared to any other picture of a face!

# load another picture of Kylie
picture_of_kylie_2 = face_recognition.load_image_file("kylie_2.jpg")
kylie_2_face_encoding = face_recognition.face_encodings(picture_of_kylie_2)[0]


# load a photo of Khloe
picture_of_khloe = face_recognition.load_image_file("khloe.jpg")
khloe_face_encoding = face_recognition.face_encodings(picture_of_khloe)[0]


check_if_faces_match(kylie_face_encoding, kylie_2_face_encoding)
check_if_faces_match(kylie_face_encoding, khloe_face_encoding)