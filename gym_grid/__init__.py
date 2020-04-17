# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 20:02:16 2020

@author: Kartik
"""

from gym.envs.registration import register

register(id='grid-v0',
         entry_point='gym_grid.envs:GridEnv',
         )