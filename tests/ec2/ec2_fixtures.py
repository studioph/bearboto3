import boto3
import pytest
from moto import mock_ec2
from tests.utils import random_str


@pytest.fixture
def ec2_client(aws_setup):
    with mock_ec2():
        yield boto3.client("ec2")


@pytest.fixture
def ec2_resource(aws_setup):
    with mock_ec2():
        yield boto3.resource("ec2")


# ============================
# WAITER
# ============================


@pytest.fixture
def gen_instance_exists_waiter(ec2_client):
    return ec2_client.get_waiter("instance_exists")


@pytest.fixture
def gen_bundle_task_complete_waiter(ec2_client):
    return ec2_client.get_waiter("bundle_task_complete")


@pytest.fixture
def gen_conversion_task_cancelled_waiter(ec2_client):
    return ec2_client.get_waiter("conversion_task_cancelled")


@pytest.fixture
def gen_conversion_task_completed_waiter(ec2_client):
    return ec2_client.get_waiter("conversion_task_completed")


@pytest.fixture
def gen_conversion_task_deleted_waiter(ec2_client):
    return ec2_client.get_waiter("conversion_task_deleted")


@pytest.fixture
def gen_customer_gateway_available_waiter(ec2_client):
    return ec2_client.get_waiter("customer_gateway_available")


@pytest.fixture
def gen_export_task_cancelled_waiter(ec2_client):
    return ec2_client.get_waiter("export_task_cancelled")


@pytest.fixture
def gen_export_task_completed_waiter(ec2_client):
    return ec2_client.get_waiter("export_task_completed")


@pytest.fixture
def gen_image_exists_waiter(ec2_client):
    return ec2_client.get_waiter("image_exists")


@pytest.fixture
def gen_image_available_waiter(ec2_client):
    return ec2_client.get_waiter("image_available")


@pytest.fixture
def gen_instance_running_waiter(ec2_client):
    return ec2_client.get_waiter("instance_running")


@pytest.fixture
def gen_instance_status_ok_waiter(ec2_client):
    return ec2_client.get_waiter("instance_status_ok")


@pytest.fixture
def gen_instance_stopped_waiter(ec2_client):
    return ec2_client.get_waiter("instance_stopped")


@pytest.fixture
def gen_instance_terminated_waiter(ec2_client):
    return ec2_client.get_waiter("instance_terminated")


@pytest.fixture
def gen_key_pair_exists_waiter(ec2_client):
    return ec2_client.get_waiter("key_pair_exists")


@pytest.fixture
def gen_nat_gateway_available_waiter(ec2_client):
    return ec2_client.get_waiter("nat_gateway_available")


@pytest.fixture
def gen_network_interface_available_waiter(ec2_client):
    return ec2_client.get_waiter("network_interface_available")


@pytest.fixture
def gen_password_data_available_waiter(ec2_client):
    return ec2_client.get_waiter("password_data_available")


@pytest.fixture
def gen_snapshot_completed_waiter(ec2_client):
    return ec2_client.get_waiter("snapshot_completed")


@pytest.fixture
def gen_security_group_exists_waiter(ec2_client):
    return ec2_client.get_waiter("security_group_exists")


@pytest.fixture
def gen_spot_instance_request_fulfilled_waiter(ec2_client):
    return ec2_client.get_waiter("spot_instance_request_fulfilled")


@pytest.fixture
def gen_subnet_available_waiter(ec2_client):
    return ec2_client.get_waiter("subnet_available")


@pytest.fixture
def gen_system_status_ok_waiter(ec2_client):
    return ec2_client.get_waiter("system_status_ok")


@pytest.fixture
def gen_volume_available_waiter(ec2_client):
    return ec2_client.get_waiter("volume_available")


@pytest.fixture
def gen_volume_deleted_waiter(ec2_client):
    return ec2_client.get_waiter("volume_deleted")


@pytest.fixture
def gen_volume_in_use_waiter(ec2_client):
    return ec2_client.get_waiter("volume_in_use")


