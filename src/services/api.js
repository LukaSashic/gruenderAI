// src/services/api.js
const API_BASE_URL = 'https://web-production-332b9.up.railway.app';

class GruenderAIAPI {
  constructor() {
    this.baseURL = API_BASE_URL;
  }

  // Health Check
  async checkHealth() {
    try {
      const response = await fetch(`${this.baseURL}/health`);
      return await response.json();
    } catch (error) {
      console.error('Health check failed:', error);
      throw error;
    }
  }

  // Start Assessment
  async startAssessment(userId, businessType, industry = 'general', location = 'germany') {
    try {
      const response = await fetch(`${this.baseURL}/api/assessment/start`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          user_id: userId,
          business_type: businessType,
          industry: industry,
          location: location
        })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      
      if (data.success) {
        return data.data; // Returns { session_id, message, business_context }
      } else {
        throw new Error('Assessment start failed');
      }
    } catch (error) {
      console.error('Error starting assessment:', error);
      throw error;
    }
  }

  // Submit Response
  async submitResponse(sessionId, itemId, responseValue) {
    try {
      const response = await fetch(`${this.baseURL}/api/assessment/respond`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          session_id: sessionId,
          item_id: itemId,
          response_value: responseValue
        })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      return data.data;
    } catch (error) {
      console.error('Error submitting response:', error);
      throw error;
    }
  }

  // Get Session Details
  async getSession(sessionId) {
    try {
      const response = await fetch(`${this.baseURL}/api/assessment/session/${sessionId}`);
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      return data.data;
    } catch (error) {
      console.error('Error getting session:', error);
      throw error;
    }
  }

  // Assessment Health Check
  async checkAssessmentHealth() {
    try {
      const response = await fetch(`${this.baseURL}/api/assessment/health`);
      return await response.json();
    } catch (error) {
      console.error('Assessment health check failed:', error);
      throw error;
    }
  }
}

// Export singleton instance
export const api = new GruenderAIAPI();
export default api;
