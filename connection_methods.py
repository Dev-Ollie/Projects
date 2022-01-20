import time
connection_methods = {"Wired Wireless": "\nTwo modes of connection.\n",
                    "Ethernet": "\nWired connection standard\n", 
                    "Ethernet Cables Include": "\nPhysical Connections, Data Handling, Error Handling.\n", 
                    "Frame": "\nA single Ethernet packet of data.", "MAC": "Media Access Control.\n", 
                    "Data Collision": "\nTwo data packets trying to use a cable at the same time so neither can get through without getting corrupted.\n",
                    "Handshaking": "\nThe agreed way for two devices to exchange data.\n",
                    "Wifi and Bluetooth": "\nTwo Wireless connection standards.\n",
                    "Bluetooth features include": "\nWorks when devices are close, uses very little power\n",
                    "Wifi limitations": "\nSecurity - so encryption is essential Limited number of connections - Limited range.\n",
                    "Wifi alliance": "\nA group of companies around the world that make sure wifi enabled devices can work with each other.\n"
                    }
search_terms = "\nPlease enter any of the following search terms to see the definition:\n\nEthernet\nEthernent Cables Include\nFrame\nData Collision\nHandshaking\nWifi and Bluetooth\nBluetooth features include\nWifi limitations\nWifi alliance"

x = False
while x == False:
    x = True
    print(search_terms)
    search = input("\nEnter the term: ")
    if search in connection_methods:
        print(connection_methods[search])
        time.sleep(3)
        x = False
    else:
        print("\nPlease enter a valid search term.\n")
        time.sleep(3)
        x = False