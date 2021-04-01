import shutil
import os.path
import os

def clean_all_repositories(path):
    try:
        shutil.rmtree(path, ignore_errors=True)
    except Exception as e:
        print(e)