from mrjob.job import MRJob

class countColleges(MRJob):
    def mapper(self, _, line):
        line = line.split(',')
        pub_priv = line[2]
        yield "key", (pub_priv, 1)

    def combiner(self, keys, vals):
        num_colleges = 0
        num_pub = 0
        num_priv = 0
        for v in vals:
            num_colleges += v[1]
            if v[0] == '1':
                num_pub += 1
            if v[0] == '2':
                num_priv += 1
        yield "key", (num_colleges, num_pub, num_priv)

    def reducer(self, keys, values):
        total_num_colleges =0
        num_pub = 0
        num_priv = 0
        for v in values:
            total_num_colleges = v[0]
            num_pub = v[1]
            num_priv = v[2]
        yield "total_num_colleges", total_num_colleges
        yield "num_pub", num_pub
        yield "num_priv", num_priv

if __name__ == '__main__':
    countColleges.run()

