import xml.etree.ElementTree as ET
import csv
import os

ANNOTATIONS_RAW_DIR = '../dataset/annotations-raw/'
CSV_PATH = '../dataset/annotations/'
FOLDERS = ['arrabida', 'camara', 'clerigos', 'musica', 'serralves']


csv_data = open('../dataset/annotations/annotations.csv', 'w', newline='')
csvwriter = csv.writer(csv_data)

for folder in FOLDERS:
	path = ANNOTATIONS_RAW_DIR + folder
	csv_path = CSV_PATH + folder

	for filename in os.listdir(path):
		tree = ET.parse(path + '/' + filename)
		root = tree.getroot()

		annotation = []

		count = 0
		filename = root.find('filename').text
		filename_without_extension = filename.split('.')[0]
		folder = filename.split('-')[0]
		image_path = 'images/' + folder + '/' + filename

		object = root.find('object')
		bounding_box = object.find('bndbox')
		xmin = bounding_box.find('xmin').text
		xmax = bounding_box.find('xmax').text
		ymin = bounding_box.find('ymin').text
		ymax = bounding_box.find('ymax').text

		if "." in xmin or "." in xmax or "." in ymin or "." in ymax:
			continue

		annotation.append(image_path)
		annotation.append(xmin)
		annotation.append(ymin)
		annotation.append(xmax)
		annotation.append(ymax)
		annotation.append(folder)

		#csv_data = open(csv_path + '/' + filename_without_extension + '.csv', 'w')
		#csvwriter = csv.writer(csv_data)
		csvwriter.writerow(annotation)
		#csvwriter.writerow(annotation)
		#csv_data.close()




csv_data.close()