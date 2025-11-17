"""
GründerAI Integrated Assessment System - Phase 3 Complete
The most sophisticated entrepreneurial personality assessment and business intelligence platform

Integrates:
- Advanced IRT-CAT adaptive testing
- Contextual trait weighting
- Friction analysis and intervention mandates
- Gründungszuschuss optimization
- Comprehensive business intelligence
"""

import json
import math
import random
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional, Any
import statistics

# Import our components (standalone versions for demo)
class IntegratedGruenderAI:
    """
    Complete GründerAI Assessment System
    Transforms personality assessment into sophisticated business intelligence
    """
    
    def __init__(self):
        # Initialize all subsystems
        self.initialize_irt_system()
        self.initialize_contextual_scoring()
        self.initialize_friction_analysis()
        self.initialize_business_intelligence()
        
        print("🚀 GründerAI Integrated Assessment System Initialized")
        print("   ✅ Advanced IRT-CAT Engine")
        print("   ✅ Contextual Trait Weighting")
        print("   ✅ Friction Analysis & Intervention Mandates")
        print("   ✅ Business Intelligence & Gründungszuschuss Optimization")
        print("   ✅ Complete Assessment Pipeline Ready")
    
    def initialize_irt_system(self):
        """Initialize IRT-CAT assessment engine"""
        # Simplified IRT item bank for demo
        self.item_bank = [
            {
                "item_id": "risk_001",
                "dimension": "risk_taking",
                "text_de": "Ich bin bereit, finanzielle Risiken einzugehen, um mein Geschäft voranzubringen",
                "discrimination": 1.2,
                "difficulty": 0.5,
                "business_context": "general",
                "interaction_target": "risk_achievement_friction"
            },
            {
                "item_id": "autonomy_001", 
                "dimension": "autonomy_orientation",
                "text_de": "Ich arbeite am besten, wenn ich völlige Kontrolle über meine Aufgaben habe",
                "discrimination": 1.4,
                "difficulty": 0.0,
                "business_context": "general",
                "interaction_target": "autonomy_self_efficacy_friction"
            },
            {
                "item_id": "efficacy_001",
                "dimension": "self_efficacy", 
                "text_de": "Ich bin zuversichtlich, auch schwierige Geschäftsprobleme lösen zu können",
                "discrimination": 1.3,
                "difficulty": -0.2,
                "business_context": "general",
                "interaction_target": "autonomy_self_efficacy_friction"
            },
            {
                "item_id": "innovation_001",
                "dimension": "innovativeness",
                "text_de": "Ich entwickle gerne völlig neue Lösungsansätze für bestehende Probleme",
                "discrimination": 1.1,
                "difficulty": 0.3,
                "business_context": "fintech",
                "interaction_target": "innovation_autonomy_synergy"
            },
            {
                "item_id": "achievement_001",
                "dimension": "achievement_orientation",
                "text_de": "Ich setze mir sehr hohe Leistungsstandards und arbeite hart, um sie zu erreichen",
                "discrimination": 1.0,
                "difficulty": 0.1,
                "business_context": "general",
                "interaction_target": "risk_achievement_friction"
            },
            {
                "item_id": "proactive_001",
                "dimension": "proactiveness",
                "text_de": "Ich erkenne Geschäftschancen, bevor andere sie sehen",
                "discrimination": 1.3,
                "difficulty": 0.7,
                "business_context": "ecommerce",
                "interaction_target": "proactiveness_efficacy_friction"
            },
            {
                "item_id": "competitive_001",
                "dimension": "competitive_aggressiveness",
                "text_de": "Ich bin entschlossen, meine Konkurrenten zu übertreffen",
                "discrimination": 1.2,
                "difficulty": 0.4,
                "business_context": "general",
                "interaction_target": "innovation_competition_friction"
            }
        ]
        
        self.dimensions = [
            "risk_taking", "innovativeness", "self_efficacy", 
            "achievement_orientation", "proactiveness", 
            "autonomy_orientation", "competitive_aggressiveness"
        ]
    
    def initialize_contextual_scoring(self):
        """Initialize contextual trait weighting system"""
        self.trait_weights = {
            "fintech": {
                "risk_taking": 0.85, "innovativeness": 0.80, "self_efficacy": 0.75,
                "achievement_orientation": 0.70, "proactiveness": 0.65,
                "autonomy_orientation": 0.45, "competitive_aggressiveness": 0.55
            },
            "consulting": {
                "risk_taking": 0.35, "innovativeness": 0.50, "self_efficacy": 0.80,
                "achievement_orientation": 0.75, "proactiveness": 0.70,
                "autonomy_orientation": 0.85, "competitive_aggressiveness": 0.60
            },
            "restaurant": {
                "risk_taking": 0.60, "innovativeness": 0.45, "self_efficacy": 0.70,
                "achievement_orientation": 0.65, "proactiveness": 0.55,
                "autonomy_orientation": 0.75, "competitive_aggressiveness": 0.50
            },
            "ecommerce": {
                "risk_taking": 0.70, "innovativeness": 0.75, "self_efficacy": 0.65,
                "achievement_orientation": 0.80, "proactiveness": 0.85,
                "autonomy_orientation": 0.60, "competitive_aggressiveness": 0.75
            }
        }
        
        self.business_contexts = {
            "fintech": {
                "regulatory_complexity": 5, "capital_requirements": 250000,
                "gruendungszuschuss_compatibility": 0.6, "approval_probability_base": 0.55
            },
            "consulting": {
                "regulatory_complexity": 2, "capital_requirements": 15000,
                "gruendungszuschuss_compatibility": 0.9, "approval_probability_base": 0.75
            },
            "restaurant": {
                "regulatory_complexity": 3, "capital_requirements": 120000,
                "gruendungszuschuss_compatibility": 0.8, "approval_probability_base": 0.65
            },
            "ecommerce": {
                "regulatory_complexity": 3, "capital_requirements": 50000,
                "gruendungszuschuss_compatibility": 0.7, "approval_probability_base": 0.60
            }
        }
    
    def initialize_friction_analysis(self):
        """Initialize friction detection and intervention system"""
        self.friction_patterns = {
            "autonomy_self_efficacy_friction": {
                "traits": ["autonomy_orientation", "self_efficacy"],
                "conditions": {"autonomy_orientation": {"operator": ">=", "threshold": 0.6},
                             "self_efficacy": {"operator": "<=", "threshold": -0.5}},
                "severity_multiplier": 0.8,
                "description": "Hohe Autonomie mit geringer Selbstwirksamkeit führt zu Delegationsproblemen"
            },
            "risk_achievement_friction": {
                "traits": ["risk_taking", "achievement_orientation"],
                "conditions": {"risk_taking": {"operator": ">=", "threshold": 0.5},
                             "achievement_orientation": {"operator": "<=", "threshold": -0.3}},
                "severity_multiplier": 0.7,
                "description": "Hohe Risikobereitschaft ohne Leistungsorientierung führt zu unvorsichtigen Entscheidungen"
            },
            "innovation_autonomy_synergy": {
                "traits": ["innovativeness", "autonomy_orientation"],
                "conditions": {"innovativeness": {"operator": ">=", "threshold": 0.4},
                             "autonomy_orientation": {"operator": ">=", "threshold": 0.4}},
                "severity_multiplier": -0.6,  # Positive synergy
                "description": "Hohe Innovation und Autonomie verstärken sich gegenseitig positiv"
            }
        }
        
        self.intervention_mandates = {
            "delegation_paralysis": {
                "title": "Das Graduierte Delegations-Protokoll",
                "urgency": 4, "timeline": "4-6 Wochen",
                "phases": ["Micro-Delegation", "Structured Check-ins", "Responsibility Escalation"]
            },
            "reckless_decision_making": {
                "title": "Das Systematische Risiko-Management-Framework", 
                "urgency": 5, "timeline": "2-3 Wochen",
                "phases": ["Risk Matrix Creation", "Decision Approval Process", "Risk Review Meetings"]
            }
        }
    
    def initialize_business_intelligence(self):
        """Initialize business intelligence and recommendation system"""
        self.assessment_sessions = {}
        self.session_analytics = {
            "total_sessions": 0,
            "average_completion_time": 0,
            "context_distribution": {"fintech": 0, "consulting": 0, "restaurant": 0, "ecommerce": 0},
            "friction_detection_rate": 0.0
        }
    
    def start_adaptive_assessment(self, user_id: str, business_context: str, 
                                target_se: float = 0.20, max_items: int = 15) -> str:
        """
        Start adaptive assessment with context-aware item selection
        
        Args:
            user_id: Unique user identifier
            business_context: Target business context
            target_se: Target standard error for stopping
            max_items: Maximum number of items
        
        Returns:
            Session ID for the assessment
        """
        session_id = str(uuid.uuid4())
        
        # Initialize session
        session = {
            "session_id": session_id,
            "user_id": user_id,
            "business_context": business_context,
            "start_time": datetime.now(),
            "target_se": target_se,
            "max_items": max_items,
            
            # Assessment state
            "current_item": 0,
            "theta_estimates": {dim: 0.0 for dim in self.dimensions},
            "se_estimates": {dim: 1.0 for dim in self.dimensions},
            "administered_items": [],
            "responses": [],
            
            # Context-aware features
            "context_weights": self.trait_weights[business_context],
            "detected_frictions": [],
            "real_time_recommendations": [],
            
            # Completion status
            "is_complete": False,
            "completion_reason": None
        }
        
        self.assessment_sessions[session_id] = session
        self.session_analytics["total_sessions"] += 1
        self.session_analytics["context_distribution"][business_context] += 1
        
        print(f"🎯 Assessment Session Started")
        print(f"   Session ID: {session_id}")
        print(f"   Business Context: {business_context}")
        print(f"   Target SE: {target_se}")
        print(f"   Max Items: {max_items}")
        
        return session_id
    
    def get_next_item(self, session_id: str) -> Optional[Dict]:
        """
        Get next adaptive item with context-aware selection
        
        Args:
            session_id: Assessment session ID
        
        Returns:
            Next item to administer or None if assessment complete
        """
        session = self.assessment_sessions.get(session_id)
        if not session or session["is_complete"]:
            return None
        
        # Check stopping criteria
        if self.should_stop_assessment(session):
            return self.complete_assessment(session_id)
        
        # Context-aware item selection
        business_context = session["business_context"]
        administered_items = set(session["administered_items"])
        current_thetas = session["theta_estimates"]
        
        # Available items
        available_items = [item for item in self.item_bank 
                          if item["item_id"] not in administered_items]
        
        if not available_items:
            return self.complete_assessment(session_id)
        
        # Enhanced item selection algorithm
        best_item = None
        max_information = -1
        
        for item in available_items:
            dimension = item["dimension"]
            current_theta = current_thetas[dimension]
            
            # Calculate Fisher Information (simplified)
            fisher_info = self.calculate_fisher_information(current_theta, item)
            
            # Apply contextual weighting
            context_weight = session["context_weights"].get(dimension, 0.5)
            weighted_info = fisher_info * context_weight
            
            # Bonus for interaction detection
            interaction_bonus = 0.0
            if item.get("interaction_target"):
                interaction_bonus = self.assess_interaction_information_need(
                    current_thetas, item["interaction_target"]
                ) * 0.3
            
            # Business context preference
            context_bonus = 0.2 if item["business_context"] == business_context else 0.0
            
            total_information = weighted_info + interaction_bonus + context_bonus
            
            if total_information > max_information:
                max_information = total_information
                best_item = item
        
        if best_item:
            session["administered_items"].append(best_item["item_id"])
            session["current_item"] += 1
            
            # Real-time friction monitoring
            self.monitor_real_time_friction(session)
        
        return best_item
    
    def submit_response(self, session_id: str, item_id: str, response: int) -> Dict:
        """
        Submit item response and update estimates
        
        Args:
            session_id: Assessment session ID
            item_id: Item identifier
            response: Response value (1-5 Likert scale)
        
        Returns:
            Updated assessment status
        """
        session = self.assessment_sessions.get(session_id)
        if not session:
            return {"error": "Session not found"}
        
        # Find the item
        item = next((item for item in self.item_bank if item["item_id"] == item_id), None)
        if not item:
            return {"error": "Item not found"}
        
        # Store response
        response_data = {
            "item_id": item_id,
            "dimension": item["dimension"],
            "response": response,
            "timestamp": datetime.now()
        }
        session["responses"].append(response_data)
        
        # Update theta estimates (simplified IRT update)
        dimension = item["dimension"]
        self.update_theta_estimate(session, item, response)
        
        # Real-time friction detection
        detected_frictions = self.detect_real_time_friction(session)
        if detected_frictions:
            session["detected_frictions"].extend(detected_frictions)
        
        return {
            "status": "response_recorded",
            "items_completed": len(session["responses"]),
            "current_theta": session["theta_estimates"][dimension],
            "detected_frictions": len(session["detected_frictions"]),
            "assessment_complete": session["is_complete"]
        }
    
    def calculate_fisher_information(self, theta: float, item: Dict) -> float:
        """Calculate Fisher Information for item at theta level"""
        discrimination = item["discrimination"]
        difficulty = item.get("difficulty", 0.0)
        
        # Simplified Fisher Information calculation
        prob = 1 / (1 + math.exp(-discrimination * (theta - difficulty)))
        fisher_info = discrimination**2 * prob * (1 - prob)
        
        return fisher_info
    
    def update_theta_estimate(self, session: Dict, item: Dict, response: int):
        """Update theta estimate using simplified EAP estimation"""
        dimension = item["dimension"]
        
        # Convert Likert response (1-5) to dichotomous (0-1)
        # Responses 4-5 = 1 (agree), 1-3 = 0 (disagree)
        binary_response = 1 if response >= 4 else 0
        
        # Simplified theta update (in practice, use proper EAP/MAP)
        current_theta = session["theta_estimates"][dimension]
        discrimination = item["discrimination"]
        difficulty = item.get("difficulty", 0.0)
        
        # Simple update rule
        expected = 1 / (1 + math.exp(-discrimination * (current_theta - difficulty)))
        error = binary_response - expected
        learning_rate = 0.3
        
        new_theta = current_theta + learning_rate * error
        new_theta = max(-3.0, min(3.0, new_theta))  # Bound theta
        
        session["theta_estimates"][dimension] = new_theta
        
        # Update standard error (simplified)
        session["se_estimates"][dimension] *= 0.9  # Decrease SE with each response
    
    def should_stop_assessment(self, session: Dict) -> bool:
        """Determine if assessment should stop"""
        # Check maximum items
        if session["current_item"] >= session["max_items"]:
            session["completion_reason"] = "max_items_reached"
            return True
        
        # Check SE criteria for important traits
        target_se = session["target_se"]
        context_weights = session["context_weights"]
        
        important_traits_ready = 0
        total_important_traits = 0
        
        for dimension, se in session["se_estimates"].items():
            weight = context_weights.get(dimension, 0.5)
            if weight >= 0.65:  # Important trait
                total_important_traits += 1
                required_se = target_se * (0.8 if weight >= 0.8 else 0.9)
                if se <= required_se:
                    important_traits_ready += 1
        
        # Stop if 80% of important traits are ready
        if total_important_traits > 0:
            readiness_ratio = important_traits_ready / total_important_traits
            if readiness_ratio >= 0.8:
                session["completion_reason"] = "precision_criteria_met"
                return True
        
        # Minimum items check
        if session["current_item"] < 8:
            return False
        
        return False
    
    def monitor_real_time_friction(self, session: Dict):
        """Monitor for friction patterns during assessment"""
        if len(session["responses"]) < 3:  # Need minimum responses
            return
        
        current_thetas = session["theta_estimates"]
        
        for pattern_id, pattern in self.friction_patterns.items():
            friction_detected = True
            
            for trait, condition in pattern["conditions"].items():
                trait_theta = current_thetas.get(trait, 0.0)
                threshold = condition["threshold"]
                operator = condition["operator"]
                
                if operator == ">=" and trait_theta < threshold:
                    friction_detected = False
                    break
                elif operator == "<=" and trait_theta > threshold:
                    friction_detected = False
                    break
            
            if friction_detected:
                # Check if already detected
                existing = any(f["pattern_id"] == pattern_id for f in session["detected_frictions"])
                if not existing:
                    friction = {
                        "pattern_id": pattern_id,
                        "detection_time": datetime.now(),
                        "description": pattern["description"],
                        "severity": abs(pattern["severity_multiplier"]),
                        "type": "synergy" if pattern["severity_multiplier"] < 0 else "friction"
                    }
                    session["detected_frictions"].append(friction)
    
    def detect_real_time_friction(self, session: Dict) -> List[Dict]:
        """Detect new friction patterns"""
        # This would be called after each response
        # Implementation simplified for demo
        return []
    
    def assess_interaction_information_need(self, theta_estimates: Dict, interaction_target: str) -> float:
        """Assess information need for specific interaction"""
        if not interaction_target or interaction_target not in self.friction_patterns:
            return 0.0
        
        pattern = self.friction_patterns[interaction_target]
        involved_traits = pattern["traits"]
        
        # Calculate uncertainty for involved traits (simplified)
        total_uncertainty = 0.0
        for trait in involved_traits:
            # Higher theta variability = more uncertainty
            trait_theta = theta_estimates.get(trait, 0.0)
            uncertainty = 1.0 - min(1.0, abs(trait_theta) / 2.0)  # Simplified uncertainty
            total_uncertainty += uncertainty
        
        return total_uncertainty / len(involved_traits)
    
    def complete_assessment(self, session_id: str) -> Dict:
        """Complete assessment and generate comprehensive analysis"""
        session = self.assessment_sessions.get(session_id)
        if not session:
            return {"error": "Session not found"}
        
        session["is_complete"] = True
        session["end_time"] = datetime.now()
        session["completion_time"] = session["end_time"] - session["start_time"]
        
        # Generate comprehensive analysis
        analysis = self.generate_comprehensive_analysis(session)
        session["final_analysis"] = analysis
        
        print(f"✅ Assessment Complete - Session {session_id}")
        print(f"   Duration: {session['completion_time']}")
        print(f"   Items Administered: {len(session['responses'])}")
        print(f"   Reason: {session.get('completion_reason', 'unknown')}")
        
        return {
            "status": "assessment_complete",
            "session_id": session_id,
            "analysis": analysis
        }
    
    def generate_comprehensive_analysis(self, session: Dict) -> Dict:
        """Generate comprehensive business intelligence analysis"""
        business_context = session["business_context"]
        theta_estimates = session["theta_estimates"]
        detected_frictions = session["detected_frictions"]
        
        # 1. Contextual scoring analysis
        contextual_analysis = self.calculate_context_weighted_scores(
            theta_estimates, business_context
        )
        
        # 2. Friction analysis
        friction_analysis = self.analyze_detected_frictions(
            detected_frictions, theta_estimates, business_context
        )
        
        # 3. Business fitness assessment
        business_fitness = self.assess_business_fitness(
            contextual_analysis, friction_analysis, business_context
        )
        
        # 4. Gründungszuschuss optimization
        gruendungszuschuss_analysis = self.optimize_gruendungszuschuss_probability(
            business_fitness, business_context
        )
        
        # 5. Strategic recommendations
        strategic_recommendations = self.generate_strategic_recommendations(
            contextual_analysis, friction_analysis, business_context
        )
        
        # 6. Alternative context analysis
        alternative_contexts = self.analyze_alternative_contexts(theta_estimates)
        
        return {
            "assessment_metadata": {
                "session_id": session["session_id"],
                "business_context": business_context,
                "completion_time": session["completion_time"].total_seconds(),
                "items_administered": len(session["responses"]),
                "completion_reason": session.get("completion_reason")
            },
            "personality_profile": {
                "trait_scores": theta_estimates,
                "trait_percentiles": {dim: self.theta_to_percentile(theta) 
                                   for dim, theta in theta_estimates.items()},
                "dominant_traits": self.identify_dominant_traits(theta_estimates),
                "trait_reliability": session["se_estimates"]
            },
            "contextual_analysis": contextual_analysis,
            "friction_analysis": friction_analysis,
            "business_fitness": business_fitness,
            "gruendungszuschuss_analysis": gruendungszuschuss_analysis,
            "strategic_recommendations": strategic_recommendations,
            "alternative_contexts": alternative_contexts,
            "intervention_mandates": self.generate_intervention_mandates(friction_analysis),
            "business_intelligence_summary": self.generate_executive_summary(
                business_fitness, gruendungszuschuss_analysis, strategic_recommendations
            )
        }
    
    def calculate_context_weighted_scores(self, theta_scores: Dict, business_context: str) -> Dict:
        """Calculate context-weighted trait scores"""
        context_weights = self.trait_weights[business_context]
        
        weighted_scores = {}
        total_weighted = 0.0
        total_weight = 0.0
        
        for trait, theta in theta_scores.items():
            weight = context_weights.get(trait, 0.5)
            normalized = (theta + 3.0) / 6.0  # Convert to 0-1
            weighted_score = normalized * weight
            
            weighted_scores[trait] = {
                "raw_theta": theta,
                "normalized": normalized,
                "weight": weight,
                "weighted_score": weighted_score,
                "importance": "critical" if weight >= 0.8 else "high" if weight >= 0.65 else "moderate"
            }
            
            total_weighted += weighted_score
            total_weight += weight
        
        context_fitness = total_weighted / total_weight if total_weight > 0 else 0.5
        
        return {
            "business_context": business_context,
            "weighted_scores": weighted_scores,
            "context_fitness_score": context_fitness,
            "fitness_level": self.get_fitness_level(context_fitness)
        }
    
    def analyze_detected_frictions(self, detected_frictions: List, theta_scores: Dict, 
                                 business_context: str) -> Dict:
        """Analyze detected friction patterns"""
        friction_score = sum(f["severity"] for f in detected_frictions if f["type"] == "friction")
        synergy_score = sum(f["severity"] for f in detected_frictions if f["type"] == "synergy")
        
        return {
            "total_frictions": len([f for f in detected_frictions if f["type"] == "friction"]),
            "total_synergies": len([f for f in detected_frictions if f["type"] == "synergy"]),
            "friction_score": friction_score,
            "synergy_score": synergy_score,
            "net_friction": friction_score - synergy_score,
            "friction_level": self.get_friction_level(friction_score - synergy_score),
            "detected_patterns": detected_frictions
        }
    
    def assess_business_fitness(self, contextual_analysis: Dict, friction_analysis: Dict, 
                              business_context: str) -> Dict:
        """Assess overall business fitness"""
        context_fitness = contextual_analysis["context_fitness_score"]
        net_friction = friction_analysis["net_friction"]
        
        # Adjust fitness based on friction
        friction_penalty = min(0.3, net_friction * 0.2)  # Max 30% penalty
        adjusted_fitness = max(0.0, context_fitness - friction_penalty)
        
        return {
            "raw_context_fitness": context_fitness,
            "friction_adjustment": -friction_penalty,
            "adjusted_fitness_score": adjusted_fitness,
            "fitness_level": self.get_fitness_level(adjusted_fitness),
            "key_strengths": self.identify_key_strengths(contextual_analysis),
            "development_areas": self.identify_development_areas(contextual_analysis, friction_analysis)
        }
    
    def optimize_gruendungszuschuss_probability(self, business_fitness: Dict, 
                                              business_context: str) -> Dict:
        """Calculate optimized Gründungszuschuss probability"""
        context_info = self.business_contexts[business_context]
        base_probability = context_info["approval_probability_base"]
        fitness_score = business_fitness["adjusted_fitness_score"]
        
        # Fitness adjustment
        fitness_adjustment = (fitness_score - 0.5) * 0.4
        
        # Context compatibility
        compatibility = context_info["gruendungszuschuss_compatibility"]
        compatibility_adjustment = (compatibility - 0.7) * 0.15
        
        final_probability = max(0.25, min(0.95, base_probability + fitness_adjustment + compatibility_adjustment))
        
        return {
            "probability": final_probability,
            "confidence_level": self.get_confidence_level(final_probability),
            "base_probability": base_probability,
            "fitness_adjustment": fitness_adjustment,
            "compatibility_adjustment": compatibility_adjustment,
            "optimization_factors": self.get_optimization_factors(business_fitness, business_context)
        }
    
    def generate_strategic_recommendations(self, contextual_analysis: Dict, 
                                         friction_analysis: Dict, business_context: str) -> Dict:
        """Generate strategic business recommendations"""
        return {
            "immediate_actions": self.get_immediate_actions(friction_analysis),
            "development_priorities": self.get_development_priorities(contextual_analysis),
            "leverage_strengths": self.get_leverage_strategies(contextual_analysis),
            "context_optimization": self.get_context_optimization(business_context, contextual_analysis),
            "timeline_recommendations": self.get_timeline_recommendations(friction_analysis)
        }
    
    def analyze_alternative_contexts(self, theta_scores: Dict) -> Dict:
        """Analyze fit across all business contexts"""
        alternatives = {}
        
        for context in self.trait_weights.keys():
            context_analysis = self.calculate_context_weighted_scores(theta_scores, context)
            alternatives[context] = {
                "fitness_score": context_analysis["context_fitness_score"],
                "fitness_level": context_analysis["fitness_level"],
                "top_advantages": self.get_context_advantages(context, theta_scores)[:3]
            }
        
        # Rank contexts
        ranked_contexts = sorted(alternatives.items(), 
                               key=lambda x: x[1]["fitness_score"], reverse=True)
        
        return {
            "all_contexts": alternatives,
            "ranked_recommendations": ranked_contexts,
            "best_alternative": ranked_contexts[0] if ranked_contexts else None,
            "context_comparison": self.generate_context_comparison(alternatives)
        }
    
    def generate_intervention_mandates(self, friction_analysis: Dict) -> List[Dict]:
        """Generate specific intervention mandates"""
        mandates = []
        
        for friction in friction_analysis["detected_patterns"]:
            if friction["type"] == "friction":
                pattern_id = friction["pattern_id"]
                
                if "autonomy_self_efficacy" in pattern_id:
                    mandate = self.intervention_mandates["delegation_paralysis"].copy()
                    mandate["pattern_id"] = pattern_id
                    mandate["severity"] = friction["severity"]
                    mandates.append(mandate)
                elif "risk_achievement" in pattern_id:
                    mandate = self.intervention_mandates["reckless_decision_making"].copy()
                    mandate["pattern_id"] = pattern_id
                    mandate["severity"] = friction["severity"]
                    mandates.append(mandate)
        
        return sorted(mandates, key=lambda x: x["urgency"], reverse=True)
    
    def generate_executive_summary(self, business_fitness: Dict, 
                                 gruendungszuschuss_analysis: Dict, 
                                 strategic_recommendations: Dict) -> Dict:
        """Generate executive summary for business intelligence"""
        return {
            "overall_assessment": business_fitness["fitness_level"],
            "key_recommendation": strategic_recommendations["immediate_actions"][0] if strategic_recommendations["immediate_actions"] else "Continue assessment",
            "gruendungszuschuss_outlook": f"{gruendungszuschuss_analysis['probability']:.1%} ({gruendungszuschuss_analysis['confidence_level']})",
            "critical_success_factors": business_fitness["key_strengths"][:3],
            "priority_development_areas": business_fitness["development_areas"][:2],
            "business_readiness_score": business_fitness["adjusted_fitness_score"]
        }
    
    # Helper methods
    def theta_to_percentile(self, theta: float) -> int:
        """Convert theta to percentile rank"""
        return max(1, min(99, int((theta + 3) / 6 * 100)))
    
    def identify_dominant_traits(self, theta_scores: Dict) -> List[str]:
        """Identify dominant personality traits"""
        sorted_traits = sorted(theta_scores.items(), key=lambda x: x[1], reverse=True)
        return [trait for trait, score in sorted_traits[:3] if score > 0.5]
    
    def get_fitness_level(self, score: float) -> str:
        """Convert fitness score to level"""
        if score >= 0.8: return "excellent"
        elif score >= 0.65: return "good"
        elif score >= 0.5: return "adequate"
        elif score >= 0.35: return "challenging"
        else: return "difficult"
    
    def get_friction_level(self, net_friction: float) -> str:
        """Convert net friction to level"""
        if net_friction <= 0: return "optimal"
        elif net_friction <= 0.5: return "manageable"
        elif net_friction <= 1.0: return "concerning"
        else: return "critical"
    
    def get_confidence_level(self, probability: float) -> str:
        """Convert probability to confidence level"""
        if probability >= 0.8: return "sehr hoch"
        elif probability >= 0.65: return "hoch"
        elif probability >= 0.5: return "moderat"
        else: return "niedrig"
    
    def identify_key_strengths(self, contextual_analysis: Dict) -> List[str]:
        """Identify key personality strengths"""
        strengths = []
        for trait, analysis in contextual_analysis["weighted_scores"].items():
            if analysis["normalized"] >= 0.7 and analysis["weight"] >= 0.6:
                strengths.append(f"Starke {trait} ({analysis['importance']} für Geschäft)")
        return strengths[:3]
    
    def identify_development_areas(self, contextual_analysis: Dict, friction_analysis: Dict) -> List[str]:
        """Identify development priorities"""
        areas = []
        
        # From contextual analysis
        for trait, analysis in contextual_analysis["weighted_scores"].items():
            if analysis["normalized"] < 0.5 and analysis["weight"] >= 0.6:
                areas.append(f"Verbesserung {trait} (wichtig für Kontext)")
        
        # From friction analysis
        for friction in friction_analysis["detected_patterns"]:
            if friction["type"] == "friction":
                areas.append(f"Adressierung {friction['pattern_id']}")
        
        return areas[:3]
    
    def get_immediate_actions(self, friction_analysis: Dict) -> List[str]:
        """Get immediate action recommendations"""
        actions = []
        for friction in friction_analysis["detected_patterns"]:
            if friction["type"] == "friction" and friction["severity"] >= 0.7:
                actions.append(f"Implementierung Interventionsprotokoll für {friction['pattern_id']}")
        return actions or ["Fortsetzung der positiven Entwicklung"]
    
    def get_development_priorities(self, contextual_analysis: Dict) -> List[str]:
        """Get development priorities"""
        priorities = []
        for trait, analysis in contextual_analysis["weighted_scores"].items():
            if analysis["importance"] == "critical" and analysis["normalized"] < 0.6:
                priorities.append(f"Priorität: {trait} entwickeln")
        return priorities[:3]
    
    def get_leverage_strategies(self, contextual_analysis: Dict) -> List[str]:
        """Get strategies to leverage strengths"""
        strategies = []
        for trait, analysis in contextual_analysis["weighted_scores"].items():
            if analysis["normalized"] >= 0.7:
                strategies.append(f"Nutzen Sie Ihre starke {trait} als Wettbewerbsvorteil")
        return strategies[:3]
    
    def get_context_optimization(self, business_context: str, contextual_analysis: Dict) -> List[str]:
        """Get context-specific optimization strategies"""
        context_strategies = {
            "fintech": ["Fokus auf Innovation und Risikomanagement", "Regulatorische Compliance beachten"],
            "consulting": ["Expertise und Autonomie betonen", "Kundenbeziehungen stärken"],
            "restaurant": ["Operative Effizienz optimieren", "Kundenerfahrung verbessern"],
            "ecommerce": ["Digitale Kompetenzen ausbauen", "Marktorientierung schärfen"]
        }
        return context_strategies.get(business_context, ["Allgemeine Geschäftsentwicklung"])
    
    def get_timeline_recommendations(self, friction_analysis: Dict) -> Dict:
        """Get timeline-based recommendations"""
        if friction_analysis["friction_level"] == "critical":
            return {"immediate": "0-2 Wochen", "short_term": "2-6 Wochen", "medium_term": "6-12 Wochen"}
        elif friction_analysis["friction_level"] == "concerning":
            return {"immediate": "1-3 Wochen", "short_term": "3-8 Wochen", "medium_term": "8-16 Wochen"}
        else:
            return {"immediate": "2-4 Wochen", "short_term": "4-12 Wochen", "medium_term": "12-24 Wochen"}
    
    def get_context_advantages(self, context: str, theta_scores: Dict) -> List[str]:
        """Get advantages for specific context"""
        context_weights = self.trait_weights[context]
        advantages = []
        
        for trait, theta in theta_scores.items():
            weight = context_weights.get(trait, 0.5)
            normalized = (theta + 3.0) / 6.0
            
            if normalized >= 0.6 and weight >= 0.7:
                advantages.append(f"{trait}: {normalized:.2f} score × {weight:.2f} weight")
        
        return sorted(advantages, key=lambda x: float(x.split('× ')[1]), reverse=True)
    
    def generate_context_comparison(self, alternatives: Dict) -> Dict:
        """Generate context comparison insights"""
        scores = {ctx: data["fitness_score"] for ctx, data in alternatives.items()}
        best = max(scores, key=scores.get)
        worst = min(scores, key=scores.get)
        
        return {
            "best_fit": best,
            "worst_fit": worst,
            "score_range": max(scores.values()) - min(scores.values()),
            "recommendation": f"{best} ist {scores[best] - scores[worst]:.3f} Punkte besser als {worst}"
        }
    
    def get_optimization_factors(self, business_fitness: Dict, business_context: str) -> List[str]:
        """Get factors for Gründungszuschuss optimization"""
        factors = []
        
        if business_fitness["adjusted_fitness_score"] >= 0.7:
            factors.append("Starke Persönlichkeits-Business-Passung")
        
        context_info = self.business_contexts[business_context]
        if context_info["gruendungszuschuss_compatibility"] >= 0.8:
            factors.append("Hohe Gründungszuschuss-Kompatibilität")
        
        if business_fitness["friction_adjustment"] > -0.1:
            factors.append("Geringe psychologische Risikofaktoren")
        
        return factors or ["Standardbewertung"]

