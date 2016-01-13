# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from six import text_type

from contrail_api_cli.commands import Command, Arg
from contrail_api_cli.resource import Resource
from contrail_api_cli.exceptions import CommandError

from .utils import ip_type


class DNSNameserver(Command):
    ips = Arg(nargs="+", metavar='nameserver',
              help='IPs of DNS servers',
              type=ip_type,
              default=[])
    network_ipam_fqname = Arg('--network-ipam-fqname',
                              metavar='fqname',
                              help='Network IPAM fqname (default: %(default)s)',
                              default='default-domain:default-project:default-network-ipam')

    def __call__(self, ips=None, network_ipam_fqname=None):
        try:
            self.ipam = Resource('network-ipam', fq_name=network_ipam_fqname,
                                 check_fq_name=True, fetch=True)
        except ValueError as e:
            raise CommandError(text_type(e))

        if 'network_ipam_mgmt' not in self.ipam:
            self.ipam['network_ipam_mgmt'] = {
                'ipam_dns_method': 'tenant-dns-server',
                'ipam_dns_server': {
                    'tenant_dns_server_address': {
                        'ip_address': []
                    }
                }
            }


class AddDNSNameserver(DNSNameserver):
    description = 'Add DNS nameserver'

    def __call__(self, ips=None, **kwargs):
        super(AddDNSNameserver, self).__call__(ips=ips, **kwargs)
        added = False
        for ip in ips:
            if ip not in self.ipam['network_ipam_mgmt']['ipam_dns_server']['tenant_dns_server_address']['ip_address']:
                self.ipam['network_ipam_mgmt']['ipam_dns_server']['tenant_dns_server_address']['ip_address'].append(ip)
                added = True
        if added:
            self.ipam.save()
        else:
            raise CommandError('All IPs already configured')


class DelDNSNameserver(DNSNameserver):
    description = 'Del DNS nameserver'

    def __call__(self, ips=None, **kwargs):
        super(DelDNSNameserver, self).__call__(ips=ips, **kwargs)
        removed = False
        for ip in ips:
            try:
                self.ipam['network_ipam_mgmt']['ipam_dns_server']['tenant_dns_server_address']['ip_address'].remove(ip)
                removed = True
            except ValueError:
                pass
        if removed:
            self.ipam.save()
        else:
            raise CommandError('All IPs already not configured')
