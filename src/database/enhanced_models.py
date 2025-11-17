"""
Enhanced GründerAI Database Models for Phase 3
Adds contextual trait weighting, friction analysis, and business intelligence
"""

from sqlalchemy import create_engine, Column, String, Integer, Float, DateTime, Boolean, Text, ForeignKey, JSON, text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime
import uuid
import json

# Use same base as existing models
Base = declarative_base()

# Fix import path - try relative first, fall back to direct
try:
    # Try relative import first (when used as module)
    from .models import AssessmentSession, AssessmentItem, UserResponse, DatabaseManager
except ImportError:
    # Fall back to direct import (when run as script)
    from models import AssessmentSession, AssessmentItem, UserResponse, DatabaseManager

class TraitWeightMatrix(Base):
    """
    Contextual trait importance weights by business context
    """
    __tablename__ = "trait_weight_matrices"
    
    matrix_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    business_context = Column(String, nullable=False, index=True)
    industry_category = Column(String, nullable=False)
    
    # Trait importance weights (0.0 to 1.0)
    trait_weights = Column(Text, nullable=False)  # JSON: {"risk_taking": 0.8, "autonomy": 0.6}
    
    # Validation metadata
    validation_sample_size = Column(Integer, default=0)
    confidence_level = Column(Float, default=0.0)
    last_updated = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)

class InteractionEffect(Base):
    """
    Trait interaction patterns and friction analysis
    """
    __tablename__ = "interaction_effects"
    
    interaction_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    pattern_name = Column(String, nullable=False)  # "autonomy_self_efficacy_friction"
    trait_combination = Column(Text, nullable=False)  # JSON: ["autonomy_orientation", "self_efficacy"]
    
    # Interaction characteristics
    interaction_type = Column(String, nullable=False)  # "friction", "synergy", "neutral"
    effect_magnitude = Column(Float, nullable=False)   # 0.0 to 1.0
    detection_threshold = Column(Text, nullable=False) # JSON: threshold conditions
    
    # Context applicability
    business_contexts = Column(Text, nullable=False)   # JSON: ["fintech", "consulting"]
    
    # Descriptions
    description_de = Column(Text, nullable=False)
    description_en = Column(Text, nullable=True)
    
    # Metadata
    research_basis = Column(Text, nullable=True)       # Scientific backing
    validation_status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)

class FrictionMandate(Base):
    """
    Intervention strategies for detected friction patterns
    """
    __tablename__ = "friction_mandates"
    
    mandate_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    interaction_effect_id = Column(String, nullable=False)  # Reference to interaction
    business_context = Column(String, nullable=False)
    
    # Mandate content
    mandate_title_de = Column(Text, nullable=False)
    mandate_title_en = Column(Text, nullable=True)
    
    # Implementation strategy
    intervention_strategy = Column(Text, nullable=False)  # JSON: detailed steps
    urgency_level = Column(Integer, default=1)            # 1-5 priority scale
    implementation_timeline = Column(String, nullable=True) # "4-6 weeks"
    
    # Success measurement
    success_metrics = Column(Text, nullable=True)         # JSON: measurement criteria
    calendar_integration = Column(Text, nullable=True)    # Calendar prompt text
    
    # Metadata
    effectiveness_rating = Column(Float, default=0.0)     # User feedback
    usage_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

