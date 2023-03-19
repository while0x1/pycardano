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
		
for n in assetDict:
	if len(n) < 2:
		keys = list(n)
		policy_hex = keys[0].to_primitive().hex()
		asset_name = list(n[keys[0]].to_primitive())[0]
		asset_amount = list(n[keys[0]].to_primitive().values())[0]
		print(policy_hex,asset_name,asset_amount)

			
    
