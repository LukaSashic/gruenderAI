"""
GründerAI Assessment API
FIXED VERSION - Exports APIRouter for proper integration
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import sys
import os

# Add our assessment engine to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import our engine (optional - will work without it for now)
try:
    from assessment_engine.pure_python_irt import GruenderAIEngine
    engine = GruenderAIEngine()
    print("✅ Assessment engine loaded successfully")
except ImportError as e:
    print(f"⚠️ Warning: Could not load full engine: {e}")
    engine = None

# Create API Router (FIXED: Changed from FastAPI app to APIRouter)
router = APIRouter(
    tags=["assessment"],
    responses={404: {"description": "Not found"}},
)

# Request/Response models
class StartAssessmentRequest(BaseModel):
    user_id: str
    business_type: str  # "restaurant", "ecommerce", "consulting"
    industry: str = "general"
    location: str = "germany"

class StartAssessmentResponse(BaseModel):
    success: bool
    data: dict

class SubmitResponseRequest(BaseModel):
    session_id: str
    item_id: str  
    response_value: int  # 1-5

class SubmitResponseResponse(BaseModel):
    success: bool
    data: dict

# API endpoints - Note: paths are relative to router, /api prefix added in main.py

@router.get("/assessment/health")
async def assessment_health():
    """Check assessment system health"""
    return {
        "status": "healthy",
        "engine_loaded": engine is not None,
        "version": "3.0.0"
    }

@router.post("/assessment/start", response_model=StartAssessmentResponse)
async def start_assessment(request: StartAssessmentRequest):
    """
    Start new personality assessment
    
    POST /api/assessment/start
    {
        "user_id": "user123",
        "business_type": "restaurant",
        "industry": "general",
        "location": "germany"
    }
    """
    try:
        print(f"📝 Starting assessment for user: {request.user_id}")
        print(f"   Business type: {request.business_type}")
        
        # Generate session ID
        import uuid
        session_id = str(uuid.uuid4())
        
        # Return success response
        return {
            "success": True,
            "data": {
                "session_id": session_id,
                "message": "Assessment started successfully",
                "business_context": {
                    "type": request.business_type,
                    "industry": request.industry,
                    "location": request.location
                },
                "next_steps": "Use /assessment/respond to submit answers"
            }
        }
        
    except Exception as e:
        print(f"❌ Error starting assessment: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/assessment/respond", response_model=SubmitResponseResponse)
async def submit_response(request: SubmitResponseRequest):
    """
    Submit assessment response
    
    POST /api/assessment/respond
    {
        "session_id": "uuid-here",
        "item_id": "INNOV_001",
        "response_value": 4
    }
    """
    try:
        print(f"📝 Recording response for session: {request.session_id}")
        
        return {
            "success": True,
            "data": {
                "session_id": request.session_id,
                "response_recorded": True,
                "next_question": {
                    "item_id": "SAMPLE_NEXT",
                    "text": "Sample next question would appear here"
                }
            }
        }
        
    except Exception as e:
        print(f"❌ Error submitting response: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/assessment/session/{session_id}")
async def get_session(session_id: str):
    """Get assessment session details"""
    return {
        "success": True,
        "data": {
            "session_id": session_id,
            "status": "active",
            "items_completed": 0,
            "estimated_time_remaining": "15 minutes"
        }
    }

# For backward compatibility if someone imports this as an app
from fastapi import FastAPI
app = FastAPI()
app.include_router(router)

print("✅ Assessment API router initialized")