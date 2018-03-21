
from mrjob.job import MRJob

class MRElectricityVariance(MRJob):

	def mapper (self,_,line):
		line = line.split(',')
		#state = line[0]
		area = float(line[3])
		yield 'key', (area, area*area, 1)

	def combiner (self, key, somevals):
		sum = 0
		count = 0
		sum_square = 0
		for val in somevals:
			sum += val[0]
			sum_square += val[1]
			count += val[2]
		yield 'key', (sum, sum_square, count)


	def reducer (self, key, values):
		sum = 0
		count = 0
		sum_square = 0
		for val in values:
			sum += val[0]
			sum_square += val[1]
			count += val[2]
		yield 'var', sum_square/count - sum*sum/(count*count)

if __name__ == '__main__':
	MRElectricityVariance.run()

