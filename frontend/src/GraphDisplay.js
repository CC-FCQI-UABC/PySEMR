// GraphDisplay.js
import React from 'react';
import './GraphDisplay.css';
import seasonalPatientCounts from './seasonal_patient_counts.png';

function GraphDisplay() {
  return (
    <div className="graph-display">
      <img src={seasonalPatientCounts} alt="Patient Seasonal Data" className="graph-image" />
    </div>
  );
}

export default GraphDisplay;
