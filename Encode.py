import cv2
import face_recognition
import pickle
import os


class FaceEncoder:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.path_list = os.listdir(folder_path)
        self.img_list = []
        self.student_ids = []
        for path in self.path_list:
            self.img_list.append(cv2.imread(os.path.join(self.folder_path, path)))
            self.student_ids.append(os.path.splitext(path)[0])

    def find_encodings(self, images_list):
        encode_list = []
        print(images_list)
        for img in images_list:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encode_list.append(encode)

        return encode_list

    def save_encodings(self, file_path):
        encode_list_known = self.find_encodings(self.img_list)
        encode_list_known_with_ids = [encode_list_known, self.student_ids]
        file = open(file_path, 'wb')
        pickle.dump(encode_list_known_with_ids, file)
        file.close()


if __name__ == '__main__':
    folder_path = 'Images'
    file_path = 'EncodeFile.p'

    face_encoder = FaceEncoder(folder_path)
    face_encoder.save_encodings(file_path)
