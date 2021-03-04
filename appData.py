import os
import numpy as np
import matplotlib.pyplot as plt

path='F:\WhatsAppSetup.exe'

plt.title("Application Storage Size")
plt.xlabel("WhatsApp")
plt.ylabel("Size MB")

app = ['Application']


app_size = np.array(os.path.getsize(path))/2**20
plt.bar(app,app_size,width=0.8)
plt.show()

print("\n\n Application size is "+str(app_size)+" MB" )