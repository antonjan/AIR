import simplesoapy
import numpy
#pip install SimpleSoapy
# List all connected SoapySDR devices
print(simplesoapy.detect_devices(as_string=True))

# Initialize SDR device
#sdr = simplesoapy.SoapyDevice('driver=rtlsdr')
sdr = simplesoapy.SoapyDevice('driver=miri')

# Set sample rate
#sdr.sample_rate = 2.56e6
sdr.sample_rate = 8e6

# Set center frequency
sdr.freq = 29000000.0 

# Setup base buffer and start receiving samples. Base buffer size is determined
# by SoapySDR.Device.getStreamMTU(). If getStreamMTU() is not implemented by driver,
# SoapyDevice.default_buffer_size is used instead
sdr.start_stream()

# Create numpy array for received samples
samples = numpy.empty(len(sdr.buffer) * 100, numpy.complex64)

# Receive all samples
sdr.read_stream_into_buffer(samples)

# Stop receiving
sdr.stop_stream()
