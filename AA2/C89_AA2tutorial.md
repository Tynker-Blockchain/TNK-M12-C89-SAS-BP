Change Transaction Limit
========================

In this activity, you will learn to increase the limit on the number of transactions in the block.

<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10685119/c89AA2.gif" width = "401" height = "179">


Follow the given steps to complete this activity:


1. Modify the block class.


* Open file `blockchain.py`.


* Create a variable to store the transaction limit of the block.


    ```sh
    minimumTransaction = 1
    ```


* Create a variable to increment the block size of the next block.

    ```sh
    nextBlockSizeIncrement = 1
    ```


* Once the transaction is added in the block, check if the index of the block is equal to nextBlockSizeIncrement.


    ```sh
    if self.index == self.nextBlockSizeIncrement:
    ```


* Increase the limit of transactions to be stored in a block.


    ```sh
    Block.minimumTransaction +=1
    ```


* Increase the block size of the next block.


    ```sh
    Block.nextBlockSizeIncrement +=1
    ```


* Save and run the code to check the output.
