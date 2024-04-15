import React, { Component } from "react";
import axios from "axios";
import {
  Button,
  Typography,
  List,
  ListItem,
  ListItemText,
  ListItemSecondaryAction,
  IconButton,
  Grid,
  Divider,
} from "@material-ui/core";
import { Edit, Delete, Add } from "@material-ui/icons";
import { Link } from "react-router-dom";

export default class TestPlanListingPage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      objects: [],
    };
  }

  componentDidMount() {
    this.fetchObjects();
  }

  fetchObjects = async () => {
    try {
      const response = await axios.get("/api/testPlan");
      this.setState({ objects: response.data });
    } catch (error) {
      console.error("Error fetching test objects:", error);
    }
  };


  handleDelete = async (id) => {
    try {
      await axios.delete(`/api/deleteTestPlan/${id}`);
      this.setState((prevState) => ({
        objects: prevState.objects.filter((obj) => obj.id !== id),
      }));
    } catch (error) {
      console.error("Error deleting object:", error);
    }
  };

  render() {
    console.log(this.state.objects);

    return (
      <div style={{ width: "100%" }}>
        <Grid container spacing={1}>
          <Grid item xs={10}>
            <Typography variant="h4" gutterBottom>
              Test Plan Listing
            </Typography>
          </Grid>
          <Grid item xs={2}>
            <Button
              variant="contained"
              color="primary"
              to="/createTestPlan"
              component={Link}
              startIcon={<Add />}
            >
              Add Test Plan
            </Button>
          </Grid>
        </Grid>
        <List>
          {this.state.objects.map((obj) => (
            <div key={obj.id}>
              <ListItem key={obj.id}>
                <Grid container spacing={1}>
                  <Grid item xs={10}>
                    <ListItemText primary={obj.name} />
                  </Grid>
                  <Grid item xs={1}>
                    <IconButton to={`/testPlanDetails/${obj.id}`} component={Link}>
                      <Edit />
                    </IconButton>
                  </Grid>
                  <Grid item xs={1}>
                    <IconButton onClick={() => this.handleDelete(obj.id)}>
                      <Delete />
                    </IconButton>
                  </Grid>
                </Grid>
              </ListItem>
              <Divider component={"li"} />
            </div>
          ))}
        </List>
      </div>
    );
  }
}
