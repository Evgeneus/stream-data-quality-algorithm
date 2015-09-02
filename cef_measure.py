def get_CEF(O, S):
    """
    :param O:
    :param S:
    :return:
    cl(S,O): capturable
    c(S,O): captured
    ml(S,O): mis-capturable
    m(S,O): mis-captured
    c_s: coverage
    e_s: exactness
    f_s: reshness
    """
    cl = c = ml = m = 0
    N = len(O)
    for i in range(N-1):
        ml += 1
        print i, 'mis-capturable'
        if O[i] != S[i]:
            cl += 1
            print i, 'capturable'
            if O[i+1] == S[i+1]:
                c += 1
                print i, 'captured'
        if O[i+1] != S[i+1]:
            m += 1
            print i, 'mis-captured'

    ml += 1
    print N-1, 'mis-capturable'
    if O[N-1] != S[N-1]:
        cl += 1
        print N-1, 'capturable'

    c_s = float(c)/cl
    e_s = 1 - float(m)/ml
    c_delta = c
    f_s = c_delta/c       #freshness with delta=1

    print '---------------------'
    print 'total capturable: {}'.format(cl)
    print 'total captured: {}'.format(c)
    print 'total mis-capturable: {}'.format(ml)
    print 'total mis-captured: {}'.format(m)
    print '---------------------'
    print 'Coverage: {}'.format(c_s)
    print 'Exactness: {}'.format(e_s)
    print 'Freshness: {}'.format(f_s)
    print '---------------------'

    return [c_s, e_s, f_s]

if __name__ == '__main__':
    ground_truth = ['Wisc', 'Wisc', 'Wisc', 'Wisc', 'MSR']
    observed = [None, 'UW', None, 'Wisc', 'Wisc']
    
    get_CEF(ground_truth, observed)
