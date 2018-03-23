'''
obtain a random sample of 100 colleges in which:
    * each private college is equally likely to be sampled
    * each public college is equally likely to be sampled

    * sample is weighted so that in expectation there are 
    the same number of public and private colleges in the sample

'''
from random import random
from mrjob.job import MRJob

class MRStratifiedSample(MRJob):

    def mapper(self, _, line):
        line = line.split(',')
        college_name = line[0]
        pubpriv = line[2]
        x = random()
        if (pubpriv=='1'):
            if x < (500/num_public):
                yield "key", college_name
        if (pubpriv == '2'):
            if x < (500/num_private):
                yield "key", college_name
            
    def reducer(self, key, values):
        for val in values:
            yield "key", val

if __name__ == '__main__':
    MrStratifiedSample.run()
