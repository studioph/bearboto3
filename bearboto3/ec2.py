from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import (
        BundleTaskCompleteWaiter,
        ConversionTaskCancelledWaiter,
        ConversionTaskCompletedWaiter,
        ConversionTaskDeletedWaiter,
        CustomerGatewayAvailableWaiter,
        DescribeAddressesAttributePaginator,
        DescribeByoipCidrsPaginator,
        DescribeCapacityReservationFleetsPaginator,
        DescribeCapacityReservationsPaginator,
        DescribeCarrierGatewaysPaginator,
        DescribeClassicLinkInstancesPaginator,
        DescribeClientVpnAuthorizationRulesPaginator,
        DescribeClientVpnConnectionsPaginator,
        DescribeClientVpnEndpointsPaginator,
        DescribeClientVpnRoutesPaginator,
        DescribeClientVpnTargetNetworksPaginator,
        DescribeCoipPoolsPaginator,
        DescribeDhcpOptionsPaginator,
        DescribeEgressOnlyInternetGatewaysPaginator,
        DescribeExportImageTasksPaginator,
        DescribeFastSnapshotRestoresPaginator,
        DescribeFleetsPaginator,
        DescribeFlowLogsPaginator,
        DescribeFpgaImagesPaginator,
        DescribeHostReservationOfferingsPaginator,
        DescribeHostReservationsPaginator,
        DescribeHostsPaginator,
        DescribeIamInstanceProfileAssociationsPaginator,
        DescribeImportImageTasksPaginator,
        DescribeImportSnapshotTasksPaginator,
        DescribeInstanceCreditSpecificationsPaginator,
        DescribeInstanceEventWindowsPaginator,
        DescribeInstancesPaginator,
        DescribeInstanceStatusPaginator,
        DescribeInstanceTypeOfferingsPaginator,
        DescribeInstanceTypesPaginator,
        DescribeInternetGatewaysPaginator,
        DescribeIpv6PoolsPaginator,
        DescribeLaunchTemplatesPaginator,
        DescribeLaunchTemplateVersionsPaginator,
        DescribeLocalGatewayRouteTablesPaginator,
        DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator,
        DescribeLocalGatewayRouteTableVpcAssociationsPaginator,
        DescribeLocalGatewaysPaginator,
        DescribeLocalGatewayVirtualInterfaceGroupsPaginator,
        DescribeLocalGatewayVirtualInterfacesPaginator,
        DescribeManagedPrefixListsPaginator,
        DescribeMovingAddressesPaginator,
        DescribeNatGatewaysPaginator,
        DescribeNetworkAclsPaginator,
        DescribeNetworkInsightsAnalysesPaginator,
        DescribeNetworkInsightsPathsPaginator,
        DescribeNetworkInterfacePermissionsPaginator,
        DescribeNetworkInterfacesPaginator,
        DescribePrefixListsPaginator,
        DescribePrincipalIdFormatPaginator,
        DescribePublicIpv4PoolsPaginator,
        DescribeReplaceRootVolumeTasksPaginator,
        DescribeReservedInstancesModificationsPaginator,
        DescribeReservedInstancesOfferingsPaginator,
        DescribeRouteTablesPaginator,
        DescribeScheduledInstanceAvailabilityPaginator,
        DescribeScheduledInstancesPaginator,
        DescribeSecurityGroupRulesPaginator,
        DescribeSecurityGroupsPaginator,
        DescribeSnapshotsPaginator,
        DescribeSpotFleetInstancesPaginator,
        DescribeSpotFleetRequestsPaginator,
        DescribeSpotInstanceRequestsPaginator,
        DescribeSpotPriceHistoryPaginator,
        DescribeStaleSecurityGroupsPaginator,
        DescribeStoreImageTasksPaginator,
        DescribeSubnetsPaginator,
        DescribeTagsPaginator,
        DescribeTrafficMirrorFiltersPaginator,
        DescribeTrafficMirrorSessionsPaginator,
        DescribeTrafficMirrorTargetsPaginator,
        DescribeTransitGatewayAttachmentsPaginator,
        DescribeTransitGatewayConnectPeersPaginator,
        DescribeTransitGatewayConnectsPaginator,
        DescribeTransitGatewayMulticastDomainsPaginator,
        DescribeTransitGatewayPeeringAttachmentsPaginator,
        DescribeTransitGatewayRouteTablesPaginator,
        DescribeTransitGatewaysPaginator,
        DescribeTransitGatewayVpcAttachmentsPaginator,
        DescribeTrunkInterfaceAssociationsPaginator,
        DescribeVolumesModificationsPaginator,
        DescribeVolumesPaginator,
        DescribeVolumeStatusPaginator,
        DescribeVpcClassicLinkDnsSupportPaginator,
        DescribeVpcEndpointConnectionNotificationsPaginator,
        DescribeVpcEndpointConnectionsPaginator,
        DescribeVpcEndpointServiceConfigurationsPaginator,
        DescribeVpcEndpointServicePermissionsPaginator,
        DescribeVpcEndpointServicesPaginator,
        DescribeVpcEndpointsPaginator,
        DescribeVpcPeeringConnectionsPaginator,
        DescribeVpcsPaginator,
        EC2Client,
        ExportTaskCancelledWaiter,
        ExportTaskCompletedWaiter,
        GetAssociatedIpv6PoolCidrsPaginator,
        GetGroupsForCapacityReservationPaginator,
        GetInstanceTypesFromInstanceRequirementsPaginator,
        GetManagedPrefixListAssociationsPaginator,
        GetManagedPrefixListEntriesPaginator,
        GetSpotPlacementScoresPaginator,
        GetTransitGatewayAttachmentPropagationsPaginator,
        GetTransitGatewayMulticastDomainAssociationsPaginator,
        GetTransitGatewayPrefixListReferencesPaginator,
        GetTransitGatewayRouteTableAssociationsPaginator,
        GetTransitGatewayRouteTablePropagationsPaginator,
        GetVpnConnectionDeviceTypesPaginator,
        ImageAvailableWaiter,
        ImageExistsWaiter,
        InstanceExistsWaiter,
        InstanceRunningWaiter,
        InstanceStatusOkWaiter,
        InstanceStoppedWaiter,
        InstanceTerminatedWaiter,
        KeyPairExistsWaiter,
        NatGatewayAvailableWaiter,
        NetworkInterfaceAvailableWaiter,
        PasswordDataAvailableWaiter,
        SearchLocalGatewayRoutesPaginator,
        SearchTransitGatewayMulticastGroupsPaginator,
        SecurityGroupExistsWaiter,
        SnapshotCompletedWaiter,
        SpotInstanceRequestFulfilledWaiter,
        SubnetAvailableWaiter,
        SystemStatusOkWaiter,
        VolumeAvailableWaiter,
        VolumeDeletedWaiter,
        VolumeInUseWaiter,
        VpcAvailableWaiter,
        VpcExistsWaiter,
        VpcPeeringConnectionDeletedWaiter,
        VpcPeeringConnectionExistsWaiter,
        VpnConnectionAvailableWaiter,
        VpnConnectionDeletedWaiter,
    )
    from mypy_boto3_ec2.service_resource import (
        ClassicAddress,
        DhcpOptions,
        EC2ServiceResource,
        Image,
        Instance,
        InstanceVolumesCollection,
        InstanceVpcAddressesCollection,
        InternetGateway,
        KeyPair,
        KeyPairInfo,
        NetworkAcl,
        NetworkInterface,
        NetworkInterfaceAssociation,
        PlacementGroup,
        PlacementGroupInstancesCollection,
        Route,
        RouteTable,
        RouteTableAssociation,
        SecurityGroup,
        ServiceResourceClassicAddressesCollection,
        ServiceResourceDhcpOptionsSetsCollection,
        ServiceResourceImagesCollection,
        ServiceResourceInstancesCollection,
        ServiceResourceInternetGatewaysCollection,
        ServiceResourceKeyPairsCollection,
        ServiceResourceNetworkAclsCollection,
        ServiceResourceNetworkInterfacesCollection,
        ServiceResourcePlacementGroupsCollection,
        ServiceResourceRouteTablesCollection,
        ServiceResourceSecurityGroupsCollection,
        ServiceResourceSnapshotsCollection,
        ServiceResourceSubnetsCollection,
        ServiceResourceVolumesCollection,
        ServiceResourceVpcAddressesCollection,
        ServiceResourceVpcPeeringConnectionsCollection,
        ServiceResourceVpcsCollection,
        Snapshot,
        Subnet,
        SubnetInstancesCollection,
        SubnetNetworkInterfacesCollection,
        Tag,
        Volume,
        VolumeSnapshotsCollection,
        Vpc,
        VpcAcceptedVpcPeeringConnectionsCollection,
        VpcAddress,
        VpcInstancesCollection,
        VpcInternetGatewaysCollection,
        VpcNetworkAclsCollection,
        VpcNetworkInterfacesCollection,
        VpcPeeringConnection,
        VpcRequestedVpcPeeringConnectionsCollection,
        VpcRouteTablesCollection,
        VpcSecurityGroupsCollection,
        VpcSubnetsCollection,
    )
