from envs.blackjack_env import BlackjackEnv
from agents.llm_agent import LLMBlackjackAgent
from utils.logger import log
import time

if __name__ == "__main__":
    env = BlackjackEnv()
    agent = LLMBlackjackAgent()

    wins = 0
    losses = 0
    ties = 0

    for episode in range(5):
        obs = env.reset()
        done = False
        print(f"\n--- Game {episode + 1} ---")
        while not done:
            action = agent.decide(obs)
            log(f"Agent action: {action}")
            obs, reward, done = env.step(action)
            time.sleep(1)
        if reward == 1:
            log("Result: Agent wins!")
            wins += 1
        elif reward == -1:
            log("Result: Agent loses.")
            losses += 1
        else:
            log("Result: Tie.")
            ties += 1

    print(f"\nFinal stats => Wins: {wins}, Losses: {losses}, Ties: {ties}")