import processShapes  
import cv2
from RavenProblem import RavenProblem
import agent
from SemanticNetwork import SemanticNetwork

def main():

    tests = {}
    solutions = {}

    #test figures
    imageA, tests = processShapes.capture_shape("shapes/A.png", tests)
    imageB, tests = processShapes.capture_shape("shapes/B.png", tests)
    imageC, tests = processShapes.capture_shape("shapes/C.png", tests)

    #solution figures 
    image1, solutions = processShapes.capture_shape("shapes/1.png", solutions)
    image2, solutions = processShapes.capture_shape("shapes/2.png", solutions)
    image3, solutions = processShapes.capture_shape("shapes/3.png", solutions)
    image4, solutions = processShapes.capture_shape("shapes/4.png", solutions)
    image5, solutions = processShapes.capture_shape("shapes/5.png", solutions)
    image6, solutions = processShapes.capture_shape("shapes/6.png", solutions)

    ravens_problem = RavenProblem(tests, solutions)

    target = SemanticNetwork.create_network(imageA, imageB)

    agent.solve(target, imageC, solutions)



    
if __name__ == "__main__":
    main()

