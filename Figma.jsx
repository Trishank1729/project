import { useState } from "react";
import { motion } from "framer-motion";

function Input({ placeholder, type = "text" }) {
  return (
    <input
      type={type}
      placeholder={placeholder}
      className="w-full bg-gray-200 rounded-xl p-3 outline-none focus:ring-2 focus:ring-black/40 transition"
    />
  );
}

function Button({ children, onClick, danger }) {
  return (
    <button
      onClick={onClick}
      className={`w-full rounded-xl py-3 mt-6 shadow-md text-lg font-medium transition active:scale-95 ${
        danger
          ? "bg-gray-200 text-red-600"
          : "bg-gray-200 text-black hover:bg-gray-300"
      }`}
    >
      {children}
    </button>
  );
}

function Card({ children }) {
  return (
    <div className="bg-gradient-to-b from-blue-600 to-blue-700 min-h-screen flex items-center justify-center p-6">
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        className="w-full max-w-sm text-center"
      >
        {children}
      </motion.div>
    </div>
  );
}

function Login({ switchScreen }) {
  return (
    <Card>
      <h1 className="text-3xl font-bold mb-10 text-black">Maritime Platform</h1>

      <div className="space-y-5">
        <Input placeholder="Email" />
        <Input placeholder="Password" type="password" />
      </div>

      <Button onClick={() => switchScreen("profile")}>Login</Button>

      <p
        onClick={() => switchScreen("register")}
        className="mt-6 cursor-pointer text-black"
      >
        Don’t have an account? Register
      </p>
    </Card>
  );
}

function Register({ switchScreen }) {
  return (
    <Card>
      <h2 className="text-3xl font-semibold mb-2">Create Account</h2>
      <p className="mb-10 text-lg">Sign up to get started</p>

      <div className="space-y-5">
        <Input placeholder="Full Name" />
        <Input placeholder="Email" />
        <Input placeholder="Password" type="password" />
        <Input placeholder="Confirm Password" type="password" />
      </div>

      <Button onClick={() => switchScreen("profile")}>Register</Button>
    </Card>
  );
}

function Profile({ switchScreen }) {
  return (
    <Card>
      <div className="flex flex-col items-center">
        <div className="w-32 h-32 rounded-full bg-gray-200 mb-10" />

        <div className="w-full space-y-6">
          <div className="bg-gray-200 rounded-xl p-3 text-left">
            <span className="text-gray-500 mr-2">Name:</span> User
          </div>

          <div className="bg-gray-200 rounded-xl p-3 text-left">
            <span className="text-gray-500 mr-2">Email:</span> user@gmail.com
          </div>
        </div>

        <Button danger onClick={() => switchScreen("login")}>Logout</Button>
      </div>
    </Card>
  );
}

export default function App() {
  const [screen, setScreen] = useState("login");

  return (
    <>
      {screen === "login" && <Login switchScreen={setScreen} />}
      {screen === "register" && <Register switchScreen={setScreen} />}
      {screen === "profile" && <Profile switchScreen={setScreen} />}
    </>
  );
}