@pytest.fixture
def gen_vpc_available_waiter(ec2_client):
    return ec2_client.get_waiter("vpc_available")


@pytest.fixture
def gen_vpc_exists_waiter(ec2_client):
    return ec2_client.get_waiter("vpc_exists")


@pytest.fixture
def gen_vpn_connection_available_waiter(ec2_client):
    return ec2_client.get_waiter("vpn_connection_available")


@pytest.fixture
def gen_vpn_connection_deleted_waiter(ec2_client):
    return ec2_client.get_waiter("vpn_connection_deleted")


@pytest.fixture
def gen_vpc_peering_connection_exists_waiter(ec2_client):
    return ec2_client.get_waiter("vpc_peering_connection_exists")


@pytest.fixture
def gen_vpc_peering_connection_deleted_waiter(ec2_client):
    return ec2_client.get_waiter("vpc_peering_connection_deleted")


# ============================
# PAGINATOR
# ============================


@pytest.fixture
def gen_describe_route_tables_paginator(ec2_client):
    return ec2_client.get_paginator("describe_route_tables")


@pytest.fixture
def gen_describe_iam_instance_profile_associations_paginator(ec2_client):
    return ec2_client.get_paginator("describe_iam_instance_profile_associations")


@pytest.fixture
def gen_describe_instance_status_paginator(ec2_client):
    return ec2_client.get_paginator("describe_instance_status")


@pytest.fixture
def gen_describe_instances_paginator(ec2_client):
    return ec2_client.get_paginator("describe_instances")


@pytest.fixture
def gen_describe_reserved_instances_offerings_paginator(ec2_client):
    return ec2_client.get_paginator("describe_reserved_instances_offerings")


@pytest.fixture
def gen_describe_reserved_instances_modifications_paginator(ec2_client):
    return ec2_client.get_paginator("describe_reserved_instances_modifications")


@pytest.fixture
def gen_describe_security_groups_paginator(ec2_client):
    return ec2_client.get_paginator("describe_security_groups")


@pytest.fixture
def gen_describe_snapshots_paginator(ec2_client):
    return ec2_client.get_paginator("describe_snapshots")


@pytest.fixture
def gen_describe_spot_fleet_instances_paginator(ec2_client):
    return ec2_client.get_paginator("describe_spot_fleet_instances")


@pytest.fixture
def gen_describe_spot_fleet_requests_paginator(ec2_client):
    return ec2_client.get_paginator("describe_spot_fleet_requests")


@pytest.fixture
def gen_describe_spot_price_history_paginator(ec2_client):
    return ec2_client.get_paginator("describe_spot_price_history")


@pytest.fixture
def gen_describe_tags_paginator(ec2_client):
    return ec2_client.get_paginator("describe_tags")


@pytest.fixture
def gen_describe_volume_status_paginator(ec2_client):
    return ec2_client.get_paginator("describe_volume_status")


@pytest.fixture
def gen_describe_volumes_paginator(ec2_client):
    return ec2_client.get_paginator("describe_volumes")


@pytest.fixture
def gen_describe_nat_gateways_paginator(ec2_client):
    return ec2_client.get_paginator("describe_nat_gateways")


@pytest.fixture
def gen_describe_network_interfaces_paginator(ec2_client):
    return ec2_client.get_paginator("describe_network_interfaces")


@pytest.fixture
def gen_describe_vpc_endpoints_paginator(ec2_client):
    return ec2_client.get_paginator("describe_vpc_endpoints")


@pytest.fixture
def gen_describe_vpc_endpoint_services_paginator(ec2_client):
    return ec2_client.get_paginator("describe_vpc_endpoint_services")


@pytest.fixture
def gen_describe_vpc_endpoint_connections_paginator(ec2_client):
    return ec2_client.get_paginator("describe_vpc_endpoint_connections")


@pytest.fixture
def gen_describe_byoip_cidrs_paginator(ec2_client):
    return ec2_client.get_paginator("describe_byoip_cidrs")


@pytest.fixture
def gen_describe_capacity_reservations_paginator(ec2_client):
    return ec2_client.get_paginator("describe_capacity_reservations")


