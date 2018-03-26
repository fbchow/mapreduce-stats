
from random import random
from mrjob.job import MRJob

class MrSimpleRandomSample(MRJob):
    '''
    randomly sample 100 colleges (each with equal likelihood of selection)
    '''
    def mapper_init(self):
        # calculated from shell wc -l colleges.csv
        self.total_num_colleges = float(1303-1)
        self.num_samples = float(100)

    def mapper(self, _, line):
        line = line.split(',')
        college_name = line[0]
        pub_priv = line[2]

        # probability assigned to each observation
        prob = self.num_samples/self.total_num_colleges
        x = random()
        if x < prob:
            yield "key", (college_name, pub_priv)

if __name__ == '__main__':
    MrSimpleRandomSample.run()
