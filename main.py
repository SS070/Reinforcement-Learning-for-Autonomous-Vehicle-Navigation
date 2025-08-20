import GameEnv
import pygame
import numpy as np
from ddqn_keras import DDQNAgent
from tensorflow.keras.models import load_model
from collections import deque
import random, math

class Game:
    TOTAL_GAMETIME = 1000
    N_EPISODES = 10000
    REPLACE_TARGET = 50

    def __init__(self):
        self.game = GameEnv.RacingEnv()
        self.game.fps = 45
        self.ddqn_agent = DDQNAgent(alpha=0.0005, gamma=0.99, n_actions=5, epsilon=1.00, epsilon_end=0.10,
                                    epsilon_dec=0.9995, replace_target=self.REPLACE_TARGET, batch_size=2048, input_dims=19)
        self.ddqn_scores = []
        self.eps_history = []

    def run(self):
        for e in range(self.N_EPISODES):
            self.game.reset()
            done = False
            score = 0
            counter = 0
            observation_, reward, done = self.game.step(0)
            observation = np.array(observation_)
            gtime = 0
            renderFlag = False
            if e % 10 == 0 and e > 0:
                renderFlag = True
            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                action = self.ddqn_agent.choose_action(observation)
                observation_, reward, done = self.game.step(action)
                observation_ = np.array(observation_)
                if reward == 0:
                    counter += 1
                    if counter > 100:
                        done = True
                else:
                    counter = 0
                score += reward
                self.ddqn_agent.remember(observation, action, reward, observation_, int(done))
                observation = observation_
                self.ddqn_agent.learn()
                gtime += 1
                if gtime >= self.TOTAL_GAMETIME:
                    done = True
                if renderFlag:
                    self.game.render(action)
            self.eps_history.append(self.ddqn_agent.epsilon)
            self.ddqn_scores.append(score)
            avg_score = np.mean(self.ddqn_scores[max(0, e-100):(e+1)])
            if e % self.REPLACE_TARGET == 0 and e > self.REPLACE_TARGET:
                self.ddqn_agent.update_network_parameters()
            if e % 10 == 0 and e > 10:
                self.ddqn_agent.save_model()
                print("save model")
            print('episode: ', e,'score: %.2f' % score, ' average score %.2f' % avg_score, ' epsolon: ',
                  self.ddqn_agent.epsilon, ' memory size', self.ddqn_agent.memory.mem_cntr % self.ddqn_agent.memory.mem_size)

if __name__ == "__main__":
    game = Game()
    game.run()