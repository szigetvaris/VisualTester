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

export default class CreateTestPage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      // technikailag itt nekem meg nem is az implementationt kell atadnom hanem a filet fizikailag feltolteni, ezt a backend eltarolja es majd ott hatarozza meg a path-t
      implementation: null,
      name: "",
      testType: "",
    };

    this.handleCreateTestButtonPressed =
      this.handleCreateTestButtonPressed.bind(this);
    this.handleImplementationChange =
      this.handleImplementationChange.bind(this);
    this.handleNameChange = this.handleNameChange.bind(this);
    this.handleTestTypeChange = this.handleTestTypeChange.bind(this);
  }

  handleNameChange(e) {
    this.setState({
      name: e.target.value,
    });
  }

  handleTestTypeChange(e) {
    this.setState({
      testType: e.target.value,
    });
  }

  handleImplementationChange(e) {
    this.setState({
      implementation: e.target.files[0],
    });
  }

  handleCreateTestButtonPressed(e) {
    // const requestOptions = {
    //   method: "POST",
    //   headers: { "Content-Type": "application/json" },
    //   body: JSON.stringify({
    //     // ezeknek a neveknek matchelniuk kell a backendes nevekkel!
    //     name: this.state.name,
    //     testType: this.state.testType,
    //     implementation: this.state.implementation.name,
    //   }),
    // };
    // console.log(requestOptions);
    // fetch("/api/createTest", requestOptions)
    //   .then((response) => response.json())
    //   .then((data) => console.log(data));

    console.log(this.state);
    const formData = new FormData();

    formData.append("name", this.state.name);
    formData.append("testType", this.state.testType);
    formData.append("implementation", this.state.implementation);

    axios
      .post("/api/createTest", formData, {
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
            Add a new Test
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <FormControl>
            <FormHelperText>Test name</FormHelperText>
            <TextField
              required={true}
              autoFocus={true}
              onChange={this.handleNameChange}
            />
          </FormControl>
        </Grid>
        <Grid item xs={12} align="center">
          <FormControl>
            <FormHelperText>Test implementation Type</FormHelperText>
            <TextField required={true} onChange={this.handleTestTypeChange} />
          </FormControl>
        </Grid>
        <Grid item xs={12} align="center">
          <FormControl>
            <TextField
              required={true}
              type="file"
              onChange={this.handleImplementationChange}
            />
            <FormHelperText>Select the test implementation file</FormHelperText>
          </FormControl>
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            color="primary"
            variant="contained"
            onClick={this.handleCreateTestButtonPressed}
          >
            Create Test
          </Button>
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            color="secondary"
            variant="contained"
            to="/testListing"
            component={Link}
          >
            Back
          </Button>
        </Grid>
      </Grid>
    );
  }
}
