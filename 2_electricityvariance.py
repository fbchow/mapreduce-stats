'''Calculate the variance in electricity prices among the states.'''

from mrjob.job import MRJob

class MRElectricityVariance(MRJob):
	def mapper(self, _, line):
		element = line.split(',')

		yield ('key', element)



	#def reducer(self, key, values):


		# yield

if __name__ == '__main__':
	MRElectricityVariance.run()
