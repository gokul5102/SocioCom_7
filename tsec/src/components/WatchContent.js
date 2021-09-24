import React from "react";
import "./WatchContent.css";

const WatchContent = () => {

  const videoslider = (links) => {
    document.querySelector(".slider").src = links;
  };


  return (
    <div className="watch_content_container">
      {/* <DocumentMeta {...meta} /> */}
      <video className="slider" loop muted controls autoPlay>
        <source src="/Videos/vid-1.mp4" type="video/mp4" />
      </video>

      {/* Video slider ka links in an unordered list (below) */}
      <ul>
        <li onClick={() => videoslider('/Videos/vid-1.mp4')}>
          <video>
            <source src="/Videos/vid-1.mp4" type="video/mp4" />
          </video>
        </li>

        <li onClick={() => videoslider('/Videos/vid-2.mp4')}>
          <video>
            <source src="/Videos/vid-2.mp4" type="video/mp4" />
          </video>
        </li>

        <li onClick={() => videoslider('/Videos/vid-3.mp4')}>
          <video>
            <source src="/Videos/vid-3.mp4" type="video/mp4" />
          </video>
        </li>

        <li onClick={() => videoslider('/Videos/vid-4.mp4')}>
          <video>
            <source src="/Videos/vid-4.mp4" type="video/mp4" />
          </video>
        </li>

        <li onClick={() => videoslider('/Videos/vid-5.mp4')}>
          <video>
            <source src="/Videos/vid-5.mp4" type="video/mp4" />
          </video>
        </li>

      </ul>
    </div>
  );
};

export default WatchContent;
