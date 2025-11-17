"""
GründerAI Database Models for SQLite (Fully Compatible with SQLAlchemy 2.0+)
"""

from sqlalchemy import create_engine, Column, String, Integer, Float, DateTime, Boolean, Text, ForeignKey, text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship  # Updated import location
from datetime import datetime
import uuid
import json

# Create base class (updated syntax for SQLAlchemy 2.0+)
Base = declarative_base()

class AssessmentSession(Base):
    """Stores complete assessment sessions"""
    __tablename__ = "assessment_sessions"
    
    session_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, nullable=False, index=True)
    business_context = Column(Text, nullable=False)  # JSON as text
    
    # Session timing
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime, nullable=True)
    
    # Assessment configuration
    max_items = Column(Integer, default=18)
    min_items = Column(Integer, default=12)
    target_se = Column(Float, default=0.20)
    
    # Session status
    status = Column(String, default="active")
    stopping_reason = Column(String, nullable=True)
    
    # Results
    total_items_administered = Column(Integer, default=0)
    overall_theta = Column(Float, nullable=True)
    overall_se = Column(Float, nullable=True)
    reliability_score = Column(Float, nullable=True)
    
    # Relationships
    responses = relationship("UserResponse", back_populates="session")

class AssessmentItem(Base):
    """Assessment items with IRT parameters"""
    __tablename__ = "assessment_items"
    
    item_id = Column(String, primary_key=True)
    dimension = Column(String, nullable=False, index=True)
    business_context = Column(String, nullable=False, index=True)
    text_de = Column(Text, nullable=False)
    text_en = Column(Text, nullable=True)
    
    # IRT parameters
    discrimination = Column(Float, nullable=False)
    difficulty_thresholds = Column(Text, nullable=False)  # JSON as text
    
    # Metadata
    cultural_validation = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    responses = relationship("UserResponse", back_populates="item")

class UserResponse(Base):
    """Individual user responses"""
    __tablename__ = "user_responses"
    
    response_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    session_id = Column(String, ForeignKey("assessment_sessions.session_id"), nullable=False)
    item_id = Column(String, ForeignKey("assessment_items.item_id"), nullable=False)
    
    response_value = Column(Integer, nullable=False)  # 1-5
    timestamp_utc = Column(DateTime, default=datetime.utcnow)
    
    # IRT calculations
    theta_before = Column(Float, nullable=True)
    theta_after = Column(Float, nullable=True)
    se_before = Column(Float, nullable=True)
    se_after = Column(Float, nullable=True)
    fisher_information = Column(Float, nullable=True)
    
    # Relationships
    session = relationship("AssessmentSession", back_populates="responses")
    item = relationship("AssessmentItem", back_populates="responses")

class DatabaseManager:
    """SQLite database manager (fully compatible)"""
    
    def __init__(self, database_file: str = "gruender_ai.db"):
        self.database_file = database_file
        self.database_url = f"sqlite:///./{database_file}"
        
        self.engine = create_engine(
            self.database_url,
            echo=False,
            connect_args={"check_same_thread": False}
        )
        
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        print(f"🗄️  SQLite Database Manager initialized")
        print(f"   Database file: {database_file}")
    
    def create_tables(self):
        """Create all database tables"""
        try:
            Base.metadata.create_all(bind=self.engine)
            print("✅ Database tables created successfully")
            return True
        except Exception as e:
            print(f"❌ Error creating tables: {e}")
            return False
    
    def test_connection(self):
        """Test database connection (FIXED)"""
        try:
            with self.engine.connect() as connection:
                # Use text() wrapper for raw SQL (required in SQLAlchemy 2.0+)
                result = connection.execute(text("SELECT 1"))
                result.fetchone()  # Actually fetch the result
            print("✅ Database connection test successful")
            return True
        except Exception as e:
            print(f"❌ Database connection test failed: {e}")
            return False

# Test everything
if __name__ == "__main__":
    print("🧪 Testing Database Models (Fully Fixed)...")
    
    # Check SQLite
    try:
        import sqlite3
        print("✅ SQLite is built into Python and available")
    except ImportError:
        print("❌ SQLite not available")
        exit(1)
    
    # Test database
    db_manager = DatabaseManager("test_fixed.db")
    
    # Test connection (should work now)
    if db_manager.test_connection():
        print("✅ Database connection working perfectly")
    else:
        print("❌ Connection still failing")
        exit(1)
    
    # Create tables
    if db_manager.create_tables():
        print("✅ Database tables created")
    else:
        exit(1)
    
    # Test data operations
    try:
        session = db_manager.SessionLocal()
        
        # Create test session
        test_session = AssessmentSession(
            user_id="fixed_test_user",
            business_context='{"type": "restaurant", "location": "munich"}',
            status="active"
        )
        
        session.add(test_session)
        session.commit()
        
        print(f"✅ Test session created: {test_session.session_id}")
        
        # Retrieve it
        retrieved = session.query(AssessmentSession).filter_by(user_id="fixed_test_user").first()
        if retrieved:
            print(f"✅ Session retrieved: {retrieved.business_context}")
        
        session.close()
        
        print("\n🎉 ALL DATABASE TESTS PASSING!")
        print("🚀 Ready for Step 2.2: Database Connection!")
        
    except Exception as e:
        print(f"❌ Data operations failed: {e}")