@pytest.fixture
def gen_describe_classic_link_instances_paginator(ec2_client):
    return ec2_client.get_paginator("describe_classic_link_instances")


@pytest.fixture
def gen_describe_client_vpn_authorization_rules_paginator(ec2_client):
    return ec2_client.get_paginator("describe_client_vpn_authorization_rules")


@pytest.fixture
def gen_describe_client_vpn_connections_paginator(ec2_client):
    return ec2_client.get_paginator("describe_client_vpn_connections")


@pytest.fixture
def gen_describe_client_vpn_endpoints_paginator(ec2_client):
    return ec2_client.get_paginator("describe_client_vpn_endpoints")


@pytest.fixture
def gen_describe_client_vpn_routes_paginator(ec2_client):
    return ec2_client.get_paginator("describe_client_vpn_routes")


@pytest.fixture
def gen_describe_client_vpn_target_networks_paginator(ec2_client):
    return ec2_client.get_paginator("describe_client_vpn_target_networks")


@pytest.fixture
def gen_describe_egress_only_internet_gateways_paginator(ec2_client):
    return ec2_client.get_paginator("describe_egress_only_internet_gateways")


@pytest.fixture
def gen_describe_fleets_paginator(ec2_client):
    return ec2_client.get_paginator("describe_fleets")


@pytest.fixture
def gen_describe_flow_logs_paginator(ec2_client):
    return ec2_client.get_paginator("describe_flow_logs")


@pytest.fixture
def gen_describe_fpga_images_paginator(ec2_client):
    return ec2_client.get_paginator("describe_fpga_images")


@pytest.fixture
def gen_describe_host_reservation_offerings_paginator(ec2_client):
    return ec2_client.get_paginator("describe_host_reservation_offerings")


@pytest.fixture
def gen_describe_host_reservations_paginator(ec2_client):
    return ec2_client.get_paginator("describe_host_reservations")


@pytest.fixture
def gen_describe_hosts_paginator(ec2_client):
    return ec2_client.get_paginator("describe_hosts")


@pytest.fixture
def gen_describe_import_image_tasks_paginator(ec2_client):
    return ec2_client.get_paginator("describe_import_image_tasks")


@pytest.fixture
def gen_describe_import_snapshot_tasks_paginator(ec2_client):
    return ec2_client.get_paginator("describe_import_snapshot_tasks")


@pytest.fixture
def gen_describe_instance_credit_specifications_paginator(ec2_client):
    return ec2_client.get_paginator("describe_instance_credit_specifications")


@pytest.fixture
def gen_describe_launch_template_versions_paginator(ec2_client):
    return ec2_client.get_paginator("describe_launch_template_versions")


@pytest.fixture
def gen_describe_launch_templates_paginator(ec2_client):
    return ec2_client.get_paginator("describe_launch_templates")


@pytest.fixture
def gen_describe_moving_addresses_paginator(ec2_client):
    return ec2_client.get_paginator("describe_moving_addresses")


@pytest.fixture
def gen_describe_network_interface_permissions_paginator(ec2_client):
    return ec2_client.get_paginator("describe_network_interface_permissions")


@pytest.fixture
def gen_describe_prefix_lists_paginator(ec2_client):
    return ec2_client.get_paginator("describe_prefix_lists")


@pytest.fixture
def gen_describe_principal_id_format_paginator(ec2_client):
    return ec2_client.get_paginator("describe_principal_id_format")


@pytest.fixture
def gen_describe_public_ipv4_pools_paginator(ec2_client):
    return ec2_client.get_paginator("describe_public_ipv4_pools")


@pytest.fixture
def gen_describe_scheduled_instance_availability_paginator(ec2_client):
    return ec2_client.get_paginator("describe_scheduled_instance_availability")


@pytest.fixture
def gen_describe_scheduled_instances_paginator(ec2_client):
    return ec2_client.get_paginator("describe_scheduled_instances")


@pytest.fixture
def gen_describe_stale_security_groups_paginator(ec2_client):
    return ec2_client.get_paginator("describe_stale_security_groups")


