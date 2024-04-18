import React, { Component } from "react";
import {
  FormControl,
  Radio,
  Typography,
  FormHelperText,
  TextField,
  RadioGroup,
  FormControlLabel,
  FormLabel,
  Grid,
  Button,
  Paper,
} from "@material-ui/core";
import { Link } from "react-router-dom";
import {
  AccountCircle,
  BugReport,
  FormatListBulleted,
  ExitToApp,
} from "@material-ui/icons";

export default class MenuView extends Component {
  constructor(props) {
    super(props);
  }

  handleProfileOnClick(e) {
    console.log("Why are you even click this?");
  }

  render() {
    return (
      <Grid container spacing={1} style={{ padding: "20px" }}>
        <Grid item xs={12} align="center">
          <Paper
            style={{ backgroundColor: "transparent", width: 150, height: 100 }}
          >
            <img
              src="../../static/images/vt_logo5.png"
              alt="Platform Logo"
              style={{ width: 100, height: 100 }}
            />
          </Paper>
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            color="primary"
            variant="contained"
            to="/"
            component={Link}
            startIcon={<AccountCircle />}
            style={{ width: 150 }}
          >
            Profile
          </Button>
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            color="primary"
            variant="contained"
            to="/testListing"
            component={Link}
            startIcon={<BugReport />}
            style={{ width: 150 }}
          >
            Test
          </Button>
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            color="primary"
            variant="contained"
            to="/testPlanListing"
            component={Link}
            startIcon={<FormatListBulleted />}
            style={{ width: 150 }}
          >
            Testplan
          </Button>
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            color="secondary"
            variant="contained"
            to="/"
            component={Link}
            startIcon={<ExitToApp />}
            style={{ width: 150 }}
          >
            Logout
          </Button>
        </Grid>
      </Grid>
    );
  }
}
