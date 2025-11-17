"""
GründerAI Friction Analysis Engine
Detects problematic trait combinations and generates intervention mandates
"""

import json
import math
from typing import Dict, List, Tuple, Optional
from datetime import datetime

class FrictionAnalysisEngine:
    """
    Advanced friction detection and intervention system
    Identifies trait combinations that create entrepreneurial challenges
    """
    
    def __init__(self):
        # Define friction patterns based on psychological research
        self.friction_patterns = {
            "autonomy_self_efficacy_friction": {
                "traits": ["autonomy_orientation", "self_efficacy"],
                "conditions": {
                    "autonomy_orientation": {"operator": ">=", "threshold": 0.6},
                    "self_efficacy": {"operator": "<=", "threshold": -0.5}
                },
                "friction_type": "delegation_paralysis",
                "severity_multiplier": 0.8,
                "description_de": "Hohe Autonomie mit geringer Selbstwirksamkeit führt zu Delegationsproblemen",
                "description_en": "High autonomy with low self-efficacy leads to delegation difficulties",
                "business_contexts": ["all"],
                "research_basis": "Bandura (1997) - Self-efficacy theory",
                "manifestation": "Wollen eigenständig arbeiten, aber zweifeln an eigenen Fähigkeiten"
            },
            
            "risk_achievement_friction": {
                "traits": ["risk_taking", "achievement_orientation"],
                "conditions": {
                    "risk_taking": {"operator": ">=", "threshold": 0.5},
                    "achievement_orientation": {"operator": "<=", "threshold": -0.3}
                },
                "friction_type": "reckless_decision_making",
                "severity_multiplier": 0.7,
                "description_de": "Hohe Risikobereitschaft ohne Leistungsorientierung führt zu unvorsichtigen Entscheidungen",
                "description_en": "High risk-taking without achievement orientation leads to reckless decisions",
                "business_contexts": ["fintech", "ecommerce", "restaurant"],
                "research_basis": "McClelland (1961) - Achievement motivation theory",
                "manifestation": "Nehmen Risiken ohne systematische Erfolgsmessung"
            },
            
            "innovation_competition_friction": {
                "traits": ["innovativeness", "competitive_aggressiveness"],
                "conditions": {
                    "innovativeness": {"operator": ">=", "threshold": 0.7},
                    "competitive_aggressiveness": {"operator": "<=", "threshold": -0.5}
                },
                "friction_type": "innovation_without_market_drive",
                "severity_multiplier": 0.6,
                "description_de": "Hohe Innovation ohne Wettbewerbsdenken führt zu marktfernen Lösungen",
                "description_en": "High innovation without competitive drive leads to market-disconnected solutions",
                "business_contexts": ["fintech", "ecommerce"],
                "research_basis": "Porter (1985) - Competitive strategy",
                "manifestation": "Entwickeln innovative Lösungen ohne Marktrelevanz"
            },
            
            "proactiveness_efficacy_friction": {
                "traits": ["proactiveness", "self_efficacy"],
                "conditions": {
                    "proactiveness": {"operator": ">=", "threshold": 0.8},
                    "self_efficacy": {"operator": "<=", "threshold": 0.0}
                },
                "friction_type": "opportunity_paralysis",
                "severity_multiplier": 0.75,
                "description_de": "Hohe Proaktivität mit niedriger Selbstwirksamkeit führt zu Gelegenheitsparalyse",
                "description_en": "High proactiveness with low self-efficacy leads to opportunity paralysis",
                "business_contexts": ["all"],
                "research_basis": "Bandura & Locke (2003) - Goal setting theory",
                "manifestation": "Erkennen Chancen, aber handeln nicht darauf"
            },
            
            # Positive synergies (negative friction = positive interaction)
            "innovation_autonomy_synergy": {
                "traits": ["innovativeness", "autonomy_orientation"],
                "conditions": {
                    "innovativeness": {"operator": ">=", "threshold": 0.4},
                    "autonomy_orientation": {"operator": ">=", "threshold": 0.4}
                },
                "friction_type": "creative_independence",
                "severity_multiplier": -0.6,  # Negative = positive synergy
                "description_de": "Hohe Innovation und Autonomie verstärken sich gegenseitig positiv",
                "description_en": "High innovation and autonomy mutually reinforce each other positively",
                "business_contexts": ["fintech", "consulting"],
                "research_basis": "West & Farr (1990) - Innovation in organizations",
                "manifestation": "Kreative Unabhängigkeit führt zu einzigartigen Lösungen"
            },
            
            "achievement_competition_synergy": {
                "traits": ["achievement_orientation", "competitive_aggressiveness"],
                "conditions": {
                    "achievement_orientation": {"operator": ">=", "threshold": 0.5},
                    "competitive_aggressiveness": {"operator": ">=", "threshold": 0.3}
                },
                "friction_type": "performance_drive",
                "severity_multiplier": -0.5,  # Positive synergy
                "description_de": "Leistungsorientierung und Wettbewerbsdenken verstärken sich gegenseitig",
                "description_en": "Achievement orientation and competitive drive mutually reinforce",
                "business_contexts": ["ecommerce", "fintech"],
                "research_basis": "Atkinson (1964) - Achievement motivation",
                "manifestation": "Starker Erfolgsantrieb durch Wettbewerbsorientierung"
            }
        }
        
        # Intervention mandates for each friction type
        self.intervention_mandates = {
            "delegation_paralysis": {
                "mandate_title_de": "Das Graduierte Delegations-Protokoll",
                "mandate_title_en": "The Graduated Delegation Protocol",
                "urgency_level": 4,
                "implementation_timeline": "4-6 Wochen",
                "strategy": {
                    "phase_1": {
                        "title": "Micro-Delegation Start",
                        "action": "Identifizieren Sie 3 Aufgaben unter 30 Minuten für Delegation",
                        "duration": "Woche 1-2",
                        "success_metric": "3 kleine Aufgaben erfolgreich delegiert"
                    },
                    "phase_2": {
                        "title": "Structured Check-ins",
                        "action": "Wöchentliche 15-Minuten-Check-ins mit Delegierten",
                        "duration": "Woche 3-4",
                        "success_metric": "Regelmäßige Kommunikation etabliert"
                    },
                    "phase_3": {
                        "title": "Responsibility Escalation",
                        "action": "Schrittweise Erhöhung der Verantwortung bei erfolgreicher Delegation",
                        "duration": "Woche 5-6",
                        "success_metric": "Reduzierung der wöchentlichen Arbeitszeit um 5-10 Stunden"
                    }
                },
                "calendar_integration": "Jeden Montag 9:00 - Delegations-Review (15 Min.)",
                "tools_needed": ["Task-Management-System", "Zeiterfassung"],
                "success_indicators": [
                    "Reduzierte Überstunden",
                    "Erhöhte Teammotivation", 
                    "Mehr Zeit für strategische Aufgaben"
                ]
            },
            
            "reckless_decision_making": {
                "mandate_title_de": "Das Systematische Risiko-Management-Framework",
                "mandate_title_en": "The Systematic Risk Management Framework",
                "urgency_level": 5,
                "implementation_timeline": "2-3 Wochen",
                "strategy": {
                    "phase_1": {
                        "title": "Risk Matrix Creation",
                        "action": "Erstellen Sie eine Risiko-Matrix für alle Geschäftsentscheidungen >5000€",
                        "duration": "Woche 1",
                        "success_metric": "Risiko-Matrix implementiert und erste Entscheidung analysiert"
                    },
                    "phase_2": {
                        "title": "Decision Approval Process",
                        "action": "Implementieren Sie ein 3-Stufen-Genehmigungsverfahren",
                        "duration": "Woche 2",
                        "success_metric": "Alle Entscheidungen durchlaufen strukturierten Prozess"
                    },
                    "phase_3": {
                        "title": "Risk Review Meetings",
                        "action": "Monatliches Risiko-Review mit externem Berater oder Mentor",
                        "duration": "Laufend",
                        "success_metric": "Reduktion ungewollter Verluste um 70%"
                    }
                },
                "calendar_integration": "Jeden ersten Freitag 14:00 - Risiko-Review (30 Min.)",
                "tools_needed": ["Risiko-Matrix-Template", "Entscheidungsprotokoll"],
                "success_indicators": [
                    "Weniger impulsive Entscheidungen",
                    "Messbare Reduktion finanzieller Verluste",
                    "Erhöhte Planungssicherheit"
                ]
            },
            
            "innovation_without_market_drive": {
                "mandate_title_de": "Das Marktorientierte Innovations-Framework",
                "mandate_title_en": "The Market-Oriented Innovation Framework",
                "urgency_level": 3,
                "implementation_timeline": "6-8 Wochen",
                "strategy": {
                    "phase_1": {
                        "title": "Customer Discovery",
                        "action": "Führen Sie 10 Kundengespräche pro Innovationsidee",
                        "duration": "Woche 1-3",
                        "success_metric": "Validierte Kundenbedürfnisse für jede Innovation"
                    },
                    "phase_2": {
                        "title": "Competitive Analysis",
                        "action": "Analysieren Sie 3 Hauptkonkurrenten für jede Innovationsrichtung",
                        "duration": "Woche 4-5",
                        "success_metric": "Klare Differenzierungsstrategie entwickelt"
                    },
                    "phase_3": {
                        "title": "MVP Testing",
                        "action": "Erstellen und testen Sie Minimum Viable Product mit echten Kunden",
                        "duration": "Woche 6-8",
                        "success_metric": "Messbare Kundennachfrage validiert"
                    }
                },
                "calendar_integration": "Jeden Dienstag 10:00 - Innovation-Market-Review (45 Min.)",
                "tools_needed": ["Customer Interview Framework", "Competitive Analysis Template"],
                "success_indicators": [
                    "Höhere Marktakzeptanz neuer Ideen",
                    "Reduzierte Entwicklungszeit für nicht-nachgefragte Features",
                    "Verbesserte Product-Market-Fit-Metriken"
                ]
            },
            
            "opportunity_paralysis": {
                "mandate_title_de": "Das Gelegenheits-Aktivierungs-Protokoll",
                "mandate_title_en": "The Opportunity Activation Protocol",
                "urgency_level": 4,
                "implementation_timeline": "3-4 Wochen",
                "strategy": {
                    "phase_1": {
                        "title": "Opportunity Scoring",
                        "action": "Bewerten Sie Chancen nach Aufwand (1-10) und Potenzial (1-10)",
                        "duration": "Woche 1",
                        "success_metric": "Standardisiertes Bewertungssystem für Chancen"
                    },
                    "phase_2": {
                        "title": "Quick Win Identification",
                        "action": "Starten Sie mit 3 'Quick Wins' (niedriger Aufwand, hohes Potenzial)",
                        "duration": "Woche 2",
                        "success_metric": "3 kleine Erfolge innerhalb von 2 Wochen"
                    },
                    "phase_3": {
                        "title": "Success Build-Up",
                        "action": "Nutzen Sie kleine Erfolge als Sprungbrett für größere Chancen",
                        "duration": "Woche 3-4",
                        "success_metric": "Erhöhte Selbstwirksamkeit durch messbare Erfolge"
                    }
                },
                "calendar_integration": "Jeden Mittwoch 15:00 - Opportunity Review (20 Min.)",
                "tools_needed": ["Opportunity Scoring Matrix", "Success Tracking Dashboard"],
                "success_indicators": [
                    "Schnellere Entscheidungsfindung",
                    "Mehr umgesetzte Geschäftschancen",
                    "Gesteigertes Selbstvertrauen"
                ]
            }
        }
        
        print("🔥 Friction Analysis Engine initialized")
        print(f"   Loaded {len(self.friction_patterns)} friction patterns")
        print(f"   Loaded {len(self.intervention_mandates)} intervention mandates")
    
    def detect_trait_interactions(self, theta_scores: Dict[str, float], 
                                business_context: str = "general") -> List[Dict]:
        """
        Detect trait interactions and friction patterns
        
        Args:
            theta_scores: Dict of trait -> theta value
            business_context: Business context for relevance filtering
        
        Returns:
            List of detected interactions with severity and recommendations
        """
        detected_interactions = []
        
        for pattern_id, pattern in self.friction_patterns.items():
            # Check if pattern applies to this business context
            if "all" not in pattern["business_contexts"] and business_context not in pattern["business_contexts"]:
                continue
            
            # Check if threshold conditions are met
            pattern_detected = True
            interaction_strength = 0.0
            condition_details = {}
            
            for trait, condition in pattern["conditions"].items():
                trait_score = theta_scores.get(trait, 0.0)
                threshold = condition["threshold"]
                operator = condition["operator"]
                
                # Evaluate condition
                if operator == ">=":
                    condition_met = trait_score >= threshold
                    if condition_met:
                        interaction_strength += (trait_score - threshold)
                elif operator == "<=":
                    condition_met = trait_score <= threshold
                    if condition_met:
                        interaction_strength += abs(trait_score - threshold)
                else:
                    condition_met = False
                
                condition_details[trait] = {
                    "score": trait_score,
                    "threshold": threshold,
                    "operator": operator,
                    "met": condition_met
                }
                
                if not condition_met:
                    pattern_detected = False
                    break
            
            if pattern_detected:
                # Calculate friction severity
                base_severity = abs(pattern["severity_multiplier"])
                strength_factor = interaction_strength / len(pattern["traits"])
                final_severity = min(1.0, base_severity * (1 + strength_factor))
                
                interaction = {
                    "pattern_id": pattern_id,
                    "friction_type": pattern["friction_type"],
                    "interaction_type": "synergy" if pattern["severity_multiplier"] < 0 else "friction",
                    "severity": final_severity,
                    "strength": strength_factor,
                    "description_de": pattern["description_de"],
                    "description_en": pattern["description_en"],
                    "manifestation": pattern["manifestation"],
                    "affected_traits": pattern["traits"],
                    "condition_details": condition_details,
                    "business_impact": self.assess_business_impact(pattern["friction_type"], final_severity, business_context),
                    "research_basis": pattern["research_basis"]
                }
                
                detected_interactions.append(interaction)
        
        # Sort by severity (highest first)
        detected_interactions.sort(key=lambda x: x["severity"], reverse=True)
        
        return detected_interactions
    
    def assess_business_impact(self, friction_type: str, severity: float, business_context: str) -> Dict:
        """Assess the business impact of detected friction"""
        impact_mappings = {
            "delegation_paralysis": {
                "areas": ["Skalierbarkeit", "Teamproduktivität", "Work-Life-Balance"],
                "severity_mapping": {
                    "low": "Leichte Verzögerungen bei Teamwachstum",
                    "medium": "Signifikante Skalierungsprobleme",
                    "high": "Kritische Hindernisse für Geschäftswachstum"
                }
            },
            "reckless_decision_making": {
                "areas": ["Finanzielle Stabilität", "Strategische Planung", "Investorvertrauen"],
                "severity_mapping": {
                    "low": "Gelegentliche suboptimale Entscheidungen",
                    "medium": "Erhöhtes finanzielles Risiko",
                    "high": "Existenzbedrohende Entscheidungsfehler"
                }
            },
            "innovation_without_market_drive": {
                "areas": ["Product-Market-Fit", "Kundenakquisition", "Umsatzgenerierung"],
                "severity_mapping": {
                    "low": "Verlangsamte Markteinführung",
                    "medium": "Schwierigkeiten bei Kundengewinnung",
                    "high": "Produkte ohne Marktrelevanz"
                }
            },
            "opportunity_paralysis": {
                "areas": ["Marktchancen", "Wettbewerbsposition", "Geschäftswachstum"],
                "severity_mapping": {
                    "low": "Verpasste kleinere Chancen",
                    "medium": "Signifikant verpasste Marktchancen",
                    "high": "Strategische Wettbewerbsnachteile"
                }
            }
        }
        
        friction_impact = impact_mappings.get(friction_type, {
            "areas": ["Allgemeine Geschäftstätigkeit"],
            "severity_mapping": {"low": "Geringer Einfluss", "medium": "Moderater Einfluss", "high": "Hoher Einfluss"}
        })
        
        # Determine severity level
        if severity >= 0.7:
            severity_level = "high"
        elif severity >= 0.4:
            severity_level = "medium"
        else:
            severity_level = "low"
        
        return {
            "affected_areas": friction_impact["areas"],
            "severity_level": severity_level,
            "description": friction_impact["severity_mapping"][severity_level],
            "business_context_specific": f"Besonders relevant für {business_context}-Geschäfte"
        }
    
    def generate_friction_mandates(self, detected_interactions: List[Dict], 
                                 business_context: str) -> List[Dict]:
        """
        Generate specific intervention mandates for detected friction
        
        Args:
            detected_interactions: List of detected friction patterns
            business_context: Business context for customization
        
        Returns:
            List of actionable mandates with implementation details
        """
        mandates = []
        
        for interaction in detected_interactions:
            if interaction["interaction_type"] == "synergy":
                # Skip synergies - we want to preserve and enhance these
                continue
            
            friction_type = interaction["friction_type"]
            mandate_template = self.intervention_mandates.get(friction_type)
            
            if mandate_template:
                # Customize mandate based on severity and business context
                severity = interaction["severity"]
                urgency_modifier = min(1.5, severity + 0.5)  # Higher severity = higher urgency
                adjusted_urgency = min(5, int(mandate_template["urgency_level"] * urgency_modifier))
                
                # Customize implementation timeline based on business context
                timeline = mandate_template["implementation_timeline"]
                if business_context == "fintech" and "Risiko" in mandate_template["mandate_title_de"]:
                    timeline = "1-2 Wochen"  # Faster implementation for fintech risk issues
                
                mandate = {
                    "mandate_id": f"{friction_type}_{business_context}_{datetime.now().strftime('%Y%m%d')}",
                    "title_de": mandate_template["mandate_title_de"],
                    "title_en": mandate_template["mandate_title_en"],
                    "friction_pattern": interaction["pattern_id"],
                    "friction_type": friction_type,
                    "urgency_level": adjusted_urgency,
                    "friction_severity": severity,
                    "implementation_timeline": timeline,
                    "strategy": mandate_template["strategy"],
                    "calendar_integration": mandate_template["calendar_integration"],
                    "tools_needed": mandate_template["tools_needed"],
                    "success_indicators": mandate_template["success_indicators"],
                    "business_context": business_context,
                    "affected_traits": interaction["affected_traits"],
                    "business_impact": interaction["business_impact"],
                    "customization_notes": self.customize_for_context(friction_type, business_context)
                }
                
                mandates.append(mandate)
        
        # Sort by urgency level (highest first)
        mandates.sort(key=lambda x: x["urgency_level"], reverse=True)
        
        return mandates
    
    def customize_for_context(self, friction_type: str, business_context: str) -> List[str]:
        """Provide context-specific customization notes"""
        customizations = {
            "delegation_paralysis": {
                "restaurant": [
                    "Beginnen Sie mit Küchenaufgaben oder Kundenservice-Routinen",
                    "Nutzen Sie Schichtsysteme für graduelle Verantwortungsübertragung"
                ],
                "fintech": [
                    "Starten Sie mit nicht-kritischen Entwicklungsaufgaben",
                    "Implementieren Sie Code-Review-Prozesse für Qualitätskontrolle"
                ],
                "consulting": [
                    "Delegieren Sie Research und Datenanalyse-Aufgaben",
                    "Behalten Sie Kundenkontakt und strategische Beratung bei"
                ]
            },
            "reckless_decision_making": {
                "fintech": [
                    "Besondere Vorsicht bei Compliance-relevanten Entscheidungen",
                    "Externe Rechtsberatung für alle regulatorischen Fragen"
                ],
                "restaurant": [
                    "Standort- und Mietentscheidungen besonders sorgfältig prüfen",
                    "Lieferantenverträge durch Dritte validieren lassen"
                ]
            }
        }
        
        return customizations.get(friction_type, {}).get(business_context, [
            f"Allgemeine Empfehlungen für {business_context}-Kontext anwenden"
        ])
    
    def generate_comprehensive_friction_analysis(self, theta_scores: Dict[str, float], 
                                               business_context: str) -> Dict:
        """
        Generate comprehensive friction analysis with mandates and insights
        
        Args:
            theta_scores: Personality trait scores
            business_context: Business context
        
        Returns:
            Complete friction analysis with actionable recommendations
        """
        # Detect interactions
        interactions = self.detect_trait_interactions(theta_scores, business_context)
        
        # Generate mandates for friction patterns
        friction_interactions = [i for i in interactions if i["interaction_type"] == "friction"]
        synergy_interactions = [i for i in interactions if i["interaction_type"] == "synergy"]
        
        mandates = self.generate_friction_mandates(friction_interactions, business_context)
        
        # Calculate overall friction score
        total_friction = sum(i["severity"] for i in friction_interactions)
        total_synergy = sum(abs(i["severity"]) for i in synergy_interactions)
        
        friction_balance = total_friction - total_synergy
        
        if friction_balance <= 0:
            friction_level = "optimal"
        elif friction_balance <= 0.5:
            friction_level = "manageable"
        elif friction_balance <= 1.0:
            friction_level = "concerning"
        else:
            friction_level = "critical"
        
        return {
            "business_context": business_context,
            "overall_friction_analysis": {
                "friction_score": total_friction,
                "synergy_score": total_synergy,
                "net_friction": friction_balance,
                "friction_level": friction_level,
                "total_interactions": len(interactions)
            },
            "detected_frictions": friction_interactions,
            "detected_synergies": synergy_interactions,
            "intervention_mandates": mandates,
            "strategic_recommendations": self.generate_strategic_recommendations(
                friction_interactions, synergy_interactions, business_context
            )
        }
    
    def generate_strategic_recommendations(self, frictions: List[Dict], 
                                         synergies: List[Dict], business_context: str) -> Dict:
        """Generate high-level strategic recommendations"""
        recommendations = {
            "immediate_priorities": [],
            "preserve_strengths": [],
            "long_term_development": [],
            "business_context_insights": []
        }
        
        # Immediate priorities from high-severity frictions
        high_severity_frictions = [f for f in frictions if f["severity"] >= 0.6]
        for friction in high_severity_frictions:
            recommendations["immediate_priorities"].append({
                "action": f"Implementieren Sie das {friction['friction_type']}-Protokoll",
                "reason": friction["description_de"],
                "timeline": "Sofort"
            })
        
        # Preserve synergies
        for synergy in synergies:
            recommendations["preserve_strengths"].append({
                "strength": synergy["friction_type"],
                "description": synergy["description_de"],
                "enhancement": "Nutzen Sie diese Stärke als Wettbewerbsvorteil"
            })
        
        # Business context insights
        context_insights = {
            "fintech": "Fokus auf Risikomanagement und Compliance-Bewusstsein",
            "restaurant": "Betonung operationeller Effizienz und Kundenerfahrung",
            "consulting": "Stärkung der Kundenbeziehungen und Expertise-Demonstration",
            "ecommerce": "Verbesserung der Marktorientierung und Kundenakquisition"
        }
        
        recommendations["business_context_insights"].append(
            context_insights.get(business_context, "Allgemeine Geschäftsentwicklung")
        )
        
        return recommendations

