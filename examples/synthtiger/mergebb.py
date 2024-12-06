import os
import sys


def read_bounding_boxes(file_path):
    bounding_boxes = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            image_path = parts[0]
            boxes = [tuple(map(int, box.split(','))) for box in parts[1:]]
            bounding_boxes[image_path] = boxes
    return bounding_boxes

def merge_bounding_boxes(boxes):
    left = min(box[0] for box in boxes)
    top = min(box[1] for box in boxes)
    right = max(box[2] for box in boxes)
    bottom = max(box[3] for box in boxes)
    return left, top, right, bottom

def write_merged_bounding_boxes(output_file_path, bounding_boxes):
    with open(output_file_path, 'w') as file:
        for image_path, boxes in bounding_boxes.items():
            merged_box = merge_bounding_boxes(boxes)
            file.write(f"{image_path}\t{merged_box[0]},{merged_box[1]},{merged_box[2]},{merged_box[3]}\n")
    
if __name__ == "__main__":
    args = sys.argv
    if(len(args) < 3):
        print("argument missing. input file path, and output file path")
        exit()
    input_file_path = args[1]
    output_file_path = args[2]
    bounding_boxes = read_bounding_boxes(input_file_path)
    write_merged_bounding_boxes(output_file_path, bounding_boxes)
