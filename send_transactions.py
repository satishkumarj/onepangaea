import requests
import json
import os
import sys
import getopt
import time

argv = sys.argv[1:]
wallet = ''
shardId = ''
try:
    opts, args = getopt.getopt(argv,"a:s:",["walletaddress=", "sharedid="])
except getopt.GetoptError:
    print('python3 send_transactions.py -a your_wallet_address -s shard_id')
    sys.exit(2)
for opt, arg in opts:
   if opt in ("-a", "--walletaddress"):
       wallet = arg
   elif opt in ("-s", "--sharedid"):
       shardId = arg
if wallet == '' or shardId == '':
   print('python3 send_transactions.py -a your_wallet_address -s shard_id')
   sys.exit(2)
   
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
        if i == 1:
            sys.exit(2)
        time.sleep(1)
        print(online_addresses[i])


