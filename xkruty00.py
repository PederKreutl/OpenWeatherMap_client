#!/usr/bin/env python3.6
################################################################################
# File:     OpenWeatherMapClient.py                                            #
# Project:  2BIT IPK, Network client application                               #
#           Faculty of Information Technolgy                                   #
#           Brno University of Technology                                      #
# Date:     17.03.2019                                                         #
# Author:   Peter Kruty <xkruty00@stud.fit.vutbr.cz>                           #
################################################################################

# API KEY: f46dc4f4974f69bfa7ae67791582ec30

################################### MODULES ####################################
import argparse # Arguments parsing
import socket   # Sockets
import re       # Regular expressions
import json     # JSON parsing
import sys

############################## PARSING ARGUMENTS ###############################
try:
    parser = argparse.ArgumentParser();
    parser.add_argument("api_key"); # api_key argument
    parser.add_argument("city");    # city argument
    args = parser.parse_args();
except:
    sys.stderr.write("ERROR: Problem with parsing script parameters!\n");
    exit(1);


if len(sys.argv) != 3:
    sys.stderr.write("ERROR: Problem with parsing script parameters!\n");
    exit(1);

if args.api_key == "" or args.city == "":
    sys.stderr.write("ERROR: Application key or city name is missing!\n");
    exit(1);


############################ CREATING CLIENT SOCKET ############################
# Object socket and method socket() which create  client socket
# AF_INET - specifies adress family (in this case IPv4, AF_INET6 is for IPv6)
# SOCK_STREAM - specifies type of socket (in this case TCP, SOCK_DGRAM is for UDP)
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
except:
    sys.stderr.write("ERROR: Cannot create socket!\n");
    exit(1);

############################# CONNECTING TO SERVER #############################
HOST = '95.85.63.65';
PORT = 80;

try:
    client_socket.connect((HOST, PORT));
except:
    sys.stderr.write("ERROR: Cannot connect to server!\n");
    client_socket.close();
    exit(1);

########################## SENDING MESSAGE TO SERVER ###########################
host_name = 'api.openweathermap.org';
host_data = '/data/2.5/weather?q=' + args.city + '&APPID=' + args.api_key + '&units=metric&mode=json';
client_message = ('GET ' + host_data + ' HTTP/1.1\r\n'            # Request line
                  'Host: ' + host_name + '\r\n'                   # Header line
                  'Connection: close\r\n'                         # Header line
                  '\r\n');                                        # Blank line

try:
    client_socket.sendall(client_message.encode('utf-8'));
except:
    sys.stderr.write("ERROR: Cannot send message to server!\n");
    client_socket.close();
    exit(1);

################################ RECEIVING DATA ################################
try:
    weather_data = client_socket.recv(4096); 
except:
    sys.stderr.write("ERROR: Problem with receiving data from server!\n");
    client_socket.close();
    exit(1);


############################## CLOSING CONNECTION ##############################
try:
    client_socket.close();
except:
    sys.stderr.write("ERROR: Cannot close socket!\n");
    exit(1);

################################# PARSING DATA #################################
try:
    weather_data = weather_data.decode("utf-8");
    weather_data = re.search("{.*$", weather_data); # Deleting HTTP data
    weather_data = weather_data.group();
    weather_data = json.loads(weather_data); # Parsing json data
except:
    sys.stderr.write("ERROR: Problem with received data!\n");
    exit(1);

if "cod" not in weather_data:
    sys.stderr.write("ERROR: Problem with received data!\n");
    exit(1);

if (weather_data["cod"] != 200 and "message" in weather_data):
    error_msg = "ERROR " + str(weather_data["cod"]) + ": " +  str(weather_data["message"]) + "!\n"
    sys.stderr.write(error_msg);
    exit(1);
elif (weather_data["cod"] != 200):
    sys.stderr.write("ERROR: Problem with received data!\n");
    exit(1);



################################ PRINTING DATA #################################
try:
    if "name" in weather_data:
        print(weather_data["name"]);
    else:
        print("city-name: n/a");

    if "weather" in weather_data and weather_data["weather"][0] and "description" in weather_data["weather"][0]:
        print(weather_data["weather"][0]["description"]);
    else:
        print("weather-description: n/a");

    if "main" in weather_data and "temp" in weather_data["main"]:
        print("temperature: " + str(weather_data["main"]["temp"]) + "°C");
    else:
        print("temperature: n/a");

    if "main" in weather_data and "humidity" in weather_data["main"]:
        print("humidity: " + str(weather_data["main"]["humidity"]) + "%");
    else:
        print("humidity: n/a");

    if "main" in weather_data and "pressure" in weather_data["main"]:
        print("pressure: " + str(weather_data["main"]["pressure"]) + " hPa");
    else:
        print("pressure: n/a");

    if "wind" in weather_data and "speed" in weather_data["wind"]:
        print("wind-speed: " + str(weather_data["wind"]["speed"]) + " km/h");
    else:
        print("wind-speed: n/a");

    if "wind" in weather_data and "deg" in weather_data["wind"]:
        print("wind-deg: " + str(weather_data["wind"]["deg"])); 
    else:
        print("wind-deg: n/a");

except:
    sys.stderr.write("ERROR: Problem with printing output data!\n");
    exit(1);

################################# END OF FILE ##################################
