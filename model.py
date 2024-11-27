# import numpy as np
# import tensorflow as tf
# from environment import SnakeEnvironment


# class DQN:
#     def __init__(self):
#         self.model = self.create_model()
#         self.env = SnakeEnvironment()
#         self.gamma = 0.95  # discount factor

#     def create_model(self):
#         model = tf.keras.Sequential([
#             # snake's head x, y and food's x, y
#             tf.keras.layers.Input(shape=(4,)),
#             tf.keras.layers.Dense(256, activation='relu'),
#             tf.keras.layers.Dense(128, activation='relu'),
#             # 4 actions: up, down, left, right
#             tf.keras.layers.Dense(4, activation='linear')
#         ])
#         model.compile(optimizer='adam', loss='mse')
#         return model

#     def train(self, episodes):
#         for episode in range(episodes):
#             state = self.env.reset()
#             done = False
#             while not done:
#                 action = np.argmax(self.model.predict(np.array([state]))[0])
#                 next_state, reward, done = self.env.step(action)
#                 target = reward
#                 if not done:
#                     target = reward + self.gamma * \
#                         np.max(self.model.predict(np.array([next_state]))[0])
#                 target_f = self.model.predict(np.array([state]))
#                 target_f[0][action] = target
#                 self.model.train_on_batch(np.array([state]), target_f)
#                 state = next_state
#                 if done:
#                     print(
#                         f"episode: {episode}/{episodes}, score: {self.env.scoreboard.score}")

#     def save_model(self, path):
#         self.model.save(path)

#     def load_model(self, path):
#         self.model = tf.keras.models.load_model(path)


# # Example usage:
# dqn = DQN()
# dqn.train(1000)
# dqn.save_model("snake_model.h5")
