import * as React from "react";
import {
  Button,
  TextField,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
} from "@material-ui/core";
import { Add } from "@material-ui/icons";

export default function FormDialog({ fetchTests}) {
  const [open, setOpen] = React.useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const testPlanID = window.location.pathname.split("/").pop();
    const testID = tID.value;
    fetch("/api/contains", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ testPlanID, testID }),
    })
      .then((response) => {
        if (response.ok) {
          console.log("Test added to Test Plan");
        } else {
          console.error("Error adding test to Test Plan");
        }
      })
      .catch((error) => {
        console.error("Error adding test to Test Plan:", error);
      });

    fetchTests();
    handleClose();
  };

  return (
    <React.Fragment>
      <Button
        variant="contained"
        color="primary"
        startIcon={<Add />}
        onClick={handleClickOpen}
      >
        Add
      </Button>
      <Dialog
        open={open}
        onClose={handleClose}
        PaperProps={{
          component: "form",
          onSubmit: handleSubmit,
        }}
      >
        <DialogTitle>Add Test to Test Plan</DialogTitle>
        <DialogContent>
          <DialogContentText>
            Type Test ID to add test case to Test Plan.
          </DialogContentText>
          <TextField
            autoFocus
            required
            margin="dense"
            id="tID"
            name="Test ID"
            label="Test ID"
            type="e.g. 42"
            fullWidth
            variant="standard"
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button type="submit">Add</Button>
        </DialogActions>
      </Dialog>
    </React.Fragment>
  );
}
