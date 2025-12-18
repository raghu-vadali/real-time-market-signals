# src/scoring/opportunity_scorer.py
# # Opportunity Scoring (This Powers “Top Opportunities”)

""" 1. abs(momentum) → “Is price actually moving?”
    2. volume_spike → “Is a lot of people interested in this?”
    3. 1 / volatility → “Is the price movement stable? or Is it tradable (not chaos)?” """
  
class OpportunityScorer:
    def score(self, features: dict) -> float:
        # Convert raw values (with weird scales) into comparable scores in the range [0, 1].
        momentum_score = min(abs(features["momentum"]) / 0.01, 1.0)
        volume_score = min(features["volume_spike"] / 3.0, 1.0)
        volatility_penalty = min(features["volatility"] / 0.01, 1.0)

        score = (
            0.5 * momentum_score +
            0.3 * volume_score -
            0.2 * volatility_penalty
        )
        
        score = max(0.0, min(score, 1.0))
        return round(float(score), 3)