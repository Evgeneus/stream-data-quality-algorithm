def get_CEF(O, S):
    """
    :param O:
    :param S:
    :return:
    cl(S,O): capturable
    c(S,O): captured
    ml(S,O): mis-capturable
    m(S,O): mis-captured
    covg: coverage
    exac: exactness
    fresh: freshness
    """
    cl = c = ml = m = 0
    N = len(O)
    for i in range(N-1):
        ml += 1
        # print i, 'mis-capturable'
        if O[i] != S[i]:
            cl += 1
            # print i, 'capturable'
            if O[i+1] == S[i+1]:
                c += 1
                # print i, 'captured'
        if O[i+1] != S[i+1]:
            m += 1
            # print i, 'mis-captured'

    ml += 1
    # print N-1, 'mis-capturable'
    if O[N-1] != S[N-1]:
        cl += 1
        # print N-1, 'capturable'

    exac = 1 - float(m)/ml
    c_delta = float(c)
    try:
        covg = float(c)/cl
    except ZeroDivisionError:
        covg = 0.00000000001
    try:
        fresh = c_delta/c       #freshness with delta>=1
    except ZeroDivisionError:
        fresh = 0.00000000001

    print '---------------------'
    print 'total capturable: {}'.format(cl)
    print 'total captured: {}'.format(c)
    print 'total mis-capturable: {}'.format(ml)
    print 'total mis-captured: {}'.format(m)
    print '---------------------'
    print 'Coverage: {}'.format(covg)
    print 'Exactness: {}'.format(exac)
    print 'Freshness (delta>=1): {}'.format(fresh)
    print '---------------------'

    return [covg, exac, fresh]
