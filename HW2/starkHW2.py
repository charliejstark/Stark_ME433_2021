import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import csv
import pandas as pd

def csvToSignal(csvString):
    '''Returns contents of csv to a list of lists'''
    data = []   # Initialize list of lists

    with open(csvString) as f:
        reader = csv.reader(f)

        for row in reader:
            dataColumn = []

            for col in row:
                dataColumn.append(float(col))

            data.append(dataColumn)

    return data
def reorganizeList(data):
    '''Flips the indicies of the 2d list'''
    inList  = np.arange(0, len(data))
    outList = np.arange(0, len(data[0]))

    data2 = []

    for jj in outList:
        data2Col = []

        for ii in inList:
            data2Col.append(data[ii][jj])

        data2.append(data2Col)

    return data2

# Import data, save as lists of lists
sigA = reorganizeList(csvToSignal('C:/Users/User/Desktop/Senior Year/Spring 2021/MECH_ENG 499/HW2/sigA.csv'))
sigB = reorganizeList(csvToSignal('C:/Users/User/Desktop/Senior Year/Spring 2021/MECH_ENG 499/HW2/sigB.csv'))
sigC = reorganizeList(csvToSignal('C:/Users/User/Desktop/Senior Year/Spring 2021/MECH_ENG 499/HW2/sigC.csv'))
sigD = reorganizeList(csvToSignal('C:/Users/User/Desktop/Senior Year/Spring 2021/MECH_ENG 499/HW2/sigD.csv'))

#######################################################################################################

# Figure 1 - Preview data

params = {'axes.labelsize': 24,
        'axes.titlesize': 24,
        'xtick.labelsize': 18,
        'ytick.labelsize': 18,
        'legend.fontsize': 24,
        'legend.title_fontsize': 24}

plt.rcParams.update(params)

fig1, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(30,20))

ax1.plot(sigA[0], sigA[1], color='k')
ax1.set_title('Signal A', fontsize=24)
ax1.set_xlabel('Time [s]', fontsize=18)
ax1.set_ylabel('Voltage [V]', fontsize=18)

ax2.plot(sigB[0], sigB[1], color='k')
ax2.set_title('Signal B', fontsize=24)
ax2.set_xlabel('Time [s]', fontsize=18)
ax2.set_ylabel('Voltage [V]', fontsize=18)

ax3.plot(sigC[0], sigC[1], color='k')
ax3.set_title('Signal C', fontsize=24)
ax3.set_xlabel('Time [s]', fontsize=18)
ax3.set_ylabel('Voltage [V]', fontsize=18)

ax4.plot(sigD[0], sigD[1], color='k')
ax4.set_title('Signal D', fontsize=24)
ax4.set_xlabel('Time [s]', fontsize=18)
ax4.set_ylabel('Voltage [V]', fontsize=18)

plt.subplots_adjust(hspace=0.25, wspace=0.25)
plt.suptitle('Unfiltered signals', fontsize=36, fontweight='bold')
plt.show()

#######################################################################################################

# Calculate sample rates
srA = float(len(sigA[0]) / sigA[0][-1])
srB = float(len(sigB[0]) / sigB[0][-1])
srC = float(len(sigC[0]) / sigC[0][-1])
srD = float(len(sigD[0]) / sigD[0][-1])

#######################################################################################################

# Calculate fast fourier transforms

def myFFT(data, sr):

    frq = np.arange(len(data)) / (len(data) / sr)
    frq = frq[range(int(len(data)/2))]

    Y = np.fft.fft(data) / len(data)
    Y = Y[range(int(len(data)/2))]

    return frq, Y

frqA, YA = myFFT(sigA[1], srA)
frqB, YB = myFFT(sigB[1], srB)
frqC, YC = myFFT(sigC[1], srC)
frqD, YD = myFFT(sigD[1], srD)

#######################################################################################################

# Figure 2 - Preview FFTs

fig2, ((axA, axB), (axC, axD)) = plt.subplots(2,2, figsize=(30,20))

axA.loglog(frqA, abs(YA), color='k')
axA.set_xlabel('Frequency [Hz]')
axA.set_ylabel('FFT')
axA.set_title('Signal A FFT')

