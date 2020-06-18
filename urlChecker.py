import requests

existingUrls = []
existingCount =0
exists = True

with open("links.txt") as infile:
    line = infile.readline()
    lineCount=0
    while line:
       curline = line.strip()
       line = infile.readline()
       lineCount += 1
       try:
           request = requests.get("http://"+curline, timeout = 2)

       except requests.ConnectTimeout:
           print(f"{lineCount} Connection to {curline} timed out")
           exists = False

       except requests.ConnectionError:
           print(f"{lineCount} Couldn't connect to {curline}")
           exists = False

       except requests.ReadTimeout:
           print(f"{lineCount} Read timed out.")
           exists = False

       if request.status_code < 400 and exists:
            print(f"{lineCount} {curline} exists!")
            print(f"-----{request.status_code}------")
            existingUrls.append(curline)
            existingCount += 1
       else:
          print(f"{lineCount} {curline} doesn't exist!")
          exists = True


    print(f"{existingCount} active url's found:")

    counter = 1
    for url in existingUrls:
        print(f"{counter}. {url} ")
        counter+=1