import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
T = 1 / Fs
end_time = 1
time = np.linspace(0, end_time, Fs)
amp = [2, 1, 0.5, 0.2]  # 진폭
freq = [10, 20, 30, 40]  # 주파수

signal_1 = amp[0] * np.sin(freq[0] * 2 * np.pi * time)
signal_2 = amp[1] * np.sin(freq[1] * 2 * np.pi * time)
signal_3 = amp[2] * np.sin(freq[2] * 2 * np.pi * time)
signal_4 = amp[3] * np.sin(freq[3] * 2 * np.pi * time)

signal = signal_1 + signal_2 + signal_3 + signal_4


plt.subplot(2, 3, 1)
plt.plot(time, signal_1)

plt.subplot(2, 3, 2)
plt.plot(time, signal_2)

plt.subplot(2, 3, 3)
plt.plot(time, signal_3)

plt.subplot(2, 3, 4)
plt.plot(time, signal_4)

plt.subplot(2, 3, 5)
plt.plot(time, signal)


plt.subplot(2, 3, 6)
s_fft = np.fft.fft(signal) # 추후 IFFT를 위해 abs를 취하지 않은 값을 저장한다.
amplitude = abs(s_fft)*(2/len(s_fft)) # 2/len(s)을 곱해줘서 원래의 amp를 구한다.
frequency = np.fft.fftfreq(len(s_fft), T)
plt.xlim(0, 50)
plt.stem(frequency, amplitude)
plt.grid(True)
plt.show()

#출처: https://lifelong-education-dr-kim.tistory.com/entry/Python-numpy-FFT-IFFT-사용하기-주기분석 [독학하는 김박사:티스토리]




# plt.plot(time,signal_1)
# plt.plot(time,signal_2)
# plt.plot(time,signal_3)
# plt.plot(time,signal_4)


# plt.subplot(1, 1, 1)
# plt.plot(time, signal)
