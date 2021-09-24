import React from "react";
import styles from "./UploadContent.module.css"

const UploadContent = () => {
  return (
    <div>
      <center>
        <form>
          <div className={styles.upload_content_border}>
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
              <br /><br />

              {/* <div className={styles.text_feild}>
                <label>Video:</label>
              </div> */}

              <div className={styles.file_input}>
                <input type="file" accept="video/*" id="video" id="file" className={styles.file} />
                <label for="file">
                  Upload Video
                  <p className={styles.file_name}></p>
                </label>
              </div>
              <br /><br /><br />

              <div className={styles.text_feild}>
                <button type="submit" className={styles.add_patient_btn}>Upload</button>
              </div>
            </div>
          </div>
        </form>
      </center>

    </div >

  );
};

export default UploadContent;
