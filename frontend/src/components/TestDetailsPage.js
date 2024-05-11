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
import { Edit, Delete, Save, RemoveRedEye } from "@material-ui/icons";

function TestDetailsPage() {
  const [object, setObject] = useState(null);
  const [testPlans, setTestPlans] = useState([]);
  const [testExecutions, setTestExecutions] = useState([]);
  const { id } = useParams();

  useEffect(() => {
    fetchObject();
    fetchTestPlans();
    fetchTestExecutions();
  }, []);

  const listStyle = {
    maxHeight: '300px', 
    overflow: 'auto', 
    background: '#eeeeee'
  };

  const fetchObject = async () => {
    try {
      const response = await axios.get(`/api/test/${id}`);
      setObject(response.data);
    } catch (error) {
      console.error("Error fetching object:", error);
    }
  };

  const fetchTestExecutions = async () => {
    try {
      const response = await axios.get(`/api/testExecution/${id}`);
      setTestExecutions(response.data);
    } catch (error) {
      console.error("Error fetching test executions:", error);
    }
  };

  const fetchTestPlans = async () => {
    try {
      const response = await axios.get(`/api/getContainsT/${id}`);
      setTestPlans(response.data);
    } catch (error) {
      console.error("Error fetching test plans:", error);
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

  const handleNameChange = (event) => {
    object.name = event.target.value;
  };

  if (object === null) {
    return <h1>Loading...</h1>;
  }

  return (
    <div style={{ width: "100%" }}>
      <Grid container spacing={2}>
        <Grid item xs={8}>
          <TextField
            label=""
            variant="outlined"
            defaultValue={object.name}
            onChange={handleNameChange}
            inputProps={{ readOnly: false }} // Ezzel engedélyezzük a szerkesztést
            InputProps={{
              style: { fontSize: "20px", fontWeight: "bold" }, // Adjust the font size here
            }}
          />
        </Grid>
        <Grid item xs={2}>
          <Button
            variant="contained"
            color="primary"
            to="/"
            component={Link}
            startIcon={<Save />}
          >
            Save
          </Button>
        </Grid>
        <Grid item xs={2}>
          <Button
            variant="contained"
            color="secondary"
            to="/"
            component={Link}
            startIcon={<Delete />}
          >
            Delete
          </Button>
        </Grid>

        <Grid item xs={3}>
          <Typography
            variant="body1"
            gutterBottom
            style={{ fontWeight: "bold" }}
          >
            Test ID: {object.id}
          </Typography>
        </Grid>
        <Grid item xs={3}>
          <Typography
            variant="body1"
            gutterBottom
            style={{ fontWeight: "bold" }}
          >
            Test type: {object.testType}
          </Typography>
        </Grid>
        <Grid item xs={3}>
          <Typography
            variant="body1"
            gutterBottom
            style={{ fontWeight: "bold" }}
          >
            Created at: {object.createdAt}
          </Typography>
        </Grid>
      </Grid>
      <Divider style={{ height: "2px" }} />
      <Typography variant="h6" gutterBottom>
        Contained by these Test Plans:
      </Typography>
      {testPlans.length === 0 && (
        <Typography variant="body1" gutterBottom>
          No test plans contain this test
        </Typography>
      )}
      <List style={listStyle}>
        {testPlans.map((obj) => (
          <div key={obj.id}>
            <ListItem key={obj.id}>
              <Grid container spacing={1}>
                <Grid item xs={11}>
                  <ListItemText primary={obj.name} />
                </Grid>
                <Grid item xs={1}>
                  {/* <IconButton onClick={() => this.handleEdit(obj.id)}>
                      <Edit />
                    </IconButton> */}
                  <IconButton
                    to={`/testPlanDetails/${obj.id}`}
                    component={Link}
                  >
                    <Edit />
                  </IconButton>
                </Grid>
              </Grid>
            </ListItem>
            <Divider component={"li"} />
          </div>
        ))}
      </List>
      <Typography variant="h6" gutterBottom>
        Test executions:
      </Typography>
      <List style={listStyle}>
        {testExecutions.map((exe) => (
          <ListItem key={exe.id}>
            <Grid container spacing={1}>
              <Grid item xs={11}>
                <ListItemText
                  primary={`Test Execution ID: ${exe.id}`}
                  secondary={
                    <div>
                    Created at: {exe.createdAt}
                    <span
                      style={{ color: getStatusColor(exe.status) }}
                    >{`(Status: ${exe.status})`}</span>
                    </div>
                    
                  }
                />
              </Grid>
              <Grid item xs={1}>
                <IconButton to={`/`} component={Link}>
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

export default TestDetailsPage;
