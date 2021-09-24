import React from "react";
import styles from "./LogIn.module.css";
import SignUp from "./SignUp";
import { Link } from "react-router-dom";

const LogIn = () => {
  const onSubmitHandler = (event) => {
    event.preventDefault();
  };

  return (
    <div className={styles.background}>
      <center>
        <p className={styles.title}>Login </p><br />
        <p className={styles.else_page}>Not a member yet? <u><Link to="/signup">Sign up  </Link> </u></p>
      </center>

      <section>
        <span className={styles.form_image}>
          <img src="https://images.all-free-download.com/images/graphicthumb/studio_work_background_working_man_filmstrip_computer_icons_6837659.jpg" />
        </span>

        <span>
          <form onSubmit={onSubmitHandler}>
            <div className={styles.container}>
              <input className={styles.first_input} type="text" placeholder="Enter Username" name="username" required /><br />
              <input type="password" placeholder="Enter Password" name="password" required /><br /><br /><br />
              <button type="submit" className={styles.log_but}>Login</button> <br /><br /><br />
            </div>

          </form>
        </span>
      </section>
    </div>
  );
};

export default LogIn;
