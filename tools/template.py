from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_{service} import {client_types}
    from mypy_boto3_{service}.service_resource import {resource_types}
else:
    from beartype.vale import IsAttr, IsEqual
    from boto3.resources.base import ServiceResource
    from boto3.resources.collection import ResourceCollection
    from botocore.client import BaseClient
    from botocore.paginate import Paginator
    from botocore.waiter import Waiter

    from bearboto3 import Annotated

    {type_annotations}
