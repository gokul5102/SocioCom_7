import React from "react";
import styles from "./UploadContent.module.css"

const UploadContent = () => {
  return (
    <div>
      <center>
        <form>
          <div className={styles.wrapper}>
            <div className={styles.title}>
              Upload Content
            </div>

            <div className={styles.form}>
              <div className={styles.text_feild}>
                <label htmlFor="vid_title">Title:</label>
                <input type="text" id="vid_title" name="vid_title" placeholder="Your Video Title" />
              </div>

              <div className={styles.text_feild}>
                <label htmlFor="vid_desc">Description:</label>
                <input type="text" id="vid_desc" placeholder="Video Description" />
              </div>

              <div className={styles.text_feild}>
                <label htmlFor="video">Video:</label>
                <input type="file" accept="video/*" id="video" />
              </div>

              <div className={styles.text_feild}>
                <button type="submit" className={styles.add_patient_btn}>Upload</button>
              </div>
            </div>
          </div>
        </form>
      </center>

    </div >

    /* <section>

      <form>
        <label htmlFor="vid_title">Title</label>
        <input type="text" id="vid_title" name="vid_title" placeholder="Your Video Title" />

        <label htmlFor="vid_desc">Description</label>
        <input type="text" id="vid_desc" placeholder="Video Description" />

        <label htmlFor="video">Video</label>
        <input type="file" accept="video/*" id="video" />

        <input type="submit" value="Sign Up" />

        
  </form>
    </section >  */

  );
};

export default UploadContent;
