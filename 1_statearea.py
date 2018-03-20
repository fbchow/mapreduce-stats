'''
Calculate the largest, smallest, and average (mean) area for a state.
'''


from mrjob.job import MRJob 

class MRStateAreaStats(MRJob):

	def mapper(self, _, line):
		entity = line.split(',')
		area = int(entity[3]) 
		#population = int(entity[3])
		yield('1', area)


	def reducer(self, key, values):
		value = list(values)
		avg = sum(value)/len(value)
		yield ('avg', avg)
		yield('min', min(value))
		yield('max', max(value))


if __name__ == '__main__':
	MRStateAreaStats.run()
