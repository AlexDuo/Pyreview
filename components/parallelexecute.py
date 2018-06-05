
import time
def consumer(cname):
    print('%s is ready to consume sth.' % cname)
    while True:
        product = yield

        print('product %s was brought by %s' % (product, cname))

def producer(pname):
    c = consumer('BestBuy')
    c2 = consumer('NewEgg')
    c.__next__()
    c2.__next__()
    print('%s producer is going to produce iphones'%pname)
    for i in range(10):
        time.sleep(1)
        print('%s has produce two iphones, one is sending to c1, another is sending to c2'%pname)
        c.send(i)
        c2.send(i)


producer('Foxconn')
