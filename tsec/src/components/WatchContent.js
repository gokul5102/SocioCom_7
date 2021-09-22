import React from "react";
import "./WatchContent.css";

const WatchContent = () => {
  const videoslider = (links) => {
    document.querySelector(".slider").src = links;
  };

  return (
    <div class="container">
      {/* <DocumentMeta {...meta} /> */}
      <video class="slider" autoplay loop muted controls>
        <source src="./vid1.mp4" type="video/mp4" />
      </video>

      {/* Video slider ka links in an unordered list (below) */}
      <ul>
        <li onclick="videoslider('./vid1.mp4')">
          <video controls preload="none">
            <source src="./vid1.mp4" type="video/mp4 codecs='avc1, mp4a'" />
          </video>
        </li>

        <li onclick="videoslider('./vid-2.mp4')">
          <video controls>
            <source src="./vid-2.mp4" type="video/mp4" />
          </video>
        </li>

        <li onclick="videoslider('./vid-3.mp4')">
          <video controls>
            <source src="./vid-3.mp4" type="video/mp4" />
          </video>
        </li>

        <li onclick="videoslider('./vid-4.mp4')">
          <video controls>
            <source src="./vid-4.mp4" type="video/mp4" />
          </video>
        </li>

        <li onclick="videoslider('./vid-5.mp4')">
          <video controls>
            <source src="./vid-5.mp4" type="video/mp4" />
          </video>
        </li>

      </ul>
    </div>
  );
};

export default WatchContent;
