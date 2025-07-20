import random

class BlackjackEnv:
    def __init__(self):
        self.deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]*4
        self.player_hand = []
        self.dealer_hand = []

    def draw_card(self):
        return random.choice(self.deck)

    def reset(self):
        self.player_hand = [self.draw_card(), self.draw_card()]
        self.dealer_hand = [self.draw_card(), self.draw_card()]
        return self._get_obs()

    def _get_obs(self):
        return {
            "player_total": sum(self.player_hand),
            "dealer_card": self.dealer_hand[0]
        }

    def step(self, action):
        if action == "hit":
            self.player_hand.append(self.draw_card())
            if sum(self.player_hand) > 21:
                return self._get_obs(), -1, True  # busted
            else:
                return self._get_obs(), 0, False

        elif action == "stand":
            while sum(self.dealer_hand) < 17:
                self.dealer_hand.append(self.draw_card())
            player_total = sum(self.player_hand)
            dealer_total = sum(self.dealer_hand)

            if dealer_total > 21 or player_total > dealer_total:
                return self._get_obs(), 1, True
            elif player_total == dealer_total:
                return self._get_obs(), 0, True
            else:
                return self._get_obs(), -1, True

        else:
            raise ValueError("Invalid action")