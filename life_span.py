import operator


def get_initial_value(observed, cef_measures):
    initial_values = []
    observed_keys = sorted(observed.keys())
    for s in observed_keys:
        if observed.get(s)[0] not in initial_values:
            initial_values.append(observed.get(s)[0])
    if None not in initial_values:
        initial_values.append(None)

    likelihood = {}
    for value in initial_values:
        p = 1
        for s in observed_keys:
            m = len(observed.get(s))
            observed_value = observed.get(s)[0]
            coverage = cef_measures.get(s)[0]
            exactness = cef_measures.get(s)[1]

            if observed_value == value:
                if value:
                    p *= exactness*coverage
                else:
                    p *= exactness
            elif observed_value != value and observed_value:
                p *= (1-exactness)/m
            else:
                p *= exactness*(1-coverage)

        likelihood.update({value: p})

    max_likelihood_value = max(likelihood.iteritems(), key=operator.itemgetter(1))[0]

    # print 't=0'
    # print 'value={}'.format(max_likelihood_value)
    # print likelihood
    # print '---------------------'

    return max_likelihood_value


def get_life_span(observed, cef_measures):
    life_span = []
    initial_value = get_initial_value(observed, cef_measures)
    life_span.append(initial_value)

    observation_len = len(observed.get("S0"))
    observed_keys = sorted(observed.keys())
    for tr in range(1, observation_len):
        values_likelihood = {}
        for s in observed_keys:
            m = len(observed.get(s))
            value = observed.get(s)[tr]

            if value in values_likelihood.keys():
                continue

            p = 1
            for s_i in observed_keys:
                observed_value = observed.get(s_i)[tr]
                coverage = cef_measures.get(s_i)[0]
                exactness = cef_measures.get(s_i)[1]
                freshness = cef_measures.get(s_i)[2]
                if observed_value == value:
                    if observed_value:
                        p *= exactness*coverage*freshness
                    else:
                        p *= exactness*freshness
                elif observed_value != value and observed_value:
                    p *= (1-exactness)/((observation_len-1)*m)
                else:
                    p *= exactness*(1-coverage)/(observation_len-1)
            values_likelihood.update({value: p})

        max_likelihood_value = max(values_likelihood.iteritems(), key=operator.itemgetter(1))[0]
        life_span.append(max_likelihood_value)

        # print 't={}'.format(tr)
        # print 'value={}'.format(max_likelihood_value)
        # print values_likelihood
        # print '---------------------'

    return life_span