import numpy as np
from data_service import sectors

def analyze_problems(sector):
    median = np.nanmedian(sector)

    nan_count = np.isnan(sector).sum()
    too_low_count = (sector < median - 10).sum()
    too_high_count = (sector > median + 10).sum()

    invalid_count = nan_count + too_low_count + too_high_count

    return nan_count, too_low_count, too_high_count, invalid_count

def analyze_all_sectors(all_sectors):
    results = []
    sector_index = 0

    for row in all_sectors:
        for sector in row:
            counts = analyze_problems(sector)
            results.append([sector_index, *counts])
            sector_index += 1

    np.savetxt(
        "results/sensors_problems.csv",
        results,
        delimiter=",",
        fmt="%d",
        header="sector_index,nan_count,too_low_count,too_high_count,invalid_count",
        comments=""
    )

analyze_all_sectors(sectors)