# Demo and Testing
def run_comprehensive_demo():
    """Run comprehensive demonstration of the integrated system"""
    print("🚀 GründerAI Integrated Assessment System - Comprehensive Demo")
    print("=" * 80)
    
    # Initialize system
    gruender_ai = IntegratedGruenderAI()
    
    # Start assessment
    print(f"\n👤 Starting Assessment for Fintech Entrepreneur...")
    session_id = gruender_ai.start_adaptive_assessment(
        user_id="demo_user_001",
        business_context="fintech",
        target_se=0.20,
        max_items=12
    )
    
    # Simulate adaptive assessment
    print(f"\n📋 Simulating Adaptive Assessment...")
    responses = [4, 2, 5, 3, 4, 5, 2, 4, 3, 5, 4, 3]  # Sample responses
    
    for i, response in enumerate(responses): # Line 923
        # This call can return either an Item Dict OR the Analysis Dict if stopping criteria met
        item_or_analysis = gruender_ai.get_next_item(session_id) # Line 925
        
        # Check if we received the final analysis (which has the 'status' key) or None
        # If the assessment is complete, we break the item administration loop.
        if not item_or_analysis or item_or_analysis.get("status") == "assessment_complete":
            break
            
        item = item_or_analysis # Safe to use 'item' as it is a real item dict now
        
        # The original line 928 - now safe (Note: you must fix the print formatting issue below)
        print(f"   Item {i+1}: {item['dimension']} - Response: {response}") 
        
        result = gruender_ai.submit_response(session_id, item["item_id"], response)
        
        if result.get("detected_frictions", 0) > 0:
            print(f"     🔥 Friction detected during assessment!")
        
        if result.get("assessment_complete"):
            break
        
        item = item_or_analysis # Safe to use 'item' as it is a real item dict now
        
        # The original line 928 - now safe
        print(f"   Item {i+1}: {item['dimension']} - Response: {response}") 
        
        result = gruender_ai.submit_response(session_id, item["item_id"], response)
        
        if result.get("detected_frictions", 0) > 0:
            print(f"     🔥 Friction detected during assessment!")
        
        if result.get("assessment_complete"):
            break
    
    # Get final analysis
    completion_result = gruender_ai.complete_assessment(session_id)
    analysis = completion_result["analysis"]
    
    # Display comprehensive results
    print(f"\n📊 COMPREHENSIVE ASSESSMENT RESULTS")
    print("=" * 80)
    
    # Personality Profile
    personality = analysis["personality_profile"]
    print(f"\n👤 PERSONALITY PROFILE:")
    for trait, theta in personality["trait_scores"].items():
        percentile = personality["trait_percentiles"][trait]
        print(f"   {trait:25}: θ={theta:+.2f} ({percentile}th percentile)")
    
    # Business Fitness
    business_fitness = analysis["business_fitness"]
    print(f"\n🎯 BUSINESS FITNESS:")
    print(f"   Context: {analysis['contextual_analysis']['business_context']}")
    print(f"   Fitness Level: {business_fitness['fitness_level'].upper()}")
    print(f"   Fitness Score: {business_fitness['adjusted_fitness_score']:.3f}")
    print(f"   Key Strengths: {', '.join(business_fitness['key_strengths'][:2])}")
    
    # Friction Analysis
    friction = analysis["friction_analysis"]
    print(f"\n🔥 FRICTION ANALYSIS:")
    print(f"   Friction Level: {friction['friction_level'].upper()}")
    print(f"   Net Friction: {friction['net_friction']:.2f}")
    print(f"   Detected Patterns: {friction['total_frictions']} frictions, {friction['total_synergies']} synergies")
    
    # Gründungszuschuss Analysis
    gruendungszuschuss = analysis["gruendungszuschuss_analysis"]
    print(f"\n💰 GRÜNDUNGSZUSCHUSS ANALYSE:")
    print(f"   Approval Probability: {gruendungszuschuss['probability']:.1%}")
    print(f"   Confidence Level: {gruendungszuschuss['confidence_level']}")
    print(f"   Optimization Factors: {', '.join(gruendungszuschuss['optimization_factors'][:2])}")
    
    # Strategic Recommendations
    strategic = analysis["strategic_recommendations"]
    print(f"\n🎯 STRATEGIC RECOMMENDATIONS:")
    if strategic["immediate_actions"]:
        print(f"   Immediate: {strategic['immediate_actions'][0]}")
    if strategic["development_priorities"]:
        print(f"   Development: {strategic['development_priorities'][0]}")
    if strategic["leverage_strengths"]:
        print(f"   Leverage: {strategic['leverage_strengths'][0]}")
    
    # Alternative Contexts
    alternatives = analysis["alternative_contexts"]
    print(f"\n🔄 CONTEXT COMPARISON:")
    for i, (context, data) in enumerate(alternatives["ranked_recommendations"][:3], 1):
        print(f"   {i}. {context:10}: {data['fitness_score']:.3f} ({data['fitness_level']})")
    
    # Intervention Mandates
    mandates = analysis["intervention_mandates"]
    if mandates:
        print(f"\n⚡ INTERVENTION MANDATES:")
        for mandate in mandates[:2]:
            print(f"   • {mandate['title']} (Urgency: {mandate['urgency']}/5)")
            print(f"     Timeline: {mandate['timeline']}")
    
    # Executive Summary
    summary = analysis["business_intelligence_summary"]
    print(f"\n📈 EXECUTIVE SUMMARY:")
    print(f"   Overall Assessment: {summary['overall_assessment'].upper()}")
    print(f"   Business Readiness: {summary['business_readiness_score']:.1%}")
    print(f"   Gründungszuschuss Outlook: {summary['gruendungszuschuss_outlook']}")
    print(f"   Key Recommendation: {summary['key_recommendation']}")
    
    print(f"\n🎉 INTEGRATED ASSESSMENT SYSTEM DEMONSTRATION COMPLETE!")
    print("✅ Advanced IRT-CAT adaptive testing")
    print("✅ Real-time friction detection") 
    print("✅ Context-weighted scoring")
    print("✅ Comprehensive business intelligence")
    print("✅ Intervention mandate generation")
    print("✅ Gründungszuschuss optimization")
    print("✅ Strategic recommendations")
    print("✅ Alternative context analysis")
    
    return analysis

if __name__ == "__main__":
    # Run the comprehensive demonstration
    final_analysis = run_comprehensive_demo()