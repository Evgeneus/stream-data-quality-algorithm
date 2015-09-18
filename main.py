from cef_measure import get_CEF
from life_span import get_life_span

if __name__ == '__main__':
    ground_truth = ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']

    observed = {
        'S0': ['Wisc', 'UW', 'Wisc', 'MSR', 'MSR'],
        'S1': ['UW', 'UW', None, 'MSR', None],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    }
    # print observed

    #initialization of cef
    cef_measures = {}
    observed_keys = sorted(observed.keys())
    for s in observed_keys:
        # print s
        cef = [1, 0.5, 1]
        cef_measures.update({s: cef})

    iter_quantity = 0
    sources_number = len(observed_keys)
    life_span = get_life_span(observed=observed, cef_measures=cef_measures)
    print 'Initial life span: {}'.format(life_span)
    print "*********************"
    life_span_old = []

    cef_for_each_s_old = [cef for i in range(sources_number)]
    cef_delta_sum = [1, 1, 1]
    while max(cef_delta_sum) > 0.01*sources_number:
        cef_for_each_s = []
        for s in observed_keys:
            # print s
            cef = get_CEF(life_span, observed.get(s))
            cef_measures.update({s: cef})
            cef_for_each_s.append(cef)

        life_span_old = life_span
        life_span = get_life_span(observed=observed, cef_measures=cef_measures)
        iter_quantity += 1

        cef_delta_sum = [0, 0, 0]
        for old, new in zip(cef_for_each_s_old, cef_for_each_s):
            diff_for_s = [abs(x-y) for x, y in zip(old, new)]
            for i in range(len(cef_delta_sum)):
                cef_delta_sum[i] += diff_for_s[i]
        cef_for_each_s_old = cef_for_each_s

        # print 'cef_for_each_s_old: {}'.format(cef_for_each_s_old)
        print 'iter={}'.format(iter_quantity)
        print 'cef_delta_sum: {}'.format(cef_delta_sum)
        # print 'Results CEF:'
        for cef, s in zip(cef_for_each_s, observed_keys):
            print s, ': C={}, E={}, F={}'.format(cef[0], cef[1], cef[2])
        print "Object's life span: {}".format(life_span)
        print '---------------------'

    print 'iter_quantity={}'.format(iter_quantity)
