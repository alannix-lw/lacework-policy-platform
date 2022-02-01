# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, timezone
from pprint import pprint

from laceworksdk import LaceworkClient


QUERY_TEXT = """LW_Custom_Host_CVE_2022_0185 {
    source {
        LW_HE_MACHINES
    }
    filter {
        OS = 'Amazon Linux'
        and OS_VERSION = '2'
        and to_double(substring(KERNEL_RELEASE, 1, 1)) = 5
        and to_double(substring(KERNEL_RELEASE, 3, 1)) >= 1
        and to_double(substring(KERNEL_RELEASE, 3, 1)) <= 4
        and to_double(substring(KERNEL_RELEASE, 5, 3)) < 172
    }
    return {
        MID,
        HOSTNAME,
        KERNEL,
        KERNEL_RELEASE,
        KERNEL_VERSION,
        OS,
        OS_VERSION,
        TAGS,
        TAGS:"eks:cluster-name"::String as CLUSTER_NAME,
        TAGS:"eks:nodegroup-name"::String as CLUSTER_NODE_GROUP,
        TAGS:Account::String as ACCOUNT,
        TAGS:Zone::String as ZONE,
        TAGS:InstanceId::String as INSTANCE
    }
}"""


def get_start_end_times(day_delta=1):
    current_time = datetime.now(timezone.utc)
    start_time = current_time - timedelta(days=day_delta)
    start_time = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    end_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    return start_time, end_time


if __name__ == "__main__":

    lw = LaceworkClient()

    lw.set_org_level_access(True)

    user_profile = lw.user_profile.get()
    user_profile_data = user_profile.get('data', {})[0]

    lw.set_org_level_access(False)

    start_time, end_time = get_start_end_times()

    if user_profile_data.get('orgAccount', False):

        for subaccount in user_profile_data.get('accounts', []):

            print(subaccount['accountName'])

            lw.set_subaccount(subaccount['accountName'])

            response = lw.queries.execute(
                query_text=QUERY_TEXT,
                arguments={
                    "StartTimeRange": start_time,
                    "EndTimeRange": end_time
                }
            )

            pprint(response["data"])
