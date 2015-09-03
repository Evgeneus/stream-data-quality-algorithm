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

    max_likelihood = max(likelihood.iteritems(), key=operator.itemgetter(1))[0]
    return max_likelihood


def get_life_span(observed, cef_measures):
    initial_value = get_initial_value(observed, cef_measures)

    print initial_value
