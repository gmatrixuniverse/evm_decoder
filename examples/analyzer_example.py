import os
import sys
import logging
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from evm_decoder.analyzers.analyzer_manager import AnalyzerManager

# Initialize the AnalyzerManager
analyzer_manager = AnalyzerManager()

# Example transaction data
transaction_data = {
    'input': '0x3593564c000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000a000000000000000000000000000000000000000000000000000000000671562a600000000000000000000000000000000000000000000000000000000000000030b080500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000001e00000000000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000416b6f78e4e000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000005756692cd1bddc2770defee04c2b1476a0ebaba00000000000000000000000000000000000000000000000000416b6f78e4e000000000000000000000000000000000000000000000000300d3db14b378bba97600000000000000000000000000000000000000000000000000000000000000a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002000000000000000000000000c02aaa39b223fe8d0a0e5c4f27ead9083c756cc2000000000000000000000000fbb4f63821e706daf801e440a5893be59094f5cc000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006f0279540eed3fb666e8aaa4571a47e7478b6e9d0000000000000000000000000000000000000000000000000000a92a7feda000',
    'from': '0x05756692cd1BDDc2770DEfee04C2B1476A0EBAbA',
    'to': '0xEf1c6E67703c7BD7107eed8303Fbe6EC2554BF6B',
    'value': '18600000000000000',
    'chain_id': 1,  # Ethereum Mainnet
    'logs': [
        {
            'address': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
            'topics': [
                '0xe1fffcc4923d04b559f4d29a8bfc6cda04eb5b0d3c460751c2402c5c5cc9109c',
                '0x000000000000000000000000ef1c6e67703c7bd7107eed8303fbe6ec2554bf6b',
            ],
            'data': '0x00000000000000000000000000000000000000000000000000416b6f78e4e000'
        },
        {
            'address': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
            'topics': [
                '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef',
                '0x000000000000000000000000ef1c6e67703c7bd7107eed8303fbe6ec2554bf6b',
                '0x000000000000000000000000ef1c6e67703c7bd7107eed8303fbe6ec2554bf6b'
            ],
            'data': '0x00000000000000000000000000000000000000000000000000416b6f78e4e000'
        },
        {
            'address': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
            'topics': [
                '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef',
                '0x000000000000000000000000ef1c6e67703c7bd7107eed8303fbe6ec2554bf6b',
                '0x000000000000000000000000a0f9cbd4faca57764b10d55b26d86d83e9113cbb'
            ],
            'data': '0x00000000000000000000000000000000000000000000000000416b6f78e4e000'
        },
        {
            'address': '0xfbb4f63821e706dAf801E440a5893BE59094f5CC',
            'topics': [
                '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef',
                '0x000000000000000000000000a0f9cbd4faca57764b10d55b26d86d83e9113cbb',
                '0x00000000000000000000000005756692cd1bddc2770defee04c2b1476a0ebaba'
            ],
            'data': '0x0000000000000000000000000000000000000000000004813dc89f0d35197e32'
        },
        {
            'address': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48',
            'topics': [
                '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef',
                '0x000000000000000000000000b8faa80fe04a4afd30c89f40e4fcdc6dafb274d9',
                '0x000000000000000000000000e82701fd630c91d35cdb923516c6a466ecdd0d05'
            ],
            'data': '0x000000000000000000000000000000000000000000000000000de0b6b3a7640000'
        },
        {
            'address': '0xa0f9CBd4FACA57764b10d55B26D86D83e9113cBB',
            'topics': [
                '0x1c411e9a96e071241c2f21f7726b17ae89e3cab4c78be50e062b03a9fffbbad1'
            ],
            'data': '0x000000000000000000000000000000000000000000000001067b596d01011ccb000000000000000000000000000000000000000000121c87455a2f63b7938e17'
        },
        {
            'address': '0xa0f9CBd4FACA57764b10d55B26D86D83e9113cBB',
            'topics': [
                '0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822',
                '0x000000000000000000000000ef1c6e67703c7bd7107eed8303fbe6ec2554bf6b',
                '0x00000000000000000000000005756692cd1bddc2770defee04c2b1476a0ebaba'
            ],
            'data': '0x00000000000000000000000000000000000000000000000000416b6f78e4e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004813dc89f0d35197e32'
        }
    ]
}

analysis_result = analyzer_manager.analyze_from_balance_change(transaction_data)  # Empty receipt for this example
print("Transaction analysis result:", analysis_result)