axB.loglog(frqB, abs(YB), color='k')
axB.set_xlabel('Frequency [Hz]')
axB.set_ylabel('FFT')
axB.set_title('Signal B FFT')

axC.loglog(frqC, abs(YC), color='k')
axC.set_xlabel('Frequency [Hz]')
axC.set_ylabel('FFT')
axC.set_title('Signal C FFT')

axD.loglog(frqD, abs(YD), color='k')
axD.set_xlabel('Frequency [Hz]')
axD.set_ylabel('FFT')
axD.set_title('Signal D FFT')

plt.subplots_adjust(hspace=0.25, wspace=0.25)
plt.suptitle('Fast Fourier Transformed Signals', fontsize=36, fontweight='bold')
plt.show()

#######################################################################################################

# Figure 3 - Preview both Signals and FFTs

fig3, ((ax1, fftA), (ax2, fftB), (ax3, fftC), (ax4, fftD)) = plt.subplots(4, 2, figsize=(30,40))


ax1.plot(sigA[0], sigA[1], color='k')
ax1.set_title('Signal A')
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Voltage [V]')

ax2.plot(sigB[0], sigB[1], color='k')
ax2.set_title('Signal B')
ax2.set_xlabel('Time [s]')
ax2.set_ylabel('Voltage [V]')

ax3.plot(sigC[0], sigC[1], color='k')
ax3.set_title('Signal C')
ax3.set_xlabel('Time [s]')
ax3.set_ylabel('Voltage [V]')

ax4.plot(sigD[0], sigD[1], color='k')
ax4.set_title('Signal D')
ax4.set_xlabel('Time [s]')
ax4.set_ylabel('Voltage [V]')


fftA.loglog(frqA, abs(YA), color='k')
fftA.set_xlabel('Frequency [Hz]')
fftA.set_ylabel('FFT')
fftA.set_title('Signal A FFT')

fftB.loglog(frqB, abs(YB), color='k')
fftB.set_xlabel('Frequency [Hz]')
fftB.set_ylabel('FFT')
fftB.set_title('Signal B FFT')

fftC.loglog(frqC, abs(YC), color='k')
fftC.set_xlabel('Frequency [Hz]')
fftC.set_ylabel('FFT')
fftC.set_title('Signal C FFT')

fftD.loglog(frqD, abs(YD), color='k')
fftD.set_xlabel('Frequency [Hz]')
fftD.set_ylabel('FFT')
fftD.set_title('Signal D FFT')


plt.subplots_adjust(hspace=0.75, wspace=0.25)
plt.suptitle('Unfiltered Signals and FFTs', fontsize=36, fontweight='bold')
plt.show()

#######################################################################################################

# MAF Averaging
def smoothSignal(data, X):

    smoother = np.zeros(X)
    smoothed = []

    for ii in np.arange(0, len(data)):
        smoother = np.append(smoother[1:X], data[ii])
        smoothed.append((sum(smoother) / X))

    return smoothed

smoothA = smoothSignal(sigA[1], 50)
smoothB = smoothSignal(sigB[1], 100)
smoothC = smoothSignal(sigC[1], 5)
smoothD = smoothSignal(sigD[1], 50)

#######################################################################################################

# Figure 4 - MAF Smoothed
fig4, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(30,20))

ax1.plot(sigA[0], sigA[1], color='k')
ax1.plot(sigA[0], smoothA, color='r')
ax1.set_title('Signal A, # Points Averaged: 50')
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Voltage [V]')

ax2.plot(sigB[0], sigB[1], color='k')
ax2.plot(sigB[0], smoothB, color='r')
ax2.set_title('Signal B, # Points Averaged: 100')
ax2.set_xlabel('Time [s]')
ax2.set_ylabel('Voltage [V]')

ax3.plot(sigC[0], sigC[1], color='k')
ax3.plot(sigC[0], smoothC, color='r')
ax3.set_title('Signal C, # Points Averaged: 5')
ax3.set_xlabel('Time [s]')
ax3.set_ylabel('Voltage [V]')

ax4.plot(sigD[0], sigD[1], color='k', label='Original')
ax4.plot(sigD[0], smoothD, color='r', label='Filtered')
ax4.set_title('Signal D, # Points Averaged: 50')
ax4.set_xlabel('Time [s]')
ax4.set_ylabel('Voltage [V]')
#ax4.legend(loc='lower left', bbox_to_anchor= (0.0, 1.01), ncol=2,
#            borderaxespad=0, frameon=False)

