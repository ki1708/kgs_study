import matplotlib.pyplot as plt
import numpy as np


Fs = 1000
T = 1 / Fs



NUM_POINTS = 1000 # 샘플링 횟수, # 샘플링하는 시간을 1초라고 생각하면 0.001초 간격으로 샘플링한다고 생각해도됨.
MM_PI = 3.14159265358979
# 복소수 배열 생성
signal = np.zeros(NUM_POINTS, dtype=np.complex128)

signal_test =[0] * NUM_POINTS

plt.style.use('_mpl-gallery')

# make data
#linspace는 시작과 끝을 균일하게 나눈 간격의 숫자를 생성
#x = np.linspace(0, 10, 100)
#y = 4 + 2 * np.sin(2 * x)

test_frq = 10
test_frq_2= 25

for i in range(NUM_POINTS):
    #theta = i / NUM_POINTS * MM_PI # 공식 수정
    theta = i / NUM_POINTS * 2.0 * MM_PI # 세타는 2파이 * 주파수 * t 임. 지금 주파수가 밖으로 빠져나간형태.
    real_part = 1.0 * np.cos(10.0 * theta) + 0.5 * np.cos(25.0 * theta)
    imag_part = 1.0 * np.sin(10.0 * theta) + 0.5 * np.sin(25.0 * theta)
    signal[i] = complex(real_part, imag_part)
    
    signal_test[i] = 1.0*np.sin(2 * MM_PI * test_frq * i/1000 ) + 0.5*np.sin(2 * MM_PI * test_frq_2 * i/1000 )
 

# plot
# plt.plot(signal, color='red', marker='o', alpha=0.5, linewidth=2)
plt.subplot(3, 2, 1)
plt.plot(signal)
plt.xlim(0, NUM_POINTS)
plt.grid(True)



s_fft = np.fft.fft(signal) # 추후 IFFT를 위해 abs를 취하지 않은 값을 저장한다.
amplitude = abs(s_fft)*(2/len(s_fft)) # ftf의 절대값에 2/len(s)을 곱해줘서 원래의 amp를 구한다.
frequency = np.fft.fftfreq(len(s_fft), T)

plt.subplot(3, 2, 2)
plt.stem(frequency, amplitude)
plt.xlim(0, 50)
#plt.grid(True)
# plt.title('Box Plot of FFT Magnitudes')
# plt.ylabel('Magnitude')

plt.subplot(3, 2, 3)
plt.plot(signal_test)
plt.xlim(0, NUM_POINTS)
plt.grid(True)

s_fft_test = np.fft.fft(signal_test) # 추후 IFFT를 위해 abs를 취하지 않은 값을 저장한다.
amplitude_t = abs(s_fft_test)*(2/len(s_fft_test)) # ftf의 절대값에 2/len(s)을 곱해줘서 원래의 amp를 구한다.
frequency_t = np.fft.fftfreq(len(s_fft_test), T)

plt.subplot(3, 2, 4)
plt.stem(frequency_t, amplitude_t)
plt.xlim(0, 50)




plt.show()



