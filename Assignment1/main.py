import agent
from RavenProblem import RavenProblem, RavenObject
from SemanticNetwork import SemanticNetwork, Node


matrixProblem = RavenProblem.createProblem("2x1BasicProblem01.txt")

imageA = matrixProblem.test['A']  #shape in image a 
imageB = matrixProblem.test['B']  #shape in image b
imageC = matrixProblem.test['C']  #shape in image c 

targetRepresentation = SemanticNetwork.createNetwork(imageA, imageB)  #based on A & B, the semantic representation of what our goal representation should be


agent.solve(targetRepresentation, imageC, matrixProblem.solutions)


