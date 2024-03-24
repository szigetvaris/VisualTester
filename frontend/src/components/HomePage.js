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
        <div style={{ backgroundColor: "#123456" }}>
          <MenuView />
        </div>
        <div style={{ padding: "20px", width: "100%" }}>
          <Routes>
            {/* Home page route + Testing pages under development*/}
            <Route
              path="/"
              element={
                // <p>Hello this is HomePage</p>
                <CreateTestPage />
              }
            />
            <Route path="/testListing" element={<TestListingPage />} />
            <Route path="/testDetails" element={<TestDetailsPage />} />
            <Route path="/testPlanListing" element={<TestPlanListingPage />} />
            <Route path="/testPlanDetails" element={<TestPlanDetailsPage />} />
            <Route path="/createTest" element={<CreateTestPage />} />
          </Routes>
        </div>
      </Router>
    );
  }
}
