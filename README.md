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

```
   |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |
-------------------------------------------------------
1  |  O  |  O  |  O  |  O  |  O  |  O  |  O  |  O  |
-------------------------------------------------------
2  |  O  |  O  |  O  |  O  |  O  |  O  |  O  |  O  |
-------------------------------------------------------
3  |  O  |  O  |  O  |  O  |  O  |  O  |  O  |  O  |
-------------------------------------------------------
4  |  O  |  O  |  O  |  W  |  B  |  O  |  O  |  O  |
-------------------------------------------------------
5  |  O  |  O  |  O  |  B  |  W  |  O  |  O  |  O  |
-------------------------------------------------------
6  |  O  |  O  |  O  |  O  |  O  |  O  |  O  |  O  |
-------------------------------------------------------
7  |  O  |  O  |  O  |  O  |  O  |  O  |  O  |  O  |
-------------------------------------------------------
8  |  O  |  O  |  O  |  O  |  O  |  O  |  O  |  O  |
-------------------------------------------------------
```
