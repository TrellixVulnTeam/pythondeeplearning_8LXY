import gym
spa = gym.make('MountainCar-v0')
for i in range(50):
    motor = spa.reset()
    for t in range(100):
        spa.render()
        print(motor)
        action = spa.action_space.sample()
        sample, reward, done, info = spa.step(action)
