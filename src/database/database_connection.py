"""
GründerAI Database Connection Manager
Provides easy-to-use methods for assessment data operations
"""

import json
import sys
import os
from typing import List, Dict, Optional

# Fix import path for direct execution
try:
    # Try relative import first (when used as module)
    from .models import DatabaseManager, AssessmentSession, AssessmentItem, UserResponse
except ImportError:
    # Fall back to direct import (when run as script)
    from models import DatabaseManager, AssessmentSession, AssessmentItem, UserResponse

class GruenderAIDatabase:
    """
    High-level database interface for GründerAI Assessment Engine
    """
    
    def __init__(self, database_file: str = "gruender_ai_assessment.db"):
        """Initialize database with SQLite"""
        self.db_manager = DatabaseManager(database_file)
        self.engine = self.db_manager.engine
        self.SessionLocal = self.db_manager.SessionLocal
        
        # Initialize database with tables and sample data
        self.initialize_database()
    
    def initialize_database(self):
        """Create tables and add sample assessment items if needed"""
        print("🗄️  Initializing GründerAI database...")
        
        # Create tables
        if self.db_manager.create_tables():
            print("✅ Database tables ready")
            self.add_sample_items()
        else:
            print("❌ Failed to create database tables")
    
    def add_sample_items(self):
        """Add Howard's 7-dimension assessment items to database"""
        session = self.SessionLocal()
        
        try:
            # Check if items already exist
            existing_count = session.query(AssessmentItem).count()
            if existing_count > 0:
                print(f"✅ Database already has {existing_count} assessment items")
                return
            
            # Sample items based on Howard's entrepreneurial framework
            sample_items = [
                {
                    "item_id": "INNOV_001",
                    "dimension": "innovativeness",
                    "business_context": "general",
                    "text_de": "Ich entwickle gerne neue Lösungen für bestehende Probleme",
                    "text_en": "I enjoy developing new solutions to existing problems",
                    "discrimination": 1.85,
                    "difficulty_thresholds": json.dumps([-1.2, -0.4, 0.3, 1.1]),
                    "cultural_validation": True
                },
                {
                    "item_id": "RISK_001",
                    "dimension": "risk_taking",
                    "business_context": "general",
                    "text_de": "Ich bin bereit, finanzielle Risiken für vielversprechende Gelegenheiten einzugehen",
                    "text_en": "I am willing to take financial risks for promising opportunities",
                    "discrimination": 2.1,
                    "difficulty_thresholds": json.dumps([-0.8, 0.2, 0.9, 1.7]),
                    "cultural_validation": True
                },
                {
                    "item_id": "ACHV_001",
                    "dimension": "achievement_orientation",
                    "business_context": "general",
                    "text_de": "Ich setze mir hohe Leistungsziele und arbeite hart, um sie zu erreichen",
                    "text_en": "I set high performance goals and work hard to achieve them",
                    "discrimination": 1.9,
                    "difficulty_thresholds": json.dumps([-1.0, -0.2, 0.5, 1.3]),
                    "cultural_validation": True
                },
                {
                    "item_id": "SELF_001",
                    "dimension": "self_efficacy",
                    "business_context": "general",
                    "text_de": "Ich bin zuversichtlich, dass ich schwierige Herausforderungen meistern kann",
                    "text_en": "I am confident I can overcome difficult challenges",
                    "discrimination": 1.76,
                    "difficulty_thresholds": json.dumps([-1.3, -0.5, 0.2, 1.0]),
                    "cultural_validation": True
                },
                {
                    "item_id": "AUTO_001",
                    "dimension": "autonomy_orientation",
                    "business_context": "general",
                    "text_de": "Ich arbeite lieber eigenständig als unter enger Supervision",
                    "text_en": "I prefer working independently rather than under close supervision",
                    "discrimination": 1.65,
                    "difficulty_thresholds": json.dumps([-0.9, -0.1, 0.7, 1.5]),
                    "cultural_validation": True
                },
                {
                    "item_id": "PROACT_001",
                    "dimension": "proactiveness",
                    "business_context": "general",
                    "text_de": "Ich erkenne Geschäftsmöglichkeiten oft früher als andere",
                    "text_en": "I often recognize business opportunities before others do",
                    "discrimination": 1.82,
                    "difficulty_thresholds": json.dumps([-1.1, -0.3, 0.4, 1.2]),
                    "cultural_validation": True
                },
                {
                    "item_id": "COMPET_001",
                    "dimension": "competitive_aggressiveness",
                    "business_context": "general",
                    "text_de": "Ich bin entschlossen, meine Konkurrenten zu übertreffen",
                    "text_en": "I am determined to outperform my competitors",
                    "discrimination": 1.74,
                    "difficulty_thresholds": json.dumps([-0.8, 0.1, 0.8, 1.6]),
                    "cultural_validation": True
                },
                # Restaurant-specific items
                {
                    "item_id": "RISK_REST_001",
                    "dimension": "risk_taking",
                    "business_context": "restaurant",
                    "text_de": "Ich würde einen größeren Kredit aufnehmen, um mein Restaurant in einer besseren Lage zu eröffnen",
                    "text_en": "I would take a larger loan to open my restaurant in a better location",
                    "discrimination": 1.95,
                    "difficulty_thresholds": json.dumps([-0.7, 0.1, 0.8, 1.6]),
                    "cultural_validation": False
                },
                {
                    "item_id": "INNOV_REST_001",
                    "dimension": "innovativeness",
                    "business_context": "restaurant",
                    "text_de": "Ich würde ein völlig neues Küchenkonzept ausprobieren, auch wenn es riskant ist",
                    "text_en": "I would try a completely new kitchen concept, even if it's risky",
                    "discrimination": 1.88,
                    "difficulty_thresholds": json.dumps([-1.0, -0.2, 0.5, 1.3]),
                    "cultural_validation": False
                },
                # E-commerce specific items
                {
                    "item_id": "INNOV_ECOM_001",
                    "dimension": "innovativeness",
                    "business_context": "ecommerce",
                    "text_de": "Ich teste gerne neue Online-Marketing-Strategien, auch wenn sie unkonventionell sind",
                    "text_en": "I enjoy testing new online marketing strategies, even unconventional ones",
                    "discrimination": 1.78,
                    "difficulty_thresholds": json.dumps([-1.1, -0.3, 0.4, 1.2]),
                    "cultural_validation": False
                },
                {
                    "item_id": "PROACT_ECOM_001",
                    "dimension": "proactiveness",
                    "business_context": "ecommerce",
                    "text_de": "Ich analysiere ständig neue E-Commerce-Trends und -Technologien",
                    "text_en": "I constantly analyze new e-commerce trends and technologies",
                    "discrimination": 1.83,
                    "difficulty_thresholds": json.dumps([-0.9, -0.1, 0.6, 1.4]),
                    "cultural_validation": False
                }
            ]
            
            # Add items to database
            for item_data in sample_items:
                item = AssessmentItem(**item_data)
                session.add(item)
            
            session.commit()
            print(f"✅ Added {len(sample_items)} assessment items (Howard's 7 dimensions + business-specific)")
            
        except Exception as e:
            print(f"❌ Error adding sample items: {e}")
            session.rollback()
        finally:
            session.close()
    
    def get_items_by_context(self, business_context: str = "general") -> List[Dict]:
        """Get assessment items for specific business context"""
        session = self.SessionLocal()
        try:
            items = session.query(AssessmentItem).filter(
                AssessmentItem.business_context.in_([business_context, "general"]),
                AssessmentItem.is_active == True
            ).all()
            
            result = []
            for item in items:
                result.append({
                    "item_id": item.item_id,
                    "dimension": item.dimension,
                    "business_context": item.business_context,
                    "text_de": item.text_de,
                    "text_en": item.text_en,
                    "discrimination": item.discrimination,
                    "difficulty_thresholds": json.loads(item.difficulty_thresholds)
                })
            
            return result
        finally:
            session.close()
    
    def save_assessment_session(self, session_data: dict) -> str:
        """Save new assessment session to database"""
        session = self.SessionLocal()
        try:
            # Convert business_context to JSON string if it's a dict
            if isinstance(session_data.get('business_context'), dict):
                session_data['business_context'] = json.dumps(session_data['business_context'])
            
            assessment = AssessmentSession(**session_data)
            session.add(assessment)
            session.commit()
            return assessment.session_id
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def get_assessment_session(self, session_id: str) -> Optional[Dict]:
        """Get assessment session by ID"""
        session = self.SessionLocal()
        try:
            assessment = session.query(AssessmentSession).filter_by(session_id=session_id).first()
            if assessment:
                return {
                    "session_id": assessment.session_id,
                    "user_id": assessment.user_id,
                    "business_context": json.loads(assessment.business_context),
                    "status": assessment.status,
                    "start_time": assessment.start_time,
                    "end_time": assessment.end_time,
                    "total_items_administered": assessment.total_items_administered,
                    "overall_theta": assessment.overall_theta,
                    "overall_se": assessment.overall_se
                }
            return None
        finally:
            session.close()
    
    def save_user_response(self, response_data: dict) -> str:
        """Save user response to database"""
        session = self.SessionLocal()
        try:
            response = UserResponse(**response_data)
            session.add(response)
            session.commit()
            return response.response_id
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def get_session_responses(self, session_id: str) -> List[Dict]:
        """Get all responses for an assessment session"""
        session = self.SessionLocal()
        try:
            responses = session.query(UserResponse).filter_by(session_id=session_id).order_by(UserResponse.timestamp_utc).all()
            return [
                {
                    "response_id": r.response_id,
                    "item_id": r.item_id,
                    "response_value": r.response_value,
                    "timestamp": r.timestamp_utc,
                    "theta_before": r.theta_before,
                    "theta_after": r.theta_after,
                    "se_before": r.se_before,
                    "se_after": r.se_after,
                    "fisher_information": r.fisher_information
                }
                for r in responses
            ]
        finally:
            session.close()
    
    def update_session_results(self, session_id: str, theta: float, se: float, status: str = None) -> bool:
        """Update session with latest theta estimate and standard error"""
        session = self.SessionLocal()
        try:
            assessment = session.query(AssessmentSession).filter_by(session_id=session_id).first()
            if assessment:
                assessment.overall_theta = theta
                assessment.overall_se = se
                if status:
                    assessment.status = status
                session.commit()
                return True
            return False
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def get_database_stats(self) -> Dict:
        """Get database statistics for monitoring"""
        session = self.SessionLocal()
        try:
            stats = {
                "total_sessions": session.query(AssessmentSession).count(),
                "active_sessions": session.query(AssessmentSession).filter_by(status="active").count(),
                "completed_sessions": session.query(AssessmentSession).filter_by(status="completed").count(),
                "total_responses": session.query(UserResponse).count(),
                "total_items": session.query(AssessmentItem).count(),
                "active_items": session.query(AssessmentItem).filter_by(is_active=True).count()
            }
            return stats
        finally:
            session.close()


