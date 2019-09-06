# Pangaea Phase 2

Send ONE tokens to all live addresses, please follow below steps

(make sure to run the following commands in the same directory where your wallet.sh is present)

**Remove previous script file if exists**
```shell
\rm -rf  send_transactions.p*
```

**Download the latest script**
```shell
wget https://raw.githubusercontent.com/satishkumarj/onepangaea/master/send_transactions.py
```

**Run the program**
```shell
python3 send_transactions.py -a your_wallet_address -s your_shard_id
```
(ex:  ```python3 send_transactions.py -a one18ndk75w6nea5x7nxjhvv0xj6zfdsc7nks3f778 -s 0 ```)

Now program will run continueosly, if you would like to Kill the program, use
**Ctrl-Z** 

This program is tested on Linux running on the Vultr instance, it should work with other vps also you might require to install some dependencies 

Please ping me in Telegram, I will try my best to help you run it.


