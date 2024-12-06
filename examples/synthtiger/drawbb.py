import cv2
import os
import sys
from pathlib import Path

def read_bounding_boxes(file_path):
    bounding_boxes = {}
    work_dir = Path(input_file_path).parent
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            image_path = os.path.join(work_dir, parts[0])
            boxes = [tuple(map(int, box.split(','))) for box in parts[1:]]
            bounding_boxes[image_path] = boxes
    return bounding_boxes


def draw_bounding_boxes(bounding_boxes, output_dir):
    for image_path, boxes in bounding_boxes.items():
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Unable to open image {image_path}")
            return

        for box in boxes:
            left, top, right, bottom = box
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
    
        output_path = os.path.join(output_dir, os.path.basename(image_path))
        cv2.imwrite(output_path, image)
        print(f"Saved: {output_path}")

    
if __name__ == "__main__":
    args = sys.argv
    if(len(args) < 3):
        print("argument missing. annotation file path, and output directory path")
        exit()
    input_file_path = args[1]
    output_dir_path = args[2]
    bounding_boxes = read_bounding_boxes(input_file_path)
    draw_bounding_boxes(bounding_boxes, output_dir_path)
