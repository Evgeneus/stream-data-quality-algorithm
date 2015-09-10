import operator


def get_initial_value(observed, cef_measures):
    initial_values = []
    for s in observed.keys():
        if observed.get(s)[0] not in initial_values:
            initial_values.append(observed.get(s)[0])
    if None not in initial_values:
        initial_values.append(None)

    likelihood = {}
    for v in initial_values:
        p = 1
        for s in observed.keys():
            m = len(observed.get(s))
            initial_v_for_s = observed.get(s)[0]
            coverage = cef_measures.get(s)[0]
            exactness = cef_measures.get(s)[1]

            if v == initial_v_for_s:
                if v:
                    p *= exactness*coverage
                else:
                    p *= exactness
            elif v != initial_v_for_s and initial_v_for_s:
                p *= (1-exactness)/m
            else:
                p *= exactness*(1-coverage)

        likelihood.update({v: p})

    max_likelihood_value = max(likelihood.iteritems(), key=operator.itemgetter(1))[0]

    print 't=0'
    print 'value={}'.format(max_likelihood_value)
    print likelihood
    print '---------------------'

    return max_likelihood_value


def get_life_span(observed, cef_measures):
    life_span = []
    initial_value = get_initial_value(observed, cef_measures)
    life_span.append(initial_value)

    observation_len = len(observed.get("S0"))
    for tr in range(1, observation_len):
        values_liklihood = {}
        for s in observed.keys():
            m = len(observed.get(s))
            value = observed.get(s)[tr]
            coverage = cef_measures.get(s)[0]
            exactness = cef_measures.get(s)[1]
            freshness = cef_measures.get(s)[2]
            p = exactness*coverage*freshness
            p_error = (1-exactness)/((observation_len-1)*m)
            if not value:
                p_miss_transiton = exactness*(1-coverage*freshness)
                if p_miss_transiton > p and p_miss_transiton > p_error:
                    continue

            if values_liklihood.get(value):
                new_values_p = values_liklihood.get(value)[0] * p
                new_values_p_error = values_liklihood.get(value)[1] * p_error
                values_liklihood.update({value: [new_values_p, new_values_p_error]})
            else:
                values_liklihood.update({value: [p, p_error]})

        max_likelihood_value = max(values_liklihood.iteritems(), key=operator.itemgetter(1))[0]
        life_span.append(max_likelihood_value)

        print 't={}'.format(tr)
        print 'value={}'.format(max_likelihood_value)
        print values_liklihood
        print '---------------------'

    print "Object's life span: {}".format(life_span)
    return life_span