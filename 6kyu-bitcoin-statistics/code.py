def get_min_avg_max (discard, list):
    # Discard
    if len(list) <= discard * 2 + 1:
        return (0,0,0)

    list = list[discard: -discard]

    print(list)

    avg = sum(list)/len(list)    

    return (min(list), avg, max(list))

