import React, { Fragment } from "react";
import Home from "../Home";
import WatchContent from "../WatchContent";
import UploadContent from "../UploadContent";
import SignUp from "../SignUp";
import styles from "./Navbar.module.css";
import { Link } from "react-router-dom";

const Navbar = () => {
  const SignUpHandler = (event) => {
    event.preventDefault();
  };

  const LogInhandler = (event) => {
    event.preventDefault();
  };
  return (
    <Fragment>
      <header className={styles.header}>
        <Link
          to="/"
          style={{
            textDecoration: "none",
            color: "white",
            fontSize: "35px",
            fontFamily: "initial",
            fontStyle: "-moz-initial",
          }}
        >
          SOCIOCOM
        </Link>

        <Link
          to="/"
          style={{
            textDecoration: "none",
            color: "white",
            fontSize: "25px",
            fontFamily: "cursive",
          }}
        >
          Home
        </Link>
        <Link
          to="/watchcontent"
          style={{
            textDecoration: "none",
            color: "white",
            fontSize: "25px",
            fontFamily: "cursive",
          }}
        >
          Watch Content
        </Link>
        <Link
          to="/uploadcontent"
          style={{
            textDecoration: "none",
            color: "white",
            fontSize: "25px",
            fontSize: "25px",
            fontFamily: "cursive",
          }}
        >
          Upload Content
        </Link>
        <Link
          to="/login"
          style={{
            textDecoration: "none",
            color: "white",
            fontSize: "25px",
            fontSize: "25px",
            fontFamily: "cursive",
          }}
        >
          Log In
        </Link>
        <Link
          to="/signup"
          style={{
            textDecoration: "none",
            color: "white",
            fontSize: "25px",
            fontFamily: "cursive",
          }}
        >
          Sign Up
        </Link>
      </header>
    </Fragment>
  );
};

export default Navbar;
