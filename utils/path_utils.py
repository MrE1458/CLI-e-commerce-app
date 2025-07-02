import os

def get_project_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_data_path(filename):
    return os.path.join(get_project_root(), "data", filename)