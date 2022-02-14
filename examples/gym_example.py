#!/usr/bin/env python3

import gym
import numpy as np
from botbowl import BotBowlEnv


def main():
    env = BotBowlEnv()
    steps = 0

    # Play 10 games
    for _ in range(10):
        done = False
        _, _, mask = env.reset()

        while not done:
            env.render(feature_layers=True)
            aa = np.where(mask > 0.0)[0]
            action_idx = np.random.choice(aa, 1)[0]
            (_, _, mask), _, done, _ = env.step(action_idx)
            steps += 1
            print(steps)


if __name__ == "__main__":
    main()
