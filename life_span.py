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
    observation_len = len(observed.get(observed.keys()[0])[1])
    observed_keys = sorted(observed.keys())

    start_time = observed.get(observed_keys[0])[0][0]
    end_time = observed.get(observed_keys[0])[0][observation_len-1]
    life_span[0].append(start_time)
    life_span[1].append(initial_value)

    potential_values = []
    for s in observed_keys:
        s_values = observed.get(s)[1]
        for value in s_values:
            if value not in potential_values:
                potential_values.append(value)

    observation_time = observed.get(observed_keys[0])[0]

    likelihood = {}
    for tr_index, tr in enumerate(observation_time[1:observation_len-1]):   # to do!!!
        tr_index += 1
        life_span_pre_val = life_span[1][-1]
        life_span_pre_time = life_span[0][-1]
        for v in potential_values:
            if v == life_span_pre_val:
                continue
            p = 1
            for s in observed_keys:
                coverage = cef_measures.get(s)[0]
                exactness = cef_measures.get(s)[1]
                freshness = cef_measures.get(s)[2]
                observed_values = observed.get(s)[1][tr_index+1:]
                for observed_val_index, observed_val in enumerate(observed_values):
                    if observed_val == observed.get(s)[1][tr_index]:
                        if observed_val_index == len(observed_values)-1:
                            time_delta = end_time - tr
                            try:
                                p *= exactness*(1-coverage*freshness.get(time_delta)/sum(freshness.values()))
                            except ZeroDivisionError:
                                p *= exactness
                        else:
                            continue
                    else:
                        s_values = observed.get(s)[1]
                        tu_1_index = tr_index+observed_val_index
                        while tu_1_index > 0:
                            val_tu_1 = s_values[tu_1_index]
                            prev_val = s_values[tu_1_index-1]
                            if val_tu_1 != prev_val:
                                tu_1 = observation_time[tu_1_index]
                                break
                            elif tu_1_index-1 == 0:
                                tu_1 = observation_time[0]
                                break
                            tu_1_index -= 1
                        tu = observation_time[tr_index+observed_val_index+1]
                        if observed_val == v:
                            delta_high = tu - tr
                            if tr > tu_1:
                                delta_low = timedelta(seconds=0)
                            else:
                                delta_low = tu_1 - tr
                            f = 0
                            time_delta = delta_low
                            while time_delta != delta_high+timedelta(seconds=1):
                                f += freshness.get(time_delta)
                                time_delta += timedelta(seconds=1)
                            try:
                                f_normalized = f/sum(freshness.values())
                            except ZeroDivisionError:
                                f_normalized = 0.
                            p *= exactness*coverage*f_normalized
                        else:
                            p *= (1-exactness)*float((tu-tu_1).seconds)\
                                 /(observation_len*(float((end_time-life_span_pre_time).seconds)))
                        break

            likelihood.update({p: [tr, v]})
    max_likelihood_value = likelihood.get(max(likelihood.keys()))
    life_span[0].append(max_likelihood_value[0])
    life_span[1].append(max_likelihood_value[1])

    return life_span