else:
    from beartype.vale import IsAttr, IsEqual
    from boto3.resources.base import ServiceResource
    from boto3.resources.collection import ResourceCollection
    from botocore.client import BaseClient
    from botocore.paginate import Paginator
    from botocore.waiter import Waiter

    from bearboto3 import Annotated

    EC2Client = Annotated[
        BaseClient, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2"]]]
    ]
    DescribeRouteTablesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeRouteTables"]],
        ],
    ]
    DescribeIamInstanceProfileAssociationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeIamInstanceProfileAssociations"],
            ],
        ],
    ]
    DescribeInstanceStatusPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeInstanceStatus"]],
        ],
    ]
    DescribeInstancesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeInstances"]]
        ],
    ]
    DescribeReservedInstancesOfferingsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeReservedInstancesOfferings"]
            ],
        ],
    ]
    DescribeReservedInstancesModificationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeReservedInstancesModifications"],
            ],
        ],
    ]
    DescribeSecurityGroupsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeSecurityGroups"]],
        ],
    ]
    DescribeSnapshotsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeSnapshots"]]
        ],
    ]
    DescribeSpotFleetInstancesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeSpotFleetInstances"]],
        ],
    ]
    DescribeSpotFleetRequestsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeSpotFleetRequests"]],
        ],
    ]
    DescribeSpotPriceHistoryPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeSpotPriceHistory"]],
        ],
    ]
    DescribeTagsPaginator = Annotated[
        Paginator,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeTags"]]],
    ]
    DescribeVolumeStatusPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeVolumeStatus"]],
        ],
    ]
    DescribeVolumesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeVolumes"]]
        ],
    ]
    DescribeNatGatewaysPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeNatGateways"]],
        ],
    ]
    DescribeNetworkInterfacesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeNetworkInterfaces"]],
        ],
    ]
    DescribeVpcEndpointsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeVpcEndpoints"]],
        ],
    ]
    DescribeVpcEndpointServicesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeVpcEndpointServices"]],
        ],
    ]
    DescribeVpcEndpointConnectionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeVpcEndpointConnections"]],
        ],
    ]
    DescribeByoipCidrsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeByoipCidrs"]]
        ],
    ]
    DescribeCapacityReservationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeCapacityReservations"]],
        ],
    ]
    DescribeClassicLinkInstancesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeClassicLinkInstances"]],
        ],
    ]
    DescribeClientVpnAuthorizationRulesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeClientVpnAuthorizationRules"]
            ],
        ],
    ]
    DescribeClientVpnConnectionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeClientVpnConnections"]],
        ],
    ]
    DescribeClientVpnEndpointsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeClientVpnEndpoints"]],
        ],
    ]
    DescribeClientVpnRoutesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeClientVpnRoutes"]],
        ],
    ]
    DescribeClientVpnTargetNetworksPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeClientVpnTargetNetworks"]
            ],
        ],
    ]
    DescribeEgressOnlyInternetGatewaysPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeEgressOnlyInternetGateways"]
            ],
        ],
    ]
    DescribeFleetsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeFleets"]]
        ],
    ]
    DescribeFlowLogsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeFlowLogs"]]
        ],
    ]
    DescribeFpgaImagesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeFpgaImages"]]
        ],
    ]
    DescribeHostReservationOfferingsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeHostReservationOfferings"]
            ],
        ],
    ]
    DescribeHostReservationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeHostReservations"]],
        ],
    ]
    DescribeHostsPaginator = Annotated[
        Paginator,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeHosts"]]],
    ]
    DescribeImportImageTasksPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeImportImageTasks"]],
        ],
    ]
    DescribeImportSnapshotTasksPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeImportSnapshotTasks"]],
        ],
    ]
    DescribeInstanceCreditSpecificationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeInstanceCreditSpecifications"],
            ],
        ],
    ]
    DescribeLaunchTemplateVersionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeLaunchTemplateVersions"]],
        ],
    ]
    DescribeLaunchTemplatesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeLaunchTemplates"]],
        ],
    ]
    DescribeMovingAddressesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeMovingAddresses"]],
        ],
    ]
    DescribeNetworkInterfacePermissionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeNetworkInterfacePermissions"]
            ],
        ],
    ]
    DescribePrefixListsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribePrefixLists"]],
        ],
    ]
    DescribePrincipalIdFormatPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribePrincipalIdFormat"]],
        ],
    ]
    DescribePublicIpv4PoolsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribePublicIpv4Pools"]],
        ],
    ]
    DescribeScheduledInstanceAvailabilityPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeScheduledInstanceAvailability"],
            ],
        ],
    ]
    DescribeScheduledInstancesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeScheduledInstances"]],
        ],
    ]
    DescribeStaleSecurityGroupsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeStaleSecurityGroups"]],
        ],
    ]
    DescribeTransitGatewayAttachmentsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeTransitGatewayAttachments"]
            ],
        ],
    ]
    DescribeTransitGatewayRouteTablesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeTransitGatewayRouteTables"]
            ],
        ],
    ]
    DescribeTransitGatewayVpcAttachmentsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeTransitGatewayVpcAttachments"],
            ],
        ],
    ]
    DescribeTransitGatewaysPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeTransitGateways"]],
        ],
    ]
    DescribeVolumesModificationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeVolumesModifications"]],
        ],
    ]
    DescribeVpcClassicLinkDnsSupportPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeVpcClassicLinkDnsSupport"]
            ],
        ],
    ]
    DescribeVpcEndpointConnectionNotificationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeVpcEndpointConnectionNotifications"],
            ],
        ],
    ]
    DescribeVpcEndpointServiceConfigurationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeVpcEndpointServiceConfigurations"],
            ],
        ],
    ]
    DescribeVpcEndpointServicePermissionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeVpcEndpointServicePermissions"],
            ],
        ],
    ]
    DescribeVpcPeeringConnectionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeVpcPeeringConnections"]],
        ],
    ]
    GetTransitGatewayAttachmentPropagationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.GetTransitGatewayAttachmentPropagations"],
            ],
        ],
    ]
    GetTransitGatewayRouteTableAssociationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.GetTransitGatewayRouteTableAssociations"],
            ],
        ],
    ]
    GetTransitGatewayRouteTablePropagationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.GetTransitGatewayRouteTablePropagations"],
            ],
        ],
    ]
    DescribeInternetGatewaysPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeInternetGateways"]],
        ],
    ]
    DescribeNetworkAclsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeNetworkAcls"]],
        ],
    ]
    DescribeVpcsPaginator = Annotated[
        Paginator,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeVpcs"]]],
    ]
    DescribeSpotInstanceRequestsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeSpotInstanceRequests"]],
        ],
    ]
    DescribeDhcpOptionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeDhcpOptions"]],
        ],
    ]
    DescribeSubnetsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeSubnets"]]
        ],
    ]
    DescribeTrafficMirrorFiltersPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeTrafficMirrorFilters"]],
        ],
    ]
    DescribeTrafficMirrorSessionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeTrafficMirrorSessions"]],
        ],
    ]
    DescribeTrafficMirrorTargetsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeTrafficMirrorTargets"]],
        ],
    ]
    DescribeExportImageTasksPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeExportImageTasks"]],
        ],
    ]
    DescribeFastSnapshotRestoresPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeFastSnapshotRestores"]],
        ],
    ]
    DescribeIpv6PoolsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeIpv6Pools"]]
        ],
    ]
    GetAssociatedIpv6PoolCidrsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.GetAssociatedIpv6PoolCidrs"]],
        ],
    ]
    DescribeCoipPoolsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeCoipPools"]]
        ],
    ]
    DescribeInstanceTypeOfferingsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeInstanceTypeOfferings"]],
        ],
    ]
    DescribeInstanceTypesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeInstanceTypes"]],
        ],
    ]
    DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual[
                    "EC2.Paginator.DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations"
                ],
            ],
        ],
    ]
    DescribeLocalGatewayRouteTableVpcAssociationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeLocalGatewayRouteTableVpcAssociations"],
            ],
        ],
    ]
    DescribeLocalGatewayRouteTablesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeLocalGatewayRouteTables"]
            ],
        ],
    ]
    DescribeLocalGatewayVirtualInterfaceGroupsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeLocalGatewayVirtualInterfaceGroups"],
            ],
        ],
    ]
    DescribeLocalGatewayVirtualInterfacesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeLocalGatewayVirtualInterfaces"],
            ],
        ],
    ]
    DescribeLocalGatewaysPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeLocalGateways"]],
        ],
    ]
    DescribeTransitGatewayMulticastDomainsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeTransitGatewayMulticastDomains"],
            ],
        ],
    ]
    DescribeTransitGatewayPeeringAttachmentsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeTransitGatewayPeeringAttachments"],
            ],
        ],
    ]
    GetTransitGatewayMulticastDomainAssociationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.GetTransitGatewayMulticastDomainAssociations"],
            ],
        ],
    ]
    SearchLocalGatewayRoutesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.SearchLocalGatewayRoutes"]],
        ],
    ]
    SearchTransitGatewayMulticastGroupsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.SearchTransitGatewayMulticastGroups"]
            ],
        ],
    ]
    DescribeManagedPrefixListsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeManagedPrefixLists"]],
        ],
    ]
    GetManagedPrefixListAssociationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.GetManagedPrefixListAssociations"]
            ],
        ],
    ]
    GetManagedPrefixListEntriesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.GetManagedPrefixListEntries"]],
        ],
    ]
    GetGroupsForCapacityReservationPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.GetGroupsForCapacityReservation"]
            ],
        ],
    ]
    DescribeCarrierGatewaysPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeCarrierGateways"]],
        ],
    ]
    GetTransitGatewayPrefixListReferencesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.GetTransitGatewayPrefixListReferences"],
            ],
        ],
    ]
    DescribeNetworkInsightsAnalysesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeNetworkInsightsAnalyses"]
            ],
        ],
    ]
    DescribeNetworkInsightsPathsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeNetworkInsightsPaths"]],
        ],
    ]
    DescribeTransitGatewayConnectPeersPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeTransitGatewayConnectPeers"]
            ],
        ],
    ]
    DescribeTransitGatewayConnectsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeTransitGatewayConnects"]],
        ],
    ]
    DescribeAddressesAttributePaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeAddressesAttribute"]],
        ],
    ]
    DescribeReplaceRootVolumeTasksPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeReplaceRootVolumeTasks"]],
        ],
    ]
    DescribeStoreImageTasksPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeStoreImageTasks"]],
        ],
    ]
    DescribeSecurityGroupRulesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeSecurityGroupRules"]],
        ],
    ]
    DescribeInstanceEventWindowsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeInstanceEventWindows"]],
        ],
    ]
    DescribeTrunkInterfaceAssociationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeTrunkInterfaceAssociations"]
            ],
        ],
    ]
    GetVpnConnectionDeviceTypesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.GetVpnConnectionDeviceTypes"]],
        ],
    ]
    DescribeCapacityReservationFleetsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeCapacityReservationFleets"]
            ],
        ],
    ]
    GetInstanceTypesFromInstanceRequirementsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.GetInstanceTypesFromInstanceRequirements"],
            ],
        ],
    ]
    GetSpotPlacementScoresPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.GetSpotPlacementScores"]],
        ],
    ]
    InstanceExistsWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.InstanceExists"]]],
    ]
    BundleTaskCompleteWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Waiter.BundleTaskComplete"]]
        ],
    ]
    ConversionTaskCancelledWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Waiter.ConversionTaskCancelled"]],
        ],
    ]
    ConversionTaskCompletedWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Waiter.ConversionTaskCompleted"]],
        ],
    ]
    ConversionTaskDeletedWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Waiter.ConversionTaskDeleted"]]
        ],
    ]
    CustomerGatewayAvailableWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Waiter.CustomerGatewayAvailable"]],
        ],
    ]
    ExportTaskCancelledWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Waiter.ExportTaskCancelled"]]
        ],
    ]
    ExportTaskCompletedWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Waiter.ExportTaskCompleted"]]
        ],
    ]
    ImageExistsWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.ImageExists"]]],
    ]
    ImageAvailableWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.ImageAvailable"]]],
    ]
    InstanceRunningWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.InstanceRunning"]]],
    ]
    InstanceStatusOkWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.InstanceStatusOk"]]],
    ]
    InstanceStoppedWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.InstanceStopped"]]],
    ]
    InstanceTerminatedWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Waiter.InstanceTerminated"]]
        ],
    ]
    KeyPairExistsWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.KeyPairExists"]]],
    ]
    NatGatewayAvailableWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Waiter.NatGatewayAvailable"]]
        ],
    ]
    NetworkInterfaceAvailableWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Waiter.NetworkInterfaceAvailable"]],
        ],
    ]
    PasswordDataAvailableWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Waiter.PasswordDataAvailable"]]
        ],
    ]
    SnapshotCompletedWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Waiter.SnapshotCompleted"]]
        ],
    ]
    SecurityGroupExistsWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Waiter.SecurityGroupExists"]]
        ],
    ]
    SpotInstanceRequestFulfilledWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Waiter.SpotInstanceRequestFulfilled"]],
        ],
    ]
    SubnetAvailableWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.SubnetAvailable"]]],
    ]
    SystemStatusOkWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.SystemStatusOk"]]],
    ]
    VolumeAvailableWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.VolumeAvailable"]]],
    ]
    VolumeDeletedWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.VolumeDeleted"]]],
    ]
    VolumeInUseWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.VolumeInUse"]]],
    ]
    VpcAvailableWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.VpcAvailable"]]],
    ]
    VpcExistsWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.VpcExists"]]]
    ]
    VpnConnectionAvailableWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Waiter.VpnConnectionAvailable"]],
        ],
    ]
    VpnConnectionDeletedWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Waiter.VpnConnectionDeleted"]]
        ],
    ]
    VpcPeeringConnectionExistsWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Waiter.VpcPeeringConnectionExists"]],
        ],
    ]
    VpcPeeringConnectionDeletedWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Waiter.VpcPeeringConnectionDeleted"]],
        ],
    ]
    EC2ServiceResource = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.ServiceResource"]]],
    ]
    ClassicAddress = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.ClassicAddress"]]],
    ]
    DhcpOptions = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.DhcpOptions"]]],
    ]
    Image = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.Image"]]]
    ]
    Instance = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.Instance"]]],
    ]
    InternetGateway = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.InternetGateway"]]],
    ]
    KeyPair = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.KeyPair"]]]
    ]
    KeyPairInfo = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.KeyPairInfo"]]],
    ]
    NetworkAcl = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.NetworkAcl"]]],
    ]
    NetworkInterface = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.NetworkInterface"]]],
    ]
    NetworkInterfaceAssociation = Annotated[
        ServiceResource,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.NetworkInterfaceAssociation"]]
        ],
    ]
    PlacementGroup = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.PlacementGroup"]]],
    ]
    Route = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.Route"]]]
    ]
    RouteTable = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.RouteTable"]]],
    ]
    RouteTableAssociation = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.RouteTableAssociation"]]],
    ]
    SecurityGroup = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.SecurityGroup"]]],
    ]
    Snapshot = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.Snapshot"]]],
    ]
    Subnet = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.Subnet"]]]
    ]
    Tag = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.Tag"]]]
    ]
    Volume = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.Volume"]]]
    ]
    Vpc = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.Vpc"]]]
    ]
    VpcPeeringConnection = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.VpcPeeringConnection"]]],
    ]
    VpcAddress = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.VpcAddress"]]],
    ]
    ServiceResourceClassicAddressesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.classic_addressesCollection"]]
        ],
    ]
    ServiceResourceDhcpOptionsSetsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.dhcp_options_setsCollection"]]
        ],
    ]
    ServiceResourceImagesCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.imagesCollection"]]],
    ]
    ServiceResourceInstancesCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.instancesCollection"]]],
    ]
    ServiceResourceInternetGatewaysCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.internet_gatewaysCollection"]]
        ],
    ]
    ServiceResourceKeyPairsCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.key_pairsCollection"]]],
    ]
    ServiceResourceNetworkAclsCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.network_aclsCollection"]]],
    ]
    ServiceResourceNetworkInterfacesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.network_interfacesCollection"]]
        ],
    ]
    ServiceResourcePlacementGroupsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.placement_groupsCollection"]]
        ],
    ]
    ServiceResourceRouteTablesCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.route_tablesCollection"]]],
    ]
    ServiceResourceSecurityGroupsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.security_groupsCollection"]]
        ],
    ]
    ServiceResourceSnapshotsCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.snapshotsCollection"]]],
    ]
    ServiceResourceSubnetsCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.subnetsCollection"]]],
    ]
    ServiceResourceVolumesCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.volumesCollection"]]],
    ]
    ServiceResourceVpcAddressesCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.vpc_addressesCollection"]]],
    ]
    ServiceResourceVpcPeeringConnectionsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["ec2.vpc_peering_connectionsCollection"]],
        ],
    ]
    ServiceResourceVpcsCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.vpcsCollection"]]],
    ]
    InstanceVolumesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.Instance.volumesCollection"]]
        ],
    ]
    InstanceVpcAddressesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["ec2.Instance.vpc_addressesCollection"]],
        ],
    ]
    PlacementGroupInstancesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["ec2.PlacementGroup.instancesCollection"]],
        ],
    ]
    SubnetInstancesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.Subnet.instancesCollection"]]
        ],
    ]
    SubnetNetworkInterfacesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["ec2.Subnet.network_interfacesCollection"]],
        ],
    ]
    VolumeSnapshotsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.Volume.snapshotsCollection"]]
        ],
    ]
    VpcAcceptedVpcPeeringConnectionsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["ec2.Vpc.accepted_vpc_peering_connectionsCollection"],
            ],
        ],
    ]
    VpcInstancesCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.Vpc.instancesCollection"]]],
    ]
    VpcInternetGatewaysCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["ec2.Vpc.internet_gatewaysCollection"]],
        ],
    ]
    VpcNetworkAclsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.Vpc.network_aclsCollection"]]
        ],
    ]
    VpcNetworkInterfacesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["ec2.Vpc.network_interfacesCollection"]],
        ],
    ]
    VpcRequestedVpcPeeringConnectionsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["ec2.Vpc.requested_vpc_peering_connectionsCollection"],
            ],
        ],
    ]
    VpcRouteTablesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.Vpc.route_tablesCollection"]]
        ],
    ]
    VpcSecurityGroupsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["ec2.Vpc.security_groupsCollection"]],
        ],
    ]
    VpcSubnetsCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.Vpc.subnetsCollection"]]],
    ]
