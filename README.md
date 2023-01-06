# FiveM Player Count Tracker
This resource lets you track and view multiple servers' past player count via a line chart. The program uses publicly available data from txAdmin server endpoints.

## Installation
Before running the application, make sure to install the required python modules:
- Requests - `pip install requests`
- Matplotlib - `pip install matplotlib`

Once you are done installing the required modules, set up the servers you wish to track. Find the `servers` array, and add an array containing the server name, connection IP and a color of your choice: `["Example Server", "127.0.0.1", "blue"]`

If the IPv4 address is hidden behind a reverse proxy, open a terminal, and write the following: `ping exampleserver.com`

## Updates
Ideas on how to further improve the program can be shared using the Issues or Pull Requests tabs in the repository page.
- [ ] Auto refresh
- [ ] Use of FiveM server ID instead of server IP

## License
The project is licensed under the MIT License