@pytest.fixture
def gen_describe_transit_gateway_attachments_paginator(ec2_client):
    return ec2_client.get_paginator("describe_transit_gateway_attachments")


@pytest.fixture
def gen_describe_transit_gateway_route_tables_paginator(ec2_client):
    return ec2_client.get_paginator("describe_transit_gateway_route_tables")


@pytest.fixture
def gen_describe_transit_gateway_vpc_attachments_paginator(ec2_client):
    return ec2_client.get_paginator("describe_transit_gateway_vpc_attachments")


@pytest.fixture
def gen_describe_transit_gateways_paginator(ec2_client):
    return ec2_client.get_paginator("describe_transit_gateways")


@pytest.fixture
def gen_describe_volumes_modifications_paginator(ec2_client):
    return ec2_client.get_paginator("describe_volumes_modifications")


@pytest.fixture
def gen_describe_vpc_classic_link_dns_support_paginator(ec2_client):
    return ec2_client.get_paginator("describe_vpc_classic_link_dns_support")


@pytest.fixture
def gen_describe_vpc_endpoint_connection_notifications_paginator(ec2_client):
    return ec2_client.get_paginator("describe_vpc_endpoint_connection_notifications")


@pytest.fixture
def gen_describe_vpc_endpoint_service_configurations_paginator(ec2_client):
    return ec2_client.get_paginator("describe_vpc_endpoint_service_configurations")


@pytest.fixture
def gen_describe_vpc_endpoint_service_permissions_paginator(ec2_client):
    return ec2_client.get_paginator("describe_vpc_endpoint_service_permissions")


@pytest.fixture
def gen_describe_vpc_peering_connections_paginator(ec2_client):
    return ec2_client.get_paginator("describe_vpc_peering_connections")


@pytest.fixture
def gen_get_transit_gateway_attachment_propagations_paginator(ec2_client):
    return ec2_client.get_paginator("get_transit_gateway_attachment_propagations")


@pytest.fixture
def gen_get_transit_gateway_route_table_associations_paginator(ec2_client):
    return ec2_client.get_paginator("get_transit_gateway_route_table_associations")


@pytest.fixture
def gen_get_transit_gateway_route_table_propagations_paginator(ec2_client):
    return ec2_client.get_paginator("get_transit_gateway_route_table_propagations")


@pytest.fixture
def gen_describe_internet_gateways_paginator(ec2_client):
    return ec2_client.get_paginator("describe_internet_gateways")


@pytest.fixture
def gen_describe_network_acls_paginator(ec2_client):
    return ec2_client.get_paginator("describe_network_acls")


@pytest.fixture
def gen_describe_vpcs_paginator(ec2_client):
    return ec2_client.get_paginator("describe_vpcs")


@pytest.fixture
def gen_describe_spot_instance_requests_paginator(ec2_client):
    return ec2_client.get_paginator("describe_spot_instance_requests")


@pytest.fixture
def gen_describe_dhcp_options_paginator(ec2_client):
    return ec2_client.get_paginator("describe_dhcp_options")


@pytest.fixture
def gen_describe_subnets_paginator(ec2_client):
    return ec2_client.get_paginator("describe_subnets")


@pytest.fixture
def gen_describe_traffic_mirror_filters_paginator(ec2_client):
    return ec2_client.get_paginator("describe_traffic_mirror_filters")


@pytest.fixture
def gen_describe_traffic_mirror_sessions_paginator(ec2_client):
    return ec2_client.get_paginator("describe_traffic_mirror_sessions")


@pytest.fixture
def gen_describe_traffic_mirror_targets_paginator(ec2_client):
    return ec2_client.get_paginator("describe_traffic_mirror_targets")


@pytest.fixture
def gen_describe_export_image_tasks_paginator(ec2_client):
    return ec2_client.get_paginator("describe_export_image_tasks")


@pytest.fixture
def gen_describe_fast_snapshot_restores_paginator(ec2_client):
    return ec2_client.get_paginator("describe_fast_snapshot_restores")


