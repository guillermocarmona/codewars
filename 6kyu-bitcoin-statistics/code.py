def BtcStatistics (list, discard):
    # Discard
    if len(list) <= discard * 2 + 1:
        return {"err:": "You discard to many elements", "min": 0, "avg": 0, "max": 0}

    list = list[discard: -discard]

    print(list)

    avg = sum(list)/len(list)    

    return {"min": min(list), "avg": avg, "max": max(list)}



array1 = [800,1200,2100,4100,1300,700]
array2 = [1000,1500,4500,5000,5800,2000,1500]

print(BtcStatistics(array1, 2))
print(BtcStatistics(array2, 5))
