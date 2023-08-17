from web3 import Web3
import datetime

def getBlockData(blockNumber):
    try:
        apiUrl = 'https://mainnet.infura.io/v3/ec5acb1175dc468c9f3ee9a84a02fe98' 
        web3 = Web3(Web3.HTTPProvider(apiUrl))
        apiBlockData = web3.eth.get_block(blockNumber)
    except:
            apiBlockData ="NoBlock"
            return apiBlockData

    blockData = {}
    blockData['totalDifficulty'] = apiBlockData['totalDifficulty']
    blockData['blockNumber'] = apiBlockData['number']
    blockData['size'] = apiBlockData['size']
    blockData['currentHash'] = apiBlockData['hash'].hex()
    blockData['previousHash'] = apiBlockData['parentHash'].hex()  
    transactionTimeStamp = datetime.datetime.fromtimestamp(apiBlockData['timestamp'])
    readableDate = transactionTimeStamp.strftime("%Y-%m-%d %H:%M:%S")
    blockData['timestamp'] = readableDate

    #Fetch the hexadecimal of the difficulty of ethereum block.
    
    
    #Fetch the hexadecimal of the total difficulty of the chain until this ethereum block.
    
    
    #Fetch the maximum gas allowed in ethereum block.
    

    #Fetch the total used gas by all transactions in ethereum block.
    


    numberOfTransactions = len(apiBlockData['transactions'])
    blockData['numberOfTransactions'] = numberOfTransactions
    allTransactions = []
    try:
        for transactionIndex in range(1, 11):
            transaction = {}
            transactionHash = apiBlockData['transactions'][transactionIndex]
            transaction['transactionHash'] = transactionHash.hex()
            transactionDetails = web3.eth.get_transaction(transactionHash)
            transaction['srno'] = transactionIndex
            transaction['receiver'] = transactionDetails['to']
            transaction['sender'] = transactionDetails['from']
            transactionAmount = int(transactionDetails['value']) / 10 ** 18
            transaction['amount'] = transactionAmount
            allTransactions.append(transaction)
        blockData['transactions'] = allTransactions
    except:
        blockData['transactions'] = []
        return blockData  

    blockData['transactions'] = allTransactions
    return blockData   