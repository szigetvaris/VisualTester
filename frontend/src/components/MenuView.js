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
    console.log("fuck yea");
  }

  render() {
    return (
      <Grid container spacing={1} style={{ padding: "20px" }}>
        <Grid item xs={12} align="center">
          <Button
            color="primary"
            variant="contained"
            to="/"
            component={Link}
            startIcon={<AccountCircle />}
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
          >
            Logout
          </Button>
        </Grid>
      </Grid>
    );
  }
}
