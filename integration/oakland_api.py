import os

import dlt
from dlt.sources.helpers.rest_client import RESTClient
from dlt.sources.helpers.rest_client.paginators import OffsetPaginator
from dotenv import load_dotenv

# Load the .env file to environment variables for the API token.
load_dotenv()

# Get 100 results at a time up to maximum_offset results.
client = RESTClient(
    base_url="https://data.oaklandca.gov",
    headers={"X-App-Token": os.environ["OAKLAND_APP_TOKEN"]},
    paginator=OffsetPaginator(
        limit=100,
        total_path=None,
        # NOTE: This will limit to the first 1,000 rows for testing. A much larger
        # setting should be used for the full data set.
        maximum_offset=1_000,
        offset_param = "$offset",
        limit_param = "$limit",
    ),
)

@dlt.resource
def oakland_crimewatch():
    for page in client.paginate("resource/ppgh-7dqv.json"):
        yield page