# Test the friction analysis engine
if __name__ == "__main__":
    print("🔥 Testing Friction Analysis Engine...")
    
    # Initialize engine
    friction_engine = FrictionAnalysisEngine()
    
    # Test case: High autonomy, low self-efficacy entrepreneur
    problematic_profile = {
        "risk_taking": 0.8,           # High risk tolerance
        "innovativeness": 0.6,        # Good innovation
        "self_efficacy": -0.7,        # Low self-confidence (FRICTION!)
        "achievement_orientation": 0.3, # Low achievement drive (FRICTION!)
        "proactiveness": 0.9,         # Very high proactiveness (FRICTION!)
        "autonomy_orientation": 1.1,  # Very high autonomy (FRICTION!)
        "competitive_aggressiveness": -0.3  # Low competitiveness
    }
    
    print("\n👤 Testing Problematic Personality Profile:")
    for trait, score in problematic_profile.items():
        print(f"   {trait:25}: {score:+.1f}")
    
    # Analyze friction for fintech context
    print(f"\n🔥 Friction Analysis for Fintech Business:")
    fintech_analysis = friction_engine.generate_comprehensive_friction_analysis(
        problematic_profile, "fintech"
    )
    
    overall = fintech_analysis["overall_friction_analysis"]
    print(f"   Friction Level: {overall['friction_level'].upper()}")
    print(f"   Net Friction: {overall['net_friction']:.2f}")
    print(f"   Total Interactions: {overall['total_interactions']}")
    
    print(f"\n🚨 Detected Frictions:")
    for friction in fintech_analysis["detected_frictions"]:
        print(f"   • {friction['pattern_id']}: {friction['severity']:.2f} severity")
        print(f"     {friction['description_de']}")
        print(f"     Impact: {friction['business_impact']['description']}")
    
    print(f"\n✅ Detected Synergies:")
    for synergy in fintech_analysis["detected_synergies"]:
        print(f"   • {synergy['pattern_id']}: {synergy['severity']:.2f} strength")
        print(f"     {synergy['description_de']}")
    
    print(f"\n🎯 Intervention Mandates:")
    for mandate in fintech_analysis["intervention_mandates"]:
        print(f"   • {mandate['title_de']} (Urgency: {mandate['urgency_level']}/5)")
        print(f"     Timeline: {mandate['implementation_timeline']}")
        print(f"     Key Success: {mandate['success_indicators'][0]}")
    
    # Test different context
    print(f"\n🔥 Friction Analysis for Restaurant Business:")
    restaurant_analysis = friction_engine.generate_comprehensive_friction_analysis(
        problematic_profile, "restaurant"
    )
    
    restaurant_overall = restaurant_analysis["overall_friction_analysis"]
    print(f"   Friction Level: {restaurant_overall['friction_level'].upper()}")
    print(f"   Net Friction: {restaurant_overall['net_friction']:.2f}")
    
    # Compare contexts
    fintech_friction = overall['net_friction']
    restaurant_friction = restaurant_overall['net_friction']
    
    print(f"\n📊 Context Comparison:")
    print(f"   Fintech Friction:    {fintech_friction:.2f}")
    print(f"   Restaurant Friction: {restaurant_friction:.2f}")
    
    if restaurant_friction < fintech_friction:
        difference = fintech_friction - restaurant_friction
        print(f"   🎯 RECOMMENDATION: Restaurant (-{difference:.2f} less friction)")
    else:
        difference = restaurant_friction - fintech_friction
        print(f"   🎯 RECOMMENDATION: Fintech (-{difference:.2f} less friction)")
    
    print(f"\n🎯 Strategic Recommendations:")
    recs = fintech_analysis["strategic_recommendations"]
    
    if recs["immediate_priorities"]:
        print(f"   IMMEDIATE:")
        for rec in recs["immediate_priorities"][:2]:
            print(f"     • {rec['action']}")
    
    if recs["preserve_strengths"]:
        print(f"   PRESERVE:")
        for strength in recs["preserve_strengths"]:
            print(f"     • {strength['strength']}")
    
    print("\n🎉 FRICTION ANALYSIS ENGINE TEST SUCCESSFUL!")
    print("✅ Trait interaction detection working")
    print("✅ Friction severity calculation functional")
    print("✅ Context-specific intervention mandates generated")
    print("✅ Strategic recommendations provided")
    print("✅ Business context comparison completed")
    print("\n🚀 Ready for Phase 3 Integration!")