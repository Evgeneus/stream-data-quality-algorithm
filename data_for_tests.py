observed_cases = [
    # inject wrong values in S0
    {
        'S0': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    {
        'S0': ['UW', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    {
        'S0': ['UW', 'UW', 'Wisc', 'MSR', 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    {
        'S0': ['UW', 'UW', 'UW', 'MSR', 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    {
        'S0': ['UW', 'UW', 'UW', 'UW', 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    {
        'S0': ['UW', 'UW', 'UW', 'UW', 'UW'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    # inject None
    {
        'S0': [None, 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    {
        'S0': ['Wisc', None, 'Wisc', 'MSR', 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    # inject 2 None
    {
        'S0': [None, None, 'Wisc', 'MSR', 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    {
        'S0': ['Wisc', None, None, 'MSR', 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    {
        'S0': ['Wisc', None, 'Wisc', None, 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    # inject 3 None
    {
        'S0': [None, None, None, 'MSR', 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    {
        'S0': ['Wisc', None, None, None, 'MSR'],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    {
        'S0': ['Wisc', None, 'Wisc', None, None],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    {
        'S0': ['Wisc', None, 'Wisc', 'MSR', 'MSR'],
        'S1': ['Wisc', None, 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', None, 'Wisc', 'MSR', 'MSR']
    },
    # inject 4 None
    {
        'S0': [None, None, None, None, None],
        'S1': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },
    {
        'S0': ['Wisc', None, 'Wisc', 'MSR', None],
        'S1': ['Wisc', None, 'Wisc', 'MSR', 'MSR'],
        'S2': ['Wisc', None, 'Wisc', 'MSR', 'MSR']
    },
    # others
    {
        'S0': ['Wisc', None, 'Wisc', 'MSR', 'MSR'],
        'S1': ['UW', None, 'Wisc', 'UW', 'MSR'],
        'S2': ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']
    },

    ]