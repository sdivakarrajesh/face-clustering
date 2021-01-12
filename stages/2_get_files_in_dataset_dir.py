import os
cwd = os.getcwd()
p = os.path.join(cwd, 'dataset' )
results_path = os.path.join(cwd, 'results')
for subdir, dirs, files in os.walk(p):
    total = len(files)
    for file in files:
        filepath = os.path.join(subdir, file)
        print("File: %s" % filepath)