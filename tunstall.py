'''
Given alphabet, distribution of the alphabet and n
return the n-bit tunstall code
'''
def tunstall(alphabet, dist, n):
    size = len(alphabet)
    iterations = (2 ** n - size) / (size - 1)
 
    t = []
    for i, s in enumerate(alphabet):
        t.append( [s, dist[i]] )
 
    for _ in range(iterations):
        d = max(t, key=lambda p:p[1])
        ind = t.index(d)
        seq, seqProb = d
         
        for i, s in enumerate(alphabet):
            t.append( [seq + s, seqProb * dist[i]] )
        del t[ind]
 
    for i, entry in enumerate(t):
        entry[1] = '{:03b}'.format(i)
     
    return t
 
 
if __name__ == '__main__':
    n = 10
    alphabet = ['a', 'b', 'c']
    prob = [0.7, 0.2, 0.1]
 
    print tunstall(alphabet, prob, n)