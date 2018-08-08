import numpy as np
import pandas as pd
import pyshark
import subprocess
count=100
cap = pyshark.LiveCapture(interface='wlp3s0')
cap.sniff(packet_count=count)

#H=[],MI=[],HH=[],HH_jit=[],HpHp=[],packet_size=[]
try:
	Time = [str(pkt.sniff_time).split(".")[0] for pkt in cap]
	H = [pkt.ip.src for pkt in cap]
	MI = [pkt.ip.src+" "+pkt.eth.src for pkt in cap]
	HH = [pkt.ip.src+" "+pkt.ip.dst for pkt in cap]
	HH_jit = [int(pkt.sniff_timestamp.split(".")[1]) for pkt in cap]
	HpHp = [pkt.ip.src+":"+pkt[pkt.transport_layer].srcport+" "+pkt.ip.dst+":"+pkt[pkt.transport_layer].dstport for pkt in cap]
	pkt_size = [pkt.length for pkt in cap]
	cap_size = [pkt.captured_length for pkt in cap]
	time = [str(pkt.sniff_time).split(".")[0] for pkt in cap]
	src_ip = [pkt.ip.src+":"+pkt[pkt.transport_layer].srcport for pkt in cap]
	dest_ip = [pkt.ip.dst+":"+pkt[pkt.transport_layer].dstport for pkt in cap]
	src_mac = [pkt.eth.src for pkt in cap]
	dst_mac = [pkt.eth.dst for pkt in cap]
	packet = [pkt.length for pkt in cap]
	df5 = pd.DataFrame({'TIME':time})
	df5['SOURCE-IP:PORT']=src_ip
	df5['SOURCE-MAC']=src_mac
	df5['DESTINATION-IP:PORT']=dest_ip
	df5['DESTINATION-MAC']=dst_mac
	df5['PACKET_LENGTH']=packet

	df_L5 = pd.DataFrame({'Time':Time})
	df_L5['H']=H
	df_L5['MI']=MI
	df_L5['HH']=HH
	df_L5['HH_jit']=HH_jit
	df_L5['HpHp']=HpHp
	df_L5['pkt_size']=pkt_size
	df_L5['cap_size']=cap_size
	
	df_L5.to_csv('files/network_L5.csv')
except AttributeError as e:
	pass

###############################################################
cap = pyshark.LiveCapture(interface='wlp3s0')
cap.sniff(packet_count=count)

#H=[],MI=[],HH=[],HH_jit=[],HpHp=[],packet_size=[]
try:
	Time = [str(pkt.sniff_time).split(".")[0] for pkt in cap]
	H = [pkt.ip.src for pkt in cap]
	MI = [pkt.ip.src+" "+pkt.eth.src for pkt in cap]
	HH = [pkt.ip.src+" "+pkt.ip.dst for pkt in cap]
	HH_jit = [int(pkt.sniff_timestamp.split(".")[1]) for pkt in cap]
	HpHp = [pkt.ip.src+":"+pkt[pkt.transport_layer].srcport+" "+pkt.ip.dst+":"+pkt[pkt.transport_layer].dstport for pkt in cap]
	pkt_size = [pkt.length for pkt in cap]
	cap_size = [pkt.captured_length for pkt in cap]

	time = [str(pkt.sniff_time).split(".")[0] for pkt in cap]
	src_ip = [pkt.ip.src+":"+pkt[pkt.transport_layer].srcport for pkt in cap]
	dest_ip = [pkt.ip.dst+":"+pkt[pkt.transport_layer].dstport for pkt in cap]
	src_mac = [pkt.eth.src for pkt in cap]
	dst_mac = [pkt.eth.dst for pkt in cap]
	packet = [pkt.length for pkt in cap]
	df3 = pd.DataFrame({'TIME':time})
	df3['SOURCE-IP:PORT']=src_ip
	df3['SOURCE-MAC']=src_mac
	df3['DESTINATION-IP:PORT']=dest_ip
	df3['DESTINATION-MAC']=dst_mac
	df3['PACKET_LENGTH']=packet
	
	df_L3 = pd.DataFrame({'Time':Time})
	df_L3['H']=H
	df_L3['MI']=MI
	df_L3['HH']=HH
	df_L3['HH_jit']=HH_jit
	df_L3['HpHp']=HpHp
	df_L3['pkt_size']=pkt_size
	df_L3['cap_size']=cap_size


	df_L3.to_csv('files/network_L3.csv')
except AttributeError as e:
	pass

######################################################################
cap = pyshark.LiveCapture(interface='wlp3s0')
cap.sniff(packet_count=count)

#H=[],MI=[],HH=[],HH_jit=[],HpHp=[],packet_size=[]
try:
	
	Time = [str(pkt.sniff_time).split(".")[0] for pkt in cap]
	H = [pkt.ip.src for pkt in cap]
	MI = [pkt.ip.src+" "+pkt.eth.src for pkt in cap]
	HH = [pkt.ip.src+" "+pkt.ip.dst for pkt in cap]
	HH_jit = [int(pkt.sniff_timestamp.split(".")[1]) for pkt in cap]
	HpHp = [pkt.ip.src+":"+pkt[pkt.transport_layer].srcport+" "+pkt.ip.dst+":"+pkt[pkt.transport_layer].dstport for pkt in cap]
	pkt_size = [pkt.length for pkt in cap]
	cap_size = [pkt.captured_length for pkt in cap]

	time = [str(pkt.sniff_time).split(".")[0] for pkt in cap]
	src_ip = [pkt.ip.src+":"+pkt[pkt.transport_layer].srcport for pkt in cap]
	dest_ip = [pkt.ip.dst+":"+pkt[pkt.transport_layer].dstport for pkt in cap]
	src_mac = [pkt.eth.src for pkt in cap]
	dst_mac = [pkt.eth.dst for pkt in cap]
	packet = [pkt.length for pkt in cap]
	df1 = pd.DataFrame({'TIME':time})
	df1['SOURCE-IP:PORT']=src_ip
	df1['SOURCE-MAC']=src_mac
	df1['DESTINATION-IP:PORT']=dest_ip
	df1['DESTINATION-MAC']=dst_mac
	df1['PACKET_LENGTH']=packet

	df_L1 = pd.DataFrame({'Time':Time})
	df_L1['H']=H
	df_L1['MI']=MI
	df_L1['HH']=HH
	df_L1['HH_jit']=HH_jit
	df_L1['HpHp']=HpHp
	df_L1['pkt_size']=pkt_size
	df_L1['cap_size']=cap_size

	df_L1.to_csv('files/network_L1.csv')
