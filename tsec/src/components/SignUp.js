import React from "react";
import styles from "./LogIn.module.css";

const SignUp = () => {
  const onSubmitHandler = (event) => {
    event.preventDefault();
  };

  return (
    <div className={styles.background}>
      <center>
        <p className={styles.title}>Sign Up </p><br />
        <p className={styles.else_page}>Already a member? <u> Log in  </u></p>
      </center>

      <div className={styles.social_media}>
        <button className={styles.Facebook}><a className={styles.social_med_link} >Log in with Facebook</a></button>
        <button className={styles.Gmail}><a className={styles.social_med_link}>Log in with Gmail</a></button>
      </div>

      <form onSubmit={onSubmitHandler}>
        <div className={styles.container}>
          <label htmlFor="user_type">User Type:</label>
          <select id="user_type" name="user_type">
            <option value="Inflencer">Inflencer</option>
            <option value="Seller">Seller</option>
          </select><br />

          <input className={styles.first_input} type="text" id="username" name="username" placeholder="Your username.." />
          <input type="email" id="email" name="email" placeholder="Your email id.." />
          <input type="password" id="password" name="password" placeholder="Your password.." />
          <input type="text" id="phone" name="phone" placeholder="Your phone no.." />
          <input type="number" id="age" name="age" placeholder="Your age.." /><br />

          <div id="Inflencer" className={styles.extra_input}>
            <input type="text" id="fees" name="fees" placeholder="Your fees.." /><br />
          </div>

          <div id