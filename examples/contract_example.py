
from dotenv import load_dotenv
import os
import sys
import logging
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from evm_decoder.contract_manager import ContractManager
# Load environment variables
load_dotenv()

def main():
    # Initialize contract manager with your Web3 provider
    provider_url = "http://192.168.0.105:8545"
    contract_manager = ContractManager(provider_url)

    # Example addresses (Ethereum Mainnet)
    uni_v2_pair = "0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc"  # USDC/ETH pair
    uni_v3_pool = "0x8ad599c3A0ff1De082011EFDDc58f1908eb6e6D8"  # USDC/ETH pool

    try:
        # Read from Uniswap V2 pair
        print("\n=== Uniswap V2 Example ===")
        reserves = contract_manager.read_contract(
            contract_type="uni_v2",
            address=uni_v2_pair,
            method="getReserves"
        )
        print(f"Reserves: {reserves}")
        
        token0 = contract_manager.read_contract(
            contract_type="uni_v2",
            address=uni_v2_pair,
            method="token0"
        )
        print(f"Token0: {token0}")

        # Read from Uniswap V3 pool
        print("\n=== Uniswap V3 Example ===")
        slot0 = contract_manager.read_contract(
            contract_type="uni_v3",
            address=uni_v3_pool,
            method="slot0"
        )
        print(f"Slot0: {slot0}")
        
        liquidity = contract_manager.read_contract(
            contract_type="uni_v3",
            address=uni_v3_pool,
            method="liquidity"
        )
        print(f"Liquidity: {liquidity}")

        # Example of writing to contract (commented out for safety)
        """
        private_key = os.getenv("PRIVATE_KEY")
        tx_hash = contract_manager.write_contract(
            contract_type="uni_v2",
            address=uni_v2_pair,
            method="swap",
            args=[0, 1000000, "0xYourAddress", b""],
            private_key=private_key,
            gas_limit=200000
        )
        print(f"Transaction hash: {tx_hash}")
        """

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
