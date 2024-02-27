import React, { Component } from "react";
import TestDetailsPage from "./TestDetailsPage";
import TestListingPage from "./TestListingPage";
import CreateTestPage from "./CreateTestPage";
import TestPlanListingPage from "./TestPlanListingPage";
import TestPlanDetailsPage from "./TestPlanDetailsPage";
import MenuView from "./MenuView";
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
          {/* <Route path='/' element={<p>This is home page</p>} /> */}
          <Route path='/' element={<MenuView/>} />
          <Route path='/testListing' element={<TestListingPage/>} />
          <Route path='/testDetails' element={<TestDetailsPage/>} />
          <Route path='/testPlanListing' element={<TestPlanListingPage/>} />
          <Route path='/testPlanDetails' element={<TestPlanDetailsPage/>} />
          <Route path='/createTest' element={<CreateTestPage/>} />
        </Routes>
      </Router>
    );
  }
}
