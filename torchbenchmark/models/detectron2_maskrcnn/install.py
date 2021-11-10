import os
import sys
from pathlib import Path
import subprocess

def setup_data_dir():
    current_dir = Path(os.path.dirname(os.path.realpath(__file__)))
    coco2017_data_dir = os.path.join(current_dir.parent.parent, "data", ".data", "coco2017-minimal")
    assert os.path.exists(coco2017_data_dir), "Couldn't find coco2017 minimal data dir, please run install.py again."
    data_dir = os.path.join(current_dir, ".data")
    os.makedirs(data_dir, exist_ok=True)
    subprocess.check_call(['ln', '-sf', coco2017_data_dir, data_dir])

def build_detectron2():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                           'git+https://github.com/facebookresearch/detectron2.git'])

def pip_install_requirements():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', '-r', 'requirements.txt'])

if __name__ == '__main__':
    setup_data_dir()
    pip_install_requirements()
    build_detectron2()