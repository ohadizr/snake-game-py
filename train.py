from environment import SnakeEnvironment
from QLearningAgent import QLearningAgent
import pickle
import os

# Save and Load functions for Q-table


def save_q_table(agent, episode, filename="q_table.pkl"):
    with open(filename, 'wb') as file:
        data = {'q_table': agent.q_table, 'episode': episode,
                'exploration_rate': agent.exploration_rate}
        pickle.dump(data, file)


def load_q_table(agent, filename="q_table.pkl"):
    if not os.path.exists(filename):
        print("No existing Q-table found. Starting fresh!")
        return 0

    with open(filename, 'rb') as file:
        data = pickle.load(file)
        agent.q_table = data['q_table']
        last_episode = data.get('episode', 0)
        agent.exploration_rate = data.get('exploration_rate', 1.0)

        print(
            f"Loaded Q-table from episode {last_episode}. Resuming training!")
        print(f"Current exploration rate: {agent.exploration_rate}")

        return last_episode


# Initialize the environment and the agent
env = SnakeEnvironment()
agent = QLearningAgent()

last_episode = 0
last_episode = load_q_table(agent)

NUM_EPISODES = 1000
MAX_STEPS = 500

for episode in range(last_episode, NUM_EPISODES + last_episode):
    state = env.reset()
    done = False
    total_reward = 0

    for step in range(MAX_STEPS):
        action = agent.get_action(state)
        next_state, reward, done = env.step(action)
        env.render()  # This will visualize the game after each step
        agent.learn(state, action, reward, next_state)
        state = next_state
        total_reward += reward

        if done:
            break

    print(
        f"Episode: {episode}, Total Reward: {total_reward}, Steps: {step}, Exploration Rate: {agent.exploration_rate}")

    # Optionally, save Q-table every 100 episodes or so
    if episode % 100 == 0:
        save_q_table(agent, episode)

# Save Q-table after all training episodes
save_q_table(agent, episode)

env.close()  # Close the environment after training
