def compute(packets, host_ips) :
	metrics = [{}, {}, {}, {}]
	for i in range(len(packets)):

		metrics[i]['sent_requests'] = 0
		metrics[i]['received_requests'] = 0
		metrics[i]['sent_replies']=0
		metrics[i]['received_replies'] = 0
		metrics[i]['sent_request_bytes'] = 0
		metrics[i]['received_request_bytes'] = 0
		metrics[i]['sent_request_data'] = 0
		metrics[i]['received_request_data'] = 0
		metrics[i]['req_exchanges'] = 0
		metrics[i]['total_rtt'] = 0
		metrics[i]['avg_rtt'] = 0
		metrics[i]['total_reply_delay'] = 0
		metrics[i]['received_requests'] = 0

		for packet in packets[i]:
			if packet['type'] == 'request' and packet['src'] == host_ips[i]:
				metrics[i]['sent_requests'] += 1
				metrics[i]['sent_request_bytes'] += int(packet['len'])
				metrics[i]['sent_request_data'] += int(packet['len']) - 42

				response_time = 0
				for pack in packets[i]:
					if pack['num'] == packet['assoc']:
						response_time = float(pack['time'])
						break
				metrics[i]['req_exchanges'] += 1
				metrics[i]['total_rtt'] += (response_time - float(packet['time'])) * 1000

			if packet['type'] == 'reply' and packet['src'] == host_ips[i]:
				for pack in packets[i]:
					if pack['num'] == packet['assoc']:
						metrics[i]['total_reply_delay'] += float(packet['time']) - float(pack['time'])
						break
				metrics[i]['received_requests'] += 1
				metrics[i]['received_request_bytes'] += int(packet['len'])
				metrics[i]['received_request_data'] += int(packet['len']) - 42

			if packet['type'] == 'reply' and packet['src'] != host_ips[i]:
				metrics[i]['received_replies'] += 1
			if packet['type'] == 'reply' and packet['src'] == host_ips[i]:
				metrics[i]['sent_replies'] += 1
				
	for node in metrics:
		node['avg_rtt'] = node['total_rtt'] / node['req_exchanges']
		node['request_throughput'] = node['sent_request_bytes'] / node['total_rtt'] # kB and milliseconds cancel out
		node['request_goodput'] = node['sent_request_data'] / node['total_rtt']
		node['avg_reply_delay'] = node['total_reply_delay'] / node['received_requests'] * 1000000

	print(metrics)
	print('called compute function in compute_metrics.py')

