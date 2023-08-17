from web3 import Web3
import datetime

def getBlockData(blockNumber):
    try:
        apiUrl = 'https://mainnet.infura.io/v3/ec5acb1175dc468c9f3ee9a84a02fe98'
        web3 = Web3(Web3.HTTPProvider(apiUrl))
        apiBlockData = web3.eth.get_block(blockNumber)
    except:
            apiBlockData = "NoBlock"
            return apiBlockData
    
    blockData = {}
    blockData['totalDifficulty'] = apiBlockData['difficulty']
    blockData['blockNumber'] = apiBlockData['number']
    blockData['size'] = apiBlockData['size']
    blockData['currentHash'] = apiBlockData['hash'].hex()
    blockData['previousHash'] = apiBlockData['parentHash'].hex()
    transactionTimeStamp = datetime.datetime.fromtimestamp(apiBlockData['timestamp'])
    readableDate = transactionTimeStamp.strftime("%Y-%m-%d %H:%M:%S")
    blockData['timestamp'] = readableDate

    numberOfTransactions = len(apiBlockData['transactions'])
    blockData['numberOfTransactions'] = numberOfTransactions

    # Create allTransaction to []
    
    
    # Start try block
    
        # Loop through first ten transaction
        
            # Create transaction dictionary
            
            # Get transactionHash from apiBlockData and store it in transactions
            
            # Fetching the transaction details i.e 'srno', 'receiver', 'sender', 'amount'
            
            # Adding transaction to the list
            
    # Add except block
    
        # Set blockData['transactions'] to empty list
        

    # Set BlockData['transactions'] to allTransactions   
    
    return blockData    
