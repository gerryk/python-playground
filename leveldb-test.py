
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

def do_test(args, db):
    if args.batch:
        wb = leveldb.WriteBatch()
    else:
        wb = db
    t1 = Timer().start()
    for i in xrange(args.iterations):
        wb.Put(str(i), str(time.time())*args.size) # if not args.batch: wb == db
    if not args.batch:
        print "Sizes, write : %s" % t1.finish()
    else:
        print "Batch, create: %s" % t1.finish()
        t2 = Timer().start()
        db.Write(wb)
        print "Sizes, write : %s" % t2.finish()
    
def main():
    import argparse
    parser = argparse.ArgumentParser('levelDB performance tests')
    parser.add_argument('-d', '--db-path', default='./db', dest='dbpath', help='DB path')
    parser.add_argument('-i', '--iterations', type=int, default=1000000, help='Number of writes')
    parser.add_argument('-b', '--batch', action='store_true', help=
        "Use batch writes. May exhaust heap.")
    parser.add_argument('-s', '--size', type=int, default=1, help="Data size multipler")
    args = parser.parse_args()
    db = leveldb.LevelDB(args.dbpath)
    do_test(args, db)

if __name__ == "__main__":
    main()
