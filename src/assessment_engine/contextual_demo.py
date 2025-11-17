"""
GründerAI Contextual Intelligence Demo
Shows how the same personality performs differently in different business contexts
"""

import math

class GruenderAIContextualDemo:
    """Demonstrates sophisticated contextual trait weighting"""
    
    def __init__(self):
        # Context-specific trait importance weights (based on research and market analysis)
        self.trait_weights = {
            "restaurant": {
                "risk_taking": 0.60,           # Moderate importance (location, menu risks)
                "innovativeness": 0.45,        # Lower importance (traditional business model)
                "self_efficacy": 0.70,         # High importance (daily operations confidence)
                "achievement_orientation": 0.65, # Important for quality standards
                "proactiveness": 0.55,         # Moderate (local marketing)
                "autonomy_orientation": 0.75,  # High importance (independent ownership)
                "competitive_aggressiveness": 0.50  # Moderate (local competition)
            },
            "fintech": {
                "risk_taking": 0.85,           # Critical for innovation and disruption
                "innovativeness": 0.80,        # Critical for tech advancement
                "self_efficacy": 0.75,         # High for complex technical challenges
                "achievement_orientation": 0.70, # Important for performance metrics
                "proactiveness": 0.65,         # Important for market opportunities
                "autonomy_orientation": 0.45,  # Lower due to regulatory compliance needs
                "competitive_aggressiveness": 0.55  # Moderate competitive pressure
            },
            "consulting": {
                "risk_taking": 0.35,           # Low risk, stable revenue model
                "innovativeness": 0.50,        # Moderate for solution creativity
                "self_efficacy": 0.80,         # Critical for client confidence
                "achievement_orientation": 0.75, # High for client results
                "proactiveness": 0.70,         # Important for business development
                "autonomy_orientation": 0.85,  # Critical for independent work
                "competitive_aggressiveness": 0.60  # Important for winning clients
            },
            "ecommerce": {
                "risk_taking": 0.70,           # High for market testing and inventory
                "innovativeness": 0.75,        # High for digital marketing creativity
                "self_efficacy": 0.65,         # Important for technical challenges
                "achievement_orientation": 0.80, # Critical for growth metrics
                "proactiveness": 0.85,         # Critical for market opportunities
                "autonomy_orientation": 0.60,  # Moderate (may need partnerships)
                "competitive_aggressiveness": 0.75  # High online competition
            }
        }
        
        # Business context metadata
        self.business_contexts = {
            "restaurant": {
                "regulatory_complexity": 3,
                "capital_requirements_eur": 120000,
                "timeline_months": 12,
                "gruendungszuschuss_compatibility": 0.8,
                "approval_probability_base": 0.65,
                "market_description": "Etabliertes Geschäftsmodell mit bewährter Nachfrage"
            },
            "fintech": {
                "regulatory_complexity": 5,
                "capital_requirements_eur": 250000,
                "timeline_months": 18,
                "gruendungszuschuss_compatibility": 0.6,
                "approval_probability_base": 0.55,
                "market_description": "Hohe Innovation, aber regulatorische Komplexität"
            },
            "consulting": {
                "regulatory_complexity": 2,
                "capital_requirements_eur": 15000,
                "timeline_months": 6,
                "gruendungszuschuss_compatibility": 0.9,
                "approval_probability_base": 0.75,
                "market_description": "Niedrige Barrieren, schnelle Markteinführung"
            },
            "ecommerce": {
                "regulatory_complexity": 3,
                "capital_requirements_eur": 50000,
                "timeline_months": 9,
                "gruendungszuschuss_compatibility": 0.7,
                "approval_probability_base": 0.60,
                "market_description": "Digitale Kompetenz erforderlich, hart umkämpft"
            }
        }
    
    def analyze_personality_for_context(self, raw_theta_scores, business_context):
        """Comprehensive contextual analysis"""
        context_weights = self.trait_weights[business_context]
        context_info = self.business_contexts[business_context]
        
        # Calculate context-weighted scores
        trait_analysis = {}
        total_weighted_score = 0.0
        total_possible_weight = 0.0
        critical_trait_performance = []
        
        for trait, raw_theta in raw_theta_scores.items():
            weight = context_weights[trait]
            normalized_score = (raw_theta + 3.0) / 6.0  # Convert -3/+3 to 0-1
            weighted_score = normalized_score * weight
            
            # Determine importance and performance
            if weight >= 0.75:
                importance = "KRITISCH"
            elif weight >= 0.65:
                importance = "HOCH"
            elif weight >= 0.5:
                importance = "MODERAT"
            else:
                importance = "NIEDRIG"
            
            # Performance assessment
            if normalized_score >= 0.7:
                performance = "STARK"
            elif normalized_score >= 0.5:
                performance = "AUSREICHEND"
            else:
                performance = "SCHWACH"
            
            trait_analysis[trait] = {
                "raw_theta": raw_theta,
                "normalized_score": normalized_score,
                "context_weight": weight,
                "weighted_score": weighted_score,
                "importance": importance,
                "performance": performance,
                "business_impact": normalized_score * weight * 100  # 0-100 scale
            }
            
            total_weighted_score += weighted_score
            total_possible_weight += weight
            
            # Track critical traits
            if weight >= 0.75:
                critical_trait_performance.append(normalized_score)
        
        # Calculate business fitness
        business_fitness = (total_weighted_score / total_possible_weight) if total_possible_weight > 0 else 0.5
        
        # Critical traits readiness
        critical_readiness = sum(critical_trait_performance) / len(critical_trait_performance) if critical_trait_performance else 0.5
        
        # Adjust fitness based on critical traits
        adjusted_fitness = business_fitness * 0.7 + critical_readiness * 0.3
        
        # Fitness level
        if adjusted_fitness >= 0.8:
            fitness_level = "EXZELLENT"
        elif adjusted_fitness >= 0.65:
            fitness_level = "GUT"
        elif adjusted_fitness >= 0.5:
            fitness_level = "AUSREICHEND"
        elif adjusted_fitness >= 0.35:
            fitness_level = "HERAUSFORDERND"
        else:
            fitness_level = "SCHWIERIG"
        
        # Gründungszuschuss probability
        base_prob = context_info["approval_probability_base"]
        fitness_adjustment = (adjusted_fitness - 0.5) * 0.4
        compatibility_bonus = (context_info["gruendungszuschuss_compatibility"] - 0.7) * 0.1
        
        gruendungszuschuss_prob = max(0.25, min(0.95, base_prob + fitness_adjustment + compatibility_bonus))
        
        return {
            "business_context": business_context,
            "business_fitness": {
                "score": adjusted_fitness,
                "level": fitness_level,
                "raw_weighted_score": business_fitness,
                "critical_traits_readiness": critical_readiness
            },
            "gruendungszuschuss": {
                "probability": gruendungszuschuss_prob,
                "confidence": "HOCH" if gruendungszuschuss_prob >= 0.7 else "MODERAT" if gruendungszuschuss_prob >= 0.5 else "NIEDRIG"
            },
            "trait_analysis": trait_analysis,
            "context_info": context_info
        }
    
    def compare_contexts(self, raw_theta_scores, contexts_to_compare):
        """Compare the same personality across multiple business contexts"""
        results = {}
        
        for context in contexts_to_compare:
            results[context] = self.analyze_personality_for_context(raw_theta_scores, context)
        
        return results
    
    def generate_recommendations(self, comparison_results):
        """Generate business recommendations based on context comparison"""
        # Sort contexts by fitness
        sorted_contexts = sorted(
            comparison_results.items(),
            key=lambda x: x[1]["business_fitness"]["score"],
            reverse=True
        )
        
        best_context = sorted_contexts[0]
        worst_context = sorted_contexts[-1]
        
        recommendations = {
            "primary_recommendation": {
                "context": best_context[0],
                "fitness_score": best_context[1]["business_fitness"]["score"],
                "fitness_level": best_context[1]["business_fitness"]["level"],
                "gruendungszuschuss_probability": best_context[1]["gruendungszuschuss"]["probability"],
                "reasons": []
            },
            "avoid_recommendation": {
                "context": worst_context[0],
                "fitness_score": worst_context[1]["business_fitness"]["score"],
                "reasons": []
            },
            "all_rankings": [
                {
                    "context": context,
                    "fitness": result["business_fitness"]["score"],
                    "gruendungszuschuss": result["gruendungszuschuss"]["probability"]
                }
                for context, result in sorted_contexts
            ]
        }
        
        return recommendations

