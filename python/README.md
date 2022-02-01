<img src="https://techally-content.s3-us-west-1.amazonaws.com/public-content/lacework_logo_full.png" width="600">

# Lacework Python SDK

## Requirements

- Python 3.6 or higher
- Lacework API Credentials

## Org-Level Query

This example is used to show how to programatically run a Lacework query across all
accounts in a Lacework Organization. This will iterate through the accounts in which
the current user has access, and then run a defined LQL query sequentially in each
account.

[org-level-query.py](org-level-query.py)

The next logical step here is to aggregate the data returned from each query.