@pytest.fixture
def gen_describe_ipv6_pools_paginator(ec2_client):
    return ec2_client.get_paginator("describe_ipv6_pools")


@pytest.fixture
def gen_get_associated_ipv6_pool_cidrs_paginator(ec2_client):
    return ec2_client.get_paginator("get_associated_ipv6_pool_cidrs")


@pytest.fixture
def gen_describe_coip_pools_paginator(ec2_client):
    return ec2_client.get_paginator("describe_coip_pools")


@pytest.fixture
def gen_describe_instance_type_offerings_paginator(ec2_client):
    return ec2_client.get_paginator("describe_instance_type_offerings")


@pytest.fixture
def gen_describe_instance_types_paginator(ec2_client):
    return ec2_client.get_paginator("describe_instance_types")


@pytest.fixture
def gen_describe_local_gateway_route_table_virtual_interface_group_associations_paginator(
    ec2_client,
):
    return ec2_client.get_paginator(
        "describe_local_gateway_route_table_virtual_interface_group_associations"
    )


@pytest.fixture
def gen_describe_local_gateway_route_table_vpc_associations_paginator(ec2_client):
    return ec2_client.get_paginator(
        "describe_local_gateway_route_table_vpc_associations"
    )


@pytest.fixture
def gen_describe_local_gateway_route_tables_paginator(ec2_client):
    return ec2_client.get_paginator("describe_local_gateway_route_tables")


@pytest.fixture
def gen_describe_local_gateway_virtual_interface_groups_paginator(ec2_client):
    return ec2_client.get_paginator("describe_local_gateway_virtual_interface_groups")


@pytest.fixture
def gen_describe_local_gateway_virtual_interfaces_paginator(ec2_client):
    return ec2_client.get_paginator("describe_local_gateway_virtual_interfaces")


@pytest.fixture
def gen_describe_local_gateways_paginator(ec2_client):
    return ec2_client.get_paginator("describe_local_gateways")


@pytest.fixture
def gen_describe_transit_gateway_multicast_domains_paginator(ec2_client):
    return ec2_client.get_paginator("describe_transit_gateway_multicast_domains")


@pytest.fixture
def gen_describe_transit_gateway_peering_attachments_paginator(ec2_client):
    return ec2_client.get_paginator("describe_transit_gateway_peering_attachments")


@pytest.fixture
def gen_get_transit_gateway_multicast_domain_associations_paginator(ec2_client):
    return ec2_client.get_paginator("get_transit_gateway_multicast_domain_associations")


@pytest.fixture
def gen_search_local_gateway_routes_paginator(ec2_client):
    return ec2_client.get_paginator("search_local_gateway_routes")


@pytest.fixture
def gen_search_transit_gateway_multicast_groups_paginator(ec2_client):
    return ec2_client.get_paginator("search_transit_gateway_multicast_groups")


@pytest.fixture
def gen_describe_managed_prefix_lists_paginator(ec2_client):
    return ec2_client.get_paginator("describe_managed_prefix_lists")


@pytest.fixture
def gen_get_managed_prefix_list_associations_paginator(ec2_client):
    return ec2_client.get_paginator("get_managed_prefix_list_associations")


@pytest.fixture
def gen_get_managed_prefix_list_entries_paginator(ec2_client):
    return ec2_client.get_paginator("get_managed_prefix_list_entries")


@pytest.fixture
def gen_get_groups_for_capacity_reservation_paginator(ec2_client):
    return ec2_client.get_paginator("get_groups_for_capacity_reservation")


@pytest.fixture
def gen_describe_carrier_gateways_paginator(ec2_client):
    return ec2_client.get_paginator("describe_carrier_gateways")


@pytest.fixture
def gen_get_transit_gateway_prefix_list_references_paginator(ec2_client):
    return ec2_client.get_paginator("get_transit_gateway_prefix_list_references")


@pytest.fixture
def gen_describe_network_insights_analyses_paginator(ec2_client):
    return ec2_client.get_paginator("describe_network_insights_analyses")


