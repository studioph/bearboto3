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
        EC2ServiceResource,
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
        EC2ResourceMeta,
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
    from boto3.resources.base import ResourceMeta, ServiceResource
    from boto3.resources.collection import ResourceCollection
    from botocore.client import BaseClient
    from botocore.paginate import Paginator
    from botocore.waiter import Waiter

    from bearboto3 import Annotated

    BundleTaskCompleteWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    ConversionTaskCancelledWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    ConversionTaskCompletedWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    ConversionTaskDeletedWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    CustomerGatewayAvailableWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    DescribeAddressesAttributePaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeByoipCidrsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeCapacityReservationFleetsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeCapacityReservationsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeCarrierGatewaysPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeClassicLinkInstancesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeClientVpnAuthorizationRulesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeClientVpnConnectionsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeClientVpnEndpointsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeClientVpnRoutesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeClientVpnTargetNetworksPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeCoipPoolsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeDhcpOptionsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeEgressOnlyInternetGatewaysPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeExportImageTasksPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeFastSnapshotRestoresPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeFleetsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeFlowLogsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeFpgaImagesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeHostReservationOfferingsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeHostReservationsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeHostsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeIamInstanceProfileAssociationsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeImportImageTasksPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeImportSnapshotTasksPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeInstanceCreditSpecificationsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeInstanceEventWindowsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeInstancesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeInstanceStatusPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeInstanceTypeOfferingsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeInstanceTypesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeInternetGatewaysPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeIpv6PoolsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeLaunchTemplatesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeLaunchTemplateVersionsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeLocalGatewayRouteTablesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator = (
        Annotated[
            Paginator,
            IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]],
        ]
    )
    DescribeLocalGatewayRouteTableVpcAssociationsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeLocalGatewaysPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeLocalGatewayVirtualInterfaceGroupsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeLocalGatewayVirtualInterfacesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeManagedPrefixListsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeMovingAddressesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeNatGatewaysPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeNetworkAclsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeNetworkInsightsAnalysesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeNetworkInsightsPathsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeNetworkInterfacePermissionsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeNetworkInterfacesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribePrefixListsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribePrincipalIdFormatPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribePublicIpv4PoolsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeReplaceRootVolumeTasksPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeReservedInstancesModificationsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeReservedInstancesOfferingsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeRouteTablesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeScheduledInstanceAvailabilityPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeScheduledInstancesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeSecurityGroupRulesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeSecurityGroupsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeSnapshotsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeSpotFleetInstancesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeSpotFleetRequestsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeSpotInstanceRequestsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeSpotPriceHistoryPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeStaleSecurityGroupsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeStoreImageTasksPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeSubnetsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeTagsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeTrafficMirrorFiltersPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeTrafficMirrorSessionsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeTrafficMirrorTargetsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeTransitGatewayAttachmentsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeTransitGatewayConnectPeersPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeTransitGatewayConnectsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeTransitGatewayMulticastDomainsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeTransitGatewayPeeringAttachmentsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeTransitGatewayRouteTablesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeTransitGatewaysPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeTransitGatewayVpcAttachmentsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeTrunkInterfaceAssociationsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeVolumesModificationsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeVolumesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeVolumeStatusPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeVpcClassicLinkDnsSupportPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeVpcEndpointConnectionNotificationsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeVpcEndpointConnectionsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeVpcEndpointServiceConfigurationsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeVpcEndpointServicePermissionsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeVpcEndpointServicesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeVpcEndpointsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeVpcPeeringConnectionsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    DescribeVpcsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    EC2Client = Annotated[
        BaseClient, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2"]]]
    ]
    EC2ServiceResource = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.ServiceResource"]]],
    ]
    ExportTaskCancelledWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    ExportTaskCompletedWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    GetAssociatedIpv6PoolCidrsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    GetGroupsForCapacityReservationPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    GetInstanceTypesFromInstanceRequirementsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    GetManagedPrefixListAssociationsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    GetManagedPrefixListEntriesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    GetSpotPlacementScoresPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    GetTransitGatewayAttachmentPropagationsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    GetTransitGatewayMulticastDomainAssociationsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    GetTransitGatewayPrefixListReferencesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    GetTransitGatewayRouteTableAssociationsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    GetTransitGatewayRouteTablePropagationsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    GetVpnConnectionDeviceTypesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    ImageAvailableWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    ImageExistsWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    InstanceExistsWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    InstanceRunningWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    InstanceStatusOkWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    InstanceStoppedWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    InstanceTerminatedWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    KeyPairExistsWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    NatGatewayAvailableWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    NetworkInterfaceAvailableWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    PasswordDataAvailableWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    SearchLocalGatewayRoutesPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    SearchTransitGatewayMulticastGroupsPaginator = Annotated[
        Paginator, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator."]]]
    ]
    SecurityGroupExistsWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    SnapshotCompletedWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    SpotInstanceRequestFulfilledWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    SubnetAvailableWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    SystemStatusOkWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    VolumeAvailableWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    VolumeDeletedWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    VolumeInUseWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    VpcAvailableWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    VpcExistsWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    VpcPeeringConnectionDeletedWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    VpcPeeringConnectionExistsWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    VpnConnectionAvailableWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    VpnConnectionDeletedWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter."]]]
    ]
    ClassicAddress = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    DhcpOptions = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    EC2ResourceMeta = Annotated[
        ResourceMeta, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    Image = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    Instance = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    InstanceVolumesCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    InstanceVpcAddressesCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    InternetGateway = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    KeyPair = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    KeyPairInfo = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    NetworkAcl = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    NetworkInterface = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    NetworkInterfaceAssociation = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    PlacementGroup = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    PlacementGroupInstancesCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    Route = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    RouteTable = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    RouteTableAssociation = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    SecurityGroup = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    ServiceResourceClassicAddressesCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    ServiceResourceDhcpOptionsSetsCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    ServiceResourceImagesCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    ServiceResourceInstancesCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    ServiceResourceInternetGatewaysCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    ServiceResourceKeyPairsCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    ServiceResourceNetworkAclsCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    ServiceResourceNetworkInterfacesCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    ServiceResourcePlacementGroupsCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    ServiceResourceRouteTablesCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    ServiceResourceSecurityGroupsCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    ServiceResourceSnapshotsCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    ServiceResourceSubnetsCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    ServiceResourceVolumesCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    ServiceResourceVpcAddressesCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    ServiceResourceVpcPeeringConnectionsCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    ServiceResourceVpcsCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    Snapshot = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    Subnet = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    SubnetInstancesCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    SubnetNetworkInterfacesCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    Tag = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    Volume = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    VolumeSnapshotsCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    Vpc = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    VpcAcceptedVpcPeeringConnectionsCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    VpcAddress = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    VpcInstancesCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    VpcInternetGatewaysCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    VpcNetworkAclsCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    VpcNetworkInterfacesCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    VpcPeeringConnection = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    VpcRequestedVpcPeeringConnectionsCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    VpcRouteTablesCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    VpcSecurityGroupsCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
    VpcSubnetsCollection = Annotated[
        ResourceCollection, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2."]]]
    ]
