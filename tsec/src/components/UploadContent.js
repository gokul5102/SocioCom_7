import React from "react";

const UploadContent = () => {
  return (
    <div>
      <h2>Upload Content</h2>

      <section>
        <form>
          <label htmlFor="vid_title">Title</label>
          <input type="text" id="vid_title" name="vid_title" placeholder="Your Video Title" />

          <label htmlFor="vid_desc">Description</label>
          <input type="text" id="vid_desc" placeholder="Video Description" />

          <label htmlFor="video">Video</label>
          <input type="file" accept="video/*" id="video" />

          <input type="submit" value="Sign Up" />

          {/* <button type="Submit">Submit</button> */}
        </form>
      </section>
    </div>

  );
};

export default UploadContent;
