import gym

gam = gym.make('CartPole-v0')
for i in range(50):
    cart = gam.reset()
    for t in range(100):
        gam.render()
        print(cart)
        action = gam.action_space.sample()
        sample, reward, done, info = gam.step(action)
