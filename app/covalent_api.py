import requests
import random

'''Returns NFT token id list'''
def tokenID(address, chain_id):
    r = requests.get('https://api.covalenthq.com/v1/'+chain_id+'/tokens/'+address+'/nft_token_ids/?quote-currency=USD&format=JSON&key=ckey_ec93e26420d24cab8b09ef796f4')
    x1 = r.json()['data']['items'] 
    return [x1[i]['token_id'] for i in range(len(x1))]

#a1 = tokenID('0x1e988ba4692e52Bc50b375bcC8585b95c48AaD77','1')

'''Returns NFT metadata like name, description, image, owner, contract name, contract address, attributes, etc.'''
def metadata(address, chain_id, token_id):
    r = requests.get('https://api.covalenthq.com/v1/'+chain_id+'/tokens/'+address+'/nft_metadata/'+token_id+'/?quote-currency=USD&format=JSON&key=ckey_ec93e26420d24cab8b09ef796f4')
    x2 = r.json()['data']['items']
    attributes = x2[0]['nft_data'][0]['external_data']['attributes']
    description = x2[0]['nft_data'][0]['external_data']['description']
    image_url = x2[0]['nft_data'][0]['external_data']['image']
    name = x2[0]['nft_data'][0]['external_data']['name']
    owner = x2[0]['nft_data'][0]['owner']
    contract_name = x2[0]['contract_name']
    contract_address = x2[0]['contract_address']
    return {'attributes': attributes, 'description': description, 'image_url': image_url, 'name': name, 'owner': owner, 'contract_name': contract_name, 'contract_address': contract_address}
#pprint(metadata('0x1e988ba4692e52Bc50b375bcC8585b95c48AaD77','1',a1[0]))

'''Returns random NFT data from a paricular NFT collection'''
def random_nft_data(address, chain_id):
    a1 = tokenID(address, chain_id)[0:20]
    random_nft = random.choice(a1)
    return metadata(address, chain_id, random_nft)
#pprint(random_nft_data('0xF3402D09BfF30252872ec60A00305E3fD082A701','137'))
