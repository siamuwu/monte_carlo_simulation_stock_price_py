import numpy as np
import matplotlib.pyplot as plt

#formula
s_ini = float (input ("Your initial stock price: "))
m = float (input ("Expected return from historical data in %: "))/100
a = float (input ("Expected volatility in %: "))/100

N,n = 10000,252
Z = np.random.randn(N,n)
s_fin = np.zeros([N,n])
s_fin [:,0] = s_ini

for t in range(1,n):
    s_fin[:,t] = s_fin[:,t-1] * np.exp(((m-(0.5*(a**2)))*1/n)+(a*np.sqrt(1/n))*Z[:,t])

avg = np.mean(s_fin[:,n-1])
prob = np.sum(s_fin[:,n-1] > s_ini) / len(s_fin[:,n-1])

print(f"Your average final stock price is {avg:.2f}, and probability of it being more than {s_ini} is {prob:.2f}")

for i in range (10):
    plt.plot(np.linspace(0,1,n), s_fin[i,:])
plt.axhline(s_ini, color='b', linestyle='--', alpha=0.5)
plt.xlabel('Time in years')
plt.ylabel('Final stock price')
plt.title('Stock price trend')
plt.show()

plt.xlabel('Final stock price')
plt.ylabel('Probability Density')
plt.title('Probability Density Function of Stock price trend')

plt.hist(s_fin[:,-1], bins=50, density=True) #density true cz i want to see the pdf, ton find the actual probability multiply with bin width
percentile = np.percentile(s_fin[:,-1], [5,50,95])


plt.axvline(percentile[0], color='red', linestyle='--', label='5th percentile')
plt.axvline(percentile[1], color='black', linestyle='-', label='Median')
plt.axvline(percentile[2], color='red', linestyle='--', label='95th percentile')

plt.legend()
plt.show()


var_loss = s_ini - percentile[0]
print(f"There’s 5% chance of losing more than {var_loss:.2f}.\nThe 5th to 95th percentile is tells that most of the outcomes lie within the range of {percentile[0]:.2f} to {percentile[2]:.2f}.\nAnd the median, which means there is 50% chance the stock price\nwill end at {percentile[1]:.2f}.")
