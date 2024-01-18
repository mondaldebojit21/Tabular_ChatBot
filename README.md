# Tabular ChatBot

Welcome to Tabular ChatBot – your friendly AI-powered conversationalist for extracting insights from your tabular data!

<table>
  <tr>
    <td><img src="Screenshot%201.png" alt="Tabular ChatBot Demo Index" width="500"/></td>
    <td><img src="Screenshot%202.png" alt="Tabular ChatBot Demo chat" width="500"/></td>
  </tr>
</table>

## Overview

Tabular ChatBot is a unique application designed to effortlessly extract information from your CSV files using OpenAI's powerful API. This repository contains the codebase for an intuitive chatbot interface that communicates with your data in a conversational manner.

## Features

- **Chat-Based Data Extraction:** Interact with your tabular data as if chatting with a friend; no complex queries needed!
- **CSV Compatibility:** Upload any .csv file and let the chatbot dive into its contents for valuable insights.
- **OpenAI Integration:** Powered by OpenAI's API for seamless data analysis and responses.
- **Intuitive Interface:** User-friendly design for easy navigation and data interaction.

## Getting Started

### Prerequisites

- Obtain an OpenAI API key.
- Python installed on your local machine.

### Installation

1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`.

### Usage

1. Run the application.
2. Provide your OpenAI API key
3. Upload your .csv file.
4. Chat with the bot to extract information from your data effortlessly.

## Docker Image

This repository also contains the Dockerfile to build and run the Tabular ChatBot app using Docker. Use the following steps to get started:

### Docker Installation

Install Docker by following the instructions [here](https://docs.docker.com/get-docker/).

### Build and Run

Clone this repository and navigate to the directory:

```bash
  git clone https://github.com/mondaldebojit21/Tabular_ChatBot.git
  cd Tabular_ChatBot
```

Build the Docker image:

```bash
  docker build -t Tabular_ChatBot .
```

Run the Docker container:

```bash
  docker run -d -p 3000:3000 Tabular_ChatBot
```

Access the app by visiting [http://localhost:3000](http://localhost:3000) in your web browser.
