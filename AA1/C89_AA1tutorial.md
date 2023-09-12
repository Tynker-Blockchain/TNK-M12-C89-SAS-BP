Fetch additional Block details
=======================

In this activity, you will learn to fetch additional details of a live block from the Ethereum network.

<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10685183/c89AA1.gif" width = "401" height = "180">

Follow the given steps to complete this activity:


1. Fetch data from Api.


* Open file `getBlock.py`.


* Fetch the The unix timestamp for the `apiBlockData` store it in the `transactionTimeStamp` variable.


    ```sh
    transactionTimeStamp = datetime.datetime.fromtimestamp(apiBlockData['timestamp'])
    ```


* Convert the timestamp in the readable format like Y-M-H-M-S and store it in `blockData`.


    ```sh
    readableDate = transactionTimeStamp.strftime("%Y-%m-%d %H:%M:%S")

    blockData['timestamp'] = readableDate
    ```


* Fetch the hexadecimal of the difficulty of the Ethereum block from the `apiBlockData` and store it in `blockData`.

    ```sh
    blockData['difficulty'] = apiBlockData['difficulty']
    ```
   
* Fetch the hexadecimal of the total difficulty of the chain until this Ethereum block.

    ```sh
    blockData['totalDifficulty'] = apiBlockData['totalDifficulty']
    ```
   
* Fetch the maximum gas allowed in the Ethereum block.

    ```sh
    blockData['gasLimit'] = apiBlockData['gasLimit']
    ```


* Fetch the total used gas by all transactions in the Ethereum block.

    ```sh
    blockData['gasUsed'] = apiBlockData['gasUsed']
    ```


2. Display data on UI.


* Open file `index.html`


* Create a new paragraph for the extra data of the block.


    ```sh
    <p style="color:red;">Extra Data of the Block:</p>
    ```


* Show the readable timestamp of the block.


    ```sh
    Timestamp:{{blockData.timestamp}}</br>
    ```


* Show the difficulty of the block.


    ```sh
    Difficulty:{{blockData.difficulty}}</br>
    ```


* Show the total difficulty of the chain until this Ethereum block.


    ```sh
    Total Difficulty:{{blockData.totalDifficulty}}</br>
    ```


* Show the maximum gas allowed in the Ethereum block.


    ```sh
    Gas Limit:{{blockData.gasLimit}}</br>
    ```


* Show the total used gas by all transactions in the block.


    ```sh
    Gas Used:{{blockData.gasUsed}}</br>
    ```


* Save and run the code to check the output.