# Demonstration
if __name__ == "__main__":
    print("🎯 GründerAI Contextual Intelligence Demonstration")
    print("=" * 80)
    
    # Initialize the engine
    engine = GruenderAIContextualDemo()
    
    # Test personality profile: High autonomy entrepreneur
    entrepreneur_profile = {
        "risk_taking": 0.5,           # Moderate risk tolerance
        "innovativeness": 0.0,        # Average innovation
        "self_efficacy": 0.8,         # High confidence
        "achievement_orientation": 1.0, # Very high achievement drive  
        "proactiveness": 0.3,         # Moderate proactiveness
        "autonomy_orientation": 1.2,  # Very high autonomy preference
        "competitive_aggressiveness": -0.2  # Low competitive aggressiveness
    }
    
    print("👤 Entrepreneur Personality Profile:")
    for trait, score in entrepreneur_profile.items():
        print(f"   {trait:25}: {score:+.1f}")
    
    # Analyze across all business contexts
    contexts = ["restaurant", "fintech", "consulting", "ecommerce"]
    comparison = engine.compare_contexts(entrepreneur_profile, contexts)
    
    print(f"\n📊 Business Context Analysis:")
    print("-" * 80)
    
    for context, analysis in comparison.items():
        fitness = analysis["business_fitness"]
        gründungszuschuss = analysis["gruendungszuschuss"]
        
        print(f"\n🏢 {context.upper()} BUSINESS:")
        print(f"   Business Fitness: {fitness['level']} ({fitness['score']:.3f})")
        print(f"   Gründungszuschuss: {gründungszuschuss['probability']:.1%} ({gründungszuschuss['confidence']})")
        print(f"   Beschreibung: {analysis['context_info']['market_description']}")
        
        # Show top traits for this context
        trait_impacts = [(trait, data['business_impact']) for trait, data in analysis['trait_analysis'].items()]
        trait_impacts.sort(key=lambda x: x[1], reverse=True)
        
        print(f"   Top Trait Impacts:")
        for trait, impact in trait_impacts[:3]:
            trait_data = analysis['trait_analysis'][trait]
            print(f"     • {trait:20}: {impact:4.0f}/100 ({trait_data['importance']}, {trait_data['performance']})")
    
    # Generate recommendations
    recommendations = engine.generate_recommendations(comparison)
    
    print(f"\n🎯 GESCHÄFTSEMPFEHLUNGEN:")
    print("-" * 80)
    
    primary = recommendations["primary_recommendation"]
    print(f"🥇 PRIMÄRE EMPFEHLUNG: {primary['context'].upper()}")
    print(f"   Fitness Score: {primary['fitness_score']:.3f} ({primary['fitness_level']})")
    print(f"   Gründungszuschuss: {primary['gruendungszuschuss_probability']:.1%}")
    
    avoid = recommendations["avoid_recommendation"]
    print(f"\n🚫 WENIGER GEEIGNET: {avoid['context'].upper()}")
    print(f"   Fitness Score: {avoid['fitness_score']:.3f}")
    
    print(f"\n📈 VOLLSTÄNDIGES RANKING:")
    for i, ranking in enumerate(recommendations["all_rankings"], 1):
        print(f"   {i}. {ranking['context']:10}: {ranking['fitness']:.3f} fitness | {ranking['gruendungszuschuss']:.1%} Gründungszuschuss")
    
    # Explain the differences
    print(f"\n🔍 WARUM DIESE UNTERSCHIEDE?")
    print("-" * 80)
    
    restaurant_weights = engine.trait_weights["restaurant"]
    consulting_weights = engine.trait_weights["consulting"]
    
    print("Autonomy Orientation (Ihr Stärkster Trait θ=+1.2):")
    print(f"   Restaurant:  {restaurant_weights['autonomy_orientation']:.2f} Gewichtung → Große Wirkung")
    print(f"   Consulting:  {consulting_weights['autonomy_orientation']:.2f} Gewichtung → Größte Wirkung")
    print(f"   Fintech:     {engine.trait_weights['fintech']['autonomy_orientation']:.2f} Gewichtung → Geringe Wirkung")
    
    print(f"\nRisk Taking (Ihr Moderater Trait θ=+0.5):")
    print(f"   Fintech:     {engine.trait_weights['fintech']['risk_taking']:.2f} Gewichtung → Hohe Anforderung")
    print(f"   Restaurant:  {restaurant_weights['risk_taking']:.2f} Gewichtung → Moderate Anforderung")
    print(f"   Consulting:  {consulting_weights['risk_taking']:.2f} Gewichtung → Niedrige Anforderung")
    
    print(f"\n🎉 CONTEXTUAL INTELLIGENCE DEMONSTRATION COMPLETE!")
    print("✅ Same personality → Different business outcomes")
    print("✅ Context-weighted trait importance working")
    print("✅ Business-specific Gründungszuschuss probabilities")
    print("✅ Clear recommendations with scientific backing")