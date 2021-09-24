import React from "react";
import LogIn from "./LogIn";
import styles from "./LogIn.module.css";
import { Link } from "react-router-dom";


const SignUp = () => {
  const onSubmitHandler = (event) => {
    event.preventDefault();
  };

  return (
    <div className={styles.signup_background}>
      <center>
        <p className={styles.title}>Sign Up </p><br />
        <p className={styles.else_page}>Already a member? <u> <Link to="/login">Log in </Link> </u></p>
      </center>

      <section>
        <span className={styles.form_image}>
          <img src="https://images.all-free-download.com/images/graphicthumb/studio_work_background_working_man_filmstrip_computer_icons_6837659.jpg" />
        </span>

        <span>
          <form onSubmit={onSubmitHandler}>
            <div className={styles.container}>
              <input className={styles.first_input} type="text" id="username" name="username" placeholder="Your username.." />
              <input type="email" id="email" name="email" placeholder="Your email id.." />
              <input type="password" id="password" name="password" placeholder="Your password.." />
              <input type="text" id="phone" name="phone" placeholder="Your phone no.." />
              <input type="number" id="age" name="age" placeholder="Your age.." /><br />

              <br />

              <button type="submit" className={styles.log_but}>Sign Up</button> <br />

            </div>
          </form>
        </span>
      </section>
    </div>
  );
};

export default SignUp;
