from bokeh.plotting import figure, curdoc
from bokeh.driving import linear
from bokeh.models import BoxAnnotation
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.glyphs import Text
from bokeh.models import ColumnDataSource, DataRange1d, Plot, LinearAxis, Grid
from datetime import date
from random import randint
import pandas as pd
import numpy as np

p = figure(plot_width=1200, plot_height=300)

p.title.text = "NETWORK TRAFFIC CLASSIFICATION"
p.title.align = "center"
p.title.text_color = "blue"
p.title.text_font_size = "20px"

p.xaxis.axis_label = 'TIME'
p.yaxis.axis_label = 'CLASSIFICATION'

low_box = BoxAnnotation(bottom=0,top=0.5, fill_alpha=0.1, fill_color='green')
high_box = BoxAnnotation(bottom=0.5, top=1, fill_alpha=0.1, fill_color='red')
low_low_box = BoxAnnotation(bottom=-1,top=-0.5, fill_alpha=0.1, fill_color='red')
low_high_box = BoxAnnotation(bottom=-0.5, top=0, fill_alpha=0.1, fill_color='green')
p.add_layout(low_box)
p.add_layout(high_box)
p.add_layout(low_low_box)
p.add_layout(low_high_box)

r1 = p.line([], [], color="firebrick", line_width=2,legend="Bengin = 0 Malicious = 1")
ds1 = r1.data_source

###################
N = 5
x = np.linspace(0, 1, N)
y = x
a = "CDACCDACCDACCDAC"
text = [a[i*4:i*4+4] for i in range(N)]
src = ColumnDataSource(dict(x=x, y=y, text=text))
glyph = Text(x="x", y="y", text="text", angle=0.3, text_color="#96deb3")
p.add_glyph(src, glyph)
#################3

@linear()
def update(step):
	df = pd.read_csv("files/Visualization.csv")
	pred = df['Pred']
	ds1.data['x'].append(step)
	ds1.data['y'].append(pred)
	ds1.trigger('data', ds1.data, ds1.data)	

curdoc().add_root(p)
curdoc().add_periodic_callback(update, 200)

####################################################################################################3

def updatetable():
	dft = pd.read_csv("files/df.csv")
	time = dft["TIME"]
	#dns = dft["DNS_NAME"]
	src_ip_port = dft["SOURCE-IP:PORT"]
	src_mac = dft["SOURCE-MAC"]
	dst_ip_port = dft["DESTINATION-IP:PORT"]
	dst_mac = dft["DESTINATION-MAC"]
	packet_length = dft["PACKET_LENGTH"]

	data = dict(
		t=[i for i in time],
		#d=[i for i in dns],
		sip=[i for i in src_ip_port],
		smac=[i for i in src_mac],
		dip=[i for i in dst_ip_port],
		dmac=[i for i in dst_mac],
		pl=[i for i in packet_length],
		)
	source = ColumnDataSource(data)
	columns = [
		TableColumn(field="t", title="TIME"),
		#TableColumn(field="d", title="DNS NAME"),
		TableColumn(field="sip", title="SOURCE IP:PORT"),
		TableColumn(field="smac", title="SOURCE MAC"),
		TableColumn(field="dip", title="DESTINATION IP:PORT"),
		TableColumn(field="dmac", title="DESTINATION MAC"),
		TableColumn(field="pl", title="PACKET SIZE"),
		]

	data_table = DataTable(source=source, columns=columns, width=1200, height=300)
	curdoc().add_root(data_table)
curdoc().add_periodic_callback(updatetable, 60000)
