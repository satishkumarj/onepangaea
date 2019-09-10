import requests
import json
import os
import sys
import getopt
import time
import pandas as pd
import io

#argv = sys.argv[1:]
wallet = 'one18ndk75w6nea5x7nxjhvv0xj6zfdsc7nks3f778'
shardId = '0'
sent_addresses_file = "sent_addresses.txt" #D:\HarmonyOne\onepangaea\sent_addresses.txt
"""try:
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
"""
while(1):    
    url = "https://harmony.one/pga/network.csv"
    s = requests.get(url).content
    ds = pd.read_csv(io.StringIO(s.decode('utf-8')))
    """response = json.loads(requests.get("https://harmony.one/pga/network.json").text)
    online_addresses = []
    shards = response['shards']
    if bool(shards):
        for i in range(0,4):
            shard = shards['{}'.format(i)]
            if bool(shard):
                nodes = shard['nodes'] 
                if bool(nodes):
                    online_addresses.append(nodes['online'])
    """
    with open(sent_addresses_file, 'r') as f:
        sent_addresses = f.readlines()
    for  index,row in ds.iterrows():
        addr = row["Address"]
        to_shardId = row["Shard"]
        print("Address", addr)
        if not addr in sent_addresses:
            if row["Online"]:
                transfer = './wallet.sh -t transfer --from {} --to {} --amount 0.01 --pass pass:  --toShardID {} --shardID {}'.format(wallet, addr, to_shardId, shardId)
                try:
                    print("Sending 0.01 ONE to {}".format(addr))
                    os.system(transfer)    
                except getopt.GetoptError:
                    print('Exiting due to error executing transfer')
                    sys.exit(2)
                #if i == 1:
                #    sys.exit(2)
                with open(sent_addresses_file, 'a+') as f:
                    f.write("%s\n" % addr)
                time.sleep(2)
    
    open(sent_addresses_file, "w").close()