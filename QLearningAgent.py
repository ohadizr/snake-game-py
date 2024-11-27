import numpy as np


class QLearningAgent:
    def __init__(self, learning_rate=0.01, discount_factor=0.9, exploration_rate=1.0, exploration_decay_rate=0.99995, min_exploration_rate=0.10, action_space=5):
        self.q_table = {}
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay_rate = exploration_decay_rate
        self.min_exploration_rate = min_exploration_rate
        self.action_space = action_space
        self.rewards_list = []  # Store rewards for the last N episodes
        self.N = 10  # Check performance over the last 10 episodes

    def get_action(self, state):
        # Convert list to tuple to use it as a dictionary key
        state = tuple(state)
        if state not in self.q_table:
            self.q_table[state] = [0] * self.action_space

        if np.random.uniform(0, 1) < self.exploration_rate:
            return np.random.randint(self.action_space)
        else:
            return np.argmax(self.q_table[state])

    def learn(self, state, action, reward, next_state):
        state = tuple(state)  # Convert list to tuple
        next_state = tuple(next_state)

        if next_state not in self.q_table:
            self.q_table[next_state] = [0] * self.action_space

        old_value = self.q_table[state][action]
        next_max = np.max(self.q_table[next_state])

        new_value = (1 - self.learning_rate) * old_value + \
            self.learning_rate * (reward + self.discount_factor * next_max)
        self.q_table[state][action] = new_value

        # Append current reward to rewards_list and keep its size <= N
        self.rewards_list.append(reward)
        if len(self.rewards_list) > self.N:
            self.rewards_list.pop(0)

        # Adjust exploration rate based on recent performance
        # Average reward threshold set to 0, adjust as needed
        if self.exploration_rate < 0.12 and len(self.rewards_list) == self.N and np.mean(self.rewards_list) <= 0:
            self.exploration_rate += 0.05  # Increase exploration rate
            # Ensure it remains <= 1.0
            self.exploration_rate = min(1.0, self.exploration_rate)
        else:
            self.exploration_rate *= self.exploration_decay_rate
            self.exploration_rate = max(
                self.min_exploration_rate, self.exploration_rate)
