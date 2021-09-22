import React from "react";
import "./SignUp.module.css";
import { Link } from "react-router-dom";

const LogIn = () => {
  const onSubmitHandler = (event) => {
    event.preventDefault();
  };

  return (
    // <div class="background">
    //   <br /><br />
    //   <p id="login">Login </p><br /> <p id="signin">Not a member yet? <u style="color:lightblue;"><a href="/signin"> Sign in </a> </u></p>
    //   <div class="social_media">
    //     <button id="Facebook"><a style="text-decoration: none;color:white" href="{% provider_login_url 'facebook' %}">Log in with Facebook</a></button>
    //     <button id="Gmail"><a style="text-decoration: none;color:white" href="{% provider_login_url 'google' %}">Log in with Gmail</a></button>
    //   </div>

   