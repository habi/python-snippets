'''
tiny script to leave something running for a defined time
'''
import time

StartTime = time.time()
RunTime = 10  # seconds

print 'Starting at', time.strftime('%H:%M:%S', time.localtime(StartTime)), \
    'and running for', RunTime, 's.'
print 'We should thus finish around', \
    time.strftime('%H:%M:%S', time.localtime(StartTime + RunTime))
print 80 * '-'

Counter = 0
while time.time() < StartTime + RunTime:
    Counter += 1
    print 'Run', Counter, 'current time:', time.strftime('%H:%M:%S'), \
        'elapsed time:', round(time.time() - StartTime, 3)
    # Do something very important here. In this script we're just waiting a bit
    time.sleep(0.618)
print 80 * '-'

CurrentTime = time.time()

print 'We were supposed to be done at', \
    time.strftime('%H:%M:%S', time.localtime(StartTime + RunTime))
print 'We were finished at', time.strftime('%H:%M:%S',
                                            time.localtime(CurrentTime)), \
    'which is', round(StartTime + RunTime - CurrentTime, 3), 's off...'