except AttributeError as e:
	pass
#########################################################################
	cap = pyshark.LiveCapture(interface='wlp3s0')
	cap.sniff(packet_count=count)
#H=[],MI=[],HH=[],HH_jit=[],HpHp=[],packet_size=[]
try:
	Time = [str(pkt.sniff_time).split(".")[0] for pkt in cap]
	H = [pkt.ip.src for pkt in cap]
	MI = [pkt.ip.src+" "+pkt.eth.src for pkt in cap]
	HH = [pkt.ip.src+" "+pkt.ip.dst for pkt in cap]
	HH_jit = [int(pkt.sniff_timestamp.split(".")[1]) for pkt in cap]
	HpHp = [pkt.ip.src+":"+pkt[pkt.transport_layer].srcport+" "+pkt.ip.dst+":"+pkt[pkt.transport_layer].dstport for pkt in cap]
	pkt_size = [pkt.length for pkt in cap]
	cap_size = [pkt.captured_length for pkt in cap]

	time = [str(pkt.sniff_time).split(".")[0] for pkt in cap]
	src_ip = [pkt.ip.src+":"+pkt[pkt.transport_layer].srcport for pkt in cap]
	dest_ip = [pkt.ip.dst+":"+pkt[pkt.transport_layer].dstport for pkt in cap]
	src_mac = [pkt.eth.src for pkt in cap]
	dst_mac = [pkt.eth.dst for pkt in cap]
	packet = [pkt.length for pkt in cap]
	df01 = pd.DataFrame({'TIME':time})
	df01['SOURCE-IP:PORT']=src_ip
	df01['SOURCE-MAC']=src_mac
	df01['DESTINATION-IP:PORT']=dest_ip
	df01['DESTINATION-MAC']=dst_mac
	df01['PACKET_LENGTH']=packet

	df_L0_1 = pd.DataFrame({'Time':Time})
	df_L0_1['H']=H
	df_L0_1['MI']=MI
	df_L0_1['HH']=HH
	df_L0_1['HH_jit']=HH_jit
	df_L0_1['HpHp']=HpHp
	df_L0_1['pkt_size']=pkt_size
	df_L0_1['cap_size']=cap_size

	df_L0_1.to_csv('files/network_L0.1.csv')
except AttributeError as e:
	pass
#############################################################33333##############3
	cap = pyshark.LiveCapture(interface='wlp3s0')
	cap.sniff(packet_count=count)

#H=[],MI=[],HH=[],HH_jit=[],HpHp=[],packet_size=[]
try:
	Time = [str(pkt.sniff_time).split(".")[0] for pkt in cap]
	H = [pkt.ip.src for pkt in cap]
	MI = [pkt.ip.src+" "+pkt.eth.src for pkt in cap]
	HH = [pkt.ip.src+" "+pkt.ip.dst for pkt in cap]
	HH_jit = [int(pkt.sniff_timestamp.split(".")[1]) for pkt in cap]
	HpHp = [pkt.ip.src+":"+pkt[pkt.transport_layer].srcport+" "+pkt.ip.dst+":"+pkt[pkt.transport_layer].dstport for pkt in cap]
	pkt_size = [pkt.length for pkt in cap]
	cap_size = [pkt.captured_length for pkt in cap]

	time = [str(pkt.sniff_time).split(".")[0] for pkt in cap]
	src_ip = [pkt.ip.src+":"+pkt[pkt.transport_layer].srcport for pkt in cap]
	dest_ip = [pkt.ip.dst+":"+pkt[pkt.transport_layer].dstport for pkt in cap]
	src_mac = [pkt.eth.src for pkt in cap]
	dst_mac = [pkt.eth.dst for pkt in cap]
	packet = [pkt.length for pkt in cap]
	df001 = pd.DataFrame({'TIME':time})
	df001['SOURCE-IP:PORT']=src_ip
	df001['SOURCE-MAC']=src_mac
	df001['DESTINATION-IP:PORT']=dest_ip
	df001['DESTINATION-MAC']=dst_mac
	df001['PACKET_LENGTH']=packet
	
	df_L0_01 = pd.DataFrame({'Time':Time})
	df_L0_01['H']=H
	df_L0_01['MI']=MI
	df_L0_01['HH']=HH
	df_L0_01['HH_jit']=HH_jit
	df_L0_01['HpHp']=HpHp
	df_L0_01['pkt_size']=pkt_size
	df_L0_01['cap_size']=cap_size

	df_L0_01.to_csv('files/network_L0.01.csv')

except AttributeError as e:
	pass
######################################################################
try:
	df = df5.append(df3)
	df = df.append(df1)
	df = df.append(df01)
	df = df.append(df001)	
	df.to_csv("files/df.csv")
	subprocess.call(['sudo','python3','df_network.py'])
except Exception as e:
	pass
exit()
