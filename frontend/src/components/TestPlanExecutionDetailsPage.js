import axios from "axios";
import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
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
  List,
  ListItem,
  ListItemText,
  ListItemSecondaryAction,
  IconButton,
  Divider,
} from "@material-ui/core";
import { Link } from "react-router-dom";
import { Edit, Delete, Save, RemoveRedEye, ArrowBackIos } from "@material-ui/icons";

function TestPlanExecutionDetailsPage() {
  const [object, setObject] = useState(null);
  const [testExecutions, setTestExecutions] = useState([]);
  const { id } = useParams();

  useEffect(() => {
    fetchObject();
    fetchTestExecutions();
  }, []);

  const listStyle = {
    maxHeight: "300px",
    overflow: "auto",
    background: "#eeeeee",
  };

  const fetchObject = async () => {
    try {
      const response = await axios.get(`/api/testPlanExecution/${id}`);
      setObject(response.data);
    } catch (error) {
      console.error("Error fetching object:", error);
    }
  };

  const fetchTestExecutions = async () => {
    try {
      const response = await axios.get(`/api/testExecution/testPlan/${id}`);
      setTestExecutions(response.data);
    } catch (error) {
      console.error("Error fetching test executions:", error);
    }
  };

  const getStatusColor = (status) => {
    switch (status) {
      case "Failed":
        return "red";
      case "Pass":
        return "green";
      default:
        return "grey";
    }
  };

  if (object === null) {
    return <h1>Loading...</h1>;
  }

  return (
    <div style={{ width: "100%" }}>
      <Grid container spacing={2}>
        <Grid item xs={11}>
          <Typography variant="h4" gutterBottom style={{ fontWeight: "bold" }}>
            Test Plan Execution ID: {object.id}
          </Typography>
        </Grid>
        <Grid item xs={1}>
                <IconButton to={`/testPlanDetails/${object.testPlanID}`} component={Link}>
                  <ArrowBackIos />
                </IconButton>
              </Grid>
        <Grid item xs={3}>
          <Typography
            variant="body1"
            gutterBottom
            style={{ fontWeight: "bold" }}
          >
            Test Plan ID: {object.testPlanID}
          </Typography>
        </Grid>
        <Grid item xs={3}>
          <Typography
            variant="body1"
            gutterBottom
            style={{ fontWeight: "bold" }}
          >
            Last run: {object.createdAt}
          </Typography>
        </Grid>
        <Grid item xs={3}>
          <Typography
            variant="body1"
            gutterBottom
            style={{ fontWeight: "bold" }}
          >
            Status: {object.status}
          </Typography>
        </Grid>
      </Grid>
      <Divider style={{ height: "2px" }} />
      <Typography variant="h6" gutterBottom>
        Test Executions:
      </Typography>
      {testExecutions.length === 0 && (
        <Typography variant="body1" gutterBottom>
          No test executions found...
        </Typography>
      )}
      <List style={listStyle}>
        {testExecutions.map((exe) => (
          <ListItem key={exe.id}>
            <Grid container spacing={1}>
              <Grid item xs={11}>
                <ListItemText
                  primary={`Test Execution ID: ${exe.id}`}
                  secondary={
                    <div>
                      Created at: {exe.createdAt} | Status: {exe.status}
                    </div>
                  }
                />
              </Grid>
              <Grid item xs={1}>
                <IconButton to={`/testExecutionDetails/${exe.id}`} component={Link}>
                  <RemoveRedEye />
                </IconButton>
              </Grid>
            </Grid>
          </ListItem>
        ))}
      </List>
    </div>
  );
}

export default TestPlanExecutionDetailsPage;
