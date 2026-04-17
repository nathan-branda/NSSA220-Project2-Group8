def compute(packets, host_ips) :
	metrics = [{}, {}, {}, {}]
	for i in range(len(packets)):

		metrics[i]['sent_request']=0
		metrics[i]['received_requests'] = 0
		metrics[i]['sent_replies']=0
		metrics[i]['received_replies'] = 0
		metrics[i]['sent_request_bytes'] = 0
		metrics[i]['received_request_bytes'] = 0
		metrics[i]['sent_request_data'] = 0
		metrics[i]['received_request_data'] = 0

		for packet in packets[i]:
			if packet['type'] == 'request' and packet['src'] == host_ips[i]:
				metrics[i]['sent_requests'] += 1
				metrics[i]['sent_request_bytes'] += int(packet['len'])
				metrics[i]['sent_request_data'] += int(packet['len']) - 42
			if packet['type'] == 'reply' and packet['src'] == host_ips[i]:
				metrics[i]['sent_replies'] += 1

		for packet in packets[i]:
			if packet['type'] == 'request' and packet['src'] != host_ips[i]:
				metrics[i]['received_requests'] += 1
				metrics[i]['received_request_bytes'] += int(packet['len'])
				metrics[i]['received_request_data'] += int(packet['len']) - 42
			if packet['type'] == 'reply' and packet['src'] != host_ips[i]:
				metrics[i]['received_replies'] += 1

	print(metrics)
	print('called compute function in compute_metrics.py')

