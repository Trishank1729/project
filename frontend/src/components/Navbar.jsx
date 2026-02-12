import { Link } from "react-router-dom";

function Navbar() {
  const token = localStorage.getItem("token");

  return (
    <nav style={{
      backgroundColor: "#1976d2",
      padding: "15px 20px",
      display: "flex",
      justifyContent: "flex-start",
      gap: "30px",
      boxShadow: "0 2px 4px rgba(0,0,0,0.1)"
    }}>
      <Link to="/" style={{ color: "white", textDecoration: "none", fontWeight: "bold" }}>
        Maritime Tracking
      </Link>
      <div style={{ display: "flex", gap: "20px", marginLeft: "auto" }}>
        {!token ? (
          <>
            <Link to="/" style={{ color: "white", textDecoration: "none" }}>Login</Link>
            <Link to="/register" style={{ color: "white", textDecoration: "none" }}>Register</Link>
          </>
        ) : (
          <Link to="/profile" style={{ color: "white", textDecoration: "none" }}>Profile</Link>
        )}
      </div>
    </nav>
  );
}

export default Navbar;
