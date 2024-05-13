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
import {
  Edit,
  Delete,
  Save,
  RemoveRedEye,
  ArrowBackIos,
} from "@material-ui/icons";

function TestExecutionDetailsPage() {
  const [object, setObject] = useState(null);
  const [test, setTest] = useState(null);
  const [images, setImages] = useState([]);
  const [refImages, setRefImages] = useState([]);
  const { id } = useParams();

  useEffect(() => {
    fetchImages();
    fetchRefImages();
    fetchObject();
  }, []);

  const listStyle = {
    // maxHeight: "600px",
    overflow: "auto",
    background: "#eeeeee",
  };

  const fetchObject = async () => {
    try {
      const response = await axios.get(`/api/testExecution/${id}`);
      setObject(response.data);
      const testResponse = await axios.get(`/api/test/${response.data.testID}`);
      setTest(testResponse.data);
    } catch (error) {
      console.error("Error fetching object:", error);
    }
  };

  const fetchImages = async () => {
    try {
      const response = await axios.get(`/api/testImage/testExecution/${id}`);
      setImages(response.data);
    } catch (error) {
      console.error("Error fetching images:", error);
    }
  };

  const fetchRefImages = async () => {
    try {
      const response = await axios.get(`/api/testExecution/reference/${id}`);
      setRefImages(response.data);
    } catch (error) {
      console.error("Error fetching reference images:", error);
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

  if (object === null || test === null) {
    return <h1>Loading...</h1>;
  }

  return (
    <div style={{ width: "100%" }}>
      <Grid container spacing={2}>
        <Grid item xs={11}>
          <Typography variant="h4" gutterBottom style={{ fontWeight: "bold" }}>
            Test Execution ({object.id}) for {test.name}
          </Typography>
        </Grid>
        <Grid item xs={1}>
          <IconButton to={`/testDetails/${test.id}`} component={Link}>
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
        Test Report:
      </Typography>
      <List style={listStyle} >
        <ListItem  style={{ display: 'flex', textAlign: 'center' }}>
          <ListItemText primary="Step Name" secondary="Status" />
          <ListItemText primary="Reference Image" />
          <ListItemText primary="Image" />
        </ListItem>
        <Grid container spacing={1} alignItems="center" justifyContent="center">
        {images.map((image, index) => (
          <ListItem key={index} style={{ display: 'flex', textAlign: 'center' }}>
            <Grid item lg={4} style={{ maxWidth: '100%', flexBasis: '100%' }}>
            <ListItemText primary={image.name} secondary={image.status} />
            </Grid>
            <div style={{ display: 'flex', justifyContent: 'space-between' }}>
            <Grid item lg={4} style={{ maxWidth: '100%', flexBasis: '100%' }}>
            {refImages[index] && (
              <img
                src={`/api/testExecution/image/${refImages[index].id}/`}
                alt={refImages[index].name}
                style={{ width: "100%", height: "auto" }}
              />
            )}
            </Grid>
            <Grid item lg={4} style={{ maxWidth: '100%', flexBasis: '100%' }}>
            <img
              src={`/api/testExecution/image/${image.id}/`}
              alt={image.name}
              style={{ width: "100%", height: "auto" }}
            />
            </Grid>
            </div>
          </ListItem>
        ))}
        </Grid>
      </List>
    </div>
  );
}

export default TestExecutionDetailsPage;
