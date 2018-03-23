
from mrjob.job import MRJob

class MrSimpleRandomSample(MRJob):
    '''
    randomly samples colleges (each with equal likelihood of selection)
    '''
    def mapper(self, _, line):
        line = line.split(',')
        college_name = line[0]
        








if __name__ == '__main__':
    MrSimpleRandomSample.run()
