import bluetooth

### GLOBAL VARIABLES ###
props_dict = {}




### FUNCTIONS ###
def init(props):
    global props_dict
    print("Python: starting challenge init()")

    # Save properties in the global variable
    props_dict = props
    
    # Execute the challenge once during the init, so key is calculated from the beginning
    executeChallenge()
    return 0




def executeChallenge():
    print("Python: starting executeChallenge()")

    # The key will be 0000 or name+MAC depending on if the device is near or not
    cad = ""

    print("Searching...")

    devices = bluetooth.discover_devices(duration=8, lookup_names=True,
                                                flush_cache=True, lookup_class=False)


    for device in devices:
        cad=cad+device[1]+"-"
    cad=cad[:-1]
    cad=(cad.strip()).replace(" ","")
    if(len(cad)==0):
        cad='0000'

    # Get key as UTF-8 and calculate its length
    key = bytes(cad, 'utf-8')
    key_size = len(key)

    # The result is a tuple (key, key_size)
    result = (key, key_size)
    print("Python:", result)

    return result


if __name__ == "__main__":
    # Use a dictionary as example of properties obtained from the json
    props_example_dict = {"param1": "hola", "param2": 3}
    init(props_example_dict)
    executeChallenge()