@pytest.fixture
def gen_describe_network_insights_paths_paginator(ec2_client):
    return ec2_client.get_paginator("describe_network_insights_paths")


@pytest.fixture
def gen_describe_transit_gateway_connect_peers_paginator(ec2_client):
    return ec2_client.get_paginator("describe_transit_gateway_connect_peers")


@pytest.fixture
def gen_describe_transit_gateway_connects_paginator(ec2_client):
    return ec2_client.get_paginator("describe_transit_gateway_connects")


@pytest.fixture
def gen_describe_addresses_attribute_paginator(ec2_client):
    return ec2_client.get_paginator("describe_addresses_attribute")


@pytest.fixture
def gen_describe_replace_root_volume_tasks_paginator(ec2_client):
    return ec2_client.get_paginator("describe_replace_root_volume_tasks")


@pytest.fixture
def gen_describe_store_image_tasks_paginator(ec2_client):
    return ec2_client.get_paginator("describe_store_image_tasks")


@pytest.fixture
def gen_describe_security_group_rules_paginator(ec2_client):
    return ec2_client.get_paginator("describe_security_group_rules")


@pytest.fixture
def gen_describe_instance_event_windows_paginator(ec2_client):
    return ec2_client.get_paginator("describe_instance_event_windows")


@pytest.fixture
def gen_describe_trunk_interface_associations_paginator(ec2_client):
    return ec2_client.get_paginator("describe_trunk_interface_associations")


@pytest.fixture
def gen_get_vpn_connection_device_types_paginator(ec2_client):
    return ec2_client.get_paginator("get_vpn_connection_device_types")


@pytest.fixture
def gen_describe_capacity_reservation_fleets_paginator(ec2_client):
    return ec2_client.get_paginator("describe_capacity_reservation_fleets")


@pytest.fixture
def gen_get_instance_types_from_instance_requirements_paginator(ec2_client):
    return ec2_client.get_paginator("get_instance_types_from_instance_requirements")


@pytest.fixture
def gen_get_spot_placement_scores_paginator(ec2_client):
    return ec2_client.get_paginator("get_spot_placement_scores")


# ============================
# RESOURCE
# ============================


@pytest.fixture
def gen_classic_address(ec2_resource):
    return ec2_resource.ClassicAddress(random_str())


@pytest.fixture
def gen_dhcp_options(ec2_resource):
    return ec2_resource.DhcpOptions(random_str())


@pytest.fixture
def gen_image(ec2_resource):
    return ec2_resource.Image(random_str())


@pytest.fixture
def gen_instance(ec2_resource):
    return ec2_resource.Instance(random_str())


@pytest.fixture
def gen_internet_gateway(ec2_resource):
    return ec2_resource.InternetGateway(random_str())


@pytest.fixture
def gen_key_pair(ec2_resource):
    return ec2_resource.KeyPair(random_str())


@pytest.fixture
def gen_key_pair_info(ec2_resource):
    return ec2_resource.KeyPairInfo(random_str())


@pytest.fixture
def gen_network_acl(ec2_resource):
    return ec2_resource.NetworkAcl(random_str())


@pytest.fixture
def gen_network_interface(ec2_resource):
    return ec2_resource.NetworkInterface(random_str())


@pytest.fixture
def gen_network_interface_association(ec2_resource):
    return ec2_resource.NetworkInterfaceAssociation(random_str())


@pytest.fixture
def gen_placement_group(ec2_resource):
    return ec2_resource.PlacementGroup(random_str())


@pytest.fixture
def gen_route(ec2_resource):
    return ec2_resource.Route(random_str())


@pytest.fixture
def gen_route_table(ec2_resource):
    return ec2_resource.RouteTable(random_str())


@pytest.fixture
def gen_route_table_association(ec2_resource):
    return ec2_resource.RouteTableAssociation(random_str())


@pytest.fixture
def gen_security_group(ec2_resource):
    return ec2_resource.SecurityGroup(random_str())


@pytest.fixture
def gen_snapshot(ec2_resource):
    return ec2_resource.Snapshot(random_str())


