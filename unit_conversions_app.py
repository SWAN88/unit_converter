import pandas as pd
import streamlit as st

"""

Here, you can convert the units between wavelength, energy, period, and frequency :heart:

"""
option = st.selectbox(
    'What unit do you have?',
    ('Wavelength (nm)', 'Energy (eV)', 'Period (fs)', 'Frequency (THz)'))
st.write('You selected:', option)

h = 4.1357*1e-15
c = 2.9979*1e17

if option == 'Wavelength (nm)':
    input = st.slider('Input Wavelength (nm)', 100, 3000, 600)
    wavelength_out = input
    energy_out = h*c / input
    period_out = (input / c) * 1e15  #fs
    frequency_out = (1 / period_out) * 1e3  #THz

elif option == 'Energy (eV)':
    input = st.slider('Input Energy (eV)', 0.4, 12.4, 2.0)
    wavelength_out = h*c / input
    energy_out = input
    period_out = (wavelength_out / c) * 1e15
    frequency_out = (1 / period_out) * 1e3

elif option == 'Period (fs)':
    input = st.slider('Input Period (fs)', 0.334, 10.0, 2.0)
    period_out = input
    frequency_out = (1 / input) * 1e3
    wavelength_out = (c * input) * 1e-15
    energy_out = h*c / wavelength_out

elif option == 'Frequency (THz)':
    input = st.slider('Input Frequency (THz)', 100, 3000, 500)
    period_out = 1/ input
    frequency_out = input
    wavelength_out = (c / input) * 1e-12
    energy_out = h*c / wavelength_out

# st.write(wavelength_out, energy_out, period_out, frequency_out)

col1, col2 = st.columns(2)
col1.metric("Wavelength", f"{round(wavelength_out, 5)} nm")
col2.metric("Energy", f"{round(energy_out, 5)} eV")

col3, col4 = st.columns(2)
col3.metric("Period", f"{round(period_out, 5)} fs")
col4.metric("Frequency", f"{round(frequency_out, 5)} THz")

st.subheader("Constants :globe_with_meridians:")

st.latex(r'''
h = 4.1357 \times 10^{-15} \space (eV \cdot s), 
c = 2.9979 \times 10^{17} \space (nm/s),
hc = 1239.8415 \space (eV \cdot nm),
''')

st.subheader("Equations :black_nib:")

st.latex(r'''
E (eV) = \frac{hc}{\lambda (nm)},
\nu (THz)= \frac{c}{\lambda (nm)} \times 10^{15},
T(fs) = \frac{1}{\nu(THz)} \times 10^{3}
''')