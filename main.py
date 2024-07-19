import json
from src.detection.detector import Detector

def load_cameras(config_path):
    with open(config_path, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    cameras = load_cameras("cameras.json")
    detector = Detector(cameras)
    detector.run()
