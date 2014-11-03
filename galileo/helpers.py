from BeautifulSoup import BeautifulSoup
import pexpect
from re import search
from galileo.app import db
from galileo.model import Network, Computer, Port


# @async
def parse_nmap_output(xml_content):
    xml_document = BeautifulSoup(xml_content)

    network = get_network(xml_document)
    computers = get_computers(network, xml_document)

    # db.session.add(network)
    #
    # for computer in computers:
    # db.session.add(computer)

    db.session.commit()
    db.session.close_all()

    print "Scan finished."


def clear_all_data():
    pass


def get_network(xml_document):
    def extract_network_name(nmap_command):

        for arg in nmap_command.split(' '):
            if '_network.xml' in arg:
                filename_name = arg.split('_network.xml')[0]
                network_name = filename_name.split('_')[0]
                return network_name

    nmap_exec = xml_document.nmaprun['args']
    network_name = extract_network_name(nmap_exec)
    scan_info = xml_document.nmaprun.scaninfo['services']

    network = Network(name=network_name, note=scan_info)
    db.session.add(network)

    return network


def get_computers(network, xml_document):
    computers = []

    hosts = xml_document.nmaprun.findAll('host')

    for host in hosts:

        if host.status['state'] != 'up':
            continue

        host_adddress = host.address['addr']
        host_name = 'UNKNOWN'

        for hostname in host.findAll('hostnames'):
            if hostname.hostname is not None:
                host_name = hostname.hostname['name']

        # Try to resolve with SMB
        # if host_name == 'UNKNOWN':
        #       host_name = smb_name(host_adddress)

        computer = Computer()
        computer.network = network
        computer.name = host_name
        computer.ip_address = host_adddress

        # get ports
        ports = get_ports(computer, host.find('ports'))

        computers.append(computer)
        db.session.add(computer)

        print "Computer ::-> " + str(host_adddress) + " ::=:: " + str(host_name)

    return computers


def get_ports(computer, host_ports):
    ports = []

    if host_ports:
        for port in host_ports.findAll('port'):
            port_number = port['portid']
            port_state = port.state['state']
            port_service_name = port.service['name']

            port = Port()
            port.computer = computer
            port.pnumber = port_number
            port.data = port_state
            port.info = port_service_name

            ports.append(port)
            db.session.add(port)

    return ports


def smb_name(ip_address):
    def nmb_lookup(ip, timeout=30):
        command = "nmblookup -A %s" % ip
        process = pexpect.spawn(command, timeout=timeout)
        return process.read()

    def get_nmb_lookup(ip_address_hostname, process=nmb_lookup):
        return process(ip_address_hostname)

    def extract_hostname(nmblookup_ouput):
        search_row = nmblookup_ouput.split("\n")[1]
        result = search('^(.*?)<', search_row)

        hostname = "UNKNOWN"

        if result is not None:
            if result.groups() > 0:
                hostname = result.group(1).strip()

        return hostname

    nmblookup_ouput = get_nmb_lookup(ip_address_hostname=ip_address)
    return extract_hostname(nmblookup_ouput)