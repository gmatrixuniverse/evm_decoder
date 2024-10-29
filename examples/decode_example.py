import sys
import os

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from evm_decoder import DecoderManager

# Initialize the DecoderManager
decoder_manager = DecoderManager()

# Example transaction data
transaction_data = {
    'input': '0x70fef1da000000000000000000000000bac36b3fc5efafe3baa06539e29a7bf7120bc060000000000000000000000000c02aaa39b223fe8d0a0e5c4f27ead9083c756cc20000000000000000000000007a250d5630b4cf539739df2c5dacb4c659f2488d000000000000000000000000745ba16ccb4f61b048b6e43b42e5500cf93f67ce000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005200a0e9b161bc59feecb165fe2592bef3e1847a0000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000000000000000000640000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000900000000000000000000000000000000000000000000000000000000000000c80000000000000000000000000000000000000000000000000000000064f4c6630000000000000000000000000000000000000000000000000000000000000000'
}

# Decode the transaction
result = decoder_manager.decode(transaction_data)
print("Transaction decode result:", result['params']['tokenIn'])
# print(result['params'][1][-1])

# Example event data
# event_data = {
#     'topics': [
#         '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef',
#         '0x000000000000000000000000e82701fd630c91d35cdb923516c6a466ecdd0d05',
#         '0x000000000000000000000000b8faa80fe04a4afd30c89f40e4fcdc6dafb274d9'
#     ],
#     'data': '0x000000000000000000000000000000000000000000071f0a60a573248da706ca'
# }

# # Decode the event
# result = decoder_manager.decode(event_data)
# print("Event decode result:", result)

# event_data = {
#     'topic0': '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef',
#     'topic1': '0x000000000000000000000000e82701fd630c91d35cdb923516c6a466ecdd0d05',
#     'topic2': '0x000000000000000000000000b8faa80fe04a4afd30c89f40e4fcdc6dafb274d9',
#     'data': '0x000000000000000000000000000000000000000000071f0a60a573248da706ca'
# }

# # Decode the event
# result = decoder_manager.decode(event_data)
# print("Event decode result:", result)