"""
Interactive Assessment Session Simulator
Shows how users experience the adaptive IRT-CAT assessment
"""

from irt_cat_engine import IRTCATEngine
from sample_items import create_sample_item_bank
import random

class AssessmentSession:
    """Simulates a complete user assessment session"""
    
    def __init__(self):
        self.engine = IRTCATEngine()
        self.items = create_sample_item_bank()
        self.user_responses = []
        self.theta_estimates = {}
        self.administered_items = []
        
        # Initialize theta for all dimensions
        for dimension in ["innovativeness", "risk_taking", "achievement_orientation", 
                         "autonomy_orientation", "proactiveness", "locus_of_control", "self_efficacy"]:
            self.theta_estimates[dimension] = 0.0
    
    def select_next_question(self):
        """Select next question using IRT-CAT logic"""
        # Find dimension with highest uncertainty (for demo)
        available_items = [item for item in self.items if item.item_id not in self.administered_items]
        
        if not available_items:
            return None
        
        # Get dimensions of already administered items
        administered_item_objects = [item for item in self.items if item.item_id in self.administered_items]
        dimensions_asked = [item.dimension for item in administered_item_objects]
        for item in available_items:
            if item.dimension not in dimensions_asked:
                return item
        
        # Fallback: random available item
        return random.choice(available_items)
    
    def process_response(self, item, response):
        """Process user response and update estimates"""
        self.user_responses.append((item.item_id, response))
        self.administered_items.append(item.item_id)
        
        # Update theta estimate for this dimension
        current_theta = self.theta_estimates[item.dimension]
        new_theta, se = self.engine.update_theta(current_theta, item, response)
        self.theta_estimates[item.dimension] = new_theta
        
        print(f"   → {item.dimension} updated: θ = {new_theta:.2f}")
    
    def get_final_scores(self):
        """Convert theta to percentiles for user-friendly results"""
        scores = {}
        for dimension, theta in self.theta_estimates.items():
            percentile = self.engine.theta_to_percentile(theta)
            scores[dimension] = {
                'percentile': percentile,
                'theta': theta,
                'interpretation': self.interpret_score(percentile)
            }
        return scores
    
    def interpret_score(self, percentile):
        """Interpret percentile scores"""
        if percentile >= 80:
            return "Sehr hoch"
        elif percentile >= 60:
            return "Hoch" 
        elif percentile >= 40:
            return "Mittel"
        elif percentile >= 20:
            return "Niedrig"
        else:
            return "Sehr niedrig"

def simulate_assessment():
    """Run interactive assessment simulation"""
    print("🎯 GRUENDERAI PERSONALITY ASSESSMENT SIMULATION")
    print("=" * 55)
    print("Basierend auf Howard's 7-Dimensionen Forschung")
    print("Adaptive IRT-CAT Technologie")
    print("=" * 55)
    
    session = AssessmentSession()
    
    # Simulate 5 questions
    for question_num in range(1, 6):
        print(f"\n📋 FRAGE {question_num}/5")
        print("-" * 30)
        
        # Select next question
        item = session.select_next_question()
        if not item:
            break
        
        print(f"Dimension: {item.dimension.replace('_', ' ').title()}")
        print(f"Frage: {item.text_de}")
        print()
        print("Antwortmöglichkeiten:")
        print("1 = Stimme überhaupt nicht zu")
        print("2 = Stimme eher nicht zu") 
        print("3 = Neutral")
        print("4 = Stimme eher zu")
        print("5 = Stimme völlig zu")
        
        # Get user input
        while True:
            try:
                response = int(input("\nIhre Antwort (1-5): "))
                if 1 <= response <= 5:
                    break
                else:
                    print("Bitte eine Zahl zwischen 1 und 5 eingeben.")
            except ValueError:
                print("Bitte eine gültige Zahl eingeben.")
        
        # Process response
        session.process_response(item, response)
    
    # Show final results
    print("\n" + "=" * 55)
    print("📊 IHRE PERSÖNLICHKEITSAUSWERTUNG")
    print("=" * 55)
    
    scores = session.get_final_scores()
    
    for dimension, data in scores.items():
        dim_name = dimension.replace('_', ' ').title()
        print(f"\n🎯 {dim_name}:")
        print(f"   Percentil: {data['percentile']}% ({data['interpretation']})")
        print(f"   Theta: {data['theta']:.2f}")
    
    print("\n" + "=" * 55)
    print("🎉 Assessment abgeschlossen!")
    print("Bereit für Geschäftsmodell-Empfehlungen!")
    print("=" * 55)

if __name__ == "__main__":
    simulate_assessment()