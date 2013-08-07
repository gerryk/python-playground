
import leveldb
import time

class Timer(object):
    def __init__(self):
        self.t = None

    def start(self):
        self.t = time.time()
        return self

    def finish(self):
        return time.time() - self.t if self.t != None else None

def do_raw(args, db):
    t1 = Timer().start()
    for i in xrange(args.iterations):
        db.Put(str(i), str(time.time()))
    print "Raw: %s" % t1.finish()

def do_batch(args, db):
    wb = leveldb.WriteBatch()
    t1 = Timer().start()
    for i in xrange(args.iterations):
        wb.Put(str(i), str(time.time()))
    print "Batch, create: %s" % t1.finish()
    t2 = Timer().start()
    db.Write(wb)
    print "Batch, write : %s" % t2.finish()

def do_sizes(args, db):
    wb = leveldb.WriteBatch()
    t1 = Timer().start()
    for i in xrange(args.iterations/args.scale):
        wb.Put(str(i), str(time.time())*args.scale)
    print "Sizes, create: %s" % t1.finish()
    t2 = Timer().start()
    db.Write(wb)
    print "Sizes, write : %s" % t2.finish()
    
def main():
    import argparse
    parser = argparse.ArgumentParser('levelDB performance tests')
    parser.add_argument('-d', '--db-path', default='./db', dest='dbpath', help='DB path')
    parser.add_argument('-i', '--iterations', default=1000000, help='Number of writes')
    subparsers = parser.add_subparsers()
    parser_raw = subparsers.add_parser('raw', help='Raw writes, small keys')
    parser_raw.set_defaults(func=do_raw)
    parser_batch = subparsers.add_parser('batch', help='Batched writes. small keys')
    parser_batch.set_defaults(func=do_batch)
    parser_sizes = subparsers.add_parser('sizes', help='Batched writes, large keys')
    parser_sizes.add_argument('-s', '--scale', type=int, default=1, help='Size multiplier')
    parser_sizes.set_defaults(func=do_sizes)
    args = parser.parse_args()
    db = leveldb.LevelDB(args.dbpath)
    args.func(args, db)

if __name__ == "__main__":
    main()
