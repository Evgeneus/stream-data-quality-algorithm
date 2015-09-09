from cef_measure import get_CEF
from life_span import get_life_span

if __name__ == '__main__':
    ground_truth = ['Wisc', 'Wisc', 'Wisc', 'Wisc', 'MSR']
    observed = {
        'S0': [None, 'UW', None, 'Wisc', 'Wisc'],
        'S1': ['MSR', 'Wisc', 'MSR', None, 'MSR'],
        'S2': ['Wisc', None, 'Wisc', None, 'MSR']
    }

    cef_measures = {}
    for s in observed.keys():
        print s
        cef = get_CEF(ground_truth, observed.get(s))
        cef_measures.update({s: cef})

    get_life_span(observed=observed, cef_measures=cef_measures)
