# waypoint-api
![](https://img.shields.io/badge/Development-Ongoing-blue)

> A web API to query for Canadian waypoints and create simple flight plans, written in Python (Flask)

[Jump to documentation](#documentation)
<br>
[Jump to installation](#installation)


# Purpose

An extracurricular project to practice Python, SQL, client-side JavaScript, and Flask.

<br>

![Project-Screenshot](https://github.com/Hussein-249/waypoint-api/assets/105606941/687f092a-8c09-4ac0-8dd6-9f301fa55227)

# Packages & Environment

This project is being developed with Python 3.11. Project requirements are listed in ```requirements.txt```.

The in-browser map is created using Leaflet.js through a CDN. No installation of Leaflet is required.

## Installation
<a id="Installation"></a>
- Ensure that PostgreSQL is installed an PostgreSQL server is running using the following PowerShell command:
```powershell
Get-Process | Where-Object { $_.ProcessName -eq "postgres" }
```
Or Bash:
```bash
pgrep postgres || pgrep postmaster 
```
- Clone this repository
- Create a virtual environment using ```python -m venv venv```. This creates a venv folder that will contain the necessary libraries
```powershell
python -m venv venv
```
- Activate the virtual environment with ```venv\Scripts\activate```. The shell should now indicate you are in the virtual environment.
- Install the requirements with ```pip install -r requirements.txt```
```powershell
pip install -r requirements.txt
```

[//]: # (- Start the application with ```python main.py```)
- Once you are finished with the application, you can deactivate the virtual environment using ```deactivate```.

# Development Checklists
### Core Features Supported
- [x] Can query for individual waypoints via URL

### Core Features In Progress
- [ ] Can generate maps of waypoint(s)
- [ ] Finds optimal (shortest) path between multiple waypoints
- [ ] Generates flightplan based on origin, destination, and additional waypoints
- [ ] Generates headings and provides weather information in flight plan
- [ ] Includes all North American Waypoints

### Potential Features
- [ ] Responsive Design (Unlikely as the utility is not designed for mobile devices, but tablets should work fine.)

# Documentation
<a id="documentation"></a>
The documentation for this app can be found at the /documentation route.
