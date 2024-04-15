import React, { Component } from "react";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import {
  FormControl,
  Radio,
  Typography,
  FormHelperText,
  TextField,
  RadioGroup,
  FormControlLabel,
  FormLabel,
} from "@material-ui/core";
import { Link } from "react-router-dom";
import axios from "axios";
import { ArrowBackIos, Send } from "@material-ui/icons";

export default class CreateTestPlanPage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      name: "",
    };

    this.handleCreateTestPlanButtonPressed =
      this.handleCreateTestPlanButtonPressed.bind(this);
    this.handleNameChange = this.handleNameChange.bind(this);
  }

  handleNameChange(e) {
    this.setState({
      name: e.target.value,
    });
  }

  handleCreateTestPlanButtonPressed(e) {
    console.log(this.state);
    const formData = new FormData();

    formData.append("name", this.state.name);

    axios
      .post("/api/createTestPlan", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
      .then((response) => {
        console.log(response);
        // siker popup
      })
      .catch((error) => {
        console.error("Error", error);
        // sikertelenseg popup
      });
  }

  render() {
    return (
      <Grid container spacing={1}>
        <Grid item xs={12} align="center">
          <Typography component="h4" variant="h4">
            Add a new Test Plan
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <FormControl>
            <FormHelperText>Test Plan name</FormHelperText>
            <TextField
              required={true}
              autoFocus={true}
              onChange={this.handleNameChange}
            />
          </FormControl>
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            color="primary"
            variant="contained"
            onClick={this.handleCreateTestPlanButtonPressed}
            startIcon={<Send />}
          >
            Create Test Plan
          </Button>
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            color="secondary"
            variant="contained"
            to="/testPlanListing"
            component={Link}
            startIcon={<ArrowBackIos />}
          >
            Back
          </Button>
        </Grid>
      </Grid>
    );
  }
}
