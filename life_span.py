import operator
from datetime import timedelta


def get_initial_value(observed, cef_measures):
    initial_values = []
    observed_keys = sorted(observed.keys())
    for s in observed_keys:
        value = observed.get(s)[1][0]
        if value not in initial_values:
            initial_values.append(value)

    likelihood = {}
    for value in initial_values:
        p = 1
        for s in observed_keys:
            m = len(observed.get(s)[1])
            observed_value = observed.get(s)[1][0]
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

    return max_likelihood_value


def get_life_span(observed, cef_measures):
    life_span = [[], []]
    initial_value = get_initial_value(observed, cef_measures)
    observation_len = len(observed.get("S0")[1])
    observed_keys = sorted(observed.keys())

    start_time = observed.get(observed_keys[0])[0][0]
    end_time = observed.get(observed_keys[0])[0][observation_len-1]
    life_span[0].append(start_time)
    life_span[1].append(initial_value)

    observation_time = observed.get(observed_keys[0])[0]
    current_time = start_time
    while current_time != end_time:
        current_time += timedelta(seconds=1)
        values_likelihood = {}
        values = []
        for s in observed_keys:
            break_flag = False
            for t_index, t in enumerate(observation_time):
                value = observed.get(s)[1][t_index]
                if t <= life_span[0][-1]:
                    continue
                elif value == life_span[1][-1]:
                    values.append(value)
                    break
                else:
                    if not break_flag:
                        values.append(value)
                        break_flag = True
                    elif value != values[-1]:
                        values.append(value)
                        break
            print values
        values = list(set(values))
        print values













    # for tr in range(1, observation_len):
    #     values_likelihood = {}
    #     for s in observed_keys:
    #         m = len(observed.get(s)[1])
    #         value = observed.get(s)[1][tr]
    #
    #         if value in values_likelihood.keys():
    #             continue
    #
    #         p = 1
    #         for s_i in observed_keys:
    #             observed_value = observed.get(s_i)[1][tr]
    #             coverage = cef_measures.get(s_i)[0]
    #             exactness = cef_measures.get(s_i)[1]
    #             freshness = cef_measures.get(s_i)[2]
    #             if observed_value == value:
    #                 if observed_value:
    #                     p *= exactness*coverage*freshness
    #                 else:
    #                     p *= exactness*freshness
    #             elif observed_value != value and observed_value:
    #                 p *= (1-exactness)/((observation_len-1)*m)
    #             else:
    #                 p *= exactness*(1-coverage)/(observation_len-1)
    #         values_likelihood.update({value: p})
    #
    #     max_likelihood_value = max(values_likelihood.iteritems(), key=operator.itemgetter(1))[0]
    #     life_span.append(max_likelihood_value)

    return life_span