import numpy as np
import random

# Define the environment (maze)
maze = [
    [0, -1, 0, 0, 0],
    [0, -1, 0, -1, 0],
    [0, 0, 0, -1, 0],
    [-1, -1, 0, 0, 0],
    [0, 0, 0, -1, 1]
]

# Define parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate
episodes = 1000  # Number of episodes

# Initialize Q-table
q_table = np.zeros((5, 5, 4))

# Define actions: up, down, left, right
actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# Function to get next state
def get_next_state(state, action):
    next_state = (state[0] + action[0], state[1] + action[1])
    if next_state[0] < 0 or next_state[0] >= 5 or next_state[1] < 0 or next_state[1] >= 5:
        return state
    if maze[next_state[0]][next_state[1]] == -1:
        return state
    return next_state

print("Starting Q-Learning Training...")

# Training Q-Learning
for episode in range(episodes):
    state = (0, 0)
    steps = 0
    while state != (4, 4):
        if random.uniform(0, 1) < epsilon:
            action = random.choice(actions)
        else:
            action = actions[np.argmax(q_table[state[0], state[1]])]
        next_state = get_next_state(state, action)
        reward = maze[next_state[0]][next_state[1]]
        q_value = q_table[state[0], state[1], actions.index(action)]
        best_next_q = np.max(q_table[next_state[0], next_state[1]])
        q_table[state[0], state[1], actions.index(action)] = q_value + alpha * (reward + gamma * best_next_q - q_value)
        state = next_state
        steps += 1
        if steps > 100:  # Safety break to avoid infinite loops
            break

print("Training completed.")
print("Q-table:")
print(q_table)

# Print the path taken by the agent
state = (0, 0)
path = [state]
while state != (4, 4):
    action = actions[np.argmax(q_table[state[0], state[1]])]
    state = get_next_state(state, action)
    path.append(state)

print("Path taken by the agent:")
print(path)