handles, labels = ax4.get_legend_handles_labels()
fig4.legend(handles, labels, loc='upper right')
plt.subplots_adjust(hspace=0.25, wspace=0.25)
plt.suptitle('MAF Smoothed Signals', fontsize=36, fontweight='bold')
plt.show()

#######################################################################################################

# A, B Smoother

def smoothAB(data, A):

    B = 1 - A
    new_average = np.array([0])

    for ii in np.arange(0, len(data)):
            if ii != 0:
                new_average = np.append(new_average, (A * new_average[ii-1]) + (B * data[ii]))
    
    return new_average


smoothA = smoothAB(sigA[1], 0.50)
smoothB = smoothAB(sigB[1], 0.99)
smoothC = smoothAB(sigC[1], 0.05)
smoothD = smoothAB(sigD[1], 0.50)


#######################################################################################################

# Figure 5 - AB Smoothed
fig5, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(30,20))

ax1.plot(sigA[0], sigA[1], color='k')
ax1.plot(sigA[0], smoothA, color='r')
ax1.set_title('Signal A, A = 0.50, B = 0.50')
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Voltage [V]')

ax2.plot(sigB[0], sigB[1], color='k')
ax2.plot(sigB[0], smoothB, color='r')
ax2.set_title('Signal B, A = 0.99, B = 0.01')
ax2.set_xlabel('Time [s]')
ax2.set_ylabel('Voltage [V]')

ax3.plot(sigC[0], sigC[1], color='k')
ax3.plot(sigC[0], smoothC, color='r')
ax3.set_title('Signal C, A = 0.05, B = 0.95')
ax3.set_xlabel('Time [s]')
ax3.set_ylabel('Voltage [V]')

ax4.plot(sigD[0], sigD[1], color='k', label='Original')
ax4.plot(sigD[0], smoothD, color='r', label='Filtered')
ax4.set_title('Signal D, A = 0.50, B = 0.50')
ax4.set_xlabel('Time [s]')
ax4.set_ylabel('Voltage [V]')

handles, labels = ax4.get_legend_handles_labels()
fig5.legend(handles, labels, loc='upper right')
plt.subplots_adjust(hspace=0.25, wspace=0.25)
plt.suptitle('A/B Smoothed Signals', fontsize=36, fontweight='bold')
plt.show()


#######################################################################################################

# Cutoff: 100 Hz, Bandwidth: 100 Hz, Window: Rectangle
FIR_A = [
    0.001867519746044820,
    0.002275293677911463,
    0.002692845467883248,
    0.003119400211540369,
    0.003554151391578438,
    0.003996262853518041,
    0.004444870878876082,
    0.004899086349965267,
    0.005357997000181999,
    0.005820669743355830,
    0.006286153075466025,
    0.006753479541784039,
    0.007221668262275161,
    0.007689727507889525,
    0.008156657320192495,
    0.008621452166627776,
    0.009083103623574271,
    0.009540603079249766,
    0.009992944448431896,
    0.010439126890909214,
    0.010878157525543523,
    0.011309054131818317,
    0.011730847830767882,
    0.012142585737226980,
    0.012543333575412086,
    0.012932178249941664,
    0.013308230364524597,
    0.013670626680692492,
    0.014018532509122373,
    0.014351144026291085,
    0.014667690509420725,
    0.014967436482914990,
    0.015249683769748768,
    0.015513773441556675,
    0.015759087661469738,
    0.015985051414072162,
    0.016191134117190663,
    0.016376851110586923,
    0.016541765016997088,
    0.016685486971350718,
    0.016807677714403370,
    0.016908048547430839,
    0.016986362145057821,
    0.017042433223728004,
    0.017076129063764694,
    0.017087369883420026,
    0.017076129063764694,
    0.017042433223728004,
    0.016986362145057821,
    0.016908048547430839,
    0.016807677714403370,
    0.016685486971350718,
    0.016541765016997088,
    0.016376851110586923,
    0.016191134117190663,
    0.015985051414072162,
    0.015759087661469738,
    0.015513773441556675,
    0.015249683769748768,
    0.014967436482914990,
    0.014667690509420725,
    0.014351144026291085,
    0.014018532509122373,
    0.013670626680692492,
    0.013308230364524597,
    0.012932178249941664,
    0.012543333575412086,
    0.012142585737226980,
    0.011730847830767882,
    0.011309054131818317,
    0.010878157525543523,
    0.010439126890909214,
    0.009992944448431896,
    0.009540603079249766,
    0.009083103623574271,
    0.008621452166627776,
    0.008156657320192495,
    0.007689727507889525,
    0.007221668262275161,
    0.006753479541784039,
    0.006286153075466025,
    0.005820669743355830,
    0.005357997000181999,
    0.004899086349965267,
    0.004444870878876082,
    0.003996262853518041,
    0.003554151391578438,
    0.003119400211540369,
    0.002692845467883248,
    0.002275293677911463,
    0.001867519746044820,
]

