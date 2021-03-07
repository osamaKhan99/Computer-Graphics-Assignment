import os
import numpy as np
import matplotlib.pyplot as plt
img_size=0
vid_size=0
aud_size=0
doc_size=0

path=os.path.join(os.getcwd(),"data")
data=os.listdir(path)

for i in data:
    if i.lower().endswith(('.png', '.jpg', '.jpeg', '.svg')):
        img_size=img_size+os.path.getsize(os.path.join(path,i))
        
    elif i.lower().endswith(('.mp4', '.3gp', '.mov','.avi','.wmv','.mpg')):
        vid_size=vid_size+os.path.getsize(os.path.join(path,i))
        
    elif i.lower().endswith(('.txt', '.pdf', '.ppt','.xlsx', '.docx')):
        doc_size=doc_size+os.path.getsize(os.path.join(path,i))
        
    elif i.lower().endswith(('.mp3', '.wav', '.m4a','.wma')):
        aud_size=aud_size+os.path.getsize(os.path.join(path,i))

plt.title("Data Statistics")
plt.xlabel("Data")
plt.ylabel("Size in MB")
media = ['Images', 'Videos', 'Audios', 'Documents']
media_size = np.array([img_size,vid_size,aud_size,doc_size])/2**20
plt.bar(media,media_size)
plt.show()