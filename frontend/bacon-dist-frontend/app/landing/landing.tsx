import {
    Alert,
    Button,
    Container,
    Grid,
    Stack,
    TextField,
} from "@mui/material";
import SendIcon from "@mui/icons-material/Send";
import axios from "axios";
import { useState } from "react";

export const Landing = () => {
    const [loading, setLoading] = useState(false);
    const [actorName, setActorName] = useState("");
    const [baconDistance, setBaconDistance] = useState("");
    const [displayBaconDistance, setDisplayBaconDistance] = useState(false);
    const [displayError, setDisplayError] = useState(false);

    const getActorBaconDistance = () => {
        const actorNameElement = document.getElementById(
            "Actor Name",
        ) as HTMLInputElement;

        const actorNameValue = actorNameElement.value;

        if (actorNameValue == "") {
            setDisplayError(true);
            return;
        }

        setDisplayError(false);
        setActorName(actorNameValue);
        setLoading(true);

        axios
            .get(`http://127.0.0.1:8000/bacon-dist/${actorNameValue}`)
            .then((response) => {
                setBaconDistance(response.data["bacon_distance"]);
                setDisplayBaconDistance(true);
            })
            .catch((reason) => {
                setDisplayBaconDistance(false);
            })
            .finally(() => {
                setLoading(false);
            });
    };

    return (
        <>
            <Container maxWidth="sm">
                <Grid container>
                    <Stack spacing={2}>
                        <center>
                            <h1>Bacon Distance Calculator</h1>
                        </center>
                        <Alert icon={false} severity="info">
                            "Six Degrees of Kevin Bacon or Bacon's Law is a
                            parlor game where players challenge each other to
                            choose an actor whom they connect to another actor
                            via a film in which both actors appeared: this is
                            repeated to try to find the shortest path that leads
                            to prolific American actor Kevin Bacon. It rests on
                            the assumption that anyone involved in the Hollywood
                            film industry can be linked through their film roles
                            to Bacon within six steps." - Wikipedia
                        </Alert>
                        <TextField
                            label="Actor Name"
                            id="Actor Name"
                            error={displayError}
                            helperText={
                                displayError
                                    ? "Please enter an actors name"
                                    : ""
                            }
                        />
                        <Button
                            variant="contained"
                            endIcon={<SendIcon />}
                            onClick={getActorBaconDistance}
                            loading={loading}
                            loadingPosition="end"
                        >
                            Go
                        </Button>
                        <center>
                            <h2
                                hidden={!displayBaconDistance}
                            >{`Bacon Distance of ${actorName} is ${baconDistance}`}</h2>
                        </center>
                    </Stack>
                </Grid>
            </Container>
        </>
    );
};
