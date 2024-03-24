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

export default class MenuView extends Component {
  constructor(props) {
    super(props);
  }

  handleProfileOnClick(e) {
    console.log("fuck yea");
  }

  render() {
    return (
      <Grid container spacing={1} style={{padding: '20px'}}>
        <Grid item xs={12} align="center">
          <Button
            color="primary"
            variant="contained"
            to="/"
            component={Link}
          >
            👤 Profile
          </Button>
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            color="primary"
            variant="contained"
            to="/testListing"
            component={Link}
          >
            🎯 Test
          </Button>
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            color="primary"
            variant="contained"
            to="/testPlanListing"
            component={Link}
          >
            📋 Testplan
          </Button>
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            color="secondary"
            variant="contained"
            to="/"
            component={Link}
          >
            Logout
          </Button>
        </Grid>
      </Grid>
    );
  }
}
