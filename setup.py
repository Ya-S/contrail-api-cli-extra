import sys
from setuptools import setup, find_packages

install_requires = [
    #'contrail-api-cli>=0.1b1'
    'pycassa',
    'kazoo',
]
test_requires = []

if sys.version_info[0] == 2:
    test_requires.append('mock')


setup(
    name='contrail-api-cli-extra',
    version='0.2',
    description="Supplementary commands for contrail-api-cli",
    author="Jean-Philippe Braun",
    author_email="eon@patapon.info",
    maintainer="Jean-Philippe Braun",
    maintainer_email="eon@patapon.info",
    url="http://www.github.com/eonpatapon/contrail-api-cli-extra",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    scripts=[],
    license="MIT",
    entry_points={
        'contrail_api_cli.provision': [
            'add-sas = contrail_api_cli_extra.provision.service_appliance_set:AddSAS',
            'del-sas = contrail_api_cli_extra.provision.service_appliance_set:DelSAS',
            'list-sas = contrail_api_cli_extra.provision.service_appliance_set:ListSAS',
            'set-global-asn = contrail_api_cli_extra.provision.global_asn:SetGlobalASN',
            'get-global-asn = contrail_api_cli_extra.provision.global_asn:GetGlobalASN',
            'add-dns-nameserver = contrail_api_cli_extra.provision.dns_nameserver:AddDNSNameserver',
            'del-dns-nameserver = contrail_api_cli_extra.provision.dns_nameserver:DelDNSNameserver',
            'list-dns-nameserver = contrail_api_cli_extra.provision.dns_nameserver:ListDNSNameserver',
            'add-bgp-router = contrail_api_cli_extra.provision.bgp_router:AddBGPRouter',
            'del-bgp-router = contrail_api_cli_extra.provision.bgp_router:DelBGPRouter',
            'list-bgp-router = contrail_api_cli_extra.provision.bgp_router:ListBGPRouter',
            'add-linklocal = contrail_api_cli_extra.provision.linklocal:AddLinklocal',
            'del-linklocal = contrail_api_cli_extra.provision.linklocal:DelLinklocal',
            'list-linklocal = contrail_api_cli_extra.provision.linklocal:ListLinklocal',
            'set-route-targets = contrail_api_cli_extra.provision.route_target:SetRouteTargets',
            'get-route-targets = contrail_api_cli_extra.provision.route_target:GetRouteTargets',
            'set-encaps = contrail_api_cli_extra.provision.encapsulation:SetEncapsulation',
            'get-encaps = contrail_api_cli_extra.provision.encapsulation:GetEncapsulation',
            'add-vrouter = contrail_api_cli_extra.provision.vrouter:AddVRouter',
            'del-vrouter = contrail_api_cli_extra.provision.vrouter:DelVRouter',
            'list-vrouter = contrail_api_cli_extra.provision.vrouter:ListVRouter',
            'add-config = contrail_api_cli_extra.provision.config:AddConfig',
            'del-config = contrail_api_cli_extra.provision.config:DelConfig',
            'list-config = contrail_api_cli_extra.provision.config:ListConfig',
            'add-analytics = contrail_api_cli_extra.provision.analytics:AddAnalytics',
            'del-analytics = contrail_api_cli_extra.provision.analytics:DelAnalytics',
            'list-analytics = contrail_api_cli_extra.provision.analytics:ListAnalytics',
            'add-vn = contrail_api_cli_extra.provision.vn:AddVN',
            'del-vn = contrail_api_cli_extra.provision.vn:DelVN',
            'list-vn = contrail_api_cli_extra.provision.vn:ListVNs',
            'set-subnets = contrail_api_cli_extra.provision.subnet:SetSubnets',
            'get-subnets = contrail_api_cli_extra.provision.subnet:GetSubnets',
        ],
        'contrail_api_cli.command': [
            'provision = contrail_api_cli_extra.provision.provision:Provision',
            'clean-orphaned-acl = contrail_api_cli_extra.clean.orphaned_acl:OrphanedACL',
            'clean-stale-lbaas-si = contrail_api_cli_extra.clean.lbaas:CleanStaleLBaasSI',
            'clean-stale-route-target = contrail_api_cli_extra.clean.rt:CleanStaleRT',
            'clean-si-scheduling = contrail_api_cli_extra.clean.si:CleanSIScheduling',
            'migrate-si = contrail_api_cli_extra.migration.si:MigrateSI110221',
            'rpf = contrail_api_cli_extra.misc.rpf:RPF',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: User Interfaces',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4'
    ],
    tests_require=test_requires,
    test_suite="tests"
)
