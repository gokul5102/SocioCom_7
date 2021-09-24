import React from "react";
import Navbar from "./Navbar/Navbar";
import styles from "./Home.module.css";
import SignUp from "./SignUp";
import WatchContent from "./WatchContent";
import LogIn from "./LogIn";

const Home = () => {
  return (
    <div>
      <section className={styles.intro_section}>
        <div>
          <span>
            <video className={styles.intro_video} loop muted controls autoPlay>
              <source src="/Videos/vid-1.mp4" type="video/mp4" />
            </video>
          </span>

          <span>
            <div className={styles.text_on_left_video}>
              <h1>SocioCom</h1>
              <p>A Video Content Platform </p><br />
              <p style={{
                fontSize: "23px",
              }}>
                ~ Stream and Upload Media.
              </p><br />

              <button>Learn More</button>
            </div>
          </span>
        </div>
      </section>
      <br /><br /><br /><br />

      <section className={styles.services}>
        <h1>What we do?</h1>
        <section className={styles.video_content_info}>
          <span>
            <img src="https://wikipout.com/wp-content/uploads/2021/06/Sharing-Video-Content-With-The-World.jpg" />
          </span>

          <span>
            <div className={styles.video_content_text}>
              <h1>Video Content Platform</h1>
              <p>"Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod
                tempor incididunt ut labore et dolore magna aliqua.Ut enim ad minim veniam,
                quis nostrud exercitation ullamco laboris nisiut aliquip ex ea commodo
                consequat.Duis aute irure dolor in reprehenderit in voluptate velit esse
                cillum dolore eu fugiat nulla pariatur.Excepteur sint occaecat cupidatat
                non proident, sunt in culpa qui officia deserunt mollit anim id est
                laborum."
              </p>
            </div>
          </span>
        </section>
        <br /> <br />
      </section>
    </div>

  );
};

export default Home;
