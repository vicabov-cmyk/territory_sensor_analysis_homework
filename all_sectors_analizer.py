import numpy as np

def find_sectors():
    data = np.loadtxt(
        "results/sensors_analysis.csv",
        delimiter=",",
        skiprows=1
    )

    sector_indexes = data[:, 0].astype(int)
    temperatures = data[:, 3]

    average_temperature = np.mean(temperatures)

    coldest = np.argsort(temperatures)[:10]

    warmest = np.argsort(temperatures)[-10:][::-1]

    closest = np.argsort(
        np.abs(temperatures - average_temperature)
    )[:30]

    print("Coldest:", sector_indexes[coldest])
    print("Warmest:", sector_indexes[warmest])
    print("Closest:", sector_indexes[closest])

    results = []

    for index in coldest:
        results.append([sector_indexes[index], "coldest"])

    for index in warmest:
        results.append([sector_indexes[index], "warmest"])

    for index in closest:
        results.append([sector_indexes[index], "closest"])

    np.savetxt(
        "results/all_sectors.csv",
        results,
        delimiter=",",
        fmt="%s",
        header="sector_index,category",
        comments=""
    )

find_sectors()