# openAI-gym Reversi/Othello

This is original "Reversi env" for reinforcement learning.  

## Issues  
how to control early adaption for learning.  
how to control opponent invalid action.  

## Usage

1. append Reversi folder to gym/gym/envs/
2. add registration info for reversi to gym/gym/envs/__init__.py (refer to the end of the file)


## Script

```Python
import gym
env = gym.make('Reversi8x8-v0')
env.reset()
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        action = env.action_space.sample()
        print(action)
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            print(reward)
            break
```
