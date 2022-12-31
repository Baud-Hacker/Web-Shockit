import asyncio
import websockets
import sys
import logging





async def main():
    logger = logging.getLogger('websockets')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    with open(sys.argv[2], "r") as wordlist:
        with open(sys.argv[3], "r") as request:
            url = sys.argv[4]
            requestdata = request.read()
            async with websockets.connect(url) as ws:
                for wordline in wordlist:
                    fuzzreq = str(requestdata).replace("%%FUZZME%%",str(wordline).replace("\n",""))
                    await ws.send(fuzzreq)

                    # uncomment to wait for reponse.
                    reponse = await ws.recv()
                    #print(f'Reponse length: {len(reponse)} Request length: {len(reponse)}')



async def bin_main():
    logger = logging.getLogger('websockets')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    with open(sys.argv[2], "r") as wordlist:
        with open(sys.argv[3], "rb") as request:
            url = sys.argv[4]
            requestdata = request.read()

            async with websockets.connect(url) as ws:
                for wordline in wordlist:
                    fuzzreq = str(requestdata).replace("%%FUZZME%%", str(wordline).replace("\n", ""))
                    await ws.send(fuzzreq)
                    reponse = await ws.recv()





if __name__ == "__main__":
    if sys.argv[1] == "txt":
        asyncio.run(main())
    elif sys.argv[1] == "bin":
        asyncio.run(bin_main())
    elif sys.argv[1] == "-h":
        print("""
 oooooo   oooooo     oooo            .o8             .oooooo..o oooo                            oooo         o8o      .   
 `888.    `888.     .8'            \"888            d8P'    `Y8 `888                            `888         `\"'    .o8   
  `888.   .8888.   .8'    .ooooo.   888oooo.       Y88bo.       888 .oo.    .ooooo.   .ooooo.   888  oooo  oooo  .o888oo 
   `888  .8'`888. .8'    d88' `88b  d88' `88b       `\"Y8888o.   888P\"Y88b  d88' `88b d88' `\"Y8  888 .8P'   `888    888   
    `888.8'  `888.8'     888ooo888  888   888           `\"Y88b  888   888  888   888 888        888888.     888    888   
     `888'    `888'      888    .o  888   888      oo     .d8P  888   888  888   888 888   .o8  888 `88b.   888    888 . 
      `8'      `8'       `Y8bod8P'  `Y8bod8P'      8\"\"88888P'  o888o o888o `Y8bod8P' `Y8bod8P' o888o o888o o888o   \"888\" 

Command example: 'python main.py [bin|txt] [wordlist file] [request file] [wss://|ws:// example.com]""")
    else:
        print("""
 oooooo   oooooo     oooo            .o8             .oooooo..o oooo                            oooo         o8o      .   
 `888.    `888.     .8'            \"888            d8P'    `Y8 `888                            `888         `\"'    .o8   
  `888.   .8888.   .8'    .ooooo.   888oooo.       Y88bo.       888 .oo.    .ooooo.   .ooooo.   888  oooo  oooo  .o888oo 
   `888  .8'`888. .8'    d88' `88b  d88' `88b       `\"Y8888o.   888P\"Y88b  d88' `88b d88' `\"Y8  888 .8P'   `888    888   
    `888.8'  `888.8'     888ooo888  888   888           `\"Y88b  888   888  888   888 888        888888.     888    888   
     `888'    `888'      888    .o  888   888      oo     .d8P  888   888  888   888 888   .o8  888 `88b.   888    888 . 
      `8'      `8'       `Y8bod8P'  `Y8bod8P'      8\"\"88888P'  o888o o888o `Y8bod8P' `Y8bod8P' o888o o888o o888o   \"888\" 

Command example: 'python main.py [bin|txt] [wordlist file] [request file] [wss://|ws:// URL]""")
