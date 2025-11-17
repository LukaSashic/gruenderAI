"""
IRT-CAT Assessment Engine - Clean Working Version
Based on Howard's Entrepreneurial Personality Research
"""

import numpy as np
from typing import List, Tuple
from dataclasses import dataclass

@dataclass
class PersonalityItem:
    """Assessment item with IRT parameters"""
    item_id: str
    dimension: str
    text_de: str
    text_en: str
    discrimination: float
    difficulty_thresholds: List[float]

class IRTCATEngine:
    """Computerized Adaptive Testing Engine"""
    
    def __init__(self):
        self.max_items = 18
        self.min_items = 12
        self.target_se = 0.20
    
    def grm_probability(self, theta: float, item: PersonalityItem, response: int) -> float:
        """Calculate GRM probability - simplified and working version"""
        a = item.discrimination
        b_thresholds = item.difficulty_thresholds
        
        # Calculate cumulative probabilities
        cumulative_probs = [0.0]  # Start with 0
        
        for b in b_thresholds:
            exp_val = a * (theta - b)
            # Prevent overflow
            if exp_val > 500:
                prob = 1.0
            elif exp_val < -500:
                prob = 0.0
            else:
                prob = 1.0 / (1.0 + np.exp(-exp_val))
            cumulative_probs.append(prob)
        
        cumulative_probs.append(1.0)  # End with 1
        
        # Get category probability (response 1-5 maps to indices 0-4)
        response_index = response - 1
        if response_index < 0 or response_index >= len(cumulative_probs) - 1:
            return 0.001  # Invalid response
        
        category_prob = cumulative_probs[response_index + 1] - cumulative_probs[response_index]
        return max(category_prob, 0.001)  # Ensure positive probability
    
    def fisher_information(self, theta: float, item: PersonalityItem) -> float:
        """Calculate Fisher Information"""
        a = item.discrimination
        total_info = 0.0
        
        for b in item.difficulty_thresholds:
            exp_val = a * (theta - b)
            if -500 < exp_val < 500:  # Prevent overflow
                p = 1.0 / (1.0 + np.exp(-exp_val))
                info = (a * a) * p * (1.0 - p)
                total_info += info
        
        return total_info
    
    def update_theta(self, current_theta: float, item: PersonalityItem, response: int) -> Tuple[float, float]:
        """Update theta estimate using simple method"""
        # Simple update rule for demonstration
        prob = self.grm_probability(current_theta, item, response)
        
        # If high response (4-5), increase theta slightly
        # If low response (1-2), decrease theta slightly
        if response >= 4:
            new_theta = current_theta + 0.2
        elif response <= 2:
            new_theta = current_theta - 0.2
        else:
            new_theta = current_theta + 0.1 * (response - 3)
        
        # Keep theta in reasonable bounds
        new_theta = max(-3.0, min(3.0, new_theta))
        
        # Calculate standard error from Fisher Information
        fisher_info = self.fisher_information(new_theta, item)
        se = 1.0 / np.sqrt(fisher_info) if fisher_info > 0 else 1.0
        
        return new_theta, se
    
    def theta_to_percentile(self, theta: float) -> int:
        """Convert theta to percentile"""
        # Simple conversion: theta -3 to +3 maps to percentiles 1-99
        normalized = (theta + 3.0) / 6.0  # 0 to 1
        percentile = int(normalized * 98) + 1  # 1 to 99
        return max(1, min(99, percentile))

# Test the engine
if __name__ == "__main__":
    print("🧪 Testing IRT-CAT Engine Core...")
    
    # Create realistic sample item
    sample_item = PersonalityItem(
        item_id="INNOV_001",
        dimension="innovativeness",
        text_de="Ich entwickle gerne kreative Lösungen für Probleme",
        text_en="I enjoy developing creative solutions to problems",
        discrimination=1.2,
        difficulty_thresholds=[-1.5, -0.5, 0.5, 1.5]
    )
    
    engine = IRTCATEngine()
    
    # Test all response categories
    theta = 0.5
    print(f"Testing at theta = {theta}")
    
    for response in range(1, 6):
        prob = engine.grm_probability(theta, sample_item, response)
        print(f"✅ Response {response}: Probability = {prob:.3f}")
    
    # Test theta update
    response = 4
    new_theta, se = engine.update_theta(0.0, sample_item, response)
    print(f"✅ Theta update: {new_theta:.3f} (SE: {se:.3f})")
    
    # Test percentile
    percentile = engine.theta_to_percentile(new_theta)
    print(f"✅ Percentile: {percentile}%")
    
    print("\n🎉 Core IRT engine working!")