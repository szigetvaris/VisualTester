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
} from "@material-ui/core";
import { Link } from "react-router-dom";

import AddTestDialog from "./dialogs/AddTestDialog";

function TestPlanDetailsPage() {
  const [object, setObject] = useState(null);
  const { id } = useParams();

  useEffect(() => {
    fetchObject();
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


  const handleNameChange = (event) => {
    object.name = event.target.value;
  };


  if (object === null) {
    return (
      <div>
        <p>Loading...</p>
      </div>
    );
  }

  return (
    <div style={{ backgroundColor: "#fff199", width: "100%" }}>
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
    </div>
  );
}

export default TestPlanDetailsPage;
