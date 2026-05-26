import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {

  const [file, setFile] = useState(null);

  const [message, setMessage] = useState("");

  const [records, setRecords] = useState([]);
  const [stats, setStats] = useState({
  total_records: 0,
  suspicious_records: 0,
  approved_records: 0
});

  const fetchRecords = async () => {

    const response = await axios.get(
      "https://breathe-esg-backend-vtjo.onrender.com/api/records/"
    );

    setRecords(response.data);
  };
  const fetchStats = async () => {

  const response = await axios.get(
    "https://breathe-esg-backend-vtjo.onrender.com/api/stats/"
  );

  setStats(response.data);
};

  useEffect(() => {
  fetchRecords();
  fetchStats();
}, []);

  const handleUpload = async () => {

    if (!file) {
      alert("Please select file");
      return;
    }

    const formData = new FormData();

    formData.append("file", file);

    try {

      const response = await axios.post(
        "https://breathe-esg-backend-vtjo.onrender.com/api/upload/sap/",
        formData
      );

      setMessage(response.data.message);

      fetchRecords();
      fetchStats();

    } catch (error) {

      console.error(error);

      setMessage("Upload failed");
    }
  };
  const handleUtilityUpload = async () => {

  if (!file) {
    alert("Please select file");
    return;
  }

  const formData = new FormData();

  formData.append("file", file);

  try {

    const response = await axios.post(
      "https://breathe-esg-backend-vtjo.onrender.com/api/upload/utility/",
      formData
    );

    setMessage(response.data.message);

    fetchRecords();
    fetchStats();

  } catch (error) {

    console.error(error);

    setMessage("Utility upload failed");
  }
};
const handleTravelUpload = async () => {

  if (!file) {
    alert("Please select file");
    return;
  }

  const formData = new FormData();

  formData.append("file", file);

  try {

    const response = await axios.post(
      "https://breathe-esg-backend-vtjo.onrender.com/api/upload/travel/",
      formData
    );

    setMessage(response.data.message);

    fetchRecords();
    fetchStats();

  } catch (error) {

    console.error(error);

    setMessage("Travel upload failed");
  }
};
  const updateStatus = async (id, status) => {

  try {

    await axios.post(
      `https://breathe-esg-backend-vtjo.onrender.com/api/records/${id}/status/`,
      {
        status: status
      }
    );

    fetchRecords();
    fetchStats();

  } catch (error) {

    console.error(error);
  }
};

  return (
    <div style={{
  padding: "40px",
  fontFamily: "Arial",
  backgroundColor: "#f4f6f8",
  minHeight: "100vh"
}}>

      <h1 style={{
  color: "#1f2937",
  marginBottom: "30px"
}}>
  Breathe ESG Dashboard
</h1>
      <div style={{
  display: "flex",
  gap: "20px",
  marginBottom: "40px",
  flexWrap: "wrap"
}}>

  <div style={{
  backgroundColor: "white",
  padding: "20px",
  width: "220px",
  borderRadius: "10px",
  boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
}}>
    <h3>Total Records</h3>
    <h1>{stats.total_records}</h1>
  </div>

  <div style={{
  backgroundColor: "white",
  padding: "20px",
  width: "220px",
  borderRadius: "10px",
  boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
}}>
    <h3>Suspicious Records</h3>
    <h1>{stats.suspicious_records}</h1>
  </div>

  <div style={{
  backgroundColor: "white",
  padding: "20px",
  width: "220px",
  borderRadius: "10px",
  boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
}}>
    <h3>Approved Records</h3>
    <h1>{stats.approved_records}</h1>
  </div>

</div>

      <h2>SAP CSV Upload</h2>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={handleUpload}>
        Upload CSV
      </button>
      <button
  onClick={handleUtilityUpload}
  style={{
    marginLeft: "10px"
  }}
>
  Upload Utility CSV
</button>
<button
  onClick={handleTravelUpload}
  style={{
    marginLeft: "10px"
  }}
>
  Upload Travel CSV
</button>

      <p>{message}</p>

      <hr />

      <h2>Normalized Records</h2>

      <table border="1" cellPadding="10">

        <thead>
  <tr>

    <th style={{
      padding: "12px",
      backgroundColor: "#e5e7eb"
    }}>
      Category
    </th>

    <th style={{
      padding: "12px",
      backgroundColor: "#e5e7eb"
    }}>
      Quantity
    </th>

    <th style={{
      padding: "12px",
      backgroundColor: "#e5e7eb"
    }}>
      Unit
    </th>

    <th style={{
      padding: "12px",
      backgroundColor: "#e5e7eb"
    }}>
      Scope
    </th>

    <th style={{
      padding: "12px",
      backgroundColor: "#e5e7eb"
    }}>
      Suspicious
    </th>

    <th style={{
      padding: "12px",
      backgroundColor: "#e5e7eb"
    }}>
      Status
    </th>

    <th style={{
      padding: "12px",
      backgroundColor: "#e5e7eb"
    }}>
      Actions
    </th>

  </tr>
</thead>

        <tbody>

          {records.map((record) => (

            <tr
              key={record.id}
              style={{
                backgroundColor:
                  record.suspicious_flag
                    ? "#ffcccc"
                    : "white"
              }}
            >

              <td>{record.category}</td>

              <td>{record.quantity}</td>

              <td>{record.normalized_unit}</td>

              <td>{record.scope}</td>

              <td>
                {record.suspicious_flag
                  ? "Yes"
                  : "No"}
              </td>
              <td>{record.status}</td>

<td>

  <button
    onClick={() =>
      updateStatus(record.id, "APPROVED")
    }
     style={{
    backgroundColor: "#16a34a",
    color: "white",
    border: "none",
    padding: "8px 12px",
    borderRadius: "6px",
    cursor: "pointer"
  }}
  >
    Approve
  </button>

  <button
    onClick={() =>
      updateStatus(record.id, "REJECTED")
    }
    style={{
  marginLeft: "10px",
  backgroundColor: "#dc2626",
  color: "white",
  border: "none",
  padding: "8px 12px",
  borderRadius: "6px",
  cursor: "pointer"
}}
  >
    Reject
  </button>

</td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}

export default App;