# Log Parsing Project

This project involves parsing log data from standard input and computing various metrics related to the logs. The script reads lines in a specific format and aggregates statistics based on the content.

## Requirements

- Python 3.4.3 or higher
- No additional libraries are required for this project.

## File Structure

## Input Format

The input log lines should follow this format:

<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

## Usage

1. **Make the scripts executable** (if not done already):

   ```bash
   chmod +x 0-generator.py 0-stats.py

