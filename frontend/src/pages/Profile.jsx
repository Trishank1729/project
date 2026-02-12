import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import API from "../services/api";

function Profile() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const token = localStorage.getItem("token");
        if (!token) {
          navigate("/");
          return;
        }
        const res = await API.get("/profile/");
        setUser(res.data);
      } catch (error) {
        setError("Failed to load profile. Please try again.");
        if (error.response?.status === 401) {
          localStorage.removeItem("token");
          navigate("/");
        }
      } finally {
        setLoading(false);
      }
    };

    fetchProfile();
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  if (loading) {
    return (
      <div style={{ height: "100vh", display: "flex", justifyContent: "center", alignItems: "center" }}>
        <div>Loading profile...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div style={{ maxWidth: "500px", margin: "50px auto", padding: "20px" }}>
        <div style={{ color: "#d32f2f", padding: "10px", backgroundColor: "#ffebee", borderRadius: "4px" }}>
          {error}
        </div>
      </div>
    );
  }

  return (
    <div style={{ maxWidth: "500px", margin: "50px auto", padding: "20px", backgroundColor: "#f5f5f5", border: "1px solid #ccc", borderRadius: "8px" }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "20px" }}>
        <h2 style={{ margin: "0" }}>User Profile</h2>
        <button
          onClick={handleLogout}
          style={{
            padding: "8px 16px",
            backgroundColor: "#d32f2f",
            color: "white",
            border: "none",
            borderRadius: "4px",
            cursor: "pointer",
            fontWeight: "bold",
          }}
        >
          Logout
        </button>
      </div>

      {user && (
        <div style={{ display: "flex", flexDirection: "column", gap: "15px", marginTop: "20px", backgroundColor: "white", padding: "20px", borderRadius: "8px" }}>
          <div style={{ borderBottom: "1px solid #eee", paddingBottom: "10px" }}>
            <strong style={{ color: "#666" }}>Full Name:</strong>
            <p style={{ margin: "5px 0 0 0", fontSize: "16px" }}>{user.fullname || "N/A"}</p>
          </div>
          <div style={{ borderBottom: "1px solid #eee", paddingBottom: "10px" }}>
            <strong style={{ color: "#666" }}>Username:</strong>
            <p style={{ margin: "5px 0 0 0", fontSize: "16px" }}>{user.username || "N/A"}</p>
          </div>
          <div style={{ borderBottom: "1px solid #eee", paddingBottom: "10px" }}>
            <strong style={{ color: "#666" }}>Email:</strong>
            <p style={{ margin: "5px 0 0 0", fontSize: "16px" }}>{user.email || "N/A"}</p>
          </div>
          <div style={{ borderBottom: "1px solid #eee", paddingBottom: "10px" }}>
            <strong style={{ color: "#666" }}>Role:</strong>
            <p style={{ margin: "5px 0 0 0", fontSize: "16px" }}>{user.role || "User"}</p>
          </div>
          <div>
            <strong style={{ color: "#666" }}>Member Since:</strong>
            <p style={{ margin: "5px 0 0 0", fontSize: "16px" }}>{new Date(user.joined || Date.now()).toLocaleDateString()}</p>
          </div>
        </div>
      )}

      <button
        style={{
          marginTop: "20px",
          width: "100%",
          padding: "12px",
          backgroundColor: "#1976d2",
          color: "white",
          border: "none",
          borderRadius: "4px",
          cursor: "pointer",
          fontWeight: "bold",
        }}
      >
        Edit Profile
      </button>
    </div>
  );
}

export default Profile;
