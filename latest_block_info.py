
from web3 import Web3

# Connect to Ethereum network
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if connected
if web3.isConnected():
    print("Connected to Ethereum network!")
else:
    print("Failed to connect.")
    exit()

# Fetch the latest block
latest_block = web3.eth.get_block('latest')

# Display block details
print("Latest Block Information:")
print(f"Block Number: {latest_block['number']}")
print(f"Timestamp: {latest_block['timestamp']}")
print(f"Gas Used: {latest_block['gasUsed']}")
print(f"Gas Limit: {latest_block['gasLimit']}")
print(f"Miner: {latest_block['miner']}")
print(f"Number of Transactions: {len(latest_block['transactions'])}")
