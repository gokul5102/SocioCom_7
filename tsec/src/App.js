import React from "react";
import Home from "./components/Home";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import WatchContent from "./components/WatchContent";
import UploadContent from "./components/UploadContent";
import SignUp from "./components/SignUp";
import LogIn from "./components/LogIn";
import Navbar from "./components/Navbar/Navbar";
import { Helmet } from "react-helmet";

function App() {
  return (
    <Router>
      <Helmet>
        <meta charSet="utf-8" />
        <title>SocioCom</title>
        <link rel="canonical" href="http://mysite.com/example" />
        <meta name="description" content="Helmet application" />
      </Helmet>
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
