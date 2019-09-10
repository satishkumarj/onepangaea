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
    
    for j in range(len(online_addresses)):
        addresses = online_addresses[j]
        for i in range(len(addresses)):
            transfer = './wallet.sh -t transfer --from {} --to {} --amount 0.0001 --pass pass:  --toShardID {} --shardID {}'.format(wallet, online_addresses[i], j, shardId)
            try:
                print("Sending 0.0001 ONE to {}".format(online_addresses[i]))
                os.system(transfer)    
            except getopt.GetoptError:
                print('Exiting due to error executing transfer')
                sys.exit(2)
            #if i == 1:
            #    sys.exit(2)
            time.sleep(2)
    


