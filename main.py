import face_recognition
import os
from pathlib import Path
from shutil import copyfile

cwd = os.getcwd()
p = os.path.join(cwd, 'dataset' )

results_path = os.path.join(cwd, 'results')
encodings = {}


def process_file(filepath):
    img = face_recognition.load_image_file(filepath)
    fe = face_recognition.face_encodings(img)
    if fe:
        fe = fe[0]
    else: return
    action_taken = False
    curr_image_cluster_id = None
    for cluster_id, cluster_encodings in encodings.items():
        results = face_recognition.compare_faces(cluster_encodings, fe)
        print("results %s %s" % (results, cluster_id))
        if all(results):
            print("cluster_id %s" % cluster_id)
            curr_image_cluster_id = cluster_id
            encodings.get(cluster_id).append(fe)
            action_taken = True

    if not action_taken:
        curr_image_cluster_id = "cluster_%s" % (len(encodings.keys()) + 1)
        print("creating new cluster %s" % curr_image_cluster_id)
        encodings[curr_image_cluster_id] = [fe]
    curr_cluster = os.path.join(results_path, curr_image_cluster_id)
    curr_cluster_dir = Path(curr_cluster)
    curr_cluster_dir.mkdir(parents=True, exist_ok=True)
    copyfile(filepath, os.path.join(curr_cluster_dir, file))


curr = 0
for subdir, dirs, files in os.walk(p):
    total = len(files)
    for file in files:
        filepath = os.path.join(subdir, file)
        print("File: %s" % filepath)
        process_file(filepath)
        curr += 1
        print("file %s/%s - %s encodings" % (curr, total, len(encodings)))


print("There are %s diff people" % len(encodings.keys()))
