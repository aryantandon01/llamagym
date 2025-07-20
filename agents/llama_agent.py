# agents/llama_agent.py

from together import Together
from dotenv import load_dotenv
import os

load_dotenv()
client = Together()

class LLMBlackjackAgent:
    def __init__(self):
        self.model = "mistralai/Mixtral-8x7B-Instruct-v0.1"

    def decide(self, observation):
        prompt = (
            f"You are a professional Blackjack player. Your hand total is {observation['player_total']} "
            f"and the dealer's visible card is {observation['dealer_card']}. Should you 'hit' or 'stand'?"
        )
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        decision = response.choices[0].message.content.strip().lower()
        return "hit" if "hit" in decision else "stand"