# Cutoff: 33 Hz, Bandwidth: 33 Hz, Window: Rectangle
FIR_B = [
    0.001867519746044820,
    0.002275293677911463,
    0.002692845467883248,
    0.003119400211540369,
    0.003554151391578438,
    0.003996262853518041,
    0.004444870878876082,
    0.004899086349965267,
    0.005357997000181999,
    0.005820669743355830,
    0.006286153075466025,
    0.006753479541784039,
    0.007221668262275161,
    0.007689727507889525,
    0.008156657320192495,
    0.008621452166627776,
    0.009083103623574271,
    0.009540603079249766,
    0.009992944448431896,
    0.010439126890909214,
    0.010878157525543523,
    0.011309054131818317,
    0.011730847830767882,
    0.012142585737226980,
    0.012543333575412086,
    0.012932178249941664,
    0.013308230364524597,
    0.013670626680692492,
    0.014018532509122373,
    0.014351144026291085,
    0.014667690509420725,
    0.014967436482914990,
    0.015249683769748768,
    0.015513773441556675,
    0.015759087661469738,
    0.015985051414072162,
    0.016191134117190663,
    0.016376851110586923,
    0.016541765016997088,
    0.016685486971350718,
    0.016807677714403370,
    0.016908048547430839,
    0.016986362145057821,
    0.017042433223728004,
    0.017076129063764694,
    0.017087369883420026,
    0.017076129063764694,
    0.017042433223728004,
    0.016986362145057821,
    0.016908048547430839,
    0.016807677714403370,
    0.016685486971350718,
    0.016541765016997088,
    0.016376851110586923,
    0.016191134117190663,
    0.015985051414072162,
    0.015759087661469738,
    0.015513773441556675,
    0.015249683769748768,
    0.014967436482914990,
    0.014667690509420725,
    0.014351144026291085,
    0.014018532509122373,
    0.013670626680692492,
    0.013308230364524597,
    0.012932178249941664,
    0.012543333575412086,
    0.012142585737226980,
    0.011730847830767882,
    0.011309054131818317,
    0.010878157525543523,
    0.010439126890909214,
    0.009992944448431896,
    0.009540603079249766,
    0.009083103623574271,
    0.008621452166627776,
    0.008156657320192495,
    0.007689727507889525,
    0.007221668262275161,
    0.006753479541784039,
    0.006286153075466025,
    0.005820669743355830,
    0.005357997000181999,
    0.004899086349965267,
    0.004444870878876082,
    0.003996262853518041,
    0.003554151391578438,
    0.003119400211540369,
    0.002692845467883248,
    0.002275293677911463,
    0.001867519746044820,
]

