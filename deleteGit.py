import shutil
import os.path
import os

def clean_all_repositories(path):
    try:
        shutil.rmtree(path, onerror=on_rm_error)
    except Exception as e:
        print(e)