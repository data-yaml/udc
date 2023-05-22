import os
from benchling import exceptions as benchling_exceptions
from benchling import models as benchling_models
from benchling import Benchling
from benchling.api import serialization_helpers
from benchling.auth import ClientCredentialsOAuth2

BENCHLING_TENANT = os.environ["BENCHLING_TENANT"]
BENCHLING_CLIENT_ID = os.environ["BENCHLING_CLIENT_ID"]
BENCHLING_CLIENT_SECRET_ARN = os.environ["BENCHLING_CLIENT_SECRET_ARN"]


benchling = Benchling(
    url=BENCHLING_TENANT,
    auth_method=ClientCredentialsOAuth2(
        client_id=BENCHLING_CLIENT_ID,
        client_secret=BENCHLING_CLIENT_SECRET_ARN,
        token_url=f"{BENCHLING_TENANT}/api/v2/token",
    ),
)


def handler(event, context):
    pass
    # result = benchling.entries.update_entry(
    #     event["detail"]["entry"]["id"],
    #     benchling_models.EntryUpdate(
    #         fields=serialization_helpers.fields(
    #             {"Quilt Catalog URL": {"value": "http://example.com"}}
    #         )
    #     ),
    # ).to_dict()
    # print(result)