@pytest.fixture
def gen_subnet(ec2_resource):
    return ec2_resource.Subnet(random_str())


@pytest.fixture
def gen_tag(ec2_resource):
    return ec2_resource.Tag(random_str())


@pytest.fixture
def gen_volume(ec2_resource):
    return ec2_resource.Volume(random_str())


@pytest.fixture
def gen_vpc(ec2_resource):
    return ec2_resource.Vpc(random_str())


@pytest.fixture
def gen_vpc_peering_connection(ec2_resource):
    return ec2_resource.VpcPeeringConnection(random_str())


@pytest.fixture
def gen_vpc_address(ec2_resource):
    return ec2_resource.VpcAddress(random_str())


# ============================
# COLLECTIONS
# ============================


@pytest.fixture
def gen_(ec2_resource):
    return ec2_resource.classic_addresses.all()


@pytest.fixture
def gen_(ec2_resource):
    return ec2_resource.dhcp_options_sets.all()


@pytest.fixture
def gen_(ec2_resource):
    return ec2_resource.images.all()


@pytest.fixture
def gen_(ec2_resource):
    return ec2_resource.instances.all()


@pytest.fixture
def gen_(ec2_resource):
    return ec2_resource.internet_gateways.all()


@pytest.fixture
def gen_(ec2_resource):
    return ec2_resource.key_pairs.all()


@pytest.fixture
def gen_(ec2_resource):
    return ec2_resource.network_acls.all()


@pytest.fixture
def gen_(ec2_resource):
    return ec2_resource.network_interfaces.all()


@pytest.fixture
def gen_(ec2_resource):
    return ec2_resource.placement_groups.all()


@pytest.fixture
def gen_(ec2_resource):
    return ec2_resource.route_tables.all()


@pytest.fixture
def gen_(ec2_resource):
    return ec2_resource.security_groups.all()


@pytest.fixture
def gen_(ec2_resource):
    return ec2_resource.snapshots.all()


@pytest.fixture
def gen_(ec2_resource):
    return ec2_resource.subnets.all()


@pytest.fixture
def gen_(ec2_resource):
    return ec2_resource.volumes.all()


@pytest.fixture
def gen_(ec2_resource):
    return ec2_resource.vpc_addresses.all()


@pytest.fixture
def gen_(ec2_resource):
    return ec2_resource.vpc_peering_connections.all()


@pytest.fixture
def gen_(ec2_resource):
    return ec2_resource.vpcs.all()


@pytest.fixture
def gen_(gen_volume):
    return gen_volume.volumes.all()


@pytest.fixture
def gen_(gen_vpc_addresse):
    return gen_vpc_addresse.vpc_addresses.all()


@pytest.fixture
def gen_(gen_instance):
    return gen_instance.instances.all()


@pytest.fixture
def gen_(gen_instance):
    return gen_instance.instances.all()


@pytest.fixture
def gen_(gen_network_interface):
    return gen_network_interface.network_interfaces.all()


@pytest.fixture
def gen_(gen_snapshot):
    return gen_snapshot.snapshots.all()


@pytest.fixture
def gen_(gen_accepted_vpc_peering_connection):
    return gen_accepted_vpc_peering_connection.accepted_vpc_peering_connections.all()


@pytest.fixture
def gen_(gen_instance):
    return gen_instance.instances.all()


@pytest.fixture
def gen_(gen_internet_gateway):
    return gen_internet_gateway.internet_gateways.all()


@pytest.fixture
def gen_(gen_network_acl):
    return gen_network_acl.network_acls.all()


@pytest.fixture
def gen_(gen_network_interface):
    return gen_network_interface.network_interfaces.all()


@pytest.fixture
def gen_(gen_requested_vpc_peering_connection):
    return gen_requested_vpc_peering_connection.requested_vpc_peering_connections.all()


@pytest.fixture
def gen_(gen_route_table):
    return gen_route_table.route_tables.all()


@pytest.fixture
def gen_(gen_security_group):
    return gen_security_group.security_groups.all()


@pytest.fixture
def gen_(gen_subnet):
    return gen_subnet.subnets.all()
