import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [robotsite, setRobotsite] = useState('');
  const [denies, setDenies] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      console.log(robotsite)
      const response = await axios.post('http://localhost:5000/api/robotscan', { robotsite });
      console.log("RESPONSE:\n",response.data);
      const data = response.data;
      setDenies(data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h1>RobotScan App</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Enter a website URL:
          <input
            type="text"
            value={robotsite}
            onChange={(e) => setRobotsite(e.target.value)}
          />
        </label>
        <button type="submit">Scan</button>
      </form>
      {denies && <pre>{denies}</pre>}
    </div>
  );
}

export default App;