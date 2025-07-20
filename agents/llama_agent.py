import openai
import os

class LLMBlackjackAgent:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def decide(self, observation):
        prompt = f"You are playing Blackjack. Your hand total is {observation['player_total']} and the dealer's visible card is {observation['dealer_card']}. Should you 'hit' or 'stand'?"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a professional Blackjack player."},
                {"role": "user", "content": prompt}
            ]
        )
        decision = response["choices"][0]["message"]["content"].strip().lower()
        return "hit" if "hit" in decision else "stand"