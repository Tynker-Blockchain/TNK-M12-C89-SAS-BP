Fetch the Transactions
=======================


In this activity, you will learn to fetch the first 10 transactions from the block data.


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/2071954/images/10670832/Activity-2-GIF.gif" width = "401" height = "217">


Follow the given steps to complete this activity:


1. Modify the block class.


* Open file `getBlock.py`


* Declare a variable `allTransaction` and set an empty array to it.


    ```sh
    allTransactions = []
    ```


* Start the `try` block.

    ```sh
    try:
    ```


* Write a for loop to get the 10 transactions.


    ```sh
    for transactionIndex in range(1, 11):
    ```


* Create a `transaction` dictionary.

    ```sh
    transaction = {}
    ```


* Use the `transactionIndex` to read the transaction hash from the API block data using.

    ```sh
    transactionHash = apiBlockData['transactions'][transactionIndex]
    ```


* Store the `transactionHash.hex()` in the `transaction` dictionary.

    ```sh
    transaction['transactionHash'] = transactionHash.hex()
    ```


* Fetch the transaction data using transaction hash value through the API.

    ```sh
    transactionDetails = web3.eth.get_transaction(transactionHash)
    ```




* Store the basic data of the transaction in the dictionary and add it to the allTransactions array.

    ```sh
    transaction['srno'] = transactionIndex
    
    transaction['receiver'] = transactionDetails['to']

    transaction['sender'] = transactionDetails['from']

    transactionAmount = int(transactionDetails['value']) / 10 ** 18

    transaction['amount'] = transactionAmount
    ```


* Add the `transaction` to the `allTransactions` array.

    ```sh
    allTransactions.append(transaction)
    ```


* Add an `except` block.

    ```sh
    except:
    ```


* Set an empty list to the `blockData['transactions']`.

    ```sh
    blockData['transactions'] = []
    ```


* Set `allTransactions` to  the `BlockData['transactions']`.

    ```sh
    blockData['transactions'] = allTransactions
    ```

* Save and run the code to check the output.




