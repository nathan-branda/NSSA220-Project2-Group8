from filter_packets import *
from packet_parser import *
from compute_metrics import *

host_ips = ['192.168.100.1', '192.168.100.2', '192.168.200.1', '192.168.200.2']
filter()
packets = parse()
compute(packets, host_ips)
