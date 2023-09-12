Add multiple transactions to the Block
======================================

In this activity, you will learn to add multiple transactions to the Block.


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10641875/sa3.gif" width = "401" height = "185">


Follow the given steps to complete this activity:


1. Limit the transaction.


* Open file `blockChain.py`.


* Remove the `transaction` parameter from the init() method inside class `Block`.


* Replace `transaction` with `transactions` in the `blockString`.

    ```sh
    blockString = str(self.index) + str(timestamp) + str(self.previousHash) + json.dumps(self.transactions)
    ```


* Define an addTransaction method that receives `transaction` as a parameter.


    ```sh
    def addTransaction(self, transaction):
    ```


* Check if `transaction` exists.

    ```sh
    if transaction:
    ```


* Append the `transaction` to `self.transactions`.

    ```sh
    self.transactions.append(transaction)
    ```


* Limit the number of transactions to `3` in a block by checking if the length of `self.transactions` is equal to 3, then calculate the hash.

    ```sh
    if len(self.transactions) == 3:
 		self.currentHash = self.calculateHash()
    ```


* Return `"Ready"`.

    ```sh
    return "Ready"
    ```


* Return `"Add more transactions"`if the limit is not reached.

    ```sh
    return "Add more transactions"
    ```

2. Create the block and add to blockchain.


* Open file `app.py`.


*  Remove the `transaction` key from `blockData`. The `blockData` Dictionary should look like this:

    ```sh
    blockData = {

        'index': index,


        'timestamp': time(),


        'previousHash': "No Previous Hash.",

    }
    ```


* Add a condition to check if `currentBlock` is set to None.

    ```sh
    if currentBlock == None:
    ```


* Remove the transaction parameter sent to Block() constructor. Move the entire code inside the if condition.

    ```sh
    currentBlock = Block(

        blockData["index"],

        blockData["timestamp"],

        blockData["previousHash"])
    ```


* Assign the return value from addTransaction method to the `status` variable.

    ```sh
    status = currentBlock.addTransaction(transaction)
    ```


* Check if the `status` is `Ready`.

    ```sh
    if status == "Ready":
    ```


* Move the code to add the block to the blockchain inside the if condition.

    ```sh
    chain.addBlock(currentBlock)
    ```

    ```sh
    isValid = chain.validateBlock(currentBlock)
    ```

    ```sh
    currentBlock.isValid = isValid
    ```
           
* Set the `currentBlock` to `None` inside the if condition.


    ```sh
    currentBlock = None
    ```

* Save and run the code to check the output.
