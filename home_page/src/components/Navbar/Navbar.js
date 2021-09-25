import React, { Fragment } from "react";
import Home from "../Home";
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
            fontSize: "22px",
            fontFamily: "Poppins,sans-serif",
          }}
        >
          Home
        </Link>
      </header>
    </Fragment>
  );
};

export default Navbar;
