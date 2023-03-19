BLOCK_FROST_PROJECT_ID = <your_id>

chain_context = BlockFrostChainContext(project_id=BLOCK_FROST_PROJECT_ID,base_url=ApiUrls.preprod.value,)

address = <your_address>


utxos = chain_context.utxos(str(address))

assetDict = []
for utxo in utxos:
	if utxo.output.amount.multi_asset:
		assetDict.append(utxo.output.amount.multi_asset)

policies = []
for n in assetDict:
	for q in n:
		policies.append(q.to_primitive().hex())
		
index  = 0 
for n in assetDict:
	keys = list(n)
	if len(keys) < 2:
		policy_hex = keys[0].to_primitive().hex()
		asset_name = list(n[keys[0]].to_primitive())[0]
		asset_amount = list(n[keys[0]].to_primitive().values())[0]
		print(policy_hex,asset_name,asset_amount)
	else:
		for items in n:
			if len(n[items]) < 2:
				policy_hex = items.to_primitive().hex()
				asset_name = list(n[items].to_primitive())[0]
				asset_amount = list(n[items].to_primitive().values())[0]
				print(policy_hex,asset_name,asset_amount)
			else:
				for names in n[items]:
					policy_hex = items.to_primitive().hex()
					asset_name = bytes(names)
					asset_amount = list(n[items].values())[index]
					print(policy_hex,asset_name,asset_amount)
					index += 1

#Find policy in Utxo List
find_policy = '8eb7927db11995297cd8846bda6884020d4c2dd9d8886e456921465b'
find_name = b'VeriFair_alpha_Winners'
find_nft = MultiAsset.from_primitive({bytes.fromhex(find_policy): {find_name: 1} })

find_policy = '366a7e727f403128a0c87965b23aaa95965c22dfcb6f9f41318e8412'
find_name = b'Cardano Circles'
find_nft = MultiAsset.from_primitive({bytes.fromhex(find_policy): {find_name: 1} })


for utxo in utxos:
	if utxo.output.amount.multi_asset:
		if len(utxo.output.amount.multi_asset) < 2:
			if utxo.output.amount.multi_asset == find_nft:
				print('Gotchya')
		else:
			for items in utxo.output.amount.multi_asset:
				policy = items.to_primitive().hex()
				if len(utxo.output.amount.multi_asset[items]) < 2:
					asset_name = list(utxo.output.amount.multi_asset[items].to_primitive())[0]
					print(policy,asset_name)
					if find_name == asset_name and find_policy == policy:
						print('Gotchya Here!')
				else:
					for names in utxo.output.amount.multi_asset[items]:
						asset_name = names.to_primitive()
						x = bytes(asset_name.decode('utf-8'), 'utf-8')
						if find_name == x and find_policy == policy:
							print('Gotchya Here!!!')
						print(policy,x)
						
			
    
