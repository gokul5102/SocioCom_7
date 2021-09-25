import React from "react";
// import Navbar from "./Navbar/Navbar";
import styles from "./Home.module.css";
// import { useHistory } from "react-router-dom";
const Home = () => {
  // const history = useHistory();
  const myFunction = () => {
    console.log("1234");
    document.getElementById("myDropdown").classList.toggle("show");
  };
  return (
    <div>
      <section className={styles.image_section}>
        <img src="https://media.istockphoto.com/photos/businessman-holding-a-phone-with-a-shopping-icon-online-shopping-picture-id961335672?k=20&m=961335672&s=612x612&w=0&h=42jUlKb0DnC6evRj5YDiJekarxiXExgtKD9cUoPve_M=" />

        <div className={styles.text_on_image}>
          <h1>SocioCom</h1>
          <p>A Video Content and an E-commerce platform </p>
          <br />
          <br />

          {/* <button>E-Commerce</button> */}

          <div className={styles.dropdown}>
            <button onClick className={styles.dropbtn}>
              E-Commerce
            </button>
            {/* <div id="myDropdown" className={styles.dropdownContent}>
              <a href="/">Seller</a>
              <a href="index.html">User</a>
            </div> */}
          </div>

          <button type="submit">
            <a
              href="http://localhost:3000/"
              style={{ textDecoration: "None", color: "white" }}
            >
              Video Platform
            </a>
          </button>

          <br />
          <br />
          <br />
          <br />

          <div className={styles.dropdown}>
            <button onClick className={styles.dropbtn}>
              <a
                href="http://localhost:8000/ecom/get-products/"
                style={{ textDecoration: "None", color: "white" }}
              >
                Customer
              </a>
            </button>
          </div>

          <br />
          <br />
          <br />
          <br />

          <div className={styles.dropdown}>
            <button onClick className={styles.dropbtn}>
              <a
                href="http://localhost:8000/ecom/signup"
                style={{ textDecoration: "None", color: "white" }}
              >
                Seller
              </a>
            </button>
          </div>
        </div>
      </section>
      <br />
      <br />

      <section className={styles.services}>
        <h1>Our Services</h1>
        <section className={styles.video_content_info}>
          <span>
            <img src="https://wikipout.com/wp-content/uploads/2021/06/Sharing-Video-Content-With-The-World.jpg" />
          </span>

          <span>
            <div className={styles.video_content_text}>
              <h1>Video Content Platform</h1>
              <p>
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua.Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisiut aliquip ex ea commodo consequat.Duis aute irure dolor in
                reprehenderit in voluptate velit esse cillum dolore eu fugiat
                nulla pariatur.Excepteur sint occaecat cupidatat non proident,
                sunt in culpa qui officia deserunt mollit anim id est laborum."
              </p>
            </div>
          </span>
        </section>
        <section className={styles.ecommerce_info}>
          <span>
            <img src="https://media.istockphoto.com/photos/shopping-online-concept-shopping-service-on-the-online-web-with-by-picture-id1133980246?k=20&m=1133980246&s=612x612&w=0&h=bwut2YUV7gtnjrv354523xU_9S-TtKQOqGTdiGMsPfs=" />
          </span>

          <span>
            <div className={styles.ecommerce_text}>
              <h1>E-commerce Platform</h1>
              <p>
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua.Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisiut aliquip ex ea commodo consequat. Duis aute irure dolor in
                reprehenderit in voluptate velit esse cillum dolore eu fugiat
                nulla pariatur. Excepteur sint occaecat cupidatat non proident,
                sunt in culpa qui officia deserunt mollit anim id est laborum."
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
