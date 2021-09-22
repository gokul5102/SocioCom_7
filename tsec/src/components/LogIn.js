import React from "react";
import styles from "./LogIn.module.css";
import { Link } from "react-router-dom";

const LogIn = () => {
  const onSubmitHandler = (event) => {
    event.preventDefault();
  };

  return (
    <div className={styles.background}>
      <center>
        <p className={styles.title}>Login </p><br />
        <p className={styles.else_page}>Not a member yet? <u> Sign up  </u></p>
      </center>

      <div className={styles.social_media}>
        <button className={styles.Facebook}><a className={styles.social_med_link} >Log in with Facebook</a></button>
        <button className={styles.Gmail}><a className={styles.social_med_link}>Log in with Gmail</a></button>
      </div>

      <form onSubmit={onSubmitHandler}>
        <div className={styles.container}>
          <input className={styles.first_input} type="text" placeholder="Enter Username" name="username" required /><br />
          <input type="password" placeholder="Enter Password" name="password" required /><br /><br /><br />
          <button type="submit" className={styles.log_but}>Login</button> <br />
        </div>

      </form>
    </div>
  );
};

export default LogIn;
