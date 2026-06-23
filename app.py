import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

data = np.genfromtxt("transfer.txt", delimiter = "\t", skip_header = 1)
V = data[:, 0]
I = data[:, 1]

fig1 = plt.figure()
plt.title("Transferencia")
plt.plot(V, 1e6*I)
plt.xlabel("V [V]")
plt.ylabel(r"I [$\mu$A]")

st.pyplot(fig1)

fig2 = plt.figure()
plt.title("Transferencia")
plt.plot(V, 1e6*I, color = "red")
plt.xlabel("V [V]")
plt.ylabel(r"I [$\mu$A]")

st.pyplot(fig2)
