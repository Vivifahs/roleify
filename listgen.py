def listgen(bitmask):
    templist = []
    if bitmask & 8388608:
        templist.append("CSC")
    if bitmask & 4194304:
        templist.append("CYEN")
    if bitmask & 2097152:
        templist.append("CIS")
    if bitmask & 1048576:
        templist.append("Graduates")
    if bitmask & 524288:
        templist.append("130-series")
    if bitmask & 262144:
        templist.append("220")
    if bitmask & 131072:
        templist.append("222")
    if bitmask & 65536:
        templist.append("265")
    if bitmask & 32768:
        templist.append("310")
    if bitmask & 16384:
        templist.append("325")
    if bitmask & 8192:
        templist.append("330")
    if bitmask & 4096:
        templist.append("345")
    if bitmask & 2048:
        templist.append("364")
    if bitmask & 1024:
        templist.append("403")
    if bitmask & 512:
        templist.append("404")
    if bitmask & 256:
        templist.append("430")
    if bitmask & 128:
        templist.append("442")
    if bitmask & 64:
        templist.append("443")
    if bitmask & 32:
        templist.append("450")
    if bitmask & 16:
        templist.append("452")
    if bitmask & 8:
        templist.append("470")
    if bitmask & 4:
        templist.append("475")
    if bitmask & 2:
        templist.append("493")
    if bitmask & 1:
        templist.append("498")
    return templist


    
    
    
