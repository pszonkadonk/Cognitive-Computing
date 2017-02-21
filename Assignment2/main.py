import processShapes  
import cv2
from RavenProblem import RavenProblem
import agent
from SemanticNetwork import SemanticNetwork

def main():

    tests = {}
    solutions = {}

    ravens_problem = RavenProblem(tests, solutions)


    #test figures
    imageA, ravens_problem.tests = processShapes.capture_shape("shapes/A.png", ravens_problem.test)
    imageB, ravens_problem.tests = processShapes.capture_shape("shapes/B.png", ravens_problem.test)
    imageC, ravens_problem.tests = processShapes.capture_shape("shapes/C.png", ravens_problem.test)

    #solution figures 
    image1, ravens_problem.solutions = processShapes.capture_shape("shapes/1.png", ravens_problem.solutions)
    image2, ravens_problem.solutions = processShapes.capture_shape("shapes/2.png", ravens_problem.solutions)
    image3, ravens_problem.solutions = processShapes.capture_shape("shapes/3.png", ravens_problem.solutions)
    image4, ravens_problem.solutions = processShapes.capture_shape("shapes/4.png", ravens_problem.solutions)
    image5, ravens_problem.solutions = processShapes.capture_shape("shapes/5.png", ravens_problem.solutions)
    image6, ravens_problem.solutions = processShapes.capture_shape("shapes/6.png", ravens_problem.solutions)


    target = SemanticNetwork.create_network(imageA, imageB)

    agent.solve(target, imageC, ravens_problem.solutions)



    
if __name__ == "__main__":
    main()

