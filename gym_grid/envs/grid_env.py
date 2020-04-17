# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 20:03:39 2020

@author: Kartik
"""

import gym
from gym import error,spaces,utils
from gym.utils import seeding
import numpy as np

class GridEnv(gym.Env):
    metadata={'render.modes':['human']}
    
    def __init__(self): 
        self.state=np.zeros((5,5))
        self.terminal=[[0,0],[2,4],[4,1],[4,4]]
        self.reward=[-1,0]
        self.done=0
        self.counter=0
    
    def step(self,current_state,action): #current_state->a list of two numbers
        next_state=current_state 
        if action=='up':
            if current_state[0]!=0:
                next_state=[current_state[0]-1,current_state[1]]
        elif action=='down':
            if current_state[0]!=4:
                next_state=[current_state[0]+1,current_state[1]]
        elif action=='left':
            if current_state[1]!=0:
                next_state=[current_state[0],current_state[1]-1]
        else:
            if current_state[1]!=4:
                next_state=[current_state[0],current_state[1]+1]
        if next_state in self.terminal:
            reward=self.reward[1]
        else:
            reward=self.reward[0]
        
        return next_state,reward
        
    def reset(self): ##terminal_state->list of list of the indices of terminal states
        self.state=np.zeros((5,5))
        self.reward=[-1,0]
        self.done=0
        self.counter=0
        
    def render(self,mode='human',close=False):
        for i in range(5):
            for j in range(5):
                print(self.state[i][j]+" ")
            print("")
            
    def initialize_random(self):
        self.state=np.random.random(5,5)