# Cutoff: 25 Hz, Bandwidth: 25 Hz, Window: Rectangle
FIR_C = [
    0.001867519746044820,
    0.002275293677911463,
    0.002692845467883248,
    0.003119400211540369,
    0.003554151391578438,
    0.003996262853518041,
    0.004444870878876082,
    0.004899086349965267,
    0.005357997000181999,
    0.005820669743355830,
    0.006286153075466025,
    0.006753479541784039,
    0.007221668262275161,
    0.007689727507889525,
    0.008156657320192495,
    0.008621452166627776,
    0.009083103623574271,
    0.009540603079249766,
    0.009992944448431896,
    0.010439126890909214,
    0.010878157525543523,
    0.011309054131818317,
    0.011730847830767882,
    0.012142585737226980,
    0.012543333575412086,
    0.012932178249941664,
    0.013308230364524597,
    0.013670626680692492,
    0.014018532509122373,
    0.014351144026291085,
    0.014667690509420725,
    0.014967436482914990,
    0.015249683769748768,
    0.015513773441556675,
    0.015759087661469738,
    0.015985051414072162,
    0.016191134117190663,
    0.016376851110586923,
    0.016541765016997088,
    0.016685486971350718,
    0.016807677714403370,
    0.016908048547430839,
    0.016986362145057821,
    0.017042433223728004,
    0.017076129063764694,
    0.017087369883420026,
    0.017076129063764694,
    0.017042433223728004,
    0.016986362145057821,
    0.016908048547430839,
    0.016807677714403370,
    0.016685486971350718,
    0.016541765016997088,
    0.016376851110586923,
    0.016191134117190663,
    0.015985051414072162,
    0.015759087661469738,
    0.015513773441556675,
    0.015249683769748768,
    0.014967436482914990,
    0.014667690509420725,
    0.014351144026291085,
    0.014018532509122373,
    0.013670626680692492,
    0.013308230364524597,
    0.012932178249941664,
    0.012543333575412086,
    0.012142585737226980,
    0.011730847830767882,
    0.011309054131818317,
    0.010878157525543523,
    0.010439126890909214,
    0.009992944448431896,
    0.009540603079249766,
    0.009083103623574271,
    0.008621452166627776,
    0.008156657320192495,
    0.007689727507889525,
    0.007221668262275161,
    0.006753479541784039,
    0.006286153075466025,
    0.005820669743355830,
    0.005357997000181999,
    0.004899086349965267,
    0.004444870878876082,
    0.003996262853518041,
    0.003554151391578438,
    0.003119400211540369,
    0.002692845467883248,
    0.002275293677911463,
    0.001867519746044820,
]

# Cutoff: 10 Hz, Bandwidth: 4 Hz, Window: Rectangle
FIR_D = [
    0.005347333847943900,
    0.004546014530102697,
    0.003592883372736597,
    0.002503789906745420,
    0.001298414615133528,
    -0.000000000000000002,
    -0.001364999980012160,
    -0.002767346739034415,
    -0.004175513108856049,
    -0.005556239981236629,
    -0.006875143518785017,
    -0.008097361682795132,
    -0.009188227819777817,
    -0.010113958281703432,
    -0.010842340547161138,
    -0.011343408075448463,
    -0.011590088171103284,
    -0.011558809464803921,
    -0.011230056224172886,
    -0.010588857585193640,
    -0.009625200926299022,
    -0.008334359971854942,
    -0.006717129783811907,
    -0.004779962549241264,
    -0.002534999962879733,
    0.000000000000000002,
    0.002801842064235499,
    0.005842176449072653,
    0.009087881472216095,
    0.012501539957782411,
    0.016042001543831706,
    0.019665021229645332,
    0.023323962927128305,
    0.026970555417875814,
    0.030555686996545022,
    0.034030224226345392,
    0.037345839662443925,
    0.040455833126813730,
    0.043315931150381126,
    0.045885049535839106,
    0.048126004631495106,
    0.050006159831129639,
    0.051497995009224577,
    0.052579588041653857,
    0.053234999220474449,
    0.053454551214750033,
    0.053234999220474449,
    0.052579588041653857,
    0.051497995009224577,
    0.050006159831129639,
    0.048126004631495106,
    0.045885049535839106,
    0.043315931150381126,
    0.040455833126813730,
    0.037345839662443925,
    0.034030224226345392,
    0.030555686996545022,
    0.026970555417875814,
    0.023323962927128305,
    0.019665021229645332,
    0.016042001543831706,
    0.012501539957782411,
    0.009087881472216095,
    0.005842176449072653,
    0.002801842064235499,
    0.000000000000000002,
    -0.002534999962879733,
    -0.004779962549241264,
    -0.006717129783811907,
    -0.008334359971854942,
    -0.009625200926299022,
    -0.010588857585193640,
    -0.011230056224172886,
    -0.011558809464803921,
    -0.011590088171103284,
    -0.011343408075448463,
    -0.010842340547161138,
    -0.010113958281703432,
    -0.009188227819777817,
    -0.008097361682795132,
    -0.006875143518785017,
    -0.005556239981236629,
    -0.004175513108856049,
    -0.002767346739034415,
    -0.001364999980012160,
    -0.000000000000000002,
    0.001298414615133528,
    0.002503789906745420,
    0.003592883372736597,
    0.004546014530102697,
    0.005347333847943900,
]

