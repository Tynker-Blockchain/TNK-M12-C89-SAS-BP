Fetch the Block Data
=====================

In this activity, you will learn to segregate the data that you want to display, convert it to ether and display on the console.


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/2071954/images/10670779/Activity-1-GIF.gif" width = "401" height = "225">


Follow the given steps to complete this activity:


1. Fetch the data and store it.


* Open file `getBlock.py`.


* Start the `try` block.


   ```sh
   try:
   ```


* Setup the API.

    ```sh
    apiUrl = 'https://mainnet.infura.io/v3/ec5acb1175dc468c9f3ee9a84a02fe98'
    ```


* Setup the httpprovider using `Web3(Web3.HTTPProvider(apiUrl))` to make a request on the api.

    ```sh
    web3 = Web3(Web3.HTTPProvider(apiUrl))
    ```


* Fetching the block data from API by passing the block number to `web3.eth.get_block(blockNumber)` and storing it in the variable `apiBlockData`.

    ```sh
    apiBlockData = web3.eth.get_block(blockNumber)


* Add except block.

    ```sh
    except:
    ```


* Set `apiBlockData` to `"noBlock"` inside the `except` block.

    ```sh
    apiBlockData ="noBlock"
    ```


* Return the `apiBlockData`.


    ```sh
    return apiBlockData
    ```


* Create an empty dictionary `blockData`.


    ```sh
    blockData = {}
    ```


* Store basic details such as `totalDifficulty, number, size, currentHash, previousHash` from `apiBlockData` into the `blockData` dictionary.


    ```sh
    blockData['totalDifficulty'] = apiBlockData['totalDifficulty']
    

    blockData['blockNumber'] = apiBlockData['number']

    blockData['size'] = apiBlockData['size']

    blockData['currentHash'] = apiBlockData['hash'].hex()
   
    blockData['previousHash'] = apiBlockData['parentHash'].hex()
    ```
   
* Store the number of transactions.


   ```sh
   numberOfTransactions = len(apiBlockData['transactions'])
   ```


* Set the number of `numberOfTransactions` to the `blockData`.


    ```sh
    blockData['numberOfTransactions'] = numberOfTransactions
    ```
 
* Return the `blockData`.


    ```sh
    return blockData
    ```


* Save and run the code to check the output.


