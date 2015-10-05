observed_cases = [
    # inject wrong values in S0
    # case 0
    {
        'S0': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    # case 1
    {
        'S0': ['UW', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    # case 2
    {
        'S0': ['UW', 'UW', 'Wisc', 'MSR', 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    # case 3
    {
        'S0': ['UW', 'UW', 'UW', 'MSR', 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    # case 4
    {
        'S0': ['UW', 'UW', 'UW', 'UW', 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    # case 5
    {
        'S0': ['UW', 'UW', 'UW', 'UW', 'UW'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    # inject None
    # case 6
    {
        'S0': [None, 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    # case 7
    {
        'S0': ['Wisc', None, 'Wisc', 'MSR', 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    # inject 2 None
    # case 8
    {
        'S0': [None, None, 'Wisc', 'MSR', 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    # case 9
    {
        'S0': ['Wisc', None, None, 'MSR', 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    # case 10
    {
        'S0': ['Wisc', None, 'Wisc', None, 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    # inject 3 None
    # case 11
    {
        'S0': [None, None, None, 'MSR', 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    # case 12
    {
        'S0': ['Wisc', None, None, None, 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    # case 13
    {
        'S0': ['Wisc', None, 'Wisc', None, None],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    # case 14
    {
        'S0': ['Wisc', None, 'Wisc', 'MSR', 'MSR'],
        'S1': ['Wisc', None, 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', None, 'Wisc', 'MSR', 'MSR']
    },
    # inject 4 None
    # case 15
    {
        'S0': [None, None, None, None, None],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    # case 16
    {
        'S0': ['Wisc', None, 'Wisc', 'MSR', None],
        'S1': ['Wisc', None, 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', None, 'Wisc', 'MSR', 'MSR']
    },
    # others
    # case 17
    {
        'S0': ['Wisc', None, 'Wisc', 'MSR', 'MSR'],
        'S1': ['UW', None, 'Wisc', 'UW', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    #case 18
    {
        'S0': ['Wisc', 'MSR', 'Wisc', 'Wisc', 'UCB'],
        'S1': ['MSR', 'MSR', None, 'Wisc', 'MSR'],
        'S2': ['Wisc', None, 'Wisc', 'BEA', 'MSR'],
    },
    #case 19
    {
        'S0': ['Wisc', 'MSR', 'Wisc', 'Wisc', 'UCB'],
        'S1': ['MSR', 'MSR', None, 'Wisc', 'MSR'],
        'S2': ['Wisc', None, 'Wisc', 'BEA', 'MSR'],
        'S7': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    #case 20
    {
        'S0': ['Wisc', 'MSR', 'Wisc', 'Wisc', 'UCB'],
        'S1': ['MSR', 'MSR', None, 'Wisc', 'MSR'],
        'S2': ['Wisc', None, 'Wisc', 'BEA', 'MSR'],
        'S4':['MSR', 'Wisc', 'Wisc', 'MSR', 'BEA'],
    },
    #case 21
    {
        'S0': ['Wisc', 'MSR', 'Wisc', 'Wisc', 'UCB'],
        'S1': ['MSR', 'MSR', None, 'Wisc', 'MSR'],
        'S4':['MSR', 'Wisc', 'Wisc', 'MSR', 'BEA'],
        'S7': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    #case 22
    {
        'S0': ['Wisc', 'MSR', 'Wisc', 'Wisc', 'UCB'],
        'S1': ['MSR', 'MSR', None, 'Wisc', 'MSR'],
        'S6': ['Wisc', 'Wisc', 'MSR', 'MSR', 'MSR'],
        'S7': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    #case 23
    {
        'S0': ['Wisc', 'MSR', 'Wisc', 'Wisc', 'UCB'],
        'S1': ['MSR', 'MSR', None, 'Wisc', 'MSR'],
        'S2': ['Wisc', None, 'Wisc', 'BEA', 'MSR'],
        'S4':['MSR', 'Wisc', 'Wisc', 'MSR', 'BEA'],
        'S5': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'Wisc'],
    },
    #case 24
    {
        'S0': ['Wisc', 'MSR', 'Wisc', 'Wisc', 'UCB'],
        'S1': ['MSR', 'MSR', None, 'Wisc', 'MSR'],
        'S2': ['Wisc', None, 'Wisc', 'BEA', 'MSR'],
        'S4':['MSR', 'Wisc', 'Wisc', 'MSR', 'BEA'],
        'S5': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'Wisc'],
        'S6': ['Wisc', 'Wisc', 'MSR', 'MSR', 'MSR'],
    },
    #case 25
    {
        'S0': ['Wisc', 'MSR', 'Wisc', 'Wisc', 'UCB'],
        'S1': ['MSR', 'MSR', None, 'Wisc', 'MSR'],
        'S2': ['Wisc', None, 'Wisc', 'BEA', 'MSR'],
        'S4':['MSR', 'Wisc', 'Wisc', 'MSR', 'BEA'],
        'S5': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'Wisc'],
        'S6': ['Wisc', 'Wisc', 'MSR', 'MSR', 'MSR'],
        'S7': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    #case 26
    {
        'S0': ['Wisc', 'MSR', 'Wisc', 'Wisc', 'UCB'],
        'S6': ['Wisc', 'Wisc', 'MSR', 'MSR', 'MSR'],
        'S7': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    }
    ]