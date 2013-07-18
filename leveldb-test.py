import leveldb
import time
db = leveldb.LevelDB('./db')
start = time.time()
for i in xrange(1000000):
    db.Put(str(i),str(time.time()))
finish = time.time()
print finish - start
