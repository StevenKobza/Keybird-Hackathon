import os
import numpy as np
import soundfile
import pandas
import matplotlib.pyplot as plt
import scipy as sp
from scipy.fft import fft, ifft, fftfreq

path = os.getcwd()
data_folder = path + '/data/reprocessed_filled types/samples_from_onsets/Alpine65  Blue Velvet PME Switches  POM Plate  ASMR Sound Test/'
filenames = os.listdir(data_folder)

audioset = []

for file in filenames:
    data, sr = soundfile.read(data_folder + file)
    audioset.append(data)

dataset = pandas.DataFrame.from_dict(audioset)

def getSample(number):
    sample = dataset.transpose()[number]
    return sample

sample_0 = np.array(getSample(0))
sample_1 = np.array(getSample(1))

step = 1 / len(sample_0)
x_axis = np.array(np.arange(0, 1, step))

print(sample_0)


fft_0 = sp.fft.fft(sample_0)
fft_1 = sp.fft.fft(sample_1)

fig, (ax1, ax2) = plt.subplots(2)

# Number of sample points
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N, endpoint=False)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf_0 = fft_0
xf_0 = fftfreq(N, T)[:N//2]
ax1.plot(xf_0, 2.0/N * np.abs(yf_0[0:N//2]))

yf_1 = fft_1
xf_1 = fftfreq(N, T)[:N//2]
ax2.plot(xf_1, 2.0/N * np.abs(yf_1[0:N//2]))

fig.suptitle('Fourier Transform Comparison for two audio dataframes')
plt.grid()
plt.show()
