// src/components/AssessmentResults.jsx
import React, { useState, useEffect } from 'react';
import { api } from '../services/api';

export default function AssessmentResults({ sessionId, responses }) {
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadResults();
  }, [sessionId]);

  const loadResults = async () => {
    try {
      // Get session details
      const sessionData = await api.getSession(sessionId);
      
      // Calculate simple scores (später vom Backend)
      const scores = calculateScores(responses);
      
      setResults({
        session: sessionData,
        scores: scores
      });
    } catch (err) {
      console.error('Error loading results:', err);
    } finally {
      setLoading(false);
    }
  };

  const calculateScores = (responses) => {
    // Simplified scoring (replace with backend logic later)
    const avgScore = responses.reduce((sum, r) => sum + r.value, 0) / responses.length;
    const percentile = Math.round((avgScore / 5) * 100);
    
    return {
      overall: percentile,
      dimensions: [
        { name: 'Innovativeness', score: percentile + 5 },
        { name: 'Risk-Taking', score: percentile - 3 },
        { name: 'Achievement', score: percentile + 8 },
        { name: 'Autonomy', score: percentile },
        { name: 'Proactiveness', score: percentile + 2 },
        { name: 'Locus of Control', score: percentile - 5 },
        { name: 'Self-Efficacy', score: percentile + 10 }
      ]
    };
  };

  if (loading) {
    return <div className="loading">Ergebnisse werden berechnet...</div>;
  }

  return (
    <div className="assessment-results">
      <h1>🎉 Assessment Abgeschlossen!</h1>
      
      <div className="results-summary">
        <h2>Dein Entrepreneurial Profile</h2>
        <div className="overall-score">
          <div className="score-circle">
            <span className="score-value">{results.scores.overall}</span>
            <span className="score-label">Percentile</span>
          </div>
        </div>
      </div>

      <div className="dimensions-breakdown">
        <h3>Howard's 7 Dimensionen:</h3>
        {results.scores.dimensions.map((dim, index) => (
          <div key={index} className="dimension-row">
            <span className="dimension-name">{dim.name}</span>
            <div className="dimension-bar">
              <div 
                className="dimension-fill" 
                style={{ width: `${dim.score}%` }}
              />
            </div>
            <span className="dimension-score">{dim.score}%</span>
          </div>
        ))}
      </div>

      <div className="next-steps">
        <h3>🚀 Nächste Schritte:</h3>
        <ul>
          <li>✅ Detaillierte Interpretation herunterladen</li>
          <li>✅ Personalisierte Businessplan-Empfehlungen</li>
          <li>✅ Gründungszuschuss Checkliste</li>
          <li>✅ Optimierungsvorschläge</li>
        </ul>
        <button className="download-button">
          📄 Vollständigen Report Herunterladen
        </button>
      </div>

      <div className="session-info">
        <p>Session ID: {sessionId}</p>
        <p>Fragen beantwortet: {responses.length}</p>
      </div>
    </div>
  );
}
