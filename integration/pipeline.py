import dlt

from oakland_api import oakland_crimewatch

pipeline = dlt.pipeline(destination="duckdb", dataset_name="oakland crime")

info = pipeline.run(oakland_crimewatch())

print(info)
