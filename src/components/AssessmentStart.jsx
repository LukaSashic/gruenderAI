// src/components/AssessmentStart.jsx
import React, { useState } from 'react';
import { api } from '../services/api';

export default function AssessmentStart({ onAssessmentStarted }) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [businessType, setBusinessType] = useState('restaurant');

  const businessTypes = [
    { value: 'restaurant', label: '🍽️ Restaurant / Gastronomie' },
    { value: 'consulting', label: '💼 Beratung / Consulting' },
    { value: 'ecommerce', label: '🛒 E-Commerce / Online Shop' },
    { value: 'services', label: '🔧 Dienstleistungen' },
  ];

  const handleStartAssessment = async () => {
    setLoading(true);
    setError(null);

    try {
      // Generate unique user ID (oder von Auth System)
      const userId = `user_${Date.now()}`;
      
      // Start assessment
      const result = await api.startAssessment(userId, businessType);
      
      console.log('Assessment started:', result);
      
      // Store session ID
      localStorage.setItem('assessment_session_id', result.session_id);
      localStorage.setItem('assessment_business_type', businessType);
      
      // Callback to parent component
      onAssessmentStarted(result.session_id, businessType);
      
    } catch (err) {
      console.error('Failed to start assessment:', err);
      setError('Fehler beim Starten des Assessments. Bitte versuchen Sie es erneut.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="assessment-start">
      <h1>GründerAI Personality Assessment</h1>
      <p>Optimiere deine Chancen für den Gründungszuschuss</p>

      <div className="business-type-selector">
        <label>Wähle deine Geschäftsidee:</label>
        <select 
          value={businessType} 
          onChange={(e) => setBusinessType(e.target.value)}
          disabled={loading}
        >
          {businessTypes.map(type => (
            <option key={type.value} value={type.value}>
              {type.label}
            </option>
          ))}
        </select>
      </div>

      {error && (
        <div className="error-message">
          ⚠️ {error}
        </div>
      )}

      <button 
        onClick={handleStartAssessment}
        disabled={loading}
        className="start-button"
      >
        {loading ? '⏳ Wird gestartet...' : '🚀 Assessment Starten'}
      </button>

      <div className="info-box">
        <h3>Was dich erwartet:</h3>
        <ul>
          <li>✅ 15-18 wissenschaftlich validierte Fragen</li>
          <li>✅ Howard's 7-Dimensionen Modell</li>
          <li>✅ Adaptive Testing (IRT-CAT)</li>
          <li>✅ Personalisierte Empfehlungen</li>
          <li>✅ Gründungszuschuss Optimierung</li>
        </ul>
        <p>⏱️ Dauer: ~10 Minuten</p>
      </div>
    </div>
  );
}
