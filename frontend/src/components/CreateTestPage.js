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

export default class CreateTestPage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      // technikailag itt nekem meg nem is az implementationt kell atadnom hanem a filet fizikailag feltolteni, ezt a backend eltarolja es majd ott hatarozza meg a path-t
      implementation: "",
    };

    this.handleCreateTestButtonPressed =
      this.handleCreateTestButtonPressed.bind(this);
    this.handleImplementationChange =
      this.handleImplementationChange.bind(this);
  }

  handleImplementationChange(e) {
    this.setState({
      implementation: e.target.value,
    });
  }

  handleCreateTestButtonPressed(e) {
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        // ezeknek a neveknek matchelniuk kell a backendes nevekkel!
        implementation: this.state.implementation,
      }),
    };
    fetch("/api/createTest", requestOptions)
      .then((response) => response.json())
      .then((data) => console.log(data));
  }

  render() {
    return (
      <Grid container spacing={1}>
        <Grid item xs={12} align="center">
          <Typography component="h4" variant="h4">
            Add new Test
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <FormControl component="fieldset">
            <FormHelperText>
              <div align="center">Valami form helper szoveg</div>
            </FormHelperText>
            <RadioGroup row defaultValue="true">
              <FormControlLabel
                value="true"
                control={<Radio color="primary" />}
                label="Play/Pause"
                labelPlacement="bottom"
              />
              <FormControlLabel
                value="false"
                control={<Radio color="secondary" />}
                label="No Control"
                labelPlacement="bottom"
              />
            </RadioGroup>
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
          <Button color="secondary" variant="contained" to="/" component={Link}>
            Back
          </Button>
        </Grid>
      </Grid>
    );
  }
}