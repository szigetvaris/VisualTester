import React, { Component } from "react";
import TestDetailsPage from "./TestDetailsPage";
import TestListingPage from "./TestListingPage";
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link,
    Redirect,
  } from "react-router-dom";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <Routes>
          <Route path='/' element={<p>This is home page</p>} />
          <Route path='/testListing' element={<TestListingPage/>} />
          <Route path='/testDetails' element={<TestDetailsPage/>} />
        </Routes>
      </Router>
    );
  }
}
