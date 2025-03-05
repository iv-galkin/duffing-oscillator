from numpy import zeros, linspace
import matplotlib.pyplot as plt

# осциллятор Дуффинга
# x'' + alpha * x' - beta * x + gamma * x^3 = 0

def f(u, alpha, beta, gamma):
    f = zeros(2)
    f[0] = u[1]
    f[1] = -alpha * u[1] + beta * u[0] - gamma * u[0] ** 3
    return f


M = 5000
t_0 = 0
T = 15
tau = (T - t_0) / M
t = linspace(t_0, T, M + 1)
u = zeros((M + 1, 2))
x_0 = -0.1
z_0 = 0.1 # z = x'
u[0] = [x_0, z_0]

# параметры
alpha = -0.3
beta = -2
gamma = -2


for m in range(M):
    w_1 = f(u[m], alpha, beta, gamma)
    w_2 = f(u[m] + tau * 1 / 2 * w_1, alpha, beta, gamma)
    w_3 = f(u[m] + tau * 1 / 2 * w_2, alpha, beta, gamma)
    w_4 = f(u[m] + tau * 1 * w_3, alpha, beta, gamma)
    u[m + 1] = u[m] + tau * (1 / 6 * w_1 + 1 / 3 * w_2 + 1 / 3 * w_3 + 1 / 6 * w_4)

# зависимость x(t)
plt.plot(t, u[:, 0], color='red', label='ERK4')
plt.grid()
plt.xlim(0, 15)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.xlim()
plt.ylim()
plt.show()

# зависимость x'(t)
plt.plot(t, u[:, 1])
plt.grid()
plt.xlim(0, 15)
plt.xlabel("t")
plt.ylabel("x'(t)")
plt.xlim()
plt.ylim()
plt.show()

# фазовый портрет
plt.plot(u[:, 0], u[:, 1])
plt.grid()
plt.xlabel("x(t)")
plt.ylabel("x'(t)")
plt.xlim()
plt.ylim()
plt.show()