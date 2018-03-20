'''
Calculate the largest, smallest, and average (mean) population for a state.
'''


from mrjob.job import MRJob 

class MRStatePopulationStats(MRJob):

	def mapper(self, _, line):
		entity = line.split(',')
		state = entity[2]
		#area = line[2]
		population = int(entity[4])
		yield('1', population)


	def reducer(self, key, value):
		value = list(value)
		avg = sum(value)/len(value)
		yield ('avg', avg)
		yield('min', min(value))
		yield('max', max(value))


if __name__ == '__main__':
	MRStatePopulationStats.run()
