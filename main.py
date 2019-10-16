"""
Building a basic framework for :
1. main.py 
2. env.py
3. agent.py
4. model.py
5. replaybuffer.py
"""
from env import two_link_arm_env
from agent import DDPG

# Parameters
MAX_EPISODES = 500
MAX_TIME_STEPS = 200

# Set Environment
env = two_link_arm_env() # Name of the env
state_size = env.state_size # State Size 
action_size = env.action_size # Action Size
action_bound = env.action_bound # Action Bound

# Set Agent Algorithm Method
agent = DDPG(action_size, state_size, action_bound) # Setting DDPG as agent algorithm

# Training
for i_episode in range(MAX_EPISODES): # Iterating through Episodes
    state = env.reset()
    for i_step in range(MAX_TIME_STEPS): # Iterating through time-steps
        env.render()
        action = agent.act(state)
        state_, reward, done = env.step(action)

        agent.add_experience(state, action, reward, state_ )

        if agent.memory_full:
            # Start to learn once len(replay_buffer) > Batch_Size
            agent.learn()

        state = state_
    
    # Summary 
    """
    "env" 
    env.reset()
    env.render()
    env.step(action) 

    "agent"
    agent.act(state)
    agent.step(state, action, reward, next_state)
    agent.learn()
    agent.memory_full
    """