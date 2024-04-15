import React, { Component } from "react";
import TestDetailsPage from "./TestDetailsPage";
import TestListingPage from "./TestListingPage";
import CreateTestPage from "./CreateTestPage";
import TestPlanListingPage from "./TestPlanListingPage";
import TestPlanDetailsPage from "./TestPlanDetailsPage";
import CreateTestPlanPage from "./CreateTestPlanPage";
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
        <div style={{ backgroundColor: "#292e4d" }}>
          <MenuView />
        </div>
        <div style={{ padding: "20px", width: "100%" }}>
          <Routes>
            {/* Home page route + Testing pages under development*/}
            <Route path="/" element={<p>Hello this is HomePage</p>} />
            <Route path="/testListing" element={<TestListingPage />} />
            <Route path="/testDetails/:id" element={<TestDetailsPage />} />
            <Route path="/testPlanListing" element={<TestPlanListingPage />} />
            <Route
              path="/testPlanDetails/:id"
              element={<TestPlanDetailsPage />}
            />
            <Route path="/createTest" element={<CreateTestPage />} />
            <Route path="/createTestPlan" element={<CreateTestPlanPage />} />
          </Routes>
        </div>
      </Router>
    );
  }
}
