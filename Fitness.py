# This module is used to handle operations related to fitness of a chromosome
from PIL import Image
from numpy import array
from cryptography.fernet import Fernet
from Chromosome import Chromosome
from Population import Population
class Fitness:
	def __init__(self, solution):
		self.m_solution=solution
		self.i_currSolutionIndex=0
	def incrementSolutionIndex(self):
		self.i_currSolutionIndex+=1
	# This is used to get the present solution index
	def getSolution(self):
		return self.m_solution[self.i_currSolutionIndex]
	# This is used to calculate the fitness of the chromosome for a particular solution
	def calculateFitness(self,all): 
		desiredSolution=self.m_solution[self.i_currSolutionIndex]
		# Used to store the difference from the desired solution
		absDelta=[0,0,0]
		for i in range(len(all)):
			for j in range(3):
				absDelta[j]=abs(desiredSolution-all[i].getGene(j))
			all[i].setFitness(self.getMinimumArray(absDelta))
		return all
	# This function is used to return the minimum element in list
	def getMinimumArray(self,arr):
		m=arr[0]
		for i in range(len(arr)):
			if arr[i]<m:
				m=arr[i]
		return m




