import matplotlib.pyplot as plt
ele = ['2K','4K','6K','8K','10K']
y1 = [0.000017,0.000018,0.0000206,0.0000213,0.0000222]
y2 = [0.000035,0.000039,0.0000400,0.000041,0.000044]
plt.plot(ele,y1,label="Insertion")
plt.plot(ele,y2,label="Deletion")
plt.xlabel('Number of Elements')
plt.ylabel('Time Taken(in seconds)')
plt.title('Time Analysis')
plt.legend()
plt.show()