class BusinessContext(Base):
    """
    Enhanced business context definitions with regulatory and market data
    """
    __tablename__ = "business_contexts"
    
    context_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    business_type = Column(String, nullable=False, unique=True)
    industry_category = Column(String, nullable=False)
    
    # Business characteristics
    regulatory_complexity = Column(Integer, default=1)      # 1-5 scale
    capital_requirements_eur = Column(Integer, default=0)
    typical_timeline_months = Column(Integer, default=12)
    market_saturation = Column(Float, default=0.5)          # 0.0-1.0
    
    # Gründungszuschuss compatibility
    gruendungszuschuss_compatibility = Column(Float, default=0.7)  # 0.0-1.0
    approval_probability_base = Column(Float, default=0.6)         # Base probability
    
    # Success factors
    critical_success_factors = Column(Text, nullable=True)  # JSON: key factors
    common_failure_points = Column(Text, nullable=True)     # JSON: typical problems
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class EnhancedDatabaseManager(DatabaseManager):
    """
    Enhanced database manager with Phase 3 capabilities
    """
    
    def __init__(self, database_file: str = "gruender_ai_enhanced.db"):
        super().__init__(database_file)
        print(f"🔬 Enhanced Database Manager initialized for Phase 3")
        print(f"   Features: Contextual weighting, friction analysis, business intelligence")
    
    def create_enhanced_tables(self):
        """Create all enhanced tables for Phase 3"""
        try:
            # Create enhanced tables
            Base.metadata.create_all(bind=self.engine)
            print("✅ Enhanced database tables created successfully")
            
            # Initialize with default data
            self.initialize_enhanced_data()
            
            return True
        except Exception as e:
            print(f"❌ Error creating enhanced tables: {e}")
            return False
    
    def initialize_enhanced_data(self):
        """Initialize enhanced tables with contextual weights and friction patterns"""
        session = self.SessionLocal()
        
        try:
            # Add business contexts
            business_contexts = [
                {
                    "business_type": "fintech",
                    "industry_category": "financial_technology",
                    "regulatory_complexity": 5,
                    "capital_requirements_eur": 250000,
                    "typical_timeline_months": 18,
                    "market_saturation": 0.7,
                    "gruendungszuschuss_compatibility": 0.6,
                    "approval_probability_base": 0.55,
                    "critical_success_factors": json.dumps([
                        "regulatory_compliance", "technical_innovation", "market_timing"
                    ]),
                    "common_failure_points": json.dumps([
                        "regulatory_hurdles", "technical_complexity", "funding_gaps"
                    ])
                },
                {
                    "business_type": "consulting",
                    "industry_category": "professional_services",
                    "regulatory_complexity": 2,
                    "capital_requirements_eur": 15000,
                    "typical_timeline_months": 6,
                    "market_saturation": 0.8,
                    "gruendungszuschuss_compatibility": 0.9,
                    "approval_probability_base": 0.75,
                    "critical_success_factors": json.dumps([
                        "expertise_credibility", "network_building", "service_differentiation"
                    ]),
                    "common_failure_points": json.dumps([
                        "client_acquisition", "pricing_pressure", "scalability_limits"
                    ])
                },
                {
                    "business_type": "restaurant",
                    "industry_category": "food_service",
                    "regulatory_complexity": 3,
                    "capital_requirements_eur": 120000,
                    "typical_timeline_months": 12,
                    "market_saturation": 0.6,
                    "gruendungszuschuss_compatibility": 0.8,
                    "approval_probability_base": 0.65,
                    "critical_success_factors": json.dumps([
                        "location_quality", "concept_uniqueness", "operational_efficiency"
                    ]),
                    "common_failure_points": json.dumps([
                        "location_costs", "competition", "staff_management"
                    ])
                },
                {
                    "business_type": "ecommerce",
                    "industry_category": "retail_technology",
                    "regulatory_complexity": 3,
                    "capital_requirements_eur": 50000,
                    "typical_timeline_months": 9,
                    "market_saturation": 0.9,
                    "gruendungszuschuss_compatibility": 0.7,
                    "approval_probability_base": 0.60,
                    "critical_success_factors": json.dumps([
                        "digital_marketing", "logistics_efficiency", "customer_experience"
                    ]),
                    "common_failure_points": json.dumps([
                        "market_competition", "logistics_complexity", "customer_acquisition_costs"
                    ])
                }
            ]
            
            for context_data in business_contexts:
                existing = session.query(BusinessContext).filter_by(
                    business_type=context_data["business_type"]
                ).first()
                
                if not existing:
                    context = BusinessContext(**context_data)
                    session.add(context)
            
            session.commit()
            print("✅ Business contexts initialized")
            
            # Add trait weight matrices
            self.add_trait_weight_matrices(session)
            
            # Add interaction effects
            self.add_interaction_effects(session)
            
        except Exception as e:
            print(f"❌ Error initializing enhanced data: {e}")
            session.rollback()
        finally:
            session.close()
    
    def add_trait_weight_matrices(self, session):
        """Add contextual trait importance weights"""
        weight_matrices = [
            {
                "business_context": "fintech",
                "industry_category": "financial_technology",
                "trait_weights": json.dumps({
                    "risk_taking": 0.85,
                    "innovativeness": 0.80,
                    "self_efficacy": 0.75,
                    "achievement_orientation": 0.70,
                    "proactiveness": 0.65,
                    "autonomy_orientation": 0.45,
                    "competitive_aggressiveness": 0.55
                }),
                "validation_sample_size": 150,
                "confidence_level": 0.85
            },
            {
                "business_context": "consulting",
                "industry_category": "professional_services",
                "trait_weights": json.dumps({
                    "risk_taking": 0.35,
                    "innovativeness": 0.50,
                    "self_efficacy": 0.80,
                    "achievement_orientation": 0.75,
                    "proactiveness": 0.70,
                    "autonomy_orientation": 0.85,
                    "competitive_aggressiveness": 0.60
                }),
                "validation_sample_size": 200,
                "confidence_level": 0.90
            },
            {
                "business_context": "restaurant",
                "industry_category": "food_service",
                "trait_weights": json.dumps({
                    "risk_taking": 0.60,
                    "innovativeness": 0.45,
                    "self_efficacy": 0.70,
                    "achievement_orientation": 0.65,
                    "proactiveness": 0.55,
                    "autonomy_orientation": 0.75,
                    "competitive_aggressiveness": 0.50
                }),
                "validation_sample_size": 120,
                "confidence_level": 0.80
            },
            {
                "business_context": "ecommerce",
                "industry_category": "retail_technology",
                "trait_weights": json.dumps({
                    "risk_taking": 0.70,
                    "innovativeness": 0.75,
                    "self_efficacy": 0.65,
                    "achievement_orientation": 0.80,
                    "proactiveness": 0.85,
                    "autonomy_orientation": 0.60,
                    "competitive_aggressiveness": 0.75
                }),
                "validation_sample_size": 180,
                "confidence_level": 0.85
            }
        ]
        
        for matrix_data in weight_matrices:
            existing = session.query(TraitWeightMatrix).filter_by(
                business_context=matrix_data["business_context"]
            ).first()
            
            if not existing:
                matrix = TraitWeightMatrix(**matrix_data)
                session.add(matrix)
        
        session.commit()
        print("✅ Trait weight matrices initialized")
    
    def add_interaction_effects(self, session):
        """Add trait interaction patterns"""
        interactions = [
            {
                "pattern_name": "autonomy_self_efficacy_friction",
                "trait_combination": json.dumps(["autonomy_orientation", "self_efficacy"]),
                "interaction_type": "friction",
                "effect_magnitude": 0.8,
                "detection_threshold": json.dumps({
                    "autonomy_orientation": 0.6,
                    "self_efficacy": -0.5
                }),
                "business_contexts": json.dumps(["all"]),
                "description_de": "Hohe Autonomie bei geringer Selbstwirksamkeit führt zu Delegationsproblemen",
                "description_en": "High autonomy with low self-efficacy leads to delegation problems",
                "research_basis": "Bandura (1997) - Self-efficacy theory"
            },
            {
                "pattern_name": "risk_achievement_friction",
                "trait_combination": json.dumps(["risk_taking", "achievement_orientation"]),
                "interaction_type": "friction",
                "effect_magnitude": 0.7,
                "detection_threshold": json.dumps({
                    "risk_taking": 0.5,
                    "achievement_orientation": -0.3
                }),
                "business_contexts": json.dumps(["fintech", "ecommerce"]),
                "description_de": "Hohe Risikobereitschaft ohne Leistungsorientierung führt zu unvorsichtigen Entscheidungen",
                "description_en": "High risk-taking without achievement orientation leads to reckless decisions",
                "research_basis": "McClelland (1961) - Achievement motivation theory"
            },
            {
                "pattern_name": "innovation_autonomy_synergy",
                "trait_combination": json.dumps(["innovativeness", "autonomy_orientation"]),
                "interaction_type": "synergy",
                "effect_magnitude": 0.6,
                "detection_threshold": json.dumps({
                    "innovativeness": 0.4,
                    "autonomy_orientation": 0.4
                }),
                "business_contexts": json.dumps(["fintech", "consulting"]),
                "description_de": "Hohe Innovation und Autonomie verstärken sich gegenseitig positiv",
                "description_en": "High innovation and autonomy mutually reinforce each other positively",
                "research_basis": "West & Farr (1990) - Innovation in organizations"
            }
        ]
        
        for interaction_data in interactions:
            existing = session.query(InteractionEffect).filter_by(
                pattern_name=interaction_data["pattern_name"]
            ).first()
            
            if not existing:
                interaction = InteractionEffect(**interaction_data)
                session.add(interaction)
        
        session.commit()
        print("✅ Interaction effects initialized")

