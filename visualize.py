import cv2
import os
import xml.etree.ElementTree as ET

# define paths
IMAGE_DIR = 'images'
ANNOTATION_DIR = 'annotations'

#loop through all XML files in the annotation directory
for filename in os.listdir(ANNOTATION_DIR):
    if filename.endswith('.xml'):
        #load the XML file
        xml_path = os.path.join(ANNOTATION_DIR, filename)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        #get the image filename and xml file
        image_filename = root.find('filename').text
        image_path = os.path.join(IMAGE_DIR, image_filename)
        image = cv2.imread(image_path)

        #parse the XML to get bounding boxes and labels
        for obj in root.findall('object'):
            label = obj.find('name').text
            bbox = obj.find('bndbox')
            xmin = int(bbox.find('xmin').text)
            ymin = int(bbox.find('ymin').text) 
            xmax = int(bbox.find('xmax').text)
            ymax = int(bbox.find('ymax').text)

            #draw rectangle and label on the image
            cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
            cv2.putText(image, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        #display the annotated image
        cv2.imshow('annotated image', image)
        key = cv2.waitKey(0) & 0xFF
        if key == ord('q'):
            break

cv2.destroyAllWindows()