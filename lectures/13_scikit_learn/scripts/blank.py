from pylab import *

data = array([[1, 1], [1, 0], [0.4, 0.8], [2, 5], [2, 4], [2.2, 4.6]])
target = array([0, 0, 0, 1, 1, 1])
colors = array(["blue", "red"])

p_pred = array([1.75, 2])

print(norm(data - p_pred, axis=1))


def distance(p0, P1):
    M = (p0 - P1) ** 2
    return sqrt(sum(M, axis=1))


d = distance(p_pred, data)


idx = argsort(d)
s_targ = target[idx]
n = 3
s_targ = s_targ[:n]

vote = bincount(s_targ)
pred = argmax(vote)