def myFIR(data, FIR):

    smoothed = np.array([])
    data = np.append(data, np.zeros(len(FIR)))

    for ii in np.arange(0, (len(data) - len(FIR))):
        weighted = 0
        for jj in np.arange(0, len(FIR)):
            weighted = weighted + (data[ii+jj] * FIR[jj])

        smoothed = np.append(smoothed, weighted)

    return smoothed

smoothA = myFIR(sigA[1], FIR_A)
smoothB = myFIR(sigB[1], FIR_B)
smoothC = myFIR(sigC[1], FIR_C)
smoothD = myFIR(sigD[1], FIR_D)

frqA, smoothYA = myFFT(smoothA, srA)
frqB, smoothYB = myFFT(smoothB, srB)
frqC, smoothYC = myFFT(smoothC, srC)
frqD, smoothYD = myFFT(smoothD, srD)

#######################################################################################################

# Figure 6 - FIR Smoothed

fig6, ((ax1, fftA), (ax2, fftB), (ax3, fftC), (ax4, fftD)) = plt.subplots(4, 2, figsize=(30,20))


ax1.plot(sigA[0], sigA[1], color='k')
ax1.plot(sigA[0], smoothA, color='r')
ax1.set_title('Signal A')
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Voltage [V]')

ax2.plot(sigB[0], sigB[1], color='k')
ax2.plot(sigB[0], smoothB, color='r')
ax2.set_title('Signal B')
ax2.set_xlabel('Time [s]')
ax2.set_ylabel('Voltage [V]')

ax3.plot(sigC[0], sigC[1], color='k')
ax3.plot(sigC[0], smoothC, color='r')
ax3.set_title('Signal C')
ax3.set_xlabel('Time [s]')
ax3.set_ylabel('Voltage [V]')

ax4.plot(sigD[0], sigD[1], color='k', label='Original')
ax4.plot(sigD[0], smoothD, color='r', label='Filtered')
ax4.set_title('Signal D')
ax4.set_xlabel('Time [s]')
ax4.set_ylabel('Voltage [V]')


fftA.loglog(frqA, abs(YA), color='k')
fftA.loglog(frqA, abs(smoothYA), color='r')
fftA.set_xlabel('Frequency [Hz]')
fftA.set_ylabel('FFT')
fftA.set_title('Signal A FFT')

fftB.loglog(frqB, abs(YB), color='k')
fftB.loglog(frqB, abs(smoothYB), color='r')
fftB.set_xlabel('Frequency [Hz]')
fftB.set_ylabel('FFT')
fftB.set_title('Signal B FFT')

fftC.loglog(frqC, abs(YC), color='k')
fftC.loglog(frqC, abs(smoothYC), color='r')
fftC.set_xlabel('Frequency [Hz]')
fftC.set_ylabel('FFT')
fftC.set_title('Signal C FFT')

fftD.loglog(frqD, abs(YD), color='k')
fftD.loglog(frqD, abs(smoothYD), color='r')
fftD.set_xlabel('Frequency [Hz]')
fftD.set_ylabel('FFT')
fftD.set_title('Signal D FFT')

handles, labels = ax4.get_legend_handles_labels()
fig6.legend(handles, labels, loc='upper right', title='Coefficients found in FIRs.csv')
plt.subplots_adjust(hspace=0.75, wspace=0.25)
plt.suptitle('FIR Smoothed Signals and FFTs', fontsize=36, fontweight='bold')
plt.show()


#######################################################################################################

# Write FIR coefficients to CSV

myDict = {'FIR A': FIR_A,
        'FIR B': FIR_B,
        'FIR C': FIR_C,
        'FIR D': FIR_D}


df = pd.DataFrame(myDict)
df.to_csv('C:/Users/User/Desktop/Senior Year/Spring 2021/MECH_ENG 499/HW2/FIRs.csv')

