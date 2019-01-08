import aprs
#pip install aprs
frame = aprs.parse_frame('ZR6AIC>APRS:>Hello World!')

a = aprs.TCP('ZR6AIC', '12345')
a.start()

a.send(frame)
