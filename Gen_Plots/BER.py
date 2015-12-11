__author__ = 'edgar'

import pylab
import math

# Packet length
N = 1004;

# Eb/N0 argument that goes in erfc
ratio = [];
# Square root version of ratio; ratio preserved for graphing
sqrtratio = [];

# Hold packet error generated from equation
pe = [];

# Hold bit error
pb = [];

# Custom range function to allow a floating point step
def frange(start,stop,step):
    r = start;
    while r < stop:
        yield r;
        r += step;

# Fill Eb/N0
def dgen(start,end,dp,arry):
    size = abs(start-end);
    stp = float(size)/float(dp);
    for i in frange(start, end, stp):
        arry.append(start+i);

# Perform one-to-one mapping on each element in array specified by function provided.
def pf(func, arry):
    a = [];
    a[:] = [math.erfc(x) for x in arry];
    return a;


# Generate Eb/N0 data points
dgen(0,100,10000,ratio);

# Sqrt each ratio value
ratio[:] = [math.sqrt(x) for x in ratio];

# Calculate erfc
pe = pf(math.erfc, ratio);

# Calculate bit error rate
pb[:] = [0.5*x for x in pe];

# Multiply each element by n/2 to get packet error probability (n = packet length)
pe[:] = [float(N)/float(2)*x for x in pe];


# Log scale
pb[:] = [math.log(x,10) for x in pb];
pe[:] = [math.log(x,10) for x in pe];

# Set up graph visuals
pylab.title('Theoretical BERT & PERT comparison');
pylab.xlabel('sqrt(Eb/N0)');
pylab.ylabel('log(pe),log(pb)');

# Plot packet error probability
perplot, = pylab.plot(ratio, pb, 'g', label='PER');
berplot, = pylab.plot(ratio, pe, 'b', label='BER');

# Legeeeend
pylab.legend(handles=[perplot,berplot]);
pylab.show();