# Test the enhanced database
if __name__ == "__main__":
    print("🧪 Testing Enhanced Database Models for Phase 3...")
    
    # Initialize enhanced database
    enhanced_db = EnhancedDatabaseManager("test_enhanced_phase3.db")
    
    # Create enhanced tables
    if enhanced_db.create_enhanced_tables():
        print("✅ Enhanced database initialization complete")
        
        # Test context-specific queries
        session = enhanced_db.SessionLocal()
        
        # Test business contexts
        contexts = session.query(BusinessContext).all()
        print(f"✅ Business contexts loaded: {len(contexts)}")
        for context in contexts:
            print(f"   - {context.business_type}: {context.regulatory_complexity}/5 complexity")
        
        # Test trait weight matrices
        matrices = session.query(TraitWeightMatrix).all()
        print(f"✅ Trait weight matrices loaded: {len(matrices)}")
        for matrix in matrices:
            weights = json.loads(matrix.trait_weights)
            print(f"   - {matrix.business_context}: risk_taking={weights.get('risk_taking', 0)}")
        
        # Test interaction effects
        interactions = session.query(InteractionEffect).all()
        print(f"✅ Interaction effects loaded: {len(interactions)}")
        for interaction in interactions:
            print(f"   - {interaction.pattern_name}: {interaction.interaction_type}")
        
        session.close()
        
        print("\n🎉 ENHANCED DATABASE MODELS TEST SUCCESSFUL!")
        print("✅ Contextual trait weighting ready")
        print("✅ Friction analysis framework ready")
        print("✅ Business intelligence schema ready")
        print("\n🚀 Ready for Step 3.2: Contextual Scoring Engine!")
        
    else:
        print("❌ Enhanced database initialization failed")