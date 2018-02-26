from mrjob.job import MRJob 

class MRStatePopulationStats(MRJob):

	def mapper(key, _, value):

		yield


	def reducer(key, _, value):

		yield


if __name__ = '__main__':
	MRStatePopulationStats.run()




