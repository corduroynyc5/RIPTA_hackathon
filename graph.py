import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

#test.. messing around with git
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("output.txt","r").read()
    #TODO: tokenize output.txt by sentence.. ideally convert it to a dictionary
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    tweet_num = 0
    for num in range(1,len(dataArray),3):
        y = dataArray[num]
        str1 = "compound"
        compound_index = y.index(str1)
        compound_score = float(y[compound_index+11:compound_index+14])
        yar.append(compound_score)
        xar.append(tweet_num)
        tweet_num += 1

    ax1.clear()
    ax1.plot(xar,yar)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
