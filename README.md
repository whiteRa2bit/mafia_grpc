<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Mafia service and client based on grpc


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.


### Installation

- **Local**
  1. Clone the repo
     ```sh
     git clone https://github.com/whiteRa2bit/mafia_grpc.git
     ```
  2. Create venv
     ```
     python3 -m venv venv
     . venv/bin/activate
     ```
  3. Install requirements
     ```
     pip3 install -r requirements.txt
     ```

- **Docker**

    You can either build an image yourself or pull a ready one from [Dockerhub](https://hub.docker.com/repository/docker/whitera2bit/mafia)

    - Build
        ```
        docker build -t whitera2bit/mafia . -f dockerfiles/Dockerfile
        ```

    - Pull from Dockerhub
        ```
        docker pull whitera2bit/mafia
        ```

## Usage
First run server
- If you used local setup:
    ```
    python mafia/service/mafia_service.py
    ```

- If you used docker:
    ```
    docker run --name mafia -t whitera2bit/mafia /bin/bash
    python mafia/service/mafia_service.py
    ```

Then you can connect to a running server using:
- If you used local setup:
    ```
    python mafia/service/mafia_client.py
    ```

- If you used docker:
    ```
    docker exec -it mafia /bin/bash
    python mafia/service/mafia_client.py
    ```

### Service Config
`MIN_USERS_NUM` - minimum number of users to start a game

`MAFIA_NUM` - nubmer of mafia players

### Client commands
`GET_USERS` - get list of users

`BROADCAST` - send message to other users, during night mafia and detective can communicate using it as well

`VOTE_FINISH_DAY` - vote for end of the day

`DECISION` - used to send mafia or detective decisions

`ACCUSE` - used for voting who to kill during day


## License

Distributed under the MIT License. See `LICENSE` for more information.


## Contact

Pavel Fakanov - pavel.fakanov@gmail.com

Project Link: [https://github.com/whiteRa2bit/mafia_grpc](https://github.com/whiteRa2bit/mafia_grpc)
