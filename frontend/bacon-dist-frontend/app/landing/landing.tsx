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

    const getActorBaconDistance = () => {
        const actorNameElement = document.getElementById(
            "Actor Name",
        ) as HTMLInputElement;

        setActorName(actorNameElement.value);
        setLoading(true);

        axios
            .get(`http://127.0.0.1:8000/bacon-dist/${actorNameElement.value}`)
            .then((response) => {
                console.log(response);
                setBaconDistance(response.data["bacon_distance"]);
                setDisplayBaconDistance(true);
            })
            .catch((reason) => {
                console.error(reason);
                setDisplayBaconDistance(false);
            })
            .finally(() => {
                setLoading(false);
            });
    };

    return (
        <>
            <Container maxWidth="sm">
                <Grid container sx={{ justifyContent: "center" }}>
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
                        <TextField label="Actor Name" id="Actor Name" />
                        <Button
                            variant="contained"
                            endIcon={<SendIcon />}
                            onClick={getActorBaconDistance}
                            loading={loading}
                            loadingPosition="end"
                        >
                            Go
                        </Button>
                        <h2
                            hidden={!displayBaconDistance}
                        >{`Bacon distance of ${actorName} is ${baconDistance}`}</h2>
                    </Stack>
                </Grid>
            </Container>
        </>
    );
};
