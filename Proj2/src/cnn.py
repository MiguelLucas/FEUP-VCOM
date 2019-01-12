from keras_retinanet.models import load_model
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import argparse
import os

IMAGE_TEST = '../testset/serralves/serralves-0174.jpg'
IMAGE_TEST_CONFLICT = '../testset/camara/camara-0222.jpg'

def parse_arguments():
    '''Checks for flags'''
    global IMAGE_TEST
    parser = argparse.ArgumentParser(description="Augment the map image")
    parser.add_argument('-it', '--imagetest', default=IMAGE_TEST, help='Path to the image to be augmented')
    args = parser.parse_args()
    IMAGE_TEST = args.imagetest


def main():

    parse_arguments()
    model = load_model('../models/inference_model_10.h5', backbone_name='resnet50')

    image = read_image_bgr(IMAGE_TEST)
    imagecopy = image.copy()
    imagecopy = cv2.cvtColor(imagecopy, cv2.COLOR_BGR2RGB)

    image = preprocess_image(image)
    image, scale = resize_image(image)
    boxes, scores, labels = model.predict_on_batch(np.expand_dims(image, axis=0))

    boxes /= scale
    visualize_detections(imagecopy, boxes, scores, labels)


def visualize_detections(draw, boxes, scores, labels):
    # load label to names mapping for visualization purposes
    labels_to_names = {0: 'arrabida', 1: 'camara', 2: 'clerigos', 3: 'musica', 4: 'serralves'}

    # visualize detections
    for box, score, label in zip(boxes[0], scores[0], labels[0]):
        if score < 0.5:
            break
            
        color = label_color(label)
        b = box.astype(int)
        draw_box(draw, b, color=color)
        caption = "{} {:.3f}".format(labels_to_names[label], score)
        draw_caption(draw, b, caption)
        
    plt.figure(figsize=(15, 15))
    plt.axis('off')
    plt.imshow(draw)
    plt.show()


if __name__ == '__main__':
    main()