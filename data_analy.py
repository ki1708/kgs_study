import numpy as np
import matplotlib.pyplot as plt



# 데이터 파일 경로 설정
file_mag_path = 'C:/Users/addmin/Desktop/fftw/mag_data.txt'  # data 폴더 안에 있는 mag_data.txt 파일
file_signal_path = 'C:/Users/addmin/Desktop/fftw/signal_data.txt'  # data 폴더 안에 있는 signal_data.txt 파일
file_narrow_db_data_path = 'C:/Users/addmin/Desktop/fftw/narrow_db_data.txt'  # data 폴더 안에 있는 narrow_db_data.txt 파일

# 데이터 파일 읽기
data_signal = np.loadtxt(file_signal_path)
data_mag = np.loadtxt(file_mag_path)
data_narrow_db_data = np.loadtxt(file_narrow_db_data_path)

# 기본 통계
print("기본 통계 요약:")
print(f"평균: {np.mean(data_signal)}")
print(f"표준편차: {np.std(data_signal)}")
print(f"최소값: {np.min(data_signal)}")
print(f"최대값: {np.max(data_signal)}")
print(f"중간값: {np.median(data_signal)}")

#NUM_POINTS = 200
NUM_POINTS = 32768
plt.subplot(2, 1, 1)
plt.plot(data_signal)
plt.xlim(0, NUM_POINTS)
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(data_mag)
plt.xlim(0, 200)
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(data_narrow_db_data)
plt.xlim(0, 200)
plt.grid(True)

plt.show()




# # 히스토그램 그리기
# plt.figure(figsize=(10, 6))
# plt.hist(data, bins=20, edgecolor='black')
# plt.title('Histogram of FFT Magnitudes')
# plt.xlabel('Magnitude')
# plt.ylabel('Frequency')
# plt.show()

# # 상자 그림(Box Plot) 그리기
# plt.figure(figsize=(8, 6))
# plt.boxplot(data)
# plt.title('Box Plot of FFT Magnitudes')
# plt.ylabel('Magnitude')
# plt.show()
