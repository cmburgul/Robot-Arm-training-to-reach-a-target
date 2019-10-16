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
TRAINING_MODE = True

# Set Environment
env = two_link_arm_env() # Name of the env
state_size = env.state_dim # State Size 
action_size = env.action_dim # Action Size
action_bound = env.action_bound # Action Bound

# Set Agent Algorithm Method
agent = DDPG(action_size, state_size, action_bound) # Setting DDPG as agent algorithm

# Training
def train(print_every = 100):
    scores_deque = deque(maxlen=print_every)
    scores = []
    for i_episode in range(MAX_EPISODES): # Iterating through Episodes
        state = env.reset()
        score = 0
        for i_step in range(MAX_TIME_STEPS): # Iterating through time-steps
            env.render()

            # Take actions
            action = agent.act(state)
            
            # Get next_state, reward, done
            next_state, reward, done = env.step(action)

            # Store the experience in replay buffer
            agent.step(state, action, reward, next_state )
            score += reward
            state = next_state

            if done:
                break

        scores_deque.append(score)
        scores.append(score)
        print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(scores_deque)), end=" ")
        if i_episode % print_every == 0:
            print('\rEpisode {}\t Average Score: {:.2f}'.format(i_episode, np.mean(scores_deque)))
    return scores

# Watch a Smart Agent!
def eval():
    agent.restore()
    env.render()
    env.viewer.set_vsync(True)
    s = env.reset()
    while True:
        env.render()
        a = agent.act(s)
        s, r, done = env.step(a)


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