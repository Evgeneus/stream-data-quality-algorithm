from cef_measure import get_CEF
from life_span import get_life_span

if __name__ == '__main__':
    ground_truth = ['Wisc', 'Wisc', 'Wisc', 'Wisc', 'MSR']
    observed = {
        'S0': [None, 'UW', None, 'Wisc', 'Wisc'],
        'S1': ['MSR', 'Wisc', 'MSR', None, 'MSR'],
        'S2': ['Wisc', None, 'Wisc', None, 'MSR']
    }

    #initialization of cef
    cef_measures = {}
    for s in observed.keys():
        print s
        cef = [0.5, 0.5, 0.5]
        cef_measures.update({s: cef})

    iter_quantity = 0
    life_span = get_life_span(observed=observed, cef_measures=cef_measures)
    life_span_old = []
    while life_span != life_span_old:
        for s in observed.keys():
            print s
            cef = get_CEF(life_span, observed.get(s))
            cef_measures.update({s: cef})
        life_span_old = life_span
        life_span = get_life_span(observed=observed, cef_measures=cef_measures)
        iter_quantity += 1
    print 'iter_quantity={}'.format(iter_quantity)
