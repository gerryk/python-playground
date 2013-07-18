import sys
try:    
    # a=b/0
    l=[1,7]
    #print l[10]
    open('xxx')
except (ZeroDivisionError, IndexError):
    sys.stderr.write('divide by zero or index error')
    sys.exit(1)
except (IOError):
    sys.stderr.write('File i/o error')
    sys.exit(1)
