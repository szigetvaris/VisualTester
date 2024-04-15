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
import { Edit, Delete } from "@material-ui/icons";

function TestDetailsPage() {
  const [object, setObject] = useState(null);
  const [testPlans, setTestPlans] = useState([]);
  const { id } = useParams();

  useEffect(() => {
    fetchObject();
    fetchTestPlans();
    console.log("fuck" + testPlans);
  }, []);

  const fetchObject = async () => {
    try {
      // Itt használhatom az id változót a request összeállításához
      const response = await axios.get(`/api/test/${id}`);
      setObject(response.data);
    } catch (error) {
      console.error("Error fetching object:", error);
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
          <Button variant="contained" color="primary" to="/" component={Link}>
            Save
          </Button>
        </Grid>
        <Grid item xs={2}>
          <Button variant="contained" color="secondary" to="/" component={Link}>
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
      <Divider style={{ height: '2px'}}/>
      <Typography variant="h6" gutterBottom>
        Contained by these Test Plans:
      </Typography>
      {testPlans.length === 0 && (
        <Typography variant="body1" gutterBottom>
          No test plans contain this test
        </Typography>
      )}
      <List>
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
    </div>
  );
}

export default TestDetailsPage;
