"""
GründerAI Complete Assessment System
FastAPI backend with Howard 7-dimension model, IRT-CAT, friction detection
FIXED VERSION - Uses include_router instead of mount
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import router (FIXED: Changed from 'app' to 'router')
from api.assessment_api import router as assessment_router

# Create main app
app = FastAPI(
    title="GründerAI Complete Assessment API",
    description="Howard 7-dimension model with IRT-CAT adaptive testing",
    version="3.0.0"
)

# CORS - Must be added BEFORE routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update in production to specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include assessment router with /api prefix (FIXED: Changed from mount to include_router)
app.include_router(assessment_router, prefix="/api")

@app.get("/")
async def root():
    return {
        "service": "GründerAI Complete Assessment System",
        "version": "3.0.0",
        "model": "Howard 7-Dimension Entrepreneurial Personality",
        "features": [
            "IRT-CAT Adaptive Testing",
            "Friction Analysis",
            "Contextual Scoring",
            "Database Integration",
            "Session Management"
        ],
        "status": "ready"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "api_version": "3.0.0",
        "endpoints_registered": len(app.routes)
    }

# Debug: Print all registered routes on startup
@app.on_event("startup")
async def startup_event():
    print("🚀 GründerAI API Starting...")
    print("📋 Registered Routes:")
    for route in app.routes:
        if hasattr(route, 'methods'):
            methods = ', '.join(route.methods)
            print(f"   {methods:8} {route.path}")
    print("✅ API Ready!")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    print(f"🌐 Starting server on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)