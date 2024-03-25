# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Managed Blockchain Query"
prefix = "managedblockchain-query"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchGetTokenBalance = Action("BatchGetTokenBalance")
GetAssetContract = Action("GetAssetContract")
GetTokenBalance = Action("GetTokenBalance")
GetTransaction = Action("GetTransaction")
ListAssetContracts = Action("ListAssetContracts")
ListFilteredTransactionEvents = Action("ListFilteredTransactionEvents")
ListTokenBalances = Action("ListTokenBalances")
ListTransactionEvents = Action("ListTransactionEvents")
ListTransactions = Action("ListTransactions")
