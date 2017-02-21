import os
import cv2
import RavenProblem

def capture_shape(file_name, figures):

    image = cv2.imread(file_name, 0)    

    # capture the edges of
    threshold = cv2.threshold(image,127,255,0)[1]
    im2,contours,hierarchy = cv2.findContours(threshold, 1, 2)
    num_contours = contours[0]
    epsilon = 0.01*cv2.arcLength(num_contours,True)
    approximation = cv2.approxPolyDP(num_contours, epsilon, True)  
    edges = len(approximation)

    # capture raven object information
    tag = os.path.basename(file_name).split(".")[0]
    shape = get_shape(edges)
    fill = is_filled(image)
    

    raven_object = RavenProblem.RavenObject(tag, shape, fill)
    figures[tag] = raven_object

    
    return raven_object, figures

def get_shape(edges):
      if(edges == 3):
        return "triangle"
      elif(edges == 4):
        return "square"
      elif(edges > 4):
        return "circle"
      else:
        return None

def is_filled(image):
    width, height = image.shape[0], image.shape[1]

    midPx = image[int(width/2), int(height/2)]

    if(midPx == 0):
        return True
    elif(midPx == 255):
        return False