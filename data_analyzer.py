import numpy as np
from data_service import sectors
from cleaner import clean_all_sectors

def analyze_sector(sector: np.ndarray, sector_number: int):
    min_temperature = np.nanmin(sector)
    max_temperature = np.nanmax(sector)
    mean_temperature = np.nanmean(sector)
    median_temperature = np.nanmedian(sector)
    temperature_range = max_temperature - min_temperature

    return [

        sector_number,
        min_temperature,
        max_temperature,
        mean_temperature,
        median_temperature,
        temperature_range
    ]

def process_data_sectors(all_sectors: np.ndarray) -> None:
    results = []
    sector_index = 0

    for row in all_sectors:
        for sector in row:
            results.append(analyze_sector(sector, sector_index))
            sector_index += 1

    np.savetxt(
        "results/sensors_analysis.csv",
        results,
        delimiter=",",
        fmt=["%d", "%.2f", "%.2f", "%.2f", "%2f", "%2f"],
        header="sector_index,min_temperature,max_temperature,mean_temperature,median_temperature,temperature_range",
        comments=""
    )

clean_all_sectors(sectors)
process_data_sectors(sectors)