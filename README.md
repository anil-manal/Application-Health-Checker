# Application Health Checker

This is a Python Flask web application that checks the uptime and functionality of a given application by analyzing its HTTP status codes.

## Problem Statement

Maintaining the availability and performance of applications is crucial. Applications can experience downtime or issues that may not be immediately apparent. It's important to have a tool that can automatically check the status of an application and report whether it is 'up' (functioning correctly) or 'down' (unavailable or not responding).

## Objective

The objective of this project is to develop a script that can accurately assess the status of an application. The script should:
- Check the uptime of an application by making HTTP requests.
- Determine if the application is 'up' or 'down' based on HTTP status codes.
- Provide a user-friendly web interface where users can input a URL and see the health status of the application.

## Solution

We have developed a Flask web application that meets these objectives. Here’s how the solution works:
- The user enters the URL of the application they want to check.
- The Flask application sends an HTTP GET request to the specified URL.
- Based on the HTTP response status code, the application determines if the application is 'up' (status code 200) or 'down' (any other status code or connection error).
- The result is displayed to the user on the web page.

## Features

- Simple and user-friendly interface to check application status.
- Displays the status (UP/DOWN) along with the HTTP status code.
- Provides error messages if there are issues connecting to the application.

## Deployment

The application is deployed on Vercel and can be accessed at the following URL:
[https://application-health-checker-a7w7bcrr5-anil-manals-projects.vercel.app/](https://application-health-checker-a7w7bcrr5-anil-manals-projects.vercel.app/)
