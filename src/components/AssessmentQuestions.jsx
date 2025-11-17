// src/components/AssessmentQuestions.jsx
import React, { useState, useEffect } from 'react';
import { api } from '../services/api';

export default function AssessmentQuestions({ sessionId, onComplete }) {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [responses, setResponses] = useState([]);
  const [loading, setLoading] = useState(false);

  // Sample questions (später vom Backend)
  const questions = [
    {
      id: 'INNOV_001',
      text: 'Ich entwickle gerne völlig neue Lösungsansätze, auch wenn bewährte Methoden existieren',
      dimension: 'Innovativeness'
    },
    {
      id: 'RISK_001',
      text: 'Ich bin bereit, finanzielle Risiken einzugehen, wenn die Chancen vielversprechend sind',
      dimension: 'Risk-Taking'
    },
    {
      id: 'ACHV_001',
      text: 'Ich setze mir bewusst hohe Ziele und arbeite intensiv daran, diese zu erreichen',
      dimension: 'Achievement Orientation'
    },
    // Add more questions...
  ];

  const handleResponse = async (value) => {
    setLoading(true);

    try {
      const question = questions[currentQuestion];
      
      // Submit to backend
      const result = await api.submitResponse(
        sessionId,
        question.id,
        value
      );

      console.log('Response recorded:', result);

      // Store response
      const newResponses = [...responses, {
        question_id: question.id,
        value: value,
        timestamp: new Date()
      }];
      setResponses(newResponses);

      // Next question or complete
      if (currentQuestion < questions.length - 1) {
        setCurrentQuestion(currentQuestion + 1);
      } else {
        // Assessment complete!
        onComplete(sessionId, newResponses);
      }

    } catch (err) {
      console.error('Error submitting response:', err);
      alert('Fehler beim Speichern der Antwort. Bitte versuchen Sie es erneut.');
    } finally {
      setLoading(false);
    }
  };

  const progress = ((currentQuestion + 1) / questions.length) * 100;
  const question = questions[currentQuestion];

  return (
    <div className="assessment-questions">
      {/* Progress Bar */}
      <div className="progress-bar">
        <div className="progress-fill" style={{ width: `${progress}%` }} />
        <span className="progress-text">
          Frage {currentQuestion + 1} von {questions.length}
        </span>
      </div>

      {/* Question */}
      <div className="question-card">
        <div className="dimension-label">{question.dimension}</div>
        <h2>{question.text}</h2>

        {/* Response Options */}
        <div className="response-options">
          {[
            { value: 1, label: 'Stimme überhaupt nicht zu' },
            { value: 2, label: 'Stimme eher nicht zu' },
            { value: 3, label: 'Neutral' },
            { value: 4, label: 'Stimme eher zu' },
            { value: 5, label: 'Stimme völlig zu' }
          ].map(option => (
            <button
              key={option.value}
              onClick={() => handleResponse(option.value)}
              disabled={loading}
              className="response-button"
            >
              {option.value} - {option.label}
            </button>
          ))}
        </div>
      </div>

      {/* Navigation */}
      <div className="question-navigation">
        <button
          onClick={() => setCurrentQuestion(Math.max(0, currentQuestion - 1))}
          disabled={currentQuestion === 0 || loading}
        >
          ← Zurück
        </button>
        <span>{Math.round(progress)}% Complete</span>
      </div>
    </div>
  );
}
