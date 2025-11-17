// src/App.jsx
import React, { useState, useEffect } from 'react';
import { api } from './services/api';
import AssessmentStart from './components/AssessmentStart';
import AssessmentQuestions from './components/AssessmentQuestions';
import AssessmentResults from './components/AssessmentResults';
import './App.css';

export default function App() {
  const [stage, setStage] = useState('start'); // 'start', 'questions', 'results'
  const [sessionId, setSessionId] = useState(null);
  const [businessType, setBusinessType] = useState(null);
  const [responses, setResponses] = useState([]);
  const [apiHealth, setApiHealth] = useState(null);

  // Check API health on mount
  useEffect(() => {
    checkAPIHealth();
  }, []);

  const checkAPIHealth = async () => {
    try {
      const health = await api.checkHealth();
      setApiHealth(health);
      console.log('API Health:', health);
    } catch (err) {
      console.error('API not available:', err);
      setApiHealth({ status: 'unhealthy' });
    }
  };

  const handleAssessmentStarted = (newSessionId, newBusinessType) => {
    setSessionId(newSessionId);
    setBusinessType(newBusinessType);
    setStage('questions');
  };

  const handleAssessmentComplete = (completedSessionId, completedResponses) => {
    setResponses(completedResponses);
    setStage('results');
  };

  const handleRestart = () => {
    setSessionId(null);
    setBusinessType(null);
    setResponses([]);
    setStage('start');
    localStorage.removeItem('assessment_session_id');
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>🚀 GründerAI</h1>
        <p>Personality Assessment für Gründungszuschuss</p>
        {apiHealth && (
          <div className={`api-status ${apiHealth.status}`}>
            {apiHealth.status === 'healthy' ? '🟢' : '🔴'} API Status: {apiHealth.status}
          </div>
        )}
      </header>

      <main className="app-main">
        {stage === 'start' && (
          <AssessmentStart onAssessmentStarted={handleAssessmentStarted} />
        )}

        {stage === 'questions' && (
          <AssessmentQuestions 
            sessionId={sessionId}
            onComplete={handleAssessmentComplete}
          />
        )}

        {stage === 'results' && (
          <AssessmentResults 
            sessionId={sessionId}
            responses={responses}
          />
        )}
      </main>

      <footer className="app-footer">
        {stage !== 'start' && (
          <button onClick={handleRestart} className="restart-button">
            🔄 Neues Assessment Starten
          </button>
        )}
        <p>© 2025 GründerAI - Powered by Howard's 7-Dimension Framework</p>
      </footer>
    </div>
  );
}
