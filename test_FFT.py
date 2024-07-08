import numpy as np
import matplotlib.pyplot as plt
 
fs = 100  # 샘플링 주파수 100Hz # 

#arange 함수는 시작값과 끝값을 지정하고 그 사이의 값을 균일하게 나누고 배열로 반환하는 함수
#linespce랑 비슷.

t = np.arange(0, 3, 1 / fs) # 0부터 3까지 0.01간격으로 샘플링한다. fs는 샘플링 주파수고. 1/fs는 주파수의 역수로 샘플링주기가 된다. 즉 3초동안 0.01초 간격으로 값을 샘플링한다는 의미.
#t가 가지는값은 0 , 0.01, 0.02, 0.03 , .....2.98, 2.99, 3.00 

f1 = 35  # 주파수 35Hz 파형 
f2 = 10  # 주파수 10Hz 파형 

signal = 0.6 * np.sin(2 * np.pi * f1 * t) + 3 * np.cos(2 * np.pi * f2 * t + np.pi/2) # 테스트용 시그널 생성 ( 0.6진폭의 35Hz + 3진폭의 10Hz )
# 
 
fft = np.fft.fft(signal) / len(signal)  #FFT 수행 및 정규화 (FFT 결과를 데이터길이로 나누어 정규화)
 
fft_magnitude = abs(fft) #푸리에 스펙트럼 그래프 

plt.subplot(2,1,1)
plt.plot(t,signal)
plt.grid()
 


plt.subplot(2,1,2)

#plt.stem(fft_magnitude)
length = len(signal)
f = np.linspace(-(fs / 2), fs / 2, length)  # x축 주파수 범위 설정 -50 ~ 50Hz


plt.stem(f, np.fft.fftshift(fft_magnitude))  # 주파수 영역에서 중심이 0인 FFT 결과를 그래프로 표현

plt.ylim(0,2.5)

plt.grid()



plt.show()