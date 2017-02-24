# Michael Pszonka
# Assignment 1

import agent
from RavenProblem import RavenProblem, RavenObject
from SemanticNetwork import SemanticNetwork, Node

def main():

    matrixProblem = RavenProblem.createProblem("2x1BasicProblem01.txt")  #load matrix problem

    imageA = matrixProblem.test['A']  #shape in image a 
    imageB = matrixProblem.test['B']  #shape in image b
    imageC = matrixProblem.test['C']  #shape in image c 

    #based on A & B, the semantic representation of what our goal representation should be
    targetRepresentation = SemanticNetwork.createNetwork(imageA, imageB)

    agent.solve(targetRepresentation, imageC, matrixProblem.solutions)


if __name__ == '__main__':
    main()
