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

import AddTestDialog from "./dialogs/AddTestDialog";

function TestPlanDetailsPage() {
  const [object, setObject] = useState(null);
  const [tests, setTests] = useState([]);
  const { id } = useParams();

  useEffect(() => {
    fetchObject();
    fetchTests();
  }, []);

  const fetchObject = async () => {
    try {
      // Itt használhatod az id változót a request összeállításához
      const response = await axios.get(`/api/testPlan/${id}`);
      setObject(response.data);
    } catch (error) {
      console.error("Error fetching object:", error);
    }
  };

  const fetchTests = async () => {
    try {
      const response = await axios.get(`/api/getContainsTP/${id}`);
      setTests(response.data);
    } catch (error) {
      console.error("Error fetching tests:", error);
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
          <AddTestDialog />
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
            Test Plan ID: {object.id}
          </Typography>
        </Grid>
        <Grid item xs={3}>
          <Typography
            variant="body1"
            gutterBottom
            style={{ fontWeight: "bold" }}
          >
            Last run: {object.runAt}
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
        Tests:
      </Typography>
      {tests.length === 0 && (
        <Typography variant="body1" gutterBottom>
          No test has added yet...
        </Typography>
      )}
      <List>
        {tests.map((obj) => (
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
                  <IconButton to={`/testDetails/${obj.id}`} component={Link}>
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

export default TestPlanDetailsPage;