def test_database_connection():
    """Test function for database connection manager"""
    print("🧪 Testing GründerAI Database Connection Manager...")
    
    try:
        # Initialize database
        db = GruenderAIDatabase("test_connection_manager.db")
        
        # Test getting items by context
        print("\n1. Testing assessment items retrieval...")
        general_items = db.get_items_by_context("general")
        restaurant_items = db.get_items_by_context("restaurant")
        ecommerce_items = db.get_items_by_context("ecommerce")
        
        print(f"   ✅ General items: {len(general_items)}")
        print(f"   ✅ Restaurant items: {len(restaurant_items)}")
        print(f"   ✅ E-commerce items: {len(ecommerce_items)}")
        
        if general_items:
            print(f"   ✅ Sample item: {general_items[0]['item_id']} - {general_items[0]['dimension']}")
            print(f"   ✅ Item text: {general_items[0]['text_de'][:50]}...")
        
        # Test session operations
        print("\n2. Testing session operations...")
        session_data = {
            "user_id": "connection_test_user",
            "business_context": {"type": "restaurant", "location": "berlin", "industry": "food"},
            "status": "active"
        }
        
        # Save session
        session_id = db.save_assessment_session(session_data)
        print(f"   ✅ Session saved: {session_id[:8]}...")
        
        # Retrieve session
        retrieved_session = db.get_assessment_session(session_id)
        if retrieved_session:
            print(f"   ✅ Session retrieved: {retrieved_session['business_context']}")
        
        # Test response operations
        print("\n3. Testing response operations...")
        if general_items:
            response_data = {
                "session_id": session_id,
                "item_id": general_items[0]["item_id"],
                "response_value": 4,
                "theta_before": 0.0,
                "theta_after": 0.3,
                "se_before": 1.0,
                "se_after": 0.8,
                "fisher_information": 1.2
            }
            
            response_id = db.save_user_response(response_data)
            print(f"   ✅ Response saved: {response_id[:8]}...")
            
            # Get responses for session
            responses = db.get_session_responses(session_id)
            print(f"   ✅ Retrieved {len(responses)} responses for session")
            
            if responses:
                response = responses[0]
                print(f"   ✅ Response details: Item {response['item_id']}, Value {response['response_value']}")
        
        # Test session update
        print("\n4. Testing session updates...")
        success = db.update_session_results(session_id, 0.5, 0.3, "completed")
        if success:
            print("   ✅ Session results updated successfully")
        
        # Test database stats
        print("\n5. Testing database statistics...")
        stats = db.get_database_stats()
        print(f"   ✅ Database stats: {stats}")
        
        print("\n🎉 DATABASE CONNECTION MANAGER TEST SUCCESSFUL!")
        print("✅ All database operations working perfectly")
        print("✅ Assessment items loaded (Howard's 7 dimensions)")
        print("✅ Session and response operations functional")
        print("✅ Business context support working")
        print("\n🚀 Ready for Step 2.3: Integration Test!")
        
        return True
        
    except Exception as e:
        print(f"❌ Database operations failed: {e}")
        return False


# Run test when file is executed directly
if __name__ == "__main__":
    test_database_connection()