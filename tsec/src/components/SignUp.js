import React from "react";
import styles from "./SignUp.module.css";

const SignUp = () => {
  const onSubmitHandler = (event) => {
    event.preventDefault();
  };

  return (
    <div class="random">
      <form onSubmit={onSubmitHandler}>
        <label htmlFor="username">Username</label>
        <input
          type="text"
          id="username"
          name="username"
          placeholder="Your username.."
        />

        <label htmlFor="password">Password</label>
        <input tyoe="password" id="password" placeholder="Your password.." />
        <label htmlFor="age">Age</label>
        <input type="number" id="age" placeholder="Your age.." />

        <label htmlFor="country">Country</label>
        <select id="country" name="country">
          <option value="australia">Australia</option>
          <option value="canada">Canada</option>
          <option value="france">France</option>
          <option value="india">India</option>
          <option value="usa">USA</option>
        </select>

        <input type="submit" value="Sign Up" />

        {/* <button type="Submit">Submit</button> */}
      </form>
    </div>
  );
};

export default SignUp;
