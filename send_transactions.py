import requests
import json
import os
import sys
import getopt
import time

wallet = ''
shardId = ''
def readargs(argv):
   try:
      opts, args = getopt.getopt(argv,"wa:si",["walletaddress=", "sharedid="])
   except getopt.GetoptError:
      print('send_transactions.py -wa your_wallet_address -si shard_id')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-wa", "--walletaddress"):
          wallet = arg
      elif opt in ("-si", "--sharedid"):
          shardId = arg
   if wallet == '' or shardId == '':
        print('send_transactions.py -wa your_wallet_address -si shard_id')
        sys.exit(2)

readargs(sys.argv[1:])
while(1):
    response = json.loads(requests.get("https://harmony.one/pga/network.json").text)
    online_addresses = []
    shards = response['shards']
    if bool(shards):
        for i in range(0,4):
            shard = shards['{}'.format(i)]
            if bool(shard):
                nodes = shard['nodes'] 
                if bool(nodes):
                    online_addresses.append(nodes['online'])
    
    online_addresses = sum(online_addresses, [])
    for i in range(len(online_addresses)):
        transfer = './wallet.sh -t transfer --from {} --to {} --amount 0.0001 --pass pass: --shardID {}'.format(wallet, online_addresses[i], shardId)
        os.system(transfer)
        if i == 3:
            sys.exit(2)
        time.sleep(1)
        print(online_addresses[i])

