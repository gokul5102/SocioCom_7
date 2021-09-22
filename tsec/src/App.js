import React from "react";
import Home from "./components/Home";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import WatchContent from "./components/WatchContent";
import UploadContent from "./components/UploadContent";
import SignUp from "./components/SignUp";
import LogIn from "./components/LogIn";
import Navbar from "./components/Navbar/Navbar";

function App() {
  return (
    <Router>
      <div>
        <Navbar />
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/watchcontent">
            <WatchContent />
          </Route>
          <Route path="/uploadcontent">
            <UploadContent />
          </Route>
          <Route path="/login">
            <LogIn />
          </Route>
          <Route path="/signup">
            <SignUp />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
