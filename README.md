# Web-Shockit
A Python based command line tool to fuzz web socket requests

The tool was designed out of the lack of good web socket pen testing tooling. It is designed to allow an attacker to fuzz parameters within a web socket request. 
This tool operated on both binary and text based websocket connections and is intended as a quick and easy too to allow for the manipulation of a large number of web socket requests. 

## Why?
This tool was spawned out of the requirment to interact with a websocket based API which recived JSON. OWASP ZAP was not easy to use when fuzzing web sockets and lacked easy visibility into the requests and reponses. 


## usage
The tool takes a wordlsit and a request/data you wish to fuzz. By adding %%FUZZME%% anywhere in the request you can fuzz a parameter and view the reponse. 

You can stop the tool from waithing for a reponse from the server via commething out 'reponse = await ws.recv()' within the code. This will force the fuzzer to send all of the data down the connection without waiting for a reponse from the server to send the next payload. 

```

 oooooo   oooooo     oooo            .o8             .oooooo..o oooo                            oooo         o8o      .   
 `888.    `888.     .8'            \"888            d8P'    `Y8 `888                            `888         `\"'    .o8   
  `888.   .8888.   .8'    .ooooo.   888oooo.       Y88bo.       888 .oo.    .ooooo.   .ooooo.   888  oooo  oooo  .o888oo 
   `888  .8'`888. .8'    d88' `88b  d88' `88b       `\"Y8888o.   888P\"Y88b  d88' `88b d88' `\"Y8  888 .8P'   `888    888   
    `888.8'  `888.8'     888ooo888  888   888           `\"Y88b  888   888  888   888 888        888888.     888    888   
     `888'    `888'      888    .o  888   888      oo     .d8P  888   888  888   888 888   .o8  888 `88b.   888    888 . 
      `8'      `8'       `Y8bod8P'  `Y8bod8P'      8\"\"88888P'  o888o o888o `Y8bod8P' `Y8bod8P' o888o o888o o888o   \"888\" 

Command example: 'python webShockit.py [bin|txt] [wordlist file] [request file] [wss://|ws